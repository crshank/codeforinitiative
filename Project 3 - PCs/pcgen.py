"""This script will generate random PC ideas from the D&D 5E SRD. 
This will use data from http://www.dnd5eapi.co/
"""

import urllib2, json, random

def json_opener(url):
    """Function to open URLs and output JSON
    
    Arguments:
        url -- The API URL containing JSON data
    """
    opened_url = urllib2.urlopen(url)
    data = json.loads(opened_url.read())
    return data

def selection(data):
    """This function will take the JSON data and select a random item
    
    Arguments:
        data -- the JSON data from the API
    """
    total = int(data["count"])
    option = random.randint(0, total-1)
    choice = data["results"][option]["name"]
    return choice

# Open the race and class API pages
race_data = json_opener("http://www.dnd5eapi.co/api/races")
class_data = json_opener("http://www.dnd5eapi.co/api/classes")

# Select a random race and class
race_selection = selection(race_data)
class_selection = selection(class_data)

# Output the random PC
print "Your random PC race and class: {} {}".format(race_selection, class_selection)