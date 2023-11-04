import datetime
from flask import Flask, jsonify, flash, redirect, render_template, request, session
from flask_session import Session
import requests


# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Web Page Description
@app.route("/")
def index():
    return render_template("index.html")


# Catch the ball game
@app.route('/game')
def game():
    return render_template("game.html")


# Teams ordered by its score, with the option of watching over each team roster and schedule
@app.route('/teams')
def scores():
    url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeams"

    querystring = {"rosters":"false","schedules":"false","topPerformers":"false","teamStats":"false"}

    headers = {
    	"X-RapidAPI-Key": "ce4d7f53c0msh18dda467b092edep178adbjsn5357e30009bb",
    	"X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()



    teams_info = []

    session['teamnames'] = {}
    session['teamlogos'] = {}

    # Verificando si la respuesta es exitosa
    if data['statusCode'] == 200:
        for team in data['body']:
            team_info = {
                'teamName': team['teamName'],
                'teamCity': team['teamCity'],
                'teamAbv': team['teamAbv'],
                'wins': team['wins'],
                'losses': team['loss'],
                'tie': team['tie'],
                'currentStreakResult': team['currentStreak']['result'],
                'currentStreakLength': team['currentStreak']['length'],
                'image': team['espnLogo1']
            }
            teams_info.append(team_info)

            session['teamnames'][team['teamAbv']] = team['teamCity'] + " " + team['teamName']
            session['teamlogos'][team['teamAbv']] = team['espnLogo1']

     # Sorting the teams_info list by 'wins' in descending order
    teams_info_sorted = sorted(teams_info, key=lambda x: int(x['losses']) -int(x['wins']))

    logonfl = "https://static.www.nfl.com/image/upload/v1554321393/league/nvfr7ogywskqrfaiu38m.svg"      

    # print(teams_info_sorted)
    return render_template("teams.html", teams_info=teams_info_sorted, logonfl=logonfl)


@app.route('/roster', methods=["GET", "POST"])
def roster():
    """Shows the chosen team roster"""

    if request.method == "GET":
        return redirect('/teams')

    session["logo"] = request.form.get("logo")
    session["name"] = request.form.get("name")
    session["abv"] = request.form.get("abv")

    url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeamRoster"


    querystring = {"teamAbv":session["abv"], "getStats":"true"}
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

    # Appendear la información de cada jugador
    for player in sorted_roster:
        pinfo.append({'jerseyNum':player['jerseyNum'], 
                    'longName':player['longName'], 
                    'pos':player['pos'], 
                    'exp':player['exp'], 
                    'school':player['school'], 
                    'age': player['age'], 
                    'bDay':player['bDay'], 
                    'weight':player['weight'] + ' lbs', 
                    'height': player['height'],
                    'espnHeadshot':player['espnHeadshot']
                    })
        
    #     print(f"#{player['jerseyNum']} {player['longName']} ({player['pos']}) - EXP: {player['exp']} COLLEGE: {player['school']}")
    #     print(f"  Age: {player['age']}, Weight: {player['weight']}, Height: {player['height']}")
    #     print("")
        
    # print(pinfo)

    return render_template("roster.html", pinfo=pinfo, abv=session["abv"], name=session["name"], logo=session["logo"])


@app.route('/schedule', methods=["GET", "POST"])
def schedule():


    # Falta hacer el if de lo del datetime para poner la season del schedule

    if request.method == "GET":
        return redirect('/teams')
    
    url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeamSchedule"

    session["logo"] = request.form.get("logo")
    session["name"] = request.form.get("name")
    session["abv"] = request.form.get("abv")


    now = datetime.datetime.now()

    month = now.month
    year = now.year

    if (month < 7):
        year -= 1


    querystring = {"teamAbv":session["abv"],"season":year}

    headers = {
    	"X-RapidAPI-Key": "ce4d7f53c0msh18dda467b092edep178adbjsn5357e30009bb",
    	"X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    # print(response.json())


    schedule = [] # pasar
    seascore = [0, 0, 0] 
    pend_schedule = [] # pasar

    ps_schedule = [] # pasar
    psscore = [0, 0, 0]
    pend_ps_schedule = [] # pasar

    # Contador para saber si estamos en Preseason o en Season
    counterseason = 0
    prev_week = -1


    # Iterar sobre la respuesta de el API
    for game in data['body']['schedule']:
        counterseason += 1
        prev_week += 1
        gano = 0
        perdio = 0
        empato = 0

        # Considerar la Bye Week
        if (counterseason >= 4) and ((int(game['gameWeek'][5:]) + 3 - prev_week) > 1):
            if counterseason - 3 > len(schedule):
                pend_schedule.append({'gameWeek':prev_week - 2, 
                                'opponent':"BYE WEEK",
                                'logoopp':"static/sin_fondo.png"
                                })
            else:
                schedule.append({'gameWeek':prev_week - 2, 
                                'opponent':"BYE WEEK",
                                })
            prev_week += 1

        # Formato de la fecha
        matchdate = game['gameDate'][6:] + "/" + game['gameDate'][4:6] + "/" + game['gameDate'][:4]


        # Checar quién es qué equipo
        if data['body']['team'] == game['home']:
            opponent = game['away']
        else:
            opponent = game['home']
        
        logoopp = session['teamlogos'][opponent]
        opponent = session['teamnames'][opponent]
        
        
        # Checar si ya se jugó el partido
        if 'homePts' in game and 'awayPts' in game:
            # print(f"Score: {game['home']} {game['homePts']} - {game['away']} {game['awayPts']}")

            # Checar quién ganó el partido y asignar W/L
            if game['home'] == data['body']['team']:
                if int(game['homePts']) > int(game['awayPts']):
                    gano = 1
                    result = 'W'
                elif int(game['homePts']) < int(game['awayPts']):
                    perdio = 1
                    result = 'L'
                else:
                    empato = 1
                    result = 'T'
            else:
                if int(game['homePts']) < int(game['awayPts']):
                    gano = 1
                    result = 'W'
                elif int(game['homePts']) > int(game['awayPts']):
                    perdio = 1
                    result = 'L'
                else:
                    empato = 1
                    result = 'T'

            
            # Formattear el marcador
            marcador = game['homePts'] + "-" + game['awayPts']

            # Checar el color de W/L
            if result == 'W':
                resultcolor = 'wgreen'
            else:
                resultcolor = 'lred'


            # Actualizar el conteo de victorias/derrotas de la temporada 
            if "Preseason" not in game['gameWeek']:

                # Sumar al score y formatearlo
                seascore[0] += gano
                seascore[1] += perdio
                seascore[2] += empato
                teamscore = str(seascore[0]) + "-" + str(seascore[1]) + "-" + str(seascore[2])
                

                # Hacer append a la lista de schedule
                schedule.append({'gameWeek':game['gameWeek'][5:], 
                                'logoopp':logoopp,
                                'opponent':opponent,
                                'resultcolor':resultcolor,
                                'result':result,
                                'marcador':marcador,
                                'teamscore':teamscore,
                                'matchdate':matchdate,
                                'gameTime':game['gameTime']+'m'
                                })

            # Actualizar el conteo de victorias/derrotas de la pretemporada 
            else:

                psscore[0] += gano
                psscore[1] += perdio
                psscore[2] += empato
                teamscore = str(psscore[0]) + "-" + str(psscore[1]) + "-" + str(psscore[2])

                # Hacer append a la lista de ps_schedule
                ps_schedule.append({'gameWeek':game['gameWeek'][15:], 
                                'logoopp':logoopp,
                                'opponent':opponent,
                                'resultcolor':resultcolor,
                                'result':result,
                                'marcador':marcador,
                                'teamscore':teamscore,
                                'matchdate':matchdate,
                                'gameTime':game['gameTime']+'m'
                                })

            
        # Sino se ha jugado el partido
        else:

            # Verificar si lo que falta es de preseason o season
            if counterseason >= 4:
                pend_schedule.append({'gameWeek':game['gameWeek'][5:], 
                                    'matchdate':matchdate,
                                    'logoopp':logoopp,
                                    'opponent':opponent,
                                    'gameTime':game['gameTime']+'m'
                                    })
                
            else:
                pend_ps_schedule.append({'gameWeek':game['gameWeek'][15:], 
                                        'matchdate':matchdate,
                                        'logoopp':logoopp,
                                        'opponent':opponent,
                                        'gameTime':game['gameTime']+'m'
                                    })
        
        
    return render_template("schedule.html", logo=session["logo"], ps_schedule=ps_schedule, pend_ps_schedule=pend_ps_schedule, schedule=schedule, pend_schedule=pend_schedule, name=session['teamnames'][session["abv"]])




if __name__ == '__main__':
    port = int(os.getenv("PORT", default=5001))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)
