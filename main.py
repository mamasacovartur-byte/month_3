from db import main_db
import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT


    task_list = ft.Column(spacing=25)



    def view_task(task_id, task_text):
        task_field = ft.TextField(read_only=True, value=task_text, expand=True)


        def enable_edit(e):
            task_field.read_only = not task_field.read_only
            page.update()

        edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=enable_edit)


        def save_task(e):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            page.update()

        save_button = ft.IconButton(icon=ft.icons.SAVE, on_click=save_task)


        task_row = ft.Row([task_field, edit_button, save_button])


        def delete_task(e):
            main_db.delete_task(task_id=task_id)
            if task_row in task_list.controls:
                task_list.controls.remove(task_row)


        delete_button = ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=delete_task)

        task_row.controls.append(delete_button)

        return task_row


    def add_task_db(_):
        if task_input.value:
            task_text = task_input.value
            new_task_id = main_db.add_task(task=task_text)
            task_list.controls.append(view_task(task_id=new_task_id, task_text=task_text))
            task_input.value = None
            page.update()


    task_input = ft.TextField(label="Введите задачу", expand=True, on_submit=add_task_db)
    task_add_button = ft.IconButton(icon=ft.icons.ADD, on_click=add_task_db)

    input_row = ft.Row([task_input, task_add_button])

    page.add(input_row, task_list)


if __name__ == "__main__":
    main_db.init_db()
    ft.run(main)