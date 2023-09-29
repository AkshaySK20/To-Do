todos = []
open('To-Do File.txt', 'r+', encoding='utf-8')

def show_item():
    with open("To-Do file.txt", 'r', encoding='utf-8') as file: #read from file only if the todos is empty.
        todos = file.readlines()

    for index, item in enumerate(todos):
        item = item.strip("\n")
        row = f"{index + 1}.{item}"
        print(row)
    print(f"Number of todos = {index+1}")

    return todos, index+1 #is there a need to return todos?
def write_item(todos):
    with open("To-Do file.txt", 'w', encoding="utf-8") as file:
        file.writelines(todos)
    return

while True:

    user_action = input("Do you want to add, show, edit, complete or exit?: ")
    #user_action = user_action.strip()

    match user_action:

        case "add":
            todos = show_item()
            to_do = input("Enter the todo: ") + "\n"

            todos.append(to_do)

            write_item(todos)
            print("Here is the updated todo list: ")
            show_item()

        case "show":
            show_item()

        case "edit":
            print('Here is the existing To-Dos:')
            todos = show_item()

            num = int(input("Enter the todo index number you want to edit: "))

            new_todo = input("Please enter the new todo: ") + "\n"
            todos[num-1] = new_todo
            write_item(todos)

            print(f"Here is the updated list of todos")
            show_item()


        # we have an inbuilt method of list __setitem__ which can be used to replace the object in the list. Eg:
        # todos.__setitem__(1, "Study") would mean the index 1 in the list will be replaced by "study" You can
        # find all the methods of list by executing - dir(list), __xxxxx__ are internal methods that the python uses generally
        case "complete":
            print("Here is the existing todo list: ")
            todos = show_item()
            Number = int(input("Please enter the number of the todo to mark it completed: "))

            todos[Number-1] = todos[Number-1].strip('\n') + " "+chr(10003) + "\n"
            print(f" {todos[Number-1]} has been set as completed!")

            write_item(todos)

            print('Here is the updated To-Do list:')
            show_item()

        case "delete":
            print('Here is the existing To-Dos:')

            todos = show_item()

            num = int(input(f"Please enter the todo number to delete from the list: "))
            deleted_todo = todos.pop(num-1)
            print(f"f The {deleted_todo} has been deleted from the list")

            write_item(todos)

        case "exit":
            break

        case _:
            print("Hey, you entered an unknown command!")

print("ok bye!")
