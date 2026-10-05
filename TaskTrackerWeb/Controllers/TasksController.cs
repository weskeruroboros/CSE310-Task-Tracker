using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;
using TaskTrackerWeb.Models;
using TaskTrackerWeb.Services;

namespace TaskTrackerWeb.Controllers
{
    public class TasksController : Controller
    {
        private readonly ITaskRepository _repository;

        public TasksController(ITaskRepository repository)
        {
            _repository = repository;
        }

        // GET: Tasks
        public async Task<IActionResult> Index()
        {
            var tasks = await _repository.GetAllTasksAsync();
            return View(tasks);
        }

        // GET: Tasks/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Tasks/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Title,Category,Status")] TaskItem task)
        {
            if (ModelState.IsValid)
            {
                await _repository.AddTaskAsync(task);
                return RedirectToAction(nameof(Index));
            }
            return View(task);
        }

        // GET: Tasks/Edit/5
        public async Task<IActionResult> Edit(int id)
        {
            var task = await _repository.GetTaskByIdAsync(id);
            if (task == null) return NotFound();
            return View(task);
        }

        // POST: Tasks/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Title,Category,Status,CreatedAt")] TaskItem task)
        {
            if (id != task.Id) return NotFound();

            if (ModelState.IsValid)
            {
                await _repository.UpdateTaskAsync(task);
                return RedirectToAction(nameof(Index));
            }
            return View(task);
        }

        // GET: Tasks/Delete/5
        public async Task<IActionResult> Delete(int id)
        {
            var task = await _repository.GetTaskByIdAsync(id);
            if (task == null) return NotFound();
            return View(task);
        }

        // POST: Tasks/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            await _repository.DeleteTaskAsync(id);
            return RedirectToAction(nameof(Index));
        }

        // POST: Tasks/ToggleStatus/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> ToggleStatus(int id)
        {
            var task = await _repository.GetTaskByIdAsync(id);
            if (task == null) return NotFound();

            // Toggle status between Completed and Pending
            task.Status = task.Status == "Completed" ? "Pending" : "Completed";
            await _repository.UpdateTaskAsync(task);

            return RedirectToAction(nameof(Index));
        }
    }
}