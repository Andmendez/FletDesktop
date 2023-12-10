import flet as ft


def main(page: ft.Page):
    # En este ejemplo carga 5000 textos y habilita la opcion de scroll, pero es muy lenta la pagina.
    # for i in range(5000):
    #     page.controls.append(ft.Text(f"Line {i}"))
    # page.scroll = "always"
    # page.update()

    # En este ejemplo carga 5000 textos y habilita la opcion de scroll, pero es muy lenta la pagina.
    lv = ft.ListView(expand = True, spacing=10)
    for i in range(5000):
        lv.controls.append(ft.Text(f"Line {i}"))
    page.add(lv)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)