# todos = []  # to keep data stored, we include a list later
while True:
    user_input = input('Enter add, show, edit, completed or exit: ')
    user_input = user_input.strip()
    user_input = user_input.lower()
    match user_input:
        case 'add':

            task = input('Add a task: ') + "\n"

            file = open('../Files/TDL.txt', 'r')  # Opens the file and reads it
            todos = file.readlines()  # add the content of the file to todos list. If file is empty, nothing is added
            file.close()

            todos.append(task)  # input task is added to the list

            file = open('../Files/TDL.txt', 'w')
            file.writelines(todos)  # list is reprinted on the file
            file.close()

        case 'show' | 'display':
            for index, item in enumerate(todos):
                item = item.title()
                index = index + 1
                row = f"{index}.{item}"
                print(row)
        case 'edit':
            number = input('Enter task number to edit: ')
            number = int(number) - 1
            new_task = input('Enter the new task: ')
            todos[number] = new_task
            print('Task successfully edited.')
        case 'exit':
            break

        case 'completed':
            number = int(input('Enter task number to mark completed: '))
            todos.pop(number - 1)

        case 'newfile':
            filenew = open('whatever.txt', 'w')
            file.close()

        case random_input:
            print('Please enter the correct input')




print('Thanks')

# Read function is exhaustive
# Once you open a file, cursor stats from beggining and when file.read happens, it goes till the end. If you use read
# again, it will read empty space ahead and an empty output. To fix this, use file.close and file.open again.