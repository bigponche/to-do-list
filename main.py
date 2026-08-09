from function import delete_task,complete_task,add_task,view_tasks

if __name__ == "__main__":
    tasks =[]
    while True:
        print ('1. Add task')
        print ('2. View tasks')
        print ('3. Complete task')
        print ('4. Delete task')
        print ('5. Exit')
        order=input('selecciona una opcion')
        try:
            if order == '1':
                description = input('agrega la description de la tarea')
                add = add_task(tasks, description)
                
            elif order =='2':
                view = view_tasks(tasks)
            elif order == '3':
                index = int(input('escriba un numero de la lista'))
                complete = complete_task(tasks,index)
            elif order == '4':
                index = int(input('escriba un numero de la lista'))
                delet = delete_task(tasks,index)
            elif order == '5':
                break
        except ValueError as e:
            print(f'Error {e}')
            continue
            
    
    