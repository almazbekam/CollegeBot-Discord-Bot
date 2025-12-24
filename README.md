# College Companion Discord Bot

## Description
The College Companion Discord Bot helps students stay organized, motivated, and productive while preparing for college. It combines task management, reminders, and motivational quotes to create an engaging environment for students to manage their study schedule effectively.

## Features
- **Motivational Quotes (`!quote`)**: Sends a random motivational or college-related quote.
- **Task Scheduling (`!schedule [task]`)**: Add personal study or college prep tasks. Tasks are saved persistently.
- **View Tasks (`!tasks`)**: Lists all scheduled tasks with their creation dates.
- **Task Reminders (`!reminder [task number]`)**: Sends a direct message reminder for a specific task.
- **Welcome Messages**: Automatically greets new members in the server.

## Commands
| Command                  | Description |
|---------------------------|-------------|
| `!quote`                  | Sends a random motivational or college-related quote. |
| `!schedule [task]`        | Adds a task to your personal task list. |
| `!tasks`                  | Shows all tasks you have scheduled. |
| `!reminder [task number]` | Sends a DM reminder for a specific task. |

## Notes
- Tasks are saved in `data.json` to persist between sessions.  
- The bot uses an internal quote list to ensure reliability.  
- Designed for GitHub and college demo purposes — fully functional with no duplicate messages.

## Future Improvements
- Add points/leaderboard system for completed tasks.  
- Include automated study reminders or Pomodoro timer.  
- Add daily motivational quotes automatically to a channel.

