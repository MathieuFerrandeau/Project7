ADRESS_MGS = [
    "Bien sûr voici l'adresse:",
    "Si je me souviens bien l'adresse est:",
    "Il me semble que ça se trouve ici: "
]


SUMMARY_MGS = [
    "Et t'ai je déjà raconté cette histoire ?  ",
    "Je me souviens que...  ",
    "Si tu as deux minutes , je peux te raconter une petite histoire... ",
    "Est-ce que tu savais que...  ",
]


FAILURE_MGS = [
    "Ça ne me dit rien du tout, fais attention à l'orthographe da la recherche",
    "je n'ai pas de connaissance à ce sujet-là, fais attention à l'orthographe recherché"
]

with open('key.txt', 'r') as texte:
	API_KEY = texte.read()