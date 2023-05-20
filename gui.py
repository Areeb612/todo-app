import functions
import PySimpleGUI as psg

label = psg.Text("Type in a to-do.")
input_box = psg.InputText(tooltip="Enter to-do")
add_button = psg.Button(button_text="Add")

window = psg.Window("My To-do App!", layout=[[label], [input_box, add_button]])
window.read()
window.close()
