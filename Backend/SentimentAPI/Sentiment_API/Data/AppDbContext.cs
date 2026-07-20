using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;
using Sentiment_API.Models;

namespace Sentiment_API.Data
{
    // Change inheritance to IdentityDbContext and pass the custom user class
    public class AppDbContext : IdentityDbContext<ApplicationUser>
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
        {
        }

        // Keep your existing DbSets as they are
        public DbSet<AnalysisLog> AnalysisLogs { get; set; }

        protected override void OnModelCreating(ModelBuilder builder)
        {
            base.OnModelCreating(builder);

        }
    }
}