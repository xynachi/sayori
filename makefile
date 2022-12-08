linux:
	pyinstaller --onefile sayori/main.py

exe:
	wine pyinstaller --icon=resources/icon/exe-icon.ico --hidden-import=requests --onefile --noconsole sayori/main.py

exe-console:
	wine pyinstaller --icon=resources/icon/exe-icon.ico --hidden-import=requests --onefile sayori/main.py

run:
	python sayori/main.py
