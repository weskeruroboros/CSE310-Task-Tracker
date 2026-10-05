using Microsoft.EntityFrameworkCore;
using TaskTrackerWeb.Data;
using TaskTrackerWeb.Services;
using System.Diagnostics;

var builder = WebApplication.CreateBuilder(args);

// Add MVC services to the container
builder.Services.AddControllersWithViews();

// Configure EF Core Database Connection (SQLite)
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlite(builder.Configuration.GetConnectionString("DefaultConnection")));

// Register Repository Service for Dependency Injection
builder.Services.AddScoped<ITaskRepository, TaskRepository>();

var app = builder.Build();

// CUSTOM MIDDLEWARE: Request Duration Logging & Global Exception Handling
app.Use(async (context, next) =>
{
    var watch = Stopwatch.StartNew();
    try
    {
        await next(context);
    }
    catch (Exception ex)
    {
        Console.WriteLine($"[CRITICAL ERROR] {DateTime.UtcNow}: {ex.Message}");
        throw; 
    }
    finally
    {
        watch.Stop();
        Console.WriteLine($"[LOG] Request: {context.Request.Method} {context.Request.Path} executed in {watch.ElapsedMilliseconds}ms");
    }
});

// Configure the HTTP request pipeline
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();
app.UseAuthorization();

// Route default traffic to the Tasks controller
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Tasks}/{action=Index}/{id?}");

app.Run();