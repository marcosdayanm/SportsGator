# import requests

# url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeamSchedule"

# querystring = {"teamAbv":"CHI","season":"2023"}

# headers = {
# 	"X-RapidAPI-Key": "ce4d7f53c0msh18dda467b092edep178adbjsn5357e30009bb",
# 	"X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# data = response.json()

# print(response.json())



data = {'statusCode': 200, 'body': {'team': 'CHI', 'schedule': [{'gameID': '20230812_TEN@CHI', 'seasonType': 'Preseason', 'away': 'TEN', 'teamIDHome': '6', 'gameDate': '20230812', 'gameStatus': 'Completed', 'gameWeek': 'Preseason Week 1', 'teamIDAway': '31', 'home': 'CHI', 'awayResult': 'L', 'homePts': '23', 'gameTime': '1:00p', 'gameTime_epoch': '1691859600.0', 'homeResult': 'W', 'awayPts': '17'}, {'gameID': '20230819_CHI@IND', 'seasonType': 'Preseason', 'away': 'CHI', 'teamIDHome': '14', 'gameDate': '20230819', 'gameStatus': 'Completed', 'gameWeek': 'Preseason Week 2', 'teamIDAway': '6', 'home': 'IND', 'awayResult': 'L', 'homePts': '24', 'gameTime': '7:00p', 'gameTime_epoch': '1692486000.0', 'homeResult': 'W', 'awayPts': '17'}, {'gameID': '20230826_BUF@CHI', 'seasonType': 'Preseason', 'away': 'BUF', 'teamIDHome': '6', 'gameDate': '20230826', 'gameStatus': 'Completed', 'gameWeek': 'Preseason Week 3', 'teamIDAway': '4', 'home': 'CHI', 'awayResult': 'W', 'homePts': '21', 'gameTime': '1:00p', 'gameTime_epoch': '1693069200.0', 'homeResult': 'L', 'awayPts': '24'}, {'gameID': '20230910_GB@CHI', 'seasonType': 'Regular Season', 'away': 'GB', 'teamIDHome': '6', 'gameDate': '20230910', 'gameStatus': 'Completed', 'gameWeek': 'Week 1', 'teamIDAway': '12', 'home': 'CHI', 'awayResult': 'W', 'homePts': '20', 'gameTime': '4:25p', 'gameTime_epoch': '1694377500.0', 'homeResult': 'L', 'awayPts': '38'}, {'gameID': '20230917_CHI@TB', 'seasonType': 'Regular Season', 'away': 'CHI', 'teamIDHome': '30', 'gameDate': '20230917', 'gameStatus': 'Completed', 'gameWeek': 'Week 2', 'teamIDAway': '6', 'home': 'TB', 'awayResult': 'L', 'homePts': '27', 'gameTime': '1:00p', 'gameTime_epoch': '1694970000.0', 'homeResult': 'W', 'awayPts': '17'}, {'gameID': '20230924_CHI@KC', 'seasonType': 'Regular Season', 'away': 'CHI', 'teamIDHome': '16', 'gameDate': '20230924', 'gameStatus': 'Completed', 'gameWeek': 'Week 3', 'teamIDAway': '6', 'home': 'KC', 'awayResult': 'L', 'homePts': '41', 'gameTime': '4:25p', 'gameTime_epoch': '1695587100.0', 'homeResult': 'W', 'awayPts': '10'}, {'gameID': '20231001_DEN@CHI', 'seasonType': 'Regular Season', 'away': 'DEN', 'teamIDHome': '6', 'gameDate': '20231001', 'gameStatus': 'Completed', 'gameWeek': 'Week 4', 'teamIDAway': '10', 'home': 'CHI', 'awayResult': 'W', 'homePts': '28', 'gameTime': '1:00p', 'gameTime_epoch': '1696179600.0', 'homeResult': 'L', 'awayPts': '31'}, {'gameID': '20231005_CHI@WSH', 'seasonType': 'Regular Season', 'away': 'CHI', 'teamIDHome': '32', 'gameDate': '20231005', 'gameStatus': 'Completed', 'gameWeek': 'Week 5', 'teamIDAway': '6', 'home': 'WSH', 'awayResult': 'W', 'homePts': '20', 'gameTime': '8:15p', 'gameTime_epoch': '1696551300.0', 'homeResult': 'L', 'awayPts': '40'}, {'gameID': '20231015_MIN@CHI', 'seasonType': 'Regular Season', 'away': 'MIN', 'gameTime': '1:00p', 'teamIDHome': '6', 'gameDate': '20231015', 'gameStatus': 'Scheduled', 'gameTime_epoch': '1697389200.0', 'gameWeek': 'Week 6', 'teamIDAway': '21', 'home': 'CHI'}, {'gameID': '20231022_LV@CHI', 'seasonType': 'Regular Season', 'away': 'LV', 'gameTime': '1:00p', 'teamIDHome': '6', 'gameDate': '20231022', 'gameStatus': 'Scheduled', 'gameTime_epoch': '1697994000.0', 'gameWeek': 'Week 7', 'teamIDAway': '17', 'home': 'CHI'}, {'gameID': '20231029_CHI@LAC', 'seasonType': 'Regular Season', 'away': 'CHI', 'gameTime': '8:20p', 'teamIDHome': '18', 'gameDate': '20231029', 'gameStatus': 'Scheduled', 'gameTime_epoch': '1698625200.0', 'gameWeek': 'Week 8', 'teamIDAway': '6', 'home': 'LAC'}, {'gameID': '20231105_CHI@NO', 'seasonType': 'Regular Season', 'away': 'CHI', 'gameTime': '1:00p', 'teamIDHome': '23', 'gameDate': '20231105', 'gameStatus': 'Scheduled', 'gameTime_epoch': '1699207200.0', 'gameWeek': 'Week 9', 'teamIDAway': '6', 'home': 'NO'}, {'gameID': '20231109_CAR@CHI', 'seasonType': 'Regular Season', 'away': 'CAR', 'gameTime': '8:15p', 'teamIDHome': '6', 'gameDate': '20231109', 'gameStatus': 'Scheduled', 'gameTime_epoch': '1699578900.0', 'gameWeek': 'Week 10', 'teamIDAway': '5', 'home': 'CHI'}, {'gameID': '20231119_CHI@DET', 'seasonType': 'Regular Season', 'away': 'CHI', 'gameTime': '1:00p', 'teamIDHome': '11', 'gameDate': '20231119', 'gameStatus': 'Scheduled', 'gameTime_epoch': '1700416800.0', 'gameWeek': 'Week 11', 'teamIDAway': '6', 'home': 'DET'}, {'gameID': '20231127_CHI@MIN', 'seasonType': 'Regular Season', 'away': 'CHI', 'gameTime': '8:15p', 'teamIDHome': '21', 'gameDate': '20231127', 'gameStatus': 'Scheduled', 'gameTime_epoch': '1701134100.0', 'gameWeek': 'Week 12', 'teamIDAway': '6', 'home': 'MIN'}, {'gameID': '20231210_DET@CHI', 'seasonType': 'Regular Season', 'away': 'DET', 'gameTime': '1:00p', 'teamIDHome': '6', 'gameDate': '20231210', 'gameStatus': 'Scheduled', 'gameTime_epoch': '1702231200.0', 'gameWeek': 'Week 14', 'teamIDAway': '11', 'home': 'CHI'}, {'gameID': '20231217_CHI@CLE', 'seasonType': 'Regular Season', 'away': 'CHI', 'gameTime': 'TBD', 'teamIDHome': '8', 'gameDate': '20231217', 'gameStatus': 'Scheduled', 'gameTime_epoch': '', 'gameWeek': 'Week 15', 'teamIDAway': '6', 'home': 'CLE'}, {'gameID': '20231224_ARI@CHI', 'seasonType': 'Regular Season', 'away': 'ARI', 'gameTime': '4:25p', 'teamIDHome': '6', 'gameDate': '20231224', 'gameStatus': 'Scheduled', 'gameTime_epoch': '1703453100.0', 'gameWeek': 'Week 16', 'teamIDAway': '1', 'home': 'CHI'}, {'gameID': '20231231_ATL@CHI', 'seasonType': 'Regular Season', 'away': 'ATL', 'gameTime': '1:00p', 'teamIDHome': '6', 'gameDate': '20231231', 'gameStatus': 'Scheduled', 'gameTime_epoch': '1704045600.0', 'gameWeek': 'Week 17', 'teamIDAway': '2', 'home': 'CHI'}, {'gameID': '20240107_CHI@GB', 'seasonType': 'Regular Season', 'away': 'CHI', 'gameTime': 'TBD', 'teamIDHome': '12', 'gameDate': '20240107', 'gameStatus': 'Scheduled', 'gameTime_epoch': '', 'gameWeek': 'Week 18', 'teamIDAway': '6', 'home': 'GB'}]}}



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
    print(f"Counterseason: {counterseason}")
    print(f"game['gameWeek'][5:]: {game['gameWeek'][5:]}")
    print(f"prev_week: {prev_week}\n")
    
    if (counterseason >= 4) and ((int(game['gameWeek'][5:]) + 3 - prev_week) > 1):
        if counterseason - 3 > len(schedule):
            pend_schedule.append({'gameWeek':prev_week - 3, 
                            'opponent':"BYE WEEK",
                            })
        else:
            schedule.append({'gameWeek':prev_week - 3, 
                            'opponent':"BYE WEEK",
                            })

    # Formato de la fecha
    matchdate = game['gameDate'][6:] + "/" + game['gameDate'][4:6] + "/" + game['gameDate'][:4]


    # Checar quién es qué equipo
    if data['body']['team'] == game['home']:
        opponent = game['away']
    else:
        opponent = game['home']
    
    
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
                                'opponent':opponent,
                                'gameTime':game['gameTime']+'m'
                                })
            
        else:
            pend_ps_schedule.append({'gameWeek':game['gameWeek'][15:], 
                                    'matchdate':matchdate,
                                    'opponent':opponent,
                                    'gameTime':game['gameTime']+'m'
                                })
    
    

print(f"PS Schedule: {ps_schedule}")
print(f"Pending PS Schedule: {pend_ps_schedule}")
print(f"Schedule: {schedule}")
print(f"Pending Schedule: {pend_schedule}")

