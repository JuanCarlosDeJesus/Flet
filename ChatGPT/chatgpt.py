''' Flet Chat App '''
import flet as ft


class Message():
    '''
    Message method
    '''
    def __init__(self, user_name:str, text:str, message_type:str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type


class ChatMessage():
    ''' 
    Chat method
    '''
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment = "start"
        self.control = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user_name)),
                color= ft.colors.WHITE,
                bgcolor= self.get_avatar_color(message.user_name),
            ),
            ft.Column(controls=[
                ft.Text(message.user_name, width="bold"),
                ft.Text(message.text, selectable=True, width=500),
                ]
            )
        ]
    
    def get_initials(self, user_name):
        return self.user_name[:1].capitalize()
    
    def get_avatar_color(self, user_name:str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW
        ]
        return colors_lookup[hash(user_name)%len(colors_lookup)]
    

def main(page: ft.Page):
    ''' main function '''
    page.title = "Chat App"
    
    
    
    page.add()
    


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")