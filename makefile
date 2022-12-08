linux:
	pyinstaller --onefile sayori/main.py

exe:
	wine pyinstaller --icon=resources/icon/exe-icon.ico --onefile --noconsole sayori/main.py

exe-console:
	wine pyinstaller --icon=resources/icon/exe-icon.ico --onefile sayori/main.py

run:
	python sayori/main.py
