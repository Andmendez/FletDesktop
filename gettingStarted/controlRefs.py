import flet as ft

def main(page):
### //////////////////////////////////////////////////////////////////////////////////////// ###

#Al darle click al boton aparece en la parte de abajo un Hello Andres Forero
    # first_name = ft.TextField(label="First name", autofocus=True)
    # last_name = ft.TextField(label="Last name")
    # greetings = ft.Column()

    # def btn_click(e):
    #     greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
    #     first_name.value = ""
    #     last_name.value = ""
    #     page.update()
    #     first_name.focus()

    # page.add(
    #     first_name,
    #     last_name,
    #     ft.ElevatedButton("Say hello!", on_click=btn_click),
    #     greetings,
    # )


### //////////////////////////////////////////////////////////////////////////////////////// ###

#Uso de las referencias de control:

# Las referencias de control Flet sirven para almacenar una referencia a un control de la interfaz gráfica de usuario (GUI). Esto permite acceder al control de forma segura y eficiente, sin necesidad de preocuparse por su vida útil.

# Las referencias de control Flet se pueden utilizar para las siguientes tareas:

# Acceder a las propiedades y métodos del control.
# Escuchar los eventos del control.
# Modificar el contenido del control.
  
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def btn_click(e):
        greetings.current.controls.append(
            ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!")
        )
        first_name.current.value = ""
        last_name.current.value = ""
        page.update()
        first_name.current.focus()

    page.add(
        ft.TextField(ref=first_name, label="First name", autofocus=True),
        ft.TextField(ref=last_name, label="Last name"),
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        ft.Column(ref=greetings),
    )

    #Ahora podemos ver claramente en page.add() la estructura de la página y todos los controles que la componen.

### //////////////////////////////////////////////////////////////////////////////////////// ###
ft.app(target=main)