import flet as ft

def main(page: ft.Page):
    # Configuração de página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 375
    page.window_height = 667

    txt_result = ft.Text(value="")

    # Definição de funções
    def mostrar_numero(e):
        numero = int(input_numero.value)
        if numero % 2 == 0:
            txt_result.value = "é par"
        else:
            txt_result.value = "é impar"
        page.update()

    # Criação de componentes
    input_numero = ft.TextField(label="Numero")
    btn_send = ft.FilledButton(
        text="Enviar",
        width=page.window_width,
        on_click=mostrar_numero,
    )
    # Construir o layout
    page.add(
        ft.Column(
            [
                input_numero,
                btn_send,
                txt_result,
            ]
        )
    )



ft.app(main)