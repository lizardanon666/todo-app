import functions
import time

now = time.strftime("%b %d, %T")
print('It is', now)

while True:
    user_input = input('Enter add, show, edit, complete or exit: ')
    user_input = user_input.strip()
    user_input = user_input.lower()

    if user_input.startswith('add'):
        task = user_input[4:] + "\n"

        todos = functions.get_todos()

        todos.append(task)

        functions.write_todos(todos)

    elif user_input.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            index = index + 1
            row = f"{index}.{item}"
            print(row)

    elif user_input.startswith('edit'):
        try:
            number = user_input[5:]
            number = int(number) - 1

            todos = functions.get_todos()
            new_task = input('Enter the new task: ')
            todos[number] = new_task + '\n'

            functions.write_todos(todos)

            print('Task successfully edited.')
        except ValueError:
            print("Only specify task number to edit.")
            continue

    elif 'exit' in user_input:
        break

    elif user_input.startswith('complete'):
        try:
            number = int(user_input[9:])

            todos = functions.get_todos()
            uuuu = number - 1
            todo_rem = todos[uuuu].strip('\n')
            todos.pop(number - 1)

            functions.write_todos(todos)

            print(f"Todo {todo_rem} has been removed")
        except ValueError:
            print("Only specify task number to complete.")
        except IndexError:
            print('There is no item with that number.')
            continue

    else:
        print('Please enter the correct input')

print('Thanks')
