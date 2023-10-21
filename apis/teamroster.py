import requests

url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeamRoster"

querystring = {"teamAbv":"CHI","getStats":"true"}

headers = {
	"X-RapidAPI-Key": "ce4d7f53c0msh18dda467b092edep178adbjsn5357e30009bb",
	"X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()





position_order = ['QB', 'RB', 'WR', 'TE', 'C', 'OT', 'OG', 'DE', 'DT', 'LB', 'CB', 'S']

# Ordenar la lista de jugadores
sorted_roster = sorted(data['body']['roster'], key=lambda x: (
    position_order.index(x['pos']) if x['pos'] in position_order else float('inf'),
    x['pos'],
    float('inf') if x['lastGamePlayed'] == '' else -int(x['lastGamePlayed'].split('_')[0])
))

pinfo = []


# Imprimir la información de cada jugador
for player in sorted_roster:
    pinfo.append({'jerseyNum':player['jerseyNum'], 
                  'longName':player['longName'], 
                  'pos':player['pos'], 
                  'exp':player['exp'], 
                  'school':player['school'], 
                  'age': player['age'], 
                  'bDay':player['bDay'], 
                  'weight':player['weight'], 
                  'height': player['height']})
    
    print(f"#{player['jerseyNum']} {player['longName']} ({player['pos']}) - EXP: {player['exp']} COLLEGE: {player['school']}")
    print(f"  Age: {player['age']}, Weight: {player['weight']}, Height: {player['height']}")
    print("")
    

print(pinfo)

