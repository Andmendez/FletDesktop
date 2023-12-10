# Para aumentar la usabilidad de su programa y presentar los resultados a un usuario lo antes posible, puede enviar actualizaciones
# de la página en lotes.

import flet as ft

def main(page: ft.Page):

    # add ListView to a page first
    lv = ft.ListView(expand=1, spacing=10, item_extent=50)
    page.add(lv)

    for i in range(5100):
        lv.controls.append(ft.Text(f"Line {i}"))
        # send page to a page
        if i % 500 == 0:
            page.update()
    # send the rest to a page
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)