# Voici le repo du rendu de projet de POO

## Participants

- Guillaume LANDFROID-NAZAC
- Mathis DÉRONNE
- Damien ZORZETTO
- Leo TISSOT
- Edwin LE ROYER

## install powershell

cd C:\Users\admin\PyCharmMiscProject
py -3.13 -m venv venv

.\venv\Scripts\Activate.ps1

pip install --upgrade chronobio
pip install --upgrade "chronobio[dev]"

.\venv\Scripts\python.exe -m chronobio.game.server -p 12345

.\venv\Scripts\python.exe -m chronobio.viewer -p 12345

.\venv\Scripts\python.exe -m '"nom de notre progrmme.PY' -p 12345