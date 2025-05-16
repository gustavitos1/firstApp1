import flet as ft
from flet import *
from atividade_lista.models import *


def main(page: ft.Page):
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    listas = []

    def salvar_informacoes(e):
        if not (input_titulo.value and input_autor.value and input_categoria.value and input_descricao.value):
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            with Session() as session:
                obj_livro = Livro(
                    titulo=input_titulo.value,
                    autor=input_autor.value,
                categoria=input_categoria.value,
                descricao=input_descricao.value
                )
                session.add(obj_livro)
                session.commit()
                listas.append(obj_livro)
                input_titulo.value = ""
                input_autor.value = ""
                input_categoria.value = ""
                input_descricao.value = ""
                page.overlay.append(msg_sucesso)
                msg_sucesso.open = True
                page.update()
                exibir_lista(e)

    def exibir_lista(e):
        lv_livros.controls.clear()
        with Session() as session:
            livros = session.query(Livro).all()
            for livro in livros:
                lv_livros.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.BOOK),
                        title=ft.Text(f"Livro: {livro.titulo}"),
                        subtitle=ft.Text(f"Autor: {livro.autor}"),
                        trailing=ft.PopupMenuButton(
                            icon=ft.Icons.MORE_VERT,
                            items=[
                                ft.PopupMenuItem(
                                    text="Detalhes",
                                    on_click=lambda e, obj_livro=livro: exibir_detalhes(obj_livro)
                                )
                            ],
                        )
                    )
                )
        page.update()

    def exibir_detalhes(livro):
        page.go(f"/terceira/{livro.titulo}")

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=ft.Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_autor,
                    input_categoria,
                    input_descricao,
                    ft.ElevatedButton(
                        text="Salvar",
                        on_click=salvar_informacoes
                    ),
                    ft.ElevatedButton(
                        text="Exibir Lista",
                        on_click=lambda _: page.go("/segunda"),
                    )
                ],
            )
        )

        if page.route == "/segunda":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=ft.Text("Livros"), bgcolor=Colors.PRIMARY_CONTAINER),
                        lv_livros
                    ]
                )
            )

        if page.route.startswith("/terceira/"):
            livro_nome = page.route.split("/terceira/")[1]
            with Session() as session:
                livro_selecionado = session.query(Livro).filter_by(titulo=livro_nome).first()

            if livro_selecionado:
                page.views.append(
                    View(
                        "/terceira",
                        [
                            AppBar(title=ft.Text("Detalhes do Livro"), bgcolor=Colors.PRIMARY_CONTAINER),
                            ft.Text(f"Livro: {livro_selecionado.titulo}"),
                            ft.Text(f"Autor: {livro_selecionado.autor}"),
                            ft.Text(f"Categoria: {livro_selecionado.categoria}"),
                            ft.Text(f"Descrição: {livro_selecionado.descricao}"),
                            ft.ElevatedButton(text="Voltar", on_click=lambda _: page.go("/segunda"))  # Botão para voltar
                        ]
                    )
                )
        page.update()

    def voltar(e):
        page.views.pop()
        if page.views:
            top_view = page.views[-1]
            page.go(top_view.route)
        page.update()

    msg_sucesso = ft.SnackBar(
        content=ft.Text("Valor Salvo com Sucesso"),
        bgcolor=Colors.GREEN
    )
    msg_error = ft.SnackBar(
        content=ft.Text("Preencha todos os campos"),
        bgcolor=Colors.RED
    )

    input_titulo = ft.TextField(label="Titulo")
    input_autor = ft.TextField(label="Autor")
    input_categoria = ft.TextField(label="Categoria")
    input_descricao = ft.TextField(label="Descrição")

    lv_livros = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1
    )

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(target=main)
