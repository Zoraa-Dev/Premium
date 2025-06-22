from LicenseKey import ZoraaDev
from Penyimpanan.Database.data import *
from Temporary.Terminalize.Styles import style_terminal

class Main:
    def __init__(self) -> None:
        pass
        
    def BruteForce(self):
        try:
            ZoraaDev()
        except (Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()
            
Main().BruteForce()
        
