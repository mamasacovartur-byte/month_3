import flet as ft
import os

def main(page: ft.Page):
    page.title = "Мое первое приложение!"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []

    greeting_text = ft.Text('История приветствий:')
    text_hello = ft.Text(value='Hello world')

    if os.path.exists("history.txt"):
        with open("history.txt", "r", encoding="utf-8") as file:
            greeting_history = file.readlines()
            greeting_history = [i.strip() for i in greeting_history]

        greeting_text.value = 'История приветствий:\n' + "\n".join(greeting_history)

    def on_button_click(_):
        name = name_input.value.strip()
        print(name)

        if name:
            text_hello.color = None
            text_hello.value = f"Hello {name}"
            name_input.value = None

            greeting_history.append(name)

            greeting_history[:] = greeting_history[-5:]

            greeting_text.value = 'История приветствий:\n' + "\n".join(greeting_history)

            with open("history.txt", "w", encoding="utf-8") as file:
                file.write("\n".join(greeting_history))
        else:
            text_hello.value = 'Введите корректное имя'
            text_hello.color = ft.Colors.RED

        # page.update()

    elevated_button = ft.ElevatedButton('SEND',icon=ft.Icons.SEND,on_click=on_button_click)

    def clear_history(_):
        greeting_history.clear()
        greeting_text.value = 'История приветствий:'

        with open("history.txt", "w", encoding="utf-8") as file:
            file.write("")

        # page.update()

    clear_button = ft.IconButton(icon=ft.Icons.DELETE,on_click=clear_history)

    name_input = ft.TextField(label='Введите имя',on_submit=on_button_click,expand=True)

    main_object = ft.Row([name_input, elevated_button, clear_button])
    text_row = ft.Row([text_hello], alignment=ft.MainAxisAlignment.CENTER)

    page.add(text_row, main_object, greeting_text)

ft.app(target=main)

