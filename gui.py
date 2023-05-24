import functions
import PySimpleGUI as psg

label = psg.Text("Type in a to-do.")
input_box = psg.InputText(tooltip="Enter to-do", key="todo")
add_button = psg.Button(button_text="Add")
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")
list_box = psg.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[44, 10])

window = psg.Window("My To-do App!",
                    layout=[[label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=("Helvetica", 12), )

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            window['todos'].update(values=todos)
            todos_add = functions.write_todos(todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todos = functions.get_todos()
            todo_to_complete = values['todos'][0]
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Exit":
            exit()
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case psg.WIN_CLOSED:
            break


window.close()
