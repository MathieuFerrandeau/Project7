ADDRESS_MSG = [
    "Voici l'adresse:",
    "Si je me souviens bien l'adresse est:",
    "Il me semble que ça se trouve ici: "
]


SUMMARY_MSG = [
    "T'ai je déja parlé de cette historie...  ",
    "Je me souviens que...  ",
    "Je peux te raconter une petite histoire à ce sujet... ",
    "Savais tu que...  ",
]


FAILURE_MSG = [
    "Ça ne me dit rien du tout, fais attention à l'orthographe da ta recherche",
    "je n'ai pas de connaissance à ce sujet-là, fais attention à l'orthographe de ta recherche"
]

with open('key.txt', 'r') as texte:
	API_KEY = texte.read()