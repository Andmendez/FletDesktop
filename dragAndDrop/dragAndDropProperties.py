import flet as ft

def main(page: ft.Page):
    page.title = "Drag and Drop example 2"

    def drag_accept(e):
        # obtener control arrastrable (fuente) por su ID
        src = page.get_control(e.src_id)
        # actualizar texto dentro del control arrastrable
        src.content.content.value = "0"
        # restablecer el grupo de origen, para que ya no se pueda colocar en un destino
        src.group = ""
        # actualizar texto dentro del control de destino de arrastre
        e.control.content.content.value = "1"
        # restablecer borde
        e.control.content.border = None
        page.update()

    def drag_will_accept(e):
        # borde blanco cuando se permite caer y amarillo cuando no
        e.control.content.border = ft.border.all(
            2, ft.colors.WHITE if e.data == "true" else ft.colors.YELLOW
        )
        e.control.update()

    def drag_leave(e):
        e.control.content.border = None
        e.control.update()

    page.add(
        ft.Row(
            [
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
#  mostrar un control diferente del contenido cuando la operación de arrastre está en marcha, en este caso cambia el color a rojo.
                    content_when_dragging=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.RED,
                        border_radius=5,
                    ),
# mostrar un control diferente debajo del puntero, en este caso una X
                    content_feedback=ft.Text("X"),
                ),
                ft.Container(width=100),
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
                    on_accept=drag_accept,
                    on_will_accept=drag_will_accept,
                    on_leave=drag_leave,
                ),
            ]
        )
    )

ft.app(target=main)