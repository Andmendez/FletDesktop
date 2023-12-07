# <h1>ESTRUCTURA</h1>

# Importamos la libreria y se usara con ft
import flet as ft



# Funcion principal en la cual va toda la interfaz que se ira agregando
def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()
    # add/update controls on Page
    
# Configura la aplicacion grafica y al iniciar la app se ejecutara el main como entrada principal.
ft.app(target=main)



#Internamente, cada aplicación Flet es una aplicación web e incluso si se abre en una ventana del sistema operativo nativo, un servidor
#web integrado aún se inicia en segundo plano. En este caso se le asigno el puerto 8080
# ft.app(port=8080, target=main)
# http://localhost:<port>



# Para poder ejecutar la app en la web se debe cambiar el ft.app(target = main) a
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)