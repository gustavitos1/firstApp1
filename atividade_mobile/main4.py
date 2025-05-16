import flet as ft
from datetime import datetime

def main(page: ft.Page):
    # Configuração de página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 375
    page.window_height = 667

    txt_result = ft.Text(value="")

    # Definição de funções
    def calcular_data(e):
        try:
            data_nascimento = datetime.strptime(input_data.value, "%d/%m/%Y")
            idade = 2025 - data_nascimento.year
            if idade == 0:
                txt_result.value = "invalido"
            elif  idade >= 18:
                txt_result.value = "é maior de idade"
            else:
                txt_result.value = "é menor de idade"
            page.update()
        except ValueError:
            txt_result.value = "Data inválida, Use o formato DD/MM/YYYY"


    # Criação de componentes
    input_data = ft.TextField(label="Data", hint_text="Escreva sua Data de Nascimento Ex:12/3/2006")
    btn_send = ft.FilledButton(
        text="Enviar",
        width=page.window_width,
        on_click=calcular_data,
    )

    # Construir o layout
    page.add(
        ft.Column(
            [
                input_data,
                btn_send,
                txt_result
            ]
        )
    )



ft.app(main)