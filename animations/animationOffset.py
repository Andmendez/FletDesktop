import flet as ft
cont = 0
def main(page: ft.Page):
    
    c = ft.Container(
        width=150,
        height=150,
        bgcolor="blue",
        border_radius=10,
        offset=ft.transform.Offset(-2, -2),
        animate_offset=ft.animation.Animation(1000),
    )

    def animate(e):
        global cont
        if cont == 0:
            c.offset = ft.transform.Offset(0, 0)
            cont = 1
            c.update()
            
        else:
            c.offset = ft.transform.Offset(-2, -2)
            cont = 0
            c.update()

    page.add(
        c,
        ft.ElevatedButton("Reveal!", on_click=animate),
    )

ft.app(target=main)