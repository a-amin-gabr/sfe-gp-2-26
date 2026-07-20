using System.ComponentModel.DataAnnotations;

namespace Sentiment_API.DTOs
{
    public class LoginDto
    {
        [Required(ErrorMessage = "Email is required")]
        [EmailAddress(ErrorMessage = "Invalid email format")]
        [RegularExpression(@"^[^@\s]+@[^@\s]+\.[^@\s]+$", ErrorMessage = "Please enter a valid email address with a domain (e.g., name@example.com)")]
        public required string Email { get; set; }
        public required string Password { get; set; }
    }
}