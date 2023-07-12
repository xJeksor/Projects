import React, { useState } from 'react';

const TaskList = ({ translation }) => {
  const [tasks, setTasks] = useState([]);
  const [currentTask, setCurrentTask] = useState(null);
  const [completedIntervals, setCompletedIntervals] = useState(0);
  const [targetIntervals, setTargetIntervals] = useState(0);

  const handleAddTask = () => {
    const task = {
      id: Date.now(),
      name: '',
      intervals: 0,
    };

    setTasks((prevTasks) => [...prevTasks, task]);
  };

  const handleDeleteTask = (taskId) => {
    setTasks((prevTasks) => prevTasks.filter((task) => task.id !== taskId));
  };

  const handleEditTaskName = (taskId, newName) => {
    setTasks((prevTasks) =>
      prevTasks.map((task) =>
        task.id === taskId ? { ...task, name: newName } : task
      )
    );
  };

  const handleEditTaskIntervals = (taskId, newIntervals) => {
    setTasks((prevTasks) =>
      prevTasks.map((task) =>
        task.id === taskId ? { ...task, intervals: newIntervals } : task
      )
    );
  };

  const handleStartTask = (taskId, intervals) => {
    setCurrentTask(taskId);
    setTargetIntervals(intervals);
    setCompletedIntervals(0);
  };

  const handleCompleteInterval = () => {
    setCompletedIntervals((prevIntervals) => prevIntervals + 1);

    if (completedIntervals >= targetIntervals) {
      setCurrentTask(null);
      setTargetIntervals(0);
    }
  };

  return (
    <div>
      <button onClick={handleAddTask}>{translation.addTaskButton}</button>

      {tasks.map((task) => (
        <div key={task.id}>
          <input
            type="text"
            value={task.name}
            onChange={(e) => handleEditTaskName(task.id, e.target.value)}
          />
          <input
            type="number"
            value={task.intervals}
            onChange={(e) =>
              handleEditTaskIntervals(task.id, parseInt(e.target.value))
            }
          />
          <button onClick={() => handleDeleteTask(task.id)}>
            {translation.deleteButton}
          </button>
          {!currentTask && (
            <button onClick={() => handleStartTask(task.id, task.intervals)}>
              {translation.startButton}
            </button>
          )}
        </div>
      ))}

      {currentTask && (
        <div>
          <h2>
            {translation.taskInProgressLabel}:{' '}
            {tasks.find((task) => task.id === currentTask)?.name}
          </h2>
          <p>
            {translation.completedIntervalsLabel}: {completedIntervals}/
            {targetIntervals}
          </p>
          <button onClick={handleCompleteInterval}>
            {translation.completeIntervalButton}
          </button>
        </div>
      )}
    </div>
  );
};

export default TaskList;
