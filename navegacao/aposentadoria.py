import flet as ft
from flet import *


def main(page: ft.Page):
    page.title = "INSS Simulador de Aposentadoria"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    idade = ft.TextField(label="Idade", keyboard_type=ft.KeyboardType.NUMBER)
    genero = ft.Dropdown(
        label="Genero",
        options=[
            ft.dropdown.Option("Masculino", "Masculino"),
            ft.dropdown.Option("Feminino", "Feminino"),
        ],
    )
    contribuicao = ft.TextField(
        label="Anos de Contribuição", keyboard_type=ft.KeyboardType.NUMBER
    )
    media_salarial = ft.TextField(
        label="Média salarial", keyboard_type=ft.KeyboardType.NUMBER
    )


    aposentadoria_idade = ft.Radio(label="Idade", value="Idade")
    aposentadoria_contrib = ft.Radio(label="Contribuição", value="Contribuição")
    aposentadoria_tipo = ft.RadioGroup(
        content=ft.Column(
            [
                aposentadoria_idade,
                aposentadoria_contrib,
            ]
        )
    )

    def calculos(e):
        try:
            idade_value = int(idade.value)
            contribuicao_value = int(contribuicao.value)
            media_salarial_value = float(media_salarial.value)

            beneficio = (0.6 * media_salarial_value) + (
                (contribuicao_value - 15) * 0.02 * media_salarial_value
            )

            if genero.value == "Masculino":
                if aposentadoria_tipo.value == "Idade":
                    if 65 >= idade_value >= 16 and contribuicao_value > 15:
                        txt_resultado.value = (
                            f"Você pode se aposentar por idade, beneficio: {beneficio:.2f}R$"
                        )
                        txt_resultado.color = colors.GREEN
                    elif idade_value < 16 or contribuicao_value < 15:
                        txt_resultado.value = "Você não pode se aposentar por idade ainda."
                        txt_resultado.color = colors.RED
                elif aposentadoria_tipo.value == "Contribuição":
                    if 90 >= contribuicao_value >= 35:
                        txt_resultado.value = (
                            f"Você pode se aposentar por tempo de Contribuição, beneficio: {beneficio:.2f}R$"
                        )
                        txt_resultado.color = colors.GREEN
                    elif contribuicao_value < 35:
                        txt_resultado.value = (
                            "Você ainda não pode se aposentar por contribuição."
                        )
                        txt_resultado.color = colors.RED
            elif genero.value == "Mulher":
                if aposentadoria_tipo.value == "Idade":
                    if 62 >= idade_value >= 16 and contribuicao_value > 15:
                        txt_resultado.value = (
                            f"Você pode se aposentar por idade, beneficio: {beneficio:.2f}R$"
                        )
                        txt_resultado.color = colors.GREEN
                    elif idade_value < 16 or contribuicao_value < 15:
                        txt_resultado.value = "Você não pode se aposentar por idade ainda."
                        txt_resultado.color = colors.RED
                elif aposentadoria_tipo.value == "Contribuição":
                    if 90 >= contribuicao_value >= 30:
                        txt_resultado.value = (
                            f"Você pode se aposentar por tempo de Contribuição, beneficio: {beneficio:.2f}R$"
                        )
                        txt_resultado.color = colors.GREEN
                    elif contribuicao_value < 30:
                        txt_resultado.value = (
                            "Você ainda não pode se aposentar por contribuição."
                        )
                        txt_resultado.color = colors.RED

            page.go("/resultado")
            page.update()
        except ValueError:
            txt_resultado.value = "Por favor insira valores validos"
            txt_resultado.color = colors.ORANGE
            page.update()

    # Calculate Button
    botao_calcular = ft.ElevatedButton(
        text="Calcular Aposentadoria", on_click=calculos
    )

    txt_resultado = ft.Text(value="")

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(Image(src="../static/inss.png"), title=ft.Text("INSS Simulador de Aposentadoria"), bgcolor=ft.Colors.PRIMARY_CONTAINER),
                    ft.ElevatedButton(
                        text="Simular Aposentadoria", on_click=lambda _: page.go("/segunda")
                    ),
                    ft.ElevatedButton(
                        text="Ver Regras", on_click=lambda _: page.go("/terceira")
                    ),
                    Container(
                        Image(src="../static/guaxas.png", width=90, height=90),
                        alignment=ft.alignment.bottom_right,
                        expand=True
                    )
                ],
            )
        )
        if page.route == "/segunda":
            page.views.append(
                ft.View(
                    "/segunda",
                    [
                        ft.AppBar(
                            title=ft.Text("Simular aposentadoria"),
                            bgcolor=ft.Colors.PRIMARY_CONTAINER,
                        ),
                        idade,
                        ft.Text("Genero:"),
                        genero,
                        contribuicao,
                        media_salarial,
                        ft.Text("Tipo de aposentadoria:"),
                        aposentadoria_tipo,
                        botao_calcular,
                    ],
                )
            )
        if page.route == "/terceira":
            page.views.append(
                ft.View(
                    "/terceira",
                    [
                        ft.AppBar(
                            title=ft.Text("Regras de Aposentadoria"),
                            bgcolor=ft.Colors.PRIMARY_CONTAINER,
                        ),
                        ft.Text("⚠️ Confira as regras de aposentadoria:"),
                        ft.Text("Por idade:"),
                        ft.Text(
                            "👴 - Homem - Para se aposentar é necessário ter ao menos 65 anos de idade e 15 anos de contribuição"
                        ),
                        ft.Text(
                            "👵 - Mulher - Para se aposentar é necessário ter ao menos 62 anos de idade e 15 anos de contribuição"
                        ),
                        ft.Text("-" * 120),
                        ft.Text("Por Tempo de Contribuição:"),
                        ft.Text("👴 - Homem - 35 anos de contribuição"),
                        ft.Text("👵 - Mulher - 30 anos de contribuição"),
                        ft.Text("-" * 120),
                        ft.Text("Valor Estimado do Beneficio:"),
                        ft.Text(
                            "O valor da aposentadoria será uma média de 60% da média salarial informada, acrescido de 2% por ano que exceder o tempo minimo de contribuição."
                        ),
                    ],
                )
            )
        if page.route == "/resultado":
            page.views.append(
                ft.View(
                    "/resultado",
                    [
                        ft.AppBar(
                            title=ft.Text("Resultado da Simulação"),
                            bgcolor=ft.Colors.PRIMARY_CONTAINER,
                        ),
                        txt_resultado,
                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(main)