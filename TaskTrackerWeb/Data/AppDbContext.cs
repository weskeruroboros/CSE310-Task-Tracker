using Microsoft.EntityFrameworkCore;
using TaskTrackerWeb.Models;

namespace TaskTrackerWeb.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
        {
        }

        // Maps the TaskItem model to the "Tasks" table in your SQL database
        public DbSet<TaskItem> Tasks { get; set; }
        
        // public DbSet<Project> Projects { get; set; } // Ready for when you build Project.cs
    }
}