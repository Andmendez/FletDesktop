import flet as ft

def main(page: ft.Page):
    page.title = "Drag and Drop example"

    def drag_accept(e):
        # obtener control arrastrable (fuente) por su ID
        src = page.get_control(e.src_id)
        # actualizar texto dentro del control arrastrable
        src.content.content.value = "0"
        # actualizar texto dentro del control de destino de arrastre
        e.control.content.content.value = "1"
        page.update()

    page.add(
        ft.Row(
            [
# Objeto que se puede arrastrrar, ambos objetos pertenecen al mismo grupo:
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                ),
# Separacion entre los dos cuadrados
                ft.Container(width=100),
# Objeto que recibe el otro objeto:
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center,
                    ),
#  es responsabilidad del desarrollador determinar qué sucede con los controles de "fuente" (arrastrable) y "destino"
# (destino de arrastre) cuando ocurre el evento on_accept.
                    on_accept=drag_accept,
                ),
            ]
        )
    )

ft.app(target=main)