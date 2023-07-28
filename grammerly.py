''' Fler Grammerly App '''
import flet as ft 



def main(page: ft.Page):
    ''' main function '''
    page.title = "Grammerly App"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.window_max_height = 600
    page.window_max_width = 700
    page.window_height = 600
    page.window_width = 700
    
    logo = ft.Image(src=f"logo.jpg", width=300)
    
    
    
    page.add(
        logo
    )


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")