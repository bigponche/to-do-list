
def add_task(tasks, description):
    clean = description.strip()
    if clean == "":
        raise ValueError("add a valid text") 
    new_task = {
        'description': clean,  
        'completed': False,     
    }
    tasks.append(new_task)  
    return tasks 
    
def view_tasks(tasks):
    if tasks == []:  
        print("You need to add a task firts")  # 
        return
    for i, task in enumerate(tasks, start=1):
        estado = '[x]' if task['completed'] else '[ ]'  
        print(f"{i}. {estado} {task['description']}") 
    
        
def complete_task(tasks, index):
    if index-1 <= len(tasks) and index-1 >= len(tasks): 
        tasks[index-1]['completed'] = True
    else:
        raise ValueError("Type a number in the task list")  
    
def complete_task(tasks, index):
    if index-1 < 0 or index-1 >= len(tasks):
        raise ValueError("Type a number in the task list")
    tasks[index-1]['completed'] = True
    
def delete_task(tasks, index):
    if index-1 < 0 or index-1 >= len(tasks):
        raise ValueError("Type a number in the task list")
    tasks.pop(index-1)