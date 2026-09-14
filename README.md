# 🍅 Command-Line Pomodoro Productivity Timer

A lightweight **command-line Pomodoro productivity timer** built with Python.
The application helps users manage focused work sessions and short break intervals using a real-time countdown directly in the terminal.

## ✨ Features

* ⏱️ Configurable work session duration
* ☕ Configurable short break duration
* 🔄 Real-time countdown displayed in the terminal
* ✅ Tracks the total number of completed work sessions
* 🔔 Sound notification when a session ends
* 💬 Visual notification when transitioning between work and break sessions
* 🖥️ Runs directly from Command Prompt / Terminal

## 🛠️ Requirements

* Python 3.x
* Windows operating system
* Command Prompt or any terminal

No external Python packages are required.

## 🚀 How to Run

### 1. Download the Project

Download or clone this repository to your computer.

### 2. Open Command Prompt

Open **Command Prompt** inside the project folder.

### 3. Run the Program

python pomodoro.py

### 4. Configure the Timer

The program will ask you to enter:

* Work session duration in minutes
* Break duration in minutes

Example:

Enter work time (minutes): 1
Enter break time (minutes): 1


The timer will then start the work session.

## ⏱️ How It Works

The application follows a simple Pomodoro cycle:

Work Session
     ↓
Completion Notification
     ↓
Break Session
     ↓
Completion Notification
     ↓
Start Another Work Session


The completed work-session count is displayed after every completed work session.

## 📋 Example

=============================================
       🍅 POMODORO PRODUCTIVITY TIMER
=============================================

Enter work time (minutes): 1
Enter break time (minutes): 1

💻 Work session started!

🍅 WORK | ⏱️ 00:59

When the work session finishes:

🔔 Work session completed!
✅ Completed work sessions: 1

☕ Break started!

🍅 BREAK | ⏱️ 00:59
```

After the break finishes, the program asks whether to start another work session.

## 📁 Project Structure

```text
pomodoro-timer/
│
├── pomodoro.py
├── requirements.txt
├── README.md
└── demo.mp4
```

## 🎥 Demo Video

The demo video demonstrates:

1. Starting a work session
2. Watching the live countdown
3. Transitioning from the work session to a break
4. Viewing the completed work-session count





## 🎯 Project Objective

The objective of this project is to build a lightweight timer application that implements the **Pomodoro technique** to help users manage focused work and break intervals.

## 🧰 Built With

* Python
* Command Prompt / Terminal


