import flet as ft
from flet import *


def main(page: ft.Page):
    # Configuração de página
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 700

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    ElevatedButton(text="navegar", on_click=lambda _: page.go("/segunda")),
                ],
            )
        )
        if page.route=="/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("segunda"), bgcolor=Colors.PRIMARY_CONTAINER),
                    ]
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

