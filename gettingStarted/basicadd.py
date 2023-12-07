import flet as ft
import time

def main(page: ft.Page):

### //////////////////////////////////////////////////////////////////////////////////////// ###

    # t = ft.Text()
    # page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

    # for i in range(1, 10+1):
    #     t.value = f"Step {i}" #->permite la interpolación directa de variables y expresiones dentro de una cadena.
    #     # t.value = "Step",i -> Funciona pero lo muestra dentro de parentesis
    #     page.update()
    #     time.sleep(1)

### //////////////////////////////////////////////////////////////////////////////////////// ###

# Esto hace que se adicione en fila

    # page.add(
    #     ft.Row(controls=[
    #         ft.TextField(label="Your name"),
    #         ft.ElevatedButton(text="Say my name!")
    #     ])
    # )
    # page.update()

### //////////////////////////////////////////////////////////////////////////////////////// ###
# Cuenta de 1 a 10 y imprime en pantalla pero cuando i > 4 comienza a elminar la posicion 0 y nos quedara en pantalla del 7 al 10
    for i in range(1, 10+1):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0) #Elimina la posicion 0
        page.update()
        time.sleep(0.3)



ft.app(target=main)