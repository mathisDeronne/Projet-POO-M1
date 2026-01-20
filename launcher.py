import subprocess

commands = [
    r"C:\Users\admin\PyCharmMiscProject\venv\Scripts\python.exe -m chronobio.game.server -p 12345",
    r"C:\Users\admin\PyCharmMiscProject\\venv\Scripts\python.exe -m chronobio.viewer -p 12345 --width 1500 --height 700",
    r"C:\Users\admin\PyCharmMiscProject\\venv\Scripts\python.exe -m main",
]

for cmd in commands:
    subprocess.Popen(f'start cmd /k "{cmd}"', shell=True)
