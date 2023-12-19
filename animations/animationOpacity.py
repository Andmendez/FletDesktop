# easeOutCubic curve increases the animation value quickly at the beginning of the animation and then slows down until the target
# value is reached:

# animate_opacity
# animate_rotation
# animate_scale
# animate_offset
# animate_position
# animate (Container)

import flet as ft

def main(page: ft.Page):

    c = ft.Container(
        width=150,
        height=150,
        bgcolor="blue",
        border_radius=10,
        # Tiempo en el que se demora hacer la animacion
        animate_opacity=500,
    )

    def animate_opacity(e):
        # c.opacity = 0.5 if c.opacity == 1 else 1
        # c.update()
        # Forma para cambia la opacidad del contenedor, si la opacidad es uno que es de default cambia a 0.5 y al volver a llamar
        # la funcion se vuelve a 1.
        if c.opacity == 1:
            c.opacity = 0.5
            c.update()
        else:
            c.opacity = 1
            c.update()

    page.add(
        c,
        ft.ElevatedButton(
            "Animate opacity",
            on_click=animate_opacity,
        ),
    )

ft.app(target=main)