def nome(__nome__):
    print("nome gioco:"+__nome__)

def punti():
    max_points = "punti raggiungibili sono uno"
    print(max_points)

def teams():
    teams = 'teams:2 team_rosso team_blu'.split()
    for x in teams:
        print(x)

def gioco():
    while True:
        print("\nper aggiungere punti: +1 p. rosso (o blu)")
        y = input()
        if y == "+1 p. rosso":
            print("team rosso ha vinto!")
            break
        elif y == "+1 p. blu":
            print("team blu ha vinto!")
            break
        else:
            print("errore!")
    input()

class Team:
    def __init__(self):
        self.nome = nome('')
        self.punti = punti()
        self.teams = teams()
        self.gioco = gioco()
    def nome(__nome__):
        nome(__nome__)
    def punti():
        punti()
    def teams():
        teams()
    def gioco():
        gioco()
