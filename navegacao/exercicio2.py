import flet as ft
from flet import *


def main(page: ft.Page):
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 700

    input_livro = ft.TextField(label="digite um livro")
    input_autor = ft.TextField(label="digite o autor")
    input_categoria = ft.TextField(label="digite a categoria")
    input_descricao = ft.TextField(label="coloque uma descrição")

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_livro,
                    input_autor,
                    input_categoria,
                    input_descricao,
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
                        ft.Text(f"Livro: {input_livro.value}"),
                        ft.Text(f"Autor: {input_autor.value}"),
                        ft.Text(f"Categoria: {input_categoria.value}"),
                        ft.Text(f"Descrição: {input_descricao.value}"),
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

