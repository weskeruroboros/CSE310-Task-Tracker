# Overview

This project implements a dynamic, modern Task Tracker web application built using C#, ASP.NET Core MVC, and an SQLite relational database managed via Entity Framework Core (EF Core).

This project was selected to learn the core principles of C# web development, MVC architecture, the Service/Repository design pattern (`ITaskRepository`), custom execution-logging middleware, full asynchronous CRUD operations, and responsive dashboard UI design with Bootstrap 5.

[Software Demo Video](https://youtu.be/TNwm8DpyEnw)

# Development Environment

- Framework & Language: C# / .NET 8.0 SDK (ASP.NET Core MVC & Entity Framework Core)
- Database: SQLite
- Development Tool: Visual Studio Code (including C# Dev Kit extensions)
- GitHub Repository: [https://github.com/weskeruroboros/CSE310-Task-Tracker.git]

To run the project, execute the following commands in your terminal:

```bash
cd TaskTrackerWeb
dotnet run

# Useful Websites

- [ASP.NET Core MVC Documentation](https://learn.microsoft.com/en-us/aspnet/core/mvc/overview?view=aspnetcore-10.0)
- [Entity Framework Core Documentation](https://flask-sqlalchemy.readthedocs.io/en/stable/)
- [.NET Official Documentation](https://www.python.org/)

# Future Work

- **Relational Data & Joins:** Implement a dedicated `Category` entity with Entity Framework Core Navigation Properties and Foreign Keys to demonstrate relational table joins.
- **Date Filtering & Overdue Alerts:** Add `DueDate` properties to `TaskItem` with UI badge alerts for overdue tasks and date-range filtering controls.
- **User Authentication:** Integrate ASP.NET Core Identity to support user registration, login, and multi-tenant task lists.
- **RESTful API Endpoint:** Expose API controllers delivering JSON payloads for mobile app integration or third-party webhooks.