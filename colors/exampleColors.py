import flet as ft

def main(page: ft.Page):
    
    container = ft.Container(
        width=200,
        height=200,
        # border=ft.border.all(1, ft.colors.BLACK),
        content=ft.FilledButton("Primary color"),
        theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.GREEN))
    )

    #Formas de cambiar el color a un texto:
    text = ft.Text("Write to Email: ")
    content_text = ft.TextField(label = "Email", color="#FF0000")
    button = ft.ElevatedButton("Send.", color = "#FF0000")
    # /////// #
    # text.color = ft.colors.RED  # Colores predefinidos en flet
    # /////// #
    # text.color = "#FF0000" #Colores en formato Hexadecimal
    # /////// #
    text.color = "#ffFF0000" #No transparente en Hexadecimal
    # /////// #
    # text.color = "#aaFF0000" #Transparente en Hexadecimal
    # /////// #
   

    page.add(
        ft.Row([
            text, 
            content_text,
            button
        ],
        alignment = ft.MainAxisAlignment.CENTER
        
        ),
        container
    )
    
ft.app(target=main)