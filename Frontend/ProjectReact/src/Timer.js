import React, { useState, useEffect, useRef } from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
import { useDropzone } from 'react-dropzone';

const Timer = ({ translation }) => {
  const [workTime, setWorkTime] = useState(25 * 60);
  const [shortBreakTime, setShortBreakTime] = useState(5 * 60);
  const [longBreakTime, setLongBreakTime] = useState(15 * 60);
  const [activeTime, setActiveTime] = useState(workTime);
  const [isRunning, setIsRunning] = useState(false);
  const [isBreak, setIsBreak] = useState(false);
  const [workIntervalCount, setWorkIntervalCount] = useState(0);
  const [maxWorkIntervals, setMaxWorkIntervals] = useState(4);
  const [countWorkTime, setCountWorkTime] = useState(0);
  const [countshortBreakTime, setCountshortBreakTime] = useState(0);
  const [countlongBreakTime, setCountlongBreakTime] = useState(0);

  const audioPlayer = useRef(null);

  const intervalLabels = ['Work', 'Short Break', 'Long Break'];

  const sounds = [
    { name: 'I Did It Message Tone', src: '/i-did-it-message-tone.mp3' },
    {
      name: 'Mixkit Bell Notification',
      src: '/mixkit-bell-notification-933.wav',
    },
  ];
  const [selectedSound, setSelectedSound] = useState(sounds[0].src);

  const handleSoundChange = (event) => {
    setSelectedSound(event.target.value);
  };

  function playAudio() {
    audioPlayer.current.play();
  }

  const startInterval = () => {
    setIsRunning(true);
  };

  const pauseTimer = () => {
    setIsRunning(false);
  };

  const resetTimer = () => {
    setIsRunning(false);
    setIsBreak(false);
    setActiveTime(workTime);
    setWorkIntervalCount(0);
    setCountWorkTime(0);
    setCountshortBreakTime(0);
    setCountlongBreakTime(0);
  };

  const skipInterval = () => {
    setIsBreak(!isBreak);
    if (isBreak) {
      setActiveTime(workTime);
      setWorkIntervalCount((prevCount) => prevCount + 1);
      setCountWorkTime((prevCount) => prevCount + 1);
    } else {
      if (workIntervalCount >= maxWorkIntervals) {
        setActiveTime(longBreakTime);
        setMaxWorkIntervals((prevCount) => prevCount + 4);
        setCountlongBreakTime((prevCount) => prevCount + 1);
      } else {
        setActiveTime(shortBreakTime);
        setCountshortBreakTime((prevCount) => prevCount + 1);
      }
    }
    playAudio();
  };

  const formatTime = (timeInSeconds) => {
    const minutes = Math.floor(timeInSeconds / 60);
    const seconds = timeInSeconds % 60;
    return `${minutes.toString().padStart(2, '0')}:${seconds
      .toString()
      .padStart(2, '0')}`;
  };

  const handleWorkTimeChange = (event) => {
    const newWorkTime = parseInt(event.target.value, 10) * 60;
    setWorkTime(newWorkTime);
    if (!isBreak) {
      setActiveTime(newWorkTime);
    }
  };

  const handleShortBreakTimeChange = (event) => {
    const newShortBreakTime = parseInt(event.target.value, 10) * 60;
    setShortBreakTime(newShortBreakTime);
    if (isBreak && activeTime === shortBreakTime) {
      setActiveTime(newShortBreakTime);
      setCountshortBreakTime((prevCount) => prevCount + 1);
    }
  };

  const handleLongBreakTimeChange = (event) => {
    const newLongBreakTime = parseInt(event.target.value, 10) * 60;
    setLongBreakTime(newLongBreakTime);
    if (isBreak && activeTime === longBreakTime) {
      setActiveTime(newLongBreakTime);
      setCountlongBreakTime((prevCount) => prevCount + 1);
    }
  };

  const handleMaxWorkIntervalsChange = (event) => {
    const newMaxWorkIntervals = parseInt(event.target.value, 10);
    setMaxWorkIntervals(newMaxWorkIntervals);
  };

  const handleStartWork = () => {
    setIsBreak(false);
    setActiveTime(workTime);
    setWorkIntervalCount(0);
    startInterval();
    setCountWorkTime((prevCount) => prevCount + 1);
  };

  const handleStartShortBreak = () => {
    setIsBreak(true);
    setActiveTime(shortBreakTime);
    startInterval();
    setCountshortBreakTime((prevCount) => prevCount + 1);
  };

  const handleStartLongBreak = () => {
    setIsBreak(true);
    setActiveTime(longBreakTime);
    startInterval();
    setCountlongBreakTime((prevCount) => prevCount + 1);
  };

  useEffect(() => {
    let interval = null;

    if (isRunning) {
      interval = setInterval(() => {
        setActiveTime((prevTime) => {
          if (prevTime <= 0) {
            playAudio();
            if (!isBreak) {
              if (workIntervalCount >= maxWorkIntervals) {
                setIsBreak(true);
                setActiveTime(longBreakTime);
              } else {
                setIsBreak(true);
                setActiveTime(shortBreakTime);
              }
            } else {
              setIsBreak(false);
              setActiveTime(workTime);
              setWorkIntervalCount((prevCount) => prevCount + 1);
            }
          }

          return prevTime - 1;
        });
      }, 1000);
    } else {
      clearInterval(interval);
    }

    return () => clearInterval(interval);
  }, [
    isRunning,
    isBreak,
    activeTime,
    workTime,
    shortBreakTime,
    longBreakTime,
    workIntervalCount,
    maxWorkIntervals,
  ]);

  ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
  );

  const chartData = {
    labels: ['Work Time', 'Short Break Time', 'Long Break Time'],
    datasets: [
      {
        label: 'Count',
        backgroundColor: ['#36A2EB', '#FFCE56', '#FF6384'],
        data: [countWorkTime, countshortBreakTime, countlongBreakTime],
      },
    ],
  };

  const handleImport = (importedData) => {
    try {
      const { countWorkTime, countshortBreakTime, countlongBreakTime } =
        JSON.parse(importedData);
      setCountWorkTime(countWorkTime);
      setCountshortBreakTime(countshortBreakTime);
      setCountlongBreakTime(countlongBreakTime);
    } catch (error) {
      console.error('Invalid JSON file.');
    }
  };

  const onDrop = (acceptedFiles) => {
    const fileReader = new FileReader();
    fileReader.onload = (event) => {
      const importedData = event.target.result;
      handleImport(importedData);
    };
    fileReader.readAsText(acceptedFiles[0]);
  };

  const exportData = () => {
    const jsonData = {
      countWorkTime,
      countshortBreakTime,
      countlongBreakTime,
    };
    const jsonBlob = new Blob([JSON.stringify(jsonData)], {
      type: 'application/json',
    });
    const jsonURL = URL.createObjectURL(jsonBlob);
    const downloadLink = document.createElement('a');
    downloadLink.href = jsonURL;
    downloadLink.download = 'timerData.json';
    downloadLink.click();
  };

  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  return (
    <div>
      <div>
        <label>
          {translation.workTimeLabel}
          <input
            type="number"
            value={workTime / 60}
            onChange={handleWorkTimeChange}
          />
        </label>
      </div>
      <div>
        <label>
          {translation.shortBreakTimeLabel}
          <input
            type="number"
            value={shortBreakTime / 60}
            onChange={handleShortBreakTimeChange}
          />
        </label>
      </div>
      <div>
        <label>
          {translation.longBreakTimeLabel}
          <input
            type="number"
            value={longBreakTime / 60}
            onChange={handleLongBreakTimeChange}
          />
        </label>
      </div>
      <div>
        <label>
          {translation.maxWorkIntervalsLabel}
          <input
            type="number"
            value={maxWorkIntervals}
            onChange={handleMaxWorkIntervalsChange}
          />
        </label>
      </div>
      <div>
        <select value={selectedSound} onChange={handleSoundChange}>
          {sounds.map((sound) => (
            <option key={sound.src} value={sound.src}>
              {sound.name}
            </option>
          ))}
        </select>
      </div>
      <div>
        <button onClick={handleStartWork}>{translation.startWorkButton}</button>
        <button onClick={handleStartShortBreak}>
          {translation.shortBreakButton}
        </button>
        <button onClick={handleStartLongBreak}>
          {translation.longBreakButton}
        </button>
        <button onClick={pauseTimer}>{translation.pauseButton}</button>
        <button onClick={resetTimer}>{translation.resetButton}</button>
        <button onClick={skipInterval}>{translation.skipIntervalButton}</button>
      </div>
      <div>
        <h1>
          {intervalLabels[isBreak ? (activeTime <= shortBreakTime ? 1 : 2) : 0]}
        </h1>
        <div>{formatTime(activeTime)}</div>
        <audio ref={audioPlayer} src={selectedSound} />
      </div>
      <div>
        <p>
          {translation.workIntervalCountLabel}: {workIntervalCount}
        </p>
      </div>
      <div>
        <Bar data={chartData} />
      </div>
      <div>
        <button onClick={exportData}>Export</button>
      </div>
      <div {...getRootProps()}>
        <input {...getInputProps()} />
        <p>Drag and drop a JSON file to import data</p>
      </div>
    </div>
  );
};

export default Timer;
