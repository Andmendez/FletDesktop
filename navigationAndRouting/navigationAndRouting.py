# import flet as ft
# Nos indica en que pagina estamos actuamente. PAra abrir otra se agrega /nameEnlace
# def main(page: ft.Page):
#     page.add(ft.Text(f"Initial route: {page.route}"))

#     def route_change(e: ft.RouteChangeEvent):
#         page.add(ft.Text(f"New route: {e.route}"))

#     page.on_route_change = route_change
#     page.update()

# ft.app(target=main, view=ft.AppView.WEB_BROWSER)

#Nos permite abrir una ruta de la pagina con un boton:
# import flet as ft

# def main(page: ft.Page):
#     page.add(ft.Text(f"Initial route: {page.route}"))

#     def route_change(e: ft.RouteChangeEvent):
#         page.add(ft.Text(f"New route: {e.route}"))

#     def go_store(e):
#         page.route = "/store"
#         page.update()
# #Ir a la pagina /store
#     page.on_route_change = route_change
#     page.add(ft.ElevatedButton("Go to Store", on_click=go_store))

# ft.app(target=main, view=ft.AppView.WEB_BROWSER)

# En resumen, este código define una aplicación Flet de una sola página con dos rutas (/ y /store). Cada ruta tiene su propia vista
# con elementos de interfaz de usuario, como barras de aplicación y botones. La aplicación utiliza eventos para gestionar cambios de
# ruta y la navegación entre vistas. 

import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            # Vista de la pagina principal
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    # Boton para ir a /store
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                # Vista de la pagina Store
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        # Boton para volver a home
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
# Se llama cada vez que hay un cambio en la ruta (URL) de la página
    page.on_route_change = route_change
# Esta función se llama cuando se desea volver a la vista anterior.
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)