''' Fler Grammerly App '''
import flet as ft
from standardenglish import StandardEnglish



def main(page: ft.Page):
    ''' main function '''
    page.title = "Grammerly App"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.window_max_height = 600
    page.window_max_width = 700
    page.window_height = 600
    page.window_width = 700
    page.window_frameless = True
    
    logo = ft.Image(src="logo.jpg", width=300)
    user_input = ft.TextField(hint_text="Enter your sentence...", border_radius=30)
    output_text = ft.Text(value="Your response will be generated shortly...")
    
    # submit function
    def prnt_result(e):
        answer = StandardEnglish(str(user_input.value)).convertStandardEnglish()
        output_text.value = answer[2:]
        print("=>", answer)
        page.update()
        
    # container
    output_container = ft.Container(
        content=output_text,
        margin=20,
        padding=20,
        bgcolor="#f2f2f2",
        border_radius=30
    )
    
    
    page.add(
        logo,
        user_input,
        ft.ElevatedButton(text="Submit", on_click=prnt_result),
        output_container,
        ft.Image(src="children_happy.jpg", width=500)
    )


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")