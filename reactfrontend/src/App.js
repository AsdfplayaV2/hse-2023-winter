import React, { useState, useEffect } from 'react';

const TaskList = () => {
  const [tasks, setTasks] = useState([]);
  const [newTaskName, setNewTaskName] = useState('');

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = () => {
    fetch('https://5000-asdfplayav2-hse2023wint-du7z2b0epju.ws-eu107.gitpod.io/tasks')
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          console.log('Error fetching tasks');
          throw new Error('Error fetching tasks');
        }
      })
      .then((data) => {
        console.log('Tasks fetched successfully');
        setTasks(data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const deleteTask = (id) => {
    fetch(`https://5000-asdfplayav2-hse2023wint-du7z2b0epju.ws-eu107.gitpod.io/tasks/${id}`, {
      method: 'DELETE',
    })
      .then((response) => {
        if (response.ok) {
          console.log(`Task with ID ${id} deleted successfully`);
          fetchTasks();
        } else {
          console.log(`Error deleting task with ID ${id}`);
          throw new Error(`Error deleting task with ID ${id}`);
        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const completeTask = (id) => {
    fetch(`https://5000-asdfplayav2-hse2023wint-du7z2b0epju.ws-eu107.gitpod.io/tasks/${id}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        completed: true,
      }),
    })
      .then((response) => {
        if (response.ok) {
          console.log(`Task with ID ${id} marked as completed`);
          fetchTasks();
        } else {
          console.log(`Error completing task with ID ${id}`);
          throw new Error(`Error completing task with ID ${id}`);
        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const addTask = () => {
    fetch('https://5000-asdfplayav2-hse2023wint-du7z2b0epju.ws-eu107.gitpod.io/tasks', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        taskname: newTaskName,
        completed: false,
      }),
    })
      .then((response) => {
        if (response.ok) {
          console.log('Task added successfully');
          setNewTaskName('');
          fetchTasks();
        } else {
          console.log('Error adding task');
          throw new Error('Error adding task');
        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <div>
      <h1>Task List</h1>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            {task.taskname} - {task.completed ? 'Completed' : 'Incomplete'}
            {!task.completed && (
              <>
                <button onClick={() => completeTask(task.id)}>Complete</button>
              </>
            )}
                            <button onClick={() => deleteTask(task.id)}>Delete</button>

          </li>
        ))}
      </ul>
      <form>
        <label>
          New Task:
          <input
            type="text"
            value={newTaskName}
            onChange={(e) => setNewTaskName(e.target.value)}
          />
        </label>
        <button type="button" onClick={addTask}>
          Add Task
        </button>
      </form>
    </div>
  );
};

export default TaskList;
