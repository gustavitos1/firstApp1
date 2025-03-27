import flet as ft

def main(page: ft.Page):
    # Configuração de página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 375
    page.window_height = 667

    # Definição de funções
    def somar(e):
        soma = int(num1_input.value) + int(num2_input.value)
        txt_result.value = str(soma)
        page.update()

    def subtracao(e):
        subtracao = int(num1_input.value) - int(num2_input.value)
        txt_result.value = str(subtracao)
        page.update()

    def multiplica(e):
        multiplicacao = int(num1_input.value) * int(num2_input.value)
        txt_result.value = str(multiplicacao)
        page.update()

    def divide(e):
        divisao = int(num1_input.value) / int(num2_input.value)
        txt_result.value = str(divisao)
        page.update()

    # Criação de componentes
    num1_input = ft.TextField(label="Digite um numero: ")
    num2_input = ft.TextField(label="Digite um numero: ")
    btn_sendmais = ft.FilledButton(
        text="Somar",
        width=page.window_width,
        on_click=somar,
    )
    btn_sendmenos = ft.FilledButton(
        text="Subtrair",
        width=page.window_width,
        on_click=subtracao,
    )
    btn_sendmultiplica = ft.FilledButton(
        text="Multiplicar",
        width=page.window_width,
        on_click=multiplica,
    )
    btn_senddivide = ft.FilledButton(
        text="Dividir",
        width=page.window_width,
        on_click=divide,
    )
    txt_result = ft.Text(value="")

    # Construir o layout
    page.add(
        ft.Column(
            [
                num1_input,
                num2_input,
                btn_sendmais,
                btn_sendmenos,
                btn_sendmultiplica,
                btn_senddivide,
                txt_result
            ]
        )
    )



ft.app(main)