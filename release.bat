if exist built rd /s/q build
if exist dist rd /s/q dist
if exist release rd /s/q release
if exist venv rd /s/q venv

python -m venv  venv
venv\Scripts\python -m pip install --upgrade pip
venv\Scripts\python -m pip install -r requirements.txt
venv\Scripts\python -m pip install pyinstaller

venv\Scripts\pyinstaller --clean %pyinstaller_arg% -F --add-binary "epcboot_gui/resources/win32/epcbootlib.dll;resources/win32/" epcboot_gui/epcboot_gui.py

rename dist release
if exist build rd /s/q build
if exist dist rd /s/q dist
if exist epcboot_gui.spec del epcboot_gui.spec
