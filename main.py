# from functions import get_todos, write_todos
import functions
import time

print("Welcome to the to-do list. Options are given below.")
time = time.strftime("%b %d, %Y %H:%M %p")
print(f"Today is {time}")

while True:     
    user_action = input("Type add, show, replace, remove , or exit: ")

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo.capitalize())

        functions.write_todos(todos)

    elif user_action.startswith("show"):    # Operator '|' can be used in 'if' statements for more complex conditions
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]  Example of list comprehension

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("replace"):
        try:
            todos = functions.get_todos()

            number = int(user_action[8:])
            number = number - 1

            new_todo = input("Enter a new todo: ")
            new_todo = new_todo.title()
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("You entered an incorrect command.")
            continue

    elif user_action.startswith("remove"):
        try:
            number = int(user_action[7:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index]
            todo_to_remove = todo_to_remove.strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"The todo '{todo_to_remove}' was removed from the list.")
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

print("Thanks for using!")
