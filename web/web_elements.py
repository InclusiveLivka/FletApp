import flet as ft
import database.engine as engine


all_categories = engine.read_categories()
names = ['product']

colors_dict = {
    "shadow": ft.colors.PURPLE_ACCENT,
}

all_shadow = ft.BoxShadow(
    spread_radius=0.2,
    blur_radius=10,
    color=colors_dict["shadow"],
    offset=ft.Offset(0, 2.5),
    blur_style=ft.ShadowBlurStyle.SOLID,)


items_categories = []
for i in range(0, 10):
    items_categories.append(ft.Container(
        content=ft.Stack(controls=[
            ft.Image(src="https://img.freepik.com/free-photo/the-adorable-illustration-of-kittens-playing-in-the-forest-generative-ai_260559-483.jpg?size=338&ext=jpg&ga=GA1.1.2008272138.1724025600&semt=ais_hybrid",
                     width=200,
                     height=200,

                     ),
            ft.Container(
                content=ft.Text(
                    f"category {i}", size=30, color=ft.colors.BACKGROUND, theme_style=ft.TextThemeStyle.BODY_LARGE),
                alignment=ft.Alignment(0, 0),

                on_click=lambda e, category=i: print(category),
            )]),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        bgcolor=ft.colors.BLACK,
        border_radius=30,
        shadow=all_shadow,
    ))


categories = ft.Container(
    ft.Row(controls=items_categories, scroll=True, height=200, width=399,
           spacing=15, tight=100, vertical_alignment=ft.alignment.center),
    height=200,
    width=399,
    margin=0,
    padding=0
)


page_product_add = ft.Container(
    content=ft.Column(
        controls=[
            ft.Text("Product add"),
            ft.TextField(label="Name"),
            ft.TextField(label="Price"),
            ft.TextField(label="Description"),
            ft.Dropdown(label="Categories", options=[
                        ft.dropdown.Option(category[0]) for category in all_categories]),
            ft.Row(
                controls=[ft.FloatingActionButton(
                    text="Добавить продукт", width=150), ft.FloatingActionButton(icon=ft.icons.IMAGE)],
            )
        ]))

