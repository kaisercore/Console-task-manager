import json
from datetime import*
file_name='Задачи.json'

def save_tasks(tasks):
    with open(file_name, 'w')as file:
        json.dump(tasks, file,ensure_ascii=False,indent=4)
def load_tasks():
    try:
        with open(file_name,'r')as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def show_tasks(tasks):
    if not tasks:
        print("\nСписок задач пуст\n")
        return
    print("\nСписок задач:\n")
    for index , task in enumerate(tasks,start=1):
        status = "Выполнено" if task["done"] else "Не выполнено"
        print(f"{index}. {task['title']}")
        print(f"Статус: {status}")
        print(f"Создано: {task['created']}")


def add_taks(tasks: list):
    title=input("Введите задачу: ")
    task={
        "title":title,
        "done":False,
        "created": datetime.strftime( datetime.now(), "%d/%m/%y %H:%M:%S") 
    }
    tasks.append(task)
    print("\nЗадача добавлена")
    save_tasks(tasks)
        
def complete_task(tasks: list):
    show_tasks(tasks)
    
    if not tasks:
        return
    try:
        number=int(input("Введите номер выполненой задачи: "))
        tasks[number-1]['done'] = True
        save_tasks(tasks)
        print("\nЗадача отмечена как выполненная\n") 
    except (ValueError,IndexError):
        print("\nОшибка: неверный номер задачи")

def delete_tasks(tasks):
    show_tasks(tasks)
    
    if not tasks:
        return
    
    try:
        number=int(input("Введите номер задачи: "))
        deleted = tasks.pop(number-1)
        save_tasks(tasks)
        print(f"\nЗадача '{deleted['title']}' удалена\n")
    except (ValueError, IndexError):
        print("\nНеверный номер задачи\n")
        
def exit_program(tasks):
    exit()
    
def main():
    tasks=load_tasks()
    
    while True:
        print('=' * 60)
        print("Менеджер задач")
        print('='*60)
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выполнить задачу")
        print("5. Выход")
        
        choice= int(input("Выберите действие: "))
        
        choices=[
            show_tasks,
            add_taks,
            delete_tasks,
            complete_task,
            exit_program
            ]
        
        try:
            choices[choice - 1](tasks)
        except IndexError:
            print("Неверный номер")
            
if __name__ == "__main__":
    main()