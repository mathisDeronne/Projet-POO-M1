# Dans un environnement virtuel activé

python -m chronobio.killall
# choisir un port non utilisé
PORT=$(python -c "import random; print(random.randint(2000, 3000))")
# lancer le serveur
python -m chronobio.game.server -p $PORT &
sleep 2
# lancer le viewer
python -m chronobio.viewer -p $PORT &
# lancer un joueur
python -m sample_player_client -p $PORT -u TOTO