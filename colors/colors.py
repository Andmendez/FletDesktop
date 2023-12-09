
# El valor hexadecimal debe tener el formato #aarrggbb (0xaarrggbb) o #rrggbb (0xeeggbb). En caso de que se omita aa (opacidad),
# se establece en ff (no transparente).
import flet as ft
import themes as theme

# c1 = ft.Container(bgcolor='#ff0000')
# c1 = ft.Container(bgcolor=ft.colors.YELLOW)

def main(page: ft.Page):          
    
    container = ft.Container(
        width=200,
        height=200,
        border=ft.border.all(1, ft.colors.BLACK),
        content=ft.FilledButton("Primary color"),
        theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.YELLOW))
    )
        
    page.add(container)


ft.app(target=main) 