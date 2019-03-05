#!/usr/bin/python
"""
api_requests.py 
Author: mpmsimo
Date Created: 3/31/15
Deadline: April 17th, 2015 at 11:59 PM Pacific Time (PT)

Mapping for the Riot Games Full API Reference.

The first 5 API's [champion, current-game, featured-games, game, league] are currently mapped.
https://developer.riotgames.com/api/methods

To-do list.
 * Finished adding remaining API's (2 left)
 * Store important JSON requests into their own files
"""
import api_information as ai
import api_key

import requests
import json

api_key = (api_key.api_key)
debug = True

##### debug functions
def expected_api_call(request):
	"""If debug is true, enables the below expected API call message"""
	if debug == True:
		print(request.url[:-36])

def get_response(api_call, http_method="get"):
	if http_method is "get":
		r = requests.get(api_call)
	print("Response code: {0}".format(r))

def print_api_info(summoner_names):
	"""Does what it's supposed to do"""
	print("api_domain: {0}\n"
			"api_lol: {1}\n"
			"region: {2}\n" 
			"api_url: {3}\n"
			"api_call: {4}\n"
			"api_information: {5}\n"
			"api_key: {6}".format(ai.api_domain, ai.api_lol, ai.region, ai.summoner_api_url, ai.summoner_api["by_name"], summoner_names,"?api_key=redacted"))
	
	api_call = str(ai.api_domain + ai.api_lol + ai.region + ai.summoner_api_url + ai.summoner_api["by_name"] + summoner_names + "?api_key=redacted")
	#expected_api_call(api_call)

##### api-challenge-v4.1 API query
# Next step is to store the data every 5m.
# Received response 500 (Internal Server Error)

def get_api_challenge_data():
	"""Returns NURF data (5m batches)"""
	api_call = str(ai.api_domain + ai.api_lol + ai.region + ai.api_challenge_url )# + api_key)
	payload = {"beginDate": "1:00", "api_key": api_key}
	r = requests.get(api_call, params=payload)
	#expected_api_call(r)
	print(r.url)
	print("Reponse text:\n{0}".format(r.text)) #print response code

##### summoner-v1.4 API queries
# Next step is to interpret the JSON object so we can use this information (namely ID's associated with username)
def get_summoners_by_name(summoner_names):
	"""Takes in a string or list of summoners, and returns a list of json objects"""
	api_call = ai.api_domain + ai.api_lol + ai.region + ai.summoner_api_url + ai.summoner_api["by_name"] + summoner_names
	payload = {"api_key": api_key}
	r = requests.get(api_call, params=payload)
	expected_api_call(r)
	print(json.loads(json.dumps(r.json())))
	summoner_json_object = json.loads(json.dumps(r.json()))
	return summoner_json_object

def get_summoner_id(summoner_json_object):
	"""Gets summoner id from json object"""
	for key in summoner_json_object.keys():
		#print("Key: {0}\nValue: {1}".format(key, summoner_json_object[key]))
		#print(summoner_json_object[key]["id"])
		id_info = { str(key): str(summoner_json_object[key]["id"])}
		print(id_info)

def get_summoners_by_id(summoner_ids):
	pass

def get_summoners_masteries(summoner_ids):
	pass

def get_summoners_name(summoner_ids):
	pass

def get_summoners_runes(summoner_ids):
	pass

##### match-v2.2 API queries
# Get match information which returns the following:

# (MatchDetail object)
# map_id (Check map type)
# match_duration
# match_id
# match_mode
# match_type
# match_version
# participant_identities[]
# participant[]
# platform_id
# urf_queue_types = ["URF_5x5", "BOT_URF_5x5"]
# region
# season
# teams[]
# timeline

# (Participant object)
# champion_id
# masteries
# runes
# spell1_id
# spell2_id
# stats
# team_id
# timeline

##### Main function
def main():
	#print_api_info(api_key.summoner_id)
	#get_summoners_by_name(api_key.summoner_ids)
	#summoner_json_object = get_summoners_by_name(api_key.summoner_ids)
	#get_summoner_id(summoner_json_object)
	#get_api_challenge_data()
	pass

if __name__ == "__main__":
	summoner_json_object = get_summoners_by_name(api_key.summoner_ids)
	get_summoner_id(summoner_json_object)