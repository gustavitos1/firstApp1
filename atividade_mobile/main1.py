import flet as ft


def main(page: ft.Page):
    page.title = "Nome de usuario"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667


    def mostrar_nome(e):
        txt_resultado.value = input_nome.value +" "+ input_sobrenome.value
        page.update()

    input_nome = ft.TextField(label="Nome de usuario" )
    input_sobrenome = ft.TextField(label="Sobrenome de usuario" )
    btn_enviar = ft.FilledButton(text="Enviar",
                                 width=page.window.width,
                                 on_click=mostrar_nome,
                                 )
    txt_resultado = ft.Text(value="")


    page.add(
        ft.Column(
            [
                input_nome,
                input_sobrenome,
                btn_enviar,
                txt_resultado
            ]
        )
    )


ft.app(main)