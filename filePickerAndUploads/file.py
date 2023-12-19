# File picker control opens a native OS dialog for selecting files and directories.
# File picker allows opening three dialogs:
    # Pick files - one or multiple, any files or only specific types.
    # Save file - choose directory and file name.
    # Get directory - select directory.

# When running Flet app in a browser only "Pick files" option is available and it's used for uploads only as it, obviously, doesn't
# return a full path to a selected file.


# import flet as ft

# file_picker = ft.FilePicker()
# page.overlay.append(file_picker)
# page.update()

# ft.ElevatedButton("Choose files...",
#     on_click=lambda _: file_picker.pick_files(allow_multiple=True))


# import flet as ft

# def on_dialog_result(e: ft.FilePickerResultEvent):
#     print("Selected files:", e.files)
#     print("Selected file or directory:", e.path)

# file_picker = ft.FilePicker(on_result=on_dialog_result)


# import flet as ft

# def upload_files(e):
#     upload_list = []
#     if file_picker.result != None and file_picker.result.files != None:
#         for f in file_picker.result.files:
#             upload_list.append(
#                 FilePickerUploadFile(
#                     f.name,
#                     upload_url=page.get_upload_url(f.name, 600),
#                 )
#             )
#         file_picker.upload(upload_list)

# ft.ElevatedButton("Upload", on_click=upload_files)

# ft.app(target=main, upload_dir="uploads")

# ft.app(target=main, assets_dir="assets", upload_dir="assets/uploads")

# page.add(ft.Image(src="/uploads/<some-uploaded-picture.png>"))

import flet as ft

def main(page : ft.Page):

    page.add(
        ft.ElevatedButton("Select files...", icon=ft.icons.FOLDER_OPEN, on_click=lambda _: file_picker.pick_files(allow_multiple=True)
        )
    )


ft.app(target=main)