from datetime import datetime
import flet as ft

def main(page: ft.Page):
    page.title = "Мое первое приложение!"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []

    greeting_text = ft.Text("История приветствий:")
    text_hello = ft.Text(value="Hello world")

    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            now = datetime.now()
            time_str = (f"{now.year}:{now.month:02d}:{now.day:02d} - "f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}")

            message = f"{time_str} - Привет, {name}!"

            text_hello.value = message
            text_hello.color = None
            name_input.value = ""

            greeting_history.append(message)
            greeting_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            text_hello.value = "Введите корректное имя"
            text_hello.color = ft.Colors.RED

    def clear_history(_):
        greeting_history.clear()
        greeting_text.value = "История приветствий:"

    name_input = ft.TextField(label="Введите имя",on_submit=on_button_click,expand=True)

    send_button = ft.ElevatedButton("SEND",icon=ft.Icons.SEND,on_click=on_button_click)

    clear_button = ft.IconButton(icon=ft.Icons.DELETE,on_click=clear_history)

    main_row = ft.Row([name_input, send_button, clear_button])
    text_row = ft.Row([text_hello], alignment=ft.MainAxisAlignment.CENTER)

    page.add(text_row, main_row, greeting_text)

ft.app(target=main)
