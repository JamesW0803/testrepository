// Dummy To-Do List App

let todoList = [];

function addTask(task) {
  todoList.push(task);
  console.log(`Added: "${task}"`);
}

function removeTask(task) {
  const index = todoList.indexOf(task);
  if (index > -1) {
    todoList.splice(index, 1);
    console.log(`Removed: "${task}"`);
  } else {
    console.log(`Task not found: "${task}"`);
  }
}

function showTasks() {
  console.log("To-Do List:");
  todoList.forEach((task, i) => {
    console.log(`${i + 1}. ${task}`);
  });
}

// Example usage:
addTask("Buy groceries");
addTask("Study for exam");
showTasks();
removeTask("Buy groceries");
showTasks();
