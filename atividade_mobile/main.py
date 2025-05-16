import flet as ft

def main(page: ft.Page):
    # Configuração de página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 375
    page.window_height = 667

    # Definição de funções
    def mostrar_nome(e):
        txt_result.value = input_nome.value
        page.update()

    # Criação de componentes
    input_nome = ft.TextField(label="Nome", hint_text="Digite seu nome")
    btn_send = ft.FilledButton(
        text="Enviar",
        width=page.window_width,
        on_click=mostrar_nome,
    )
    txt_result = ft.Text(value="")

    # Construir o layout
    page.add(
        ft.Column(
            [
                input_nome,
                btn_send,
                txt_result
            ]
        )
    )



ft.app(main)