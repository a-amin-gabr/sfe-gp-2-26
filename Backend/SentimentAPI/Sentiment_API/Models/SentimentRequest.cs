using System.Text.Json.Serialization;

namespace Sentiment_API.Models
{
    public class SentimentRequest
    {
        [JsonPropertyName("text")]
        public string Text { get; set; } = string.Empty;
    }
}