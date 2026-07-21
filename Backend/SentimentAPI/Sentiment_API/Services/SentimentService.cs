using System.Net.Http.Json;

namespace Sentiment_API.Services
{
    public class SentimentService
    {
        private readonly HttpClient _httpClient;

        // Injecting HttpClient to communicate with the Python FastAPI server
        public SentimentService(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        public async Task<SentimentResponse> AnalyzeSentimentAsync(string text)
        {
            // The URL of the Python server (ensure the port is correct, e.g., 8000)
            var pythonApiUrl = "http://localhost:8000/predict";

            // Sending the text data as a JSON payload to the Python server
            var response = await _httpClient.PostAsJsonAsync(pythonApiUrl, new { text = text });

            // Throws an exception if the HTTP response is unsuccessful
            response.EnsureSuccessStatusCode();

            // Deserializing the JSON response into our SentimentResponse class
            var result = await response.Content.ReadFromJsonAsync<SentimentResponse>();

            return result ?? new SentimentResponse();
        }
    }

    // A simple class to represent the expected response from the Python API
    public class SentimentResponse
    {
        public string Sentiment { get; set; } = string.Empty;
        public double Confidence { get; set; }
    }
}