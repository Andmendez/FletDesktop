# import os
# import flet as ft

# # At the start of the program we akkre setting the value of FLET_WS_MAX_MESSAGE_SIZE environment variable to 8000000 - this is the maximum size of WebSocket message
# # in bytes that can be received by Flet Server rendering the page. Default size is 1 MB, but the size of JSON message describing 5,000 container controls would exceed
# # 1 MB, so we are increasing allowed size to 8 MB.


# os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

# def main(page: ft.Page):
#     r = ft.Row(wrap=True, scroll="always", expand=True)
#     page.add(r)

#     for i in range(5000):
#         r.controls.append(
#             ft.Container(
#                 ft.Text(f"Item {i}"),
#                 width=100,
#                 height=100,
#                 alignment=ft.alignment.center,
#                 bgcolor=ft.colors.AMBER_100,
#                 border=ft.border.all(1, ft.colors.AMBER_400),
#                 border_radius=ft.border_radius.all(5),
#             )
#         )
#     page.update()

# ft.app(target=main, view=ft.AppView.WEB_BROWSER)


###         //////////         ###
# Implementado GridView el programa es mas fluido y mas estetico
import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page: ft.Page):
    gv = ft.GridView(expand=True, max_extent=100, child_aspect_ratio=1)
    page.add(gv)

    for i in range(5000):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Item {i}", color = ft.colors.BLACK),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )
        if i % 90 == 0:
            page.update()
    page.update()


ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)