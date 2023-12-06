import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.LEFT, width=100)
    txt_sum = ft.TextField(value = "0", text_align = ft.TextAlign.END, width = 100)
    def minus_click(e):
        if int(txt_number.value) > 0:
            txt_number.value = str(int(txt_number.value) - 1)
            page.update()

    def plus_click(e):
        if int(txt_number.value) < 11:
            txt_number.value = str(int(txt_number.value) + 1)
            page.update()

        if int(txt_number.value) == 11:
            txt_sum.value = str(int(txt_sum.value) + 1)
            txt_number.value = "0"
            page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Column(
            [
                txt_sum,
            ]
        )
    )
ft.app(target=main, view=ft.AppView.WEB_BROWSER)