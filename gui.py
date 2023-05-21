import functions
import PySimpleGUI as psg

label = psg.Text("Type in a to-do.")
input_box = psg.InputText(tooltip="Enter to-do", key="to-do")
add_button = psg.Button(button_text="Add")

window = psg.Window("My To-do App!",
                    layout=[[label], [input_box, add_button]],
                    font=("Helvetica", 12), )

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["to-do"] + "\n"
            todos.append(new_todo)
            todos_add = functions.write_todos(todos)
        case psg.WIN_CLOSED:
            break


window.close()
