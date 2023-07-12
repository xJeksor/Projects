import React, { useState } from 'react';
import { translations } from './translations';
import Timer from './Timer';
import TaskList from './TaskList';
import './App.sass';

const App = () => {
  const [language, setLanguage] = useState('en');
  const translation = translations[language];
  const [resetTimer, setResetTimer] = useState(false);

  return (
    <div className="app">
      <h1 className="app-title">Pomodoro Timer</h1>
      <TaskList translation={translation} />
      <div className="language-select">
        <label>
          Language:
          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
          >
            <option value="en">English</option>
            <option value="pl">Polish</option>
          </select>
        </label>
      </div>
      <Timer
        translation={translation}
        resetTimer={resetTimer}
        setResetTimer={setResetTimer}
      />
    </div>
  );
};

export default App;
