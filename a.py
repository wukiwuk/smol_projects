tasks = []
descs = {}

def displayTasks(all_tasks, descs):
    print('\nYour tasks: ')

    if len(all_tasks) <= 0:
        print('\nYou have no tasks')
    else: 
        for index, task in enumerate(all_tasks):
            print(f'{index+1}. {task} => {descs[task]}')

def newOp(all_tasks, descs):
    op=input("Press 'A' to add task, press 'E' to edit task, press 'R' to remove task, press 'Q' to turn off the app: \n")

    if op == 'A':
        addTask(all_tasks, descs)
    elif op == 'E':
        editTask(all_tasks, descs)
    elif op == 'R':
        removeTask(all_tasks, descs)
    elif op =='Q': 
        return
    else:
        newOp(all_tasks, descs)

def validTasknum(all_tasks, operation):
    task_num = input(f'Enter the number of the task number you want to {operation}\n')

    valid=False
    while not valid:
        try:
            number = int(task_num)
            valid = True
        except:
            task_num = input('Please enter a valid task number: ')

    if not (0 < number <= len(all_tasks)):
        print('Task not found!')
        validTasknum(all_tasks, operation)
    else:
        return number
    
def addDesc(task, descs):
    desc= input('Add a description: ')
    descs[task] = desc
    
    return  descs

def editTask(all_tasks, descs):
    task_num=validTasknum(all_tasks, 'edit: ')
    new_task=input('Edit Task: ')   
    all_tasks[(task_num) - 1] = new_task
    addDesc(new_task, descs)

    print(f'Task {task_num} edited!')
    displayTasks(all_tasks, descs)
    newOp(all_tasks, descs)

def removeTask(all_tasks, descs):
    task_num=validTasknum(all_tasks, 'remove: ')

    del descs[all_tasks([task_num] -1)]
    all_tasks.remove(all_tasks[(task_num ) - 1])

    print(f'\nTask {task_num} has been removed')
    displayTasks(all_tasks, descs)
    newOp(all_tasks, descs)

def addTask(all_tasks, descs):
    new_task = input('Add a task: ')
    all_tasks.append(new_task)
    new_desc= addDesc(new_task, descs)

    displayTasks(all_tasks, new_desc)
    newOp(all_tasks, descs)

addTask(tasks, descs)