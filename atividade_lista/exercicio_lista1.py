import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from atividade_lista.models1 import *


def main(page: ft.Page):
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    input_nome = ft.TextField(label="Nome")
    input_profissao = ft.TextField(label="Profissão")
    input_salario = ft.TextField(label="Salário")

    list_view = ft.ListView(height=500)
    msg_sucesso = ft.SnackBar(
        content=ft.Text("Informações salvas com sucesso!"),
        bgcolor=Colors.GREEN,
    )
    msg_erro = ft.SnackBar(
        content=ft.Text("Preencha todos os campos!"),
        bgcolor=Colors.RED,
    )

    def salvar_informacoes(e):
        nome = input_nome.value
        profissao = input_profissao.value
        salario = input_salario.value

        if not (nome and profissao and salario):
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()
            return


        with Session() as session:
            novo_nome = User(nome=nome, profissao=profissao, salario=salario)
            session.add(novo_nome)
            session.commit()

        input_nome.value = ""
        input_profissao.value = ""
        input_salario.value = ""
        page.overlay.append(msg_sucesso)
        msg_sucesso.open = True
        page.update()
        exibir_lista()

    def exibir_lista():
        list_view.controls.clear()
        with Session() as session:
            nomes = session.query(User).all()
            for nome in nomes:
                informacoes = ft.ListTile(
                    leading=ft.Icon(ft.icons.MORE_VERT),
                    title=ft.Text(f"Nome: {nome.nome}"),
                    subtitle=ft.Column(
                        [
                            ft.Text(f"Profissão: {nome.profissao}"),
                            ft.Text(f"Salário: {nome.salario}"),
                        ]
                    ),
                )
                list_view.controls.append(informacoes)
        page.update()

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    input_profissao,
                    input_salario,
                    ft.ElevatedButton(
                        text="Salvar",
                        on_click=salvar_informacoes,
                    ),
                    ft.ElevatedButton(
                        text="Exibir Lista",
                        on_click=lambda _: page.go("/segunda"),
                    ),
                ],
            )
        )
        if page.route == "/segunda":
            exibir_lista()
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Lista de Informações"), bgcolor=Colors.SECONDARY_CONTAINER),
                        list_view,
                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        if page.views:
            top_view = page.views[-1]
            page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

ft.app(main)