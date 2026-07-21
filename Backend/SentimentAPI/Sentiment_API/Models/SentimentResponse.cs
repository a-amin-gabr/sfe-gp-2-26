using System.Text.Json.Serialization;

namespace Sentiment_API.Models
{
    public class SentimentResponse
    {
        [JsonPropertyName("sentiment")]
        public string Sentiment { get; set; } = string.Empty;

        [JsonPropertyName("confidence")]
        public double Confidence { get; set; }
    }
}