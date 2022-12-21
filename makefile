linux:
	pyinstaller --onefile sayori/main.py

exe:
	wine pyinstaller --icon=resources/icon/exe-icon.ico --hidden-import=requests --hidden-import=PIL --onefile --noconsole sayori/main.py

exe-console:
	wine pyinstaller --icon=resources/icon/exe-icon.ico --hidden-import=requests --hidden-import=PIL --onefile sayori/main.py

exe-run:
	wine dist/main.exe

installer:
	wine pyinstaller --icon=resources/icon/exe-icon.ico --hidden-import=requests --onefile --noconsole tools/installer/main.py -n installer

run:
	python sayori/main.py

clean:
	rm dist/*
