import os, time
from rich.console import Console
from LicenseKey import LicenseKey as Zoraa

class Requdable:
  def __init__(self) -> None:
    pass
  
  def asset_keys(self):
    Zoraa().LicenseList()

if __name__=='__main__':
  try: os.sistem('git pull'); time.sleep(2.1); Requdable().asset_keys()
  except (Exception, requests.exceptions.ConnectionError) as e:
    Console(width = 65, style = "grey50").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
    exit()
else: Requdable().asset_keys() 
