# IMPORTANT

# key - a textual representation of a pressed key, e.g. A, Enter or F5.
# shift - True if "Shift" key is pressed.
# ctrl - True if "Control" key is pressed.
# alt - True if "Alt" ("Option") key is pressed.
# meta - True if "Command" key is pressed.

# En resumen, este código crea una aplicación que muestra información sobre las teclas presionadas (tecla específica y estado de las
# teclas modificadoras) cada vez que se presiona una tecla, y le pide al usuario que presione teclas con combinaciones específicas de
# CTRL, ALT, SHIFT y META.

import flet as ft

def main(page: ft.Page):
    def on_keyboard(e: ft.KeyboardEvent):
        page.add(
            ft.Text(
                f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
            )
        )

    page.on_keyboard_event = on_keyboard
    page.add(
        ft.Text("Press any key with a combination of CTRL, ALT, SHIFT and META keys...")
    )

ft.app(target=main)