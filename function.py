
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