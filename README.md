# Task Tracker CLI

A command-line task tracker in Python. Add, list, edit and delete tasks; they
persist to a JSON file between runs.

This was an early learning project — the point was to practise the fundamentals
end to end: modular functions, input validation, and file persistence that
survives a corrupted or missing file.

## Features

- Add, edit, list and remove tasks
- JSON persistence
- Input validation, so a wrong keystroke re-prompts instead of crashing
- A plain menu-driven interface

## Running it

Requires Python 3.

```bash
git clone https://github.com/OmerHarmankayaC/Task_Tracker.git
cd Task_Tracker
python main.py
```

## Data format

Each task is a dictionary in `tasks.json`:

```json
{
  "title": "Finish assignment",
  "desc": "Complete Python task tracker project",
  "dueDate": "2026-01-20"
}
```

## Error handling

Most input errors here are `ValueError`s, so every value is type-checked right
before use and the user is asked again on a mismatch. Two file errors are
handled the same way: a `FileNotFoundError` creates a fresh file, and a
`JSONDecodeError` replaces a corrupted one.

## Possible improvements

- A `completed` flag on tasks, and filtering by it
- Due-date validation
- Task priorities

## Author

Ömer Harmankaya — Computer Engineering student at TED University. Built for
personal practice.
