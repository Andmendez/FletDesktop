import flet as ft
import time

def main(page: ft.Page):
    ### //////////////////////////////////////////////////////////////////////////////////////// ###

# Buttons:
    # btn = ft.ElevatedButton("Click me!")
    
    # page.add(btn)

### //////////////////////////////////////////////////////////////////////////////////////// ###
### //////////////////////////////////////////////////////////////////////////////////////// ###

# Event handlers:

    # hello = ft.TextField()
    # hello.disabled = True
    # def suma(e):
    #     hello.value = "Hello"
    #     page.update()
    #     time.sleep(3)
    #     hello.value = " "
    #     page.update()

    # page.add(
    #     ft.ElevatedButton("Hello", on_click=suma),
    #     hello
    # )
### //////////////////////////////////////////////////////////////////////////////////////// ###

#TextBox
#Este codigo verifica si esta vacio al dar click en el boton, si lo esta carga un mensaje de error.
#Y si no limpia la pantalla y muesta Hello $name
    # def btn_click(e):
    #         if not txt_name.value:
    #             txt_name.error_text = "Please enter your name"
    #             page.update()
    #         else:
    #             name = txt_name.value
    #             page.clean()
    #             page.add(ft.Text(f"Hello, {name}!"))

    # txt_name = ft.TextField(label="Your name")

    # page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

### //////////////////////////////////////////////////////////////////////////////////////// ###

# Checkbox
# Al chulear el checkbox aparece un mensaje con un texto: True y al deschulearlo aparece ese texto pero con: False
    # def checkbox_changed(e):
    #         output_text.value = (
    #             f"You have learned how to ski :  {todo_check.value}."
    #         )
    #         page.update()

    # output_text = ft.Text()
    # todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
    # page.add(todo_check, output_text)



### //////////////////////////////////////////////////////////////////////////////////////// ###

# Dropdown
# Tiene multiples opciones de colores y al seleccionar uno y darle un boton aparece un texto: Color seleccionado
# en el caso de no seleccionar ninguno saldra texto: None
    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        label = "Colors:",
        width=300,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)


### //////////////////////////////////////////////////////////////////////////////////////// ###


ft.app(target=main)