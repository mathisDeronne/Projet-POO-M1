import subprocess

commands = [
    r".\venv\Scripts\python.exe -m chronobio.game.server -p 12345",
    r".\venv\Scripts\python.exe -m chronobio.viewer -p 12345",
    r'.\venv\Scripts\python.exe -m local_base -p 12345 -u "Les potes âgés"',
]

for cmd in commands:
    subprocess.Popen(f'start cmd /k "{cmd}"', shell=True)
