import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors

def main(page: ft.Page):
    # Configurações
    page.title = "Cadastro de Profissões"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Dados
    lista_profissoes = []

    # Componentes - Home
    input_profissao = ft.TextField(label="Profissão")
    input_salario = ft.TextField(label="Salário", keyboard_type=ft.KeyboardType.NUMBER)
    msg_sucesso = ft.SnackBar(content=ft.Text("Profissão salva com sucesso!"), bgcolor=Colors.GREEN)
    msg_erro = ft.SnackBar(content=ft.Text("Preencha todos os campos."), bgcolor=Colors.RED)

    # Componentes - Segunda tela
    lv_profissoes = ft.ListView(height=500)

    # Funções
    def salvar_profissao(e):
        if input_profissao.value == "" or input_salario.value == "":
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()
        else:
            try:
                salario = float(input_salario.value)
                lista_profissoes.append({"profissao": input_profissao.value, "salario": salario})
                input_profissao.value = ""
                input_salario.value = ""
                page.overlay.append(msg_sucesso)
                msg_sucesso.open = True
                page.update()
            except ValueError:
                page.overlay.append(ft.SnackBar(content=ft.Text("Salário inválido."), bgcolor=Colors.ORANGE_ACCENT_700))
                page.update()

    def exibir_lista(e):
        lv_profissoes.controls.clear()
        for item in lista_profissoes:
            lv_profissoes.controls.append(
                ft.Text(f"{item['profissao']}: R$ {item['salario']:.2f}")
            )
        page.update()

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Cadastro"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_profissao,
                    input_salario,
                    ft.ElevatedButton("Salvar", on_click=salvar_profissao),
                    ft.ElevatedButton("Exibir Lista", on_click=lambda _: page.go("/lista")),
                ],
            )
        )
        if page.route == "/lista":
            exibir_lista(e)
            page.views.append(
                View(
                    "/lista",
                    [
                        AppBar(title=Text("Lista de Profissões"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_profissoes
                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Execução do aplicativo
ft.app(main)
