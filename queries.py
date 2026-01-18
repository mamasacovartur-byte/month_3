# C R U D
# create, read, update, delete

task_table = """CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
)
"""

# create
insert_task = 'INSERT INTO tasks (task) VALUES (?)'


# read
select_task = 'SELECT id, task FROM tasks'


# update
update_task = 'UPDATE tasks SET task = ? WHERE id = ?'


# delete
delete_task = 'DELETE FROM tasks WHERE id = ?'