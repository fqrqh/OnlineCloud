import flet as ft
import webbrowser
import os
import subprocess

## en gros en haut c'est juste des services qu'on charge



def main(page: ft.Page):

    ## Ca c'est pour etre sur que ce qu'on va choisir sur le dropdown va etre le bon truck
    def handle_check_item_click(e: ft.Event[ft.PopupMenuItem]):
        e.control.checked = not e.control.checked
    


    ## La tu start le server mais j'ai remplacer le truck par un D 
    def start():
       subprocess.run(["d"]) 


    ## La sa ouvre la page avec le serv
    def open():
        url = 'https://localhost:9000'
        webbrowser.open_new(url)


    ## c'est pour voir qui est log mtn donc si tu clique il y aura ecrit ton nom
    def user():
        user = os.getlogin()
        page.show_dialog(ft.SnackBar(ft.Text(f"The Logged user is {user}")))


    ## la essaye de lire c'est juste le dropdown
    page.add(
        ft.SafeArea(
            content=ft.PopupMenuButton(
                key="popup",
                data=1,
                items=[
                    ft.PopupMenuItem(icon=ft.Icons.HTTP,content="Start Server", on_click=start),
                    ft.PopupMenuItem(icon=ft.Icons.ROUTER, content="Open Server", on_click=open),
                    ft.PopupMenuItem(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.PERSON),
                                ft.Text("Log Info"),
                            ]
                        ),
                        on_click=user, 
                    ),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(
                        content="Checked item",
                        checked=False,
                        on_click=handle_check_item_click,
                    ),
                ],
            )
        )
    )


   

    
   
    


if __name__ == "__main__":
    ft.run(main)
