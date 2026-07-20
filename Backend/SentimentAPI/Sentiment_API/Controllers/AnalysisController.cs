using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Sentiment_API.Data;     // Path to AppDbContext
using Sentiment_API.Models;   // Path to AnalysisLog
using Sentiment_API.Services; // Path to SentimentService
using System.ComponentModel.DataAnnotations;
namespace Sentiment_API.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    [Authorize]
    public class AnalysisController : ControllerBase
    {
        private readonly SentimentService _sentimentService;
        private readonly AppDbContext _context; // Added DbContext here

        // Injecting DbContext and SentimentService into the controller
        public AnalysisController(SentimentService sentimentService, AppDbContext context)
        {
            _sentimentService = sentimentService;
            _context = context;
        }

        [HttpPost("analyze")]
        public async Task<IActionResult> AnalyzeText([FromBody] TextInput input)
        {
            // Ensure the text is not empty or whitespace
            if (string.IsNullOrWhiteSpace(input.Text))
            {
                return BadRequest(new { Message = "Text cannot be empty." });
            }

            try
            {
                // 1. Fetch the result from the Python server
                var result = await _sentimentService.AnalyzeSentimentAsync(input.Text);

                // 2. Prepare the log record to be saved in the database
                var log = new AnalysisLog
                {
                    Text = input.Text,
                    Sentiment = result.Sentiment, // Value returned from Python
                    Confidence = result.Confidence, // Confidence score returned
                    CreatedAt = DateTime.UtcNow
                };

                // 3. Add the record to the database and save changes
                _context.AnalysisLogs.Add(log);
                await _context.SaveChangesAsync();

                // 4. Return the final result to the client
                return Ok(result);
            }
            catch (HttpRequestException ex)
            {
                // If the Python server is down or there is a connection issue
                return StatusCode(503, new { Message = "AI Service is unavailable.", Error = ex.Message });
            }
            catch (Exception ex)
            {
                // Any other unexpected errors
                return StatusCode(500, new { Message = "An unexpected error occurred.", Error = ex.Message });
            }
        }
    }

    // Simple class to receive text from the Request Body
    public class TextInput
    {
        [Required(ErrorMessage = "Text is required")]
        [StringLength(500, MinimumLength = 3, ErrorMessage = "Text must be between 3 and 500 characters")]
        public string Text { get; set; } = string.Empty;
    }
}