import flet as ft
from flet import *

class Livro():
    def __init__(self, livro, autor, categoria, descricao):
        self.livro = livro
        self.autor = autor
        self.categoria = categoria
        self.descricao = descricao


def main(page: ft.Page):
    # Configuração de página
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    listas = []

    def salvar_informacoes(e):
        if input_livro.value and input_autor and input_categoria and input_descricao == "":
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            obj_livro = Livro(
                livro=input_livro.value,
                autor=input_autor.value,
                categoria=input_categoria.value,
                descricao=input_descricao.value)
            listas.append(obj_livro)
            input_livro.value = ""
            input_autor.value = ""
            input_categoria.value = ""
            input_descricao.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()

    def exibir_lista(e):
        lv_livros.controls.clear()
        for livro in listas:
            lv_livros.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f"Livro - {livro.livro}"),
                    subtitle=ft.Column(
                        [
                            ft.Text(f"Autor - {livro.autor}"),
                            ft.Text(f"Categoria - {livro.categoria}"),
                            ft.Text(f"Descricao - {livro.descricao}")
                        ]
                    )

                )
            )

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
                        ft.Button(
                            text="Salvar",
                            on_click=lambda _: salvar_informacoes(e)
                        ),
                        ft.Button(
                            text="Exibir Lista",
                            on_click=lambda _: page.go("/segunda"),
                        )
                    ],
                )
            )
            if page.route=="/segunda":
                exibir_lista(e)
                page.views.append(
                    View(
                        "/segunda",
                        [
                            AppBar(title=Text("segunda"), bgcolor=Colors.PRIMARY_CONTAINER),
                            lv_livros
                        ]
                    )
                )
            page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    msg_sucesso = ft.SnackBar(
        content=ft.Text("Valor Salvo com Sucesso"),
        bgcolor=Colors.GREEN
    )
    msg_error = ft.SnackBar(
            content=ft.Text("O valor não pode estar vazio"),
            bgcolor=Colors.RED
        )

    input_livro = ft.TextField(label="Livro")
    input_autor = ft.TextField(label="Autor")
    input_categoria = ft.TextField(label="Categoria")
    input_descricao = ft.TextField(label="Descricao")


    lv_livros = ft.ListView(
            height=500,
            spacing=1,
            divider_thickness=1
        )

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(main)

