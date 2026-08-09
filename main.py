from function import delete_task,complete_task,add_task,view_tasks

if __name__ == "__main__":
    tasks =[]
    while True:
        print ('1. Add task')
        print ('2. View tasks')
        print ('3. Complete task')
        print ('4. Delete task')
        print ('5. Exit')
        order=input()
        try:
            if order == '1':
                add = add_task(tasks, description)
                tasks.append(add)
            elif order =='2':
                view = view_tasks(add)
            elif order == '3':
                complete = complete_task(tasks)
            elif order == '4':
                delet = delete_task()
            elif order == '5':
                break
        except ValueError as e:
            print(f'Error {e}')
            continue
            
    
    