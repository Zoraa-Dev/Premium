from Penyimpanan.FolderSC.instagram import Instagram
from Penyimpanan.Database.data import *
from Temporary.Terminalize.Styles import style_terminal

class Main:
    def __init__(self) -> None:
        pass
        
    def BruteForce(self):
        try:
            created = '22 Juny 2025'
            expired = 'unlimited'
            sisa = 'unlimited'
            Instagram().Chek_Cookies(created,expired,sisa)
        except (Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()
            
Main().BruteForce()
        