# Sayori

## _Discord bot for remote PC control_

## Build

### Dependencies

> Note: If you want to compile for Windows you must install python also in the wine environment.

(optional) Install python for wine.

Download python-3.x.x-amd64.exe from https://www.python.org/downloads/windows/

```sh
wine python-3*-amd64.exe
```

Install python dependencies.
```sh
pip install -r requirements # Linux
wine pip install -r requirements # (optional) Windows
```

### Make

> Note: Before you do this, you have to fill in the variables in settings.py, depending on what you want to compile.

```sh
# .exe for Windows
make exe

# .exe for Windows with debug
make exe-console

# Installer for Windows
make installer
```

#### If you want to help fork and read [TODO.md](TODO.md)
