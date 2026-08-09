# To-Do List

A console-based task manager built in Python. Supports adding, viewing, completing, and deleting tasks through a simple numbered menu interface.

## Features

- Add tasks with a text description
- View all tasks with their completion status (`[ ]` pending, `[x]` done)
- Mark any task as completed by its number
- Delete any task by its number
- Friendly error messages for all invalid inputs — the program never crashes on bad user input

## How to run it

From the project folder:

```bash
python main.py
```

The program displays a menu on each loop iteration. Select an option by typing its number.

Example session:

```
1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit
selecciona una opcion: 1
agrega la description de la tarea: buy milk
1. Add task
...
selecciona una opcion: 2
1. [ ] buy milk
```

## Data structure

Each task is stored as a Python dictionary with two keys:

```python
{
    'description': 'buy milk',  # str: the task text, stripped of leading/trailing whitespace
    'completed': False           # bool: True if done, False if pending
}
```

The full task list is a plain Python list of these dictionaries, initialized as `[]` at program start. Data does not persist between sessions — closing the program clears all tasks.

## Architecture decisions

**Dictionary with `'description'` and `'completed'` keys, not a class or namedtuple.**
For a basic to-do list with only two fields, a plain dictionary is the simplest structure that works — no overhead, no boilerplate. A class would be the right call if tasks needed methods or more complex behavior.

**`bool` for completion status, not a string like `'done'`/`'pending'`.**
A boolean is the most direct representation of a two-state value. It also enables clean ternary expressions for display (`'[x]' if task['completed'] else '[ ]'`) and straightforward filtering if a future version needs to count or separate completed tasks.

**Validation order: `.strip()` before checking empty string.**
`add_task` strips whitespace from the description *before* checking if it's empty. This catches inputs like `"   "` (spaces only) that would otherwise pass an empty-string check but produce meaningless tasks.

**`index - 1` conversion at the boundary, not inside core functions.**
Users see tasks numbered from 1. The conversion to 0-based indexing (`index - 1`) happens at the point where the user-facing number enters the core logic, keeping the internal functions consistent with Python's native indexing.

**`view_tasks` uses `print`, not `raise`, for an empty list.**
An empty task list is not an error — it's a valid program state (the user just opened the app). Raising an exception for a normal state would force the caller to wrap every `view_tasks` call in a `try/except`, which is unnecessary noise. A friendly `print` message is the right tool here.

**`enumerate(tasks, start=1)` for natural numbering.**
Using `enumerate` with `start=1` avoids manual index tracking and produces the 1-based numbering users expect, without any off-by-one arithmetic inside the loop.

## Project structure

| File | Responsibility |
|---|---|
| `requirements.py` | Task data structure definition and documented edge cases (`ERRORS_INFO`) |
| `function.py` | Core logic: `add_task()`, `view_tasks()`, `complete_task()`, `delete_task()` |
| `main.py` | Console menu interface, input handling, and error display |

## Risk Notes — how this code can break

- **Empty task description** (`""`, `"   "`) → caught by `.strip()` check in `add_task`, raises `ValueError`.
- **Index out of range** (e.g. task number 5 when only 2 tasks exist) → caught by bounds check in `complete_task` and `delete_task`, raises `ValueError`.
- **Text instead of a number for index** (e.g. `"two"`, `"a"`) → `int()` conversion in `main.py` raises `ValueError`, caught by the `try/except` block.
- **Operating on an empty list** (view, complete, or delete before adding any task) → `view_tasks` prints a friendly message; `complete_task` and `delete_task` raise `ValueError` since `index-1 >= len([])` is always true.
- **Duplicate task descriptions** → allowed by design. There is no uniqueness constraint on task text — two tasks can share the same description without any conflict.

### Known limitation

Tasks are stored in memory only. Closing the program permanently deletes all tasks — there is no file persistence in this version. Saving to and loading from a `.json` or `.txt` file is the natural next step for a future version.
