#/usr/bin/python
"""
api_information.py
msimo - 3/31/15

Contains various API information for use with API calls.

To do:
	* Complete project outline for GOWURF
	* Search for URF data ("queueType":"URF_5x5") [matchId object]
"""

# Information used in the every call
api_domain = "https://na.api.pvp.net"
region = "na"

# Optional used for most API calls
api_lol = "/api/lol/"

'''0. api-challenge-v4.1 API reference 
	Command usage: api_domain + api_lol + region + api_challenge_url
	500 Internal Server Error for  days'''
api_challenge_url = "/v4.1/game/ids"

'''1. champion-v1.2 API reference
	Command usage: api_domain + api_lol + region + champion_api_url [ + id ]'''
champion_api_url = "/v1.2/champion/"

'''2. current-game-v1.0 API reference
	Command Usage: api_domain + current_game_api_url + platform_id + "/" + summoner_id'''
current_game_api_url = "/observer-mode/rest/consumer/getSpectatorGameInfo/"

'''3. featured-game-v1.0 API reference
	Command Usage: api_domain + featured_game_api_url'''
featured_games_url = "/observer-mode/rest/featured/"

'''4. game-v1.3 API reference
	Command Usage: api_domain + api_lol + region + game_api_url + "by-summoner/" + summoner_id + "/recent"'''
game_api_url = "/v1.3/game/"

'''5. league-v2.5 API reference
	Command Usage:  api_domain + api_lol + region + league_api_url 
	[ + "by-summoner/"
		[[ + {summonerIds} ]]
		[[ + {summonerIds} + "/entry" ]] ]

     [ + "by-team/"
     	[[ + {teamIds}
     	   + {teamIds + "/entry"} ]] ]

     [ + "challenger" ]'''
league_api_url = "/v2.5/league/"

'''7. lol-status-v1.0 API reference
	Command Usage:  api_domain + lol_status_api_url
		[ + "/" + region ]'''
lol_status_api_url = "/shards"

'''8. match-v2.2 API reference
	Command Usage:  api_domain + api_lol + region + match_api_url + match_id'''
match_api_url = "/v2.2/match/"

'''9. matchhistory-v2.2 API reference
	/api/lol/{region}/v2.2/matchhistory/{summonerId}
	Command Usage:  api_domain + api_lol + region + matchhistory_api_url + summoner_id'''
match_api_url = "/v2.2/matchhistory/"

'''11. summoner-v1.4 API reference
	Command Usage:  api_domain + api_lol + region + summoner_api_url 
	[ + "by-name/" + summoner_names ]
	[ + summoner_ids ]
		[[ + "/masteries" ]]
		[[ + "/name" ]]
		[[ + "/runes" ]]

Note: summoner_names has to be a comma-sperated list no longer than 40 users.'''
summoner_api_url = "/v1.4/summoner/"
summoner_api = {"by_name": "by-name/",
					"masteries": "/masteries",
					"name": "/name",
					"runes": "/runes"}