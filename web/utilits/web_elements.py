import flet as ft

colors_dict = {
    "shadow": ft.colors.PURPLE_ACCENT,
}

names = ['knife','arrow','axe','pisol','shovel']
prices = []
descriptions = []


all_shadow = ft.BoxShadow(
    spread_radius=0.2,
    blur_radius=10,
    color=colors_dict["shadow"],
    offset=ft.Offset(0, 2.5),
    blur_style=ft.ShadowBlurStyle.SOLID,)


def handle_change_search_bar(e):
    search_query = search_bar.value.lower()
    filtered_list.controls.clear()  # Очистка предыдущих результатов
    if search_query:
        for name in names:
            if search_query in name.lower():
                filtered_list.controls.append(ft.ListTile(title=ft.Text(name)))
    e.page.update()
def handle_submit_search_bar(e):
    print("Search submitted:", search_bar.value)


# Контейнер для отображения отфильтрованных имен
filtered_list = ft.Column()

# Создание SearchBar
search_bar = ft.SearchBar(
    view_elevation=2,
    on_change=handle_change_search_bar,
    on_submit=handle_submit_search_bar,
    bar_leading=ft.Icon(ft.icons.SEARCH),
)

items_categories = []
for i in range(0, 10):
    items_categories.append(ft.Container(
        content=ft.Stack(controls=[
            ft.Image(src="https://img.freepik.com/free-photo/the-adorable-illustration-of-kittens-playing-in-the-forest-generative-ai_260559-483.jpg?size=338&ext=jpg&ga=GA1.1.2008272138.1724025600&semt=ais_hybrid",
                width=200,
                height=200,
                ),
                

            ft.Container(
                   content=ft.Text(f"category {i}",size=30,color=ft.colors.BACKGROUND,theme_style=ft.TextThemeStyle.BODY_LARGE),
                   alignment=ft.Alignment(0, 0),
                   


                   )]),
                
            
        alignment=ft.alignment.center,
        width=150,
        height=150,
        bgcolor=ft.colors.BLACK,
        border_radius=30,
        shadow=all_shadow,
    ))


categories = ft.Container(
    ft.Row(controls=items_categories, scroll=True, height=200,width=399,spacing=15,tight=100,vertical_alignment=ft.alignment.center), 
    height=200,
    width=399,
    margin=0,
    padding=0
)

items_product = []
for i in names:
    items_product.append(ft.Container(
        content=ft.Text(i,size=50),
        alignment=ft.alignment.center,
        width=399,
        height=100,
        border_radius=30,
        
        shadow=all_shadow,
        bgcolor=ft.colors.BLACK
        
    ))
products = ft.Container(content=ft.Column(controls=items_product),padding=10,margin=0)