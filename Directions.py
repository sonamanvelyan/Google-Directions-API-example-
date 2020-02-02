import requests
import json 
import re

api_key = 'AIzaSyBrw936eh8S1K1BNm_gbteR8n1hvWaTSbY'

orig = input("Enter Source: ")

dest = input("Enter Destination: ")

travel = input("Enter Preferred Travel Method: ")

def directions(origin, destination, travel_method):

    results = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin="+origin+"&destination="+destination+"&mode="+travel_method+"&key="+api_key)

    routeData = results.json()

    clean = re.compile('<.*?>')

    count = 1
    for step in routeData["routes"][0]["legs"][0]["steps"]:
        print("Step " + str(count) + ": ")
        text = str(step["html_instructions"])
        text = re.sub(clean, '', text)
        print("In " + str(step["distance"]["text"]) + ", " + text + "." + " This should take you " + str(step["duration"]["text"]))
        print()
        count = count + 1



directions(orig, dest, travel)