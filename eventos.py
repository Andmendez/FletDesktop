import flet as ft

def main(page = ft.Page):

### //////////////////////////////////////////////////////////////////////////////////////// ###
# Al darle click al boton llama la funcion que hace que aparezca el texto Clicked!
    # def button_clicked(e):
    #     page.add(ft.Text("Clicked!"))

    # page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))
    # page.update()
### //////////////////////////////////////////////////////////////////////////////////////// ###

#Al darle click al boton add una checkbox con el nombre que se le dio en el textField.

    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
    page.update()


ft.app(target=main)