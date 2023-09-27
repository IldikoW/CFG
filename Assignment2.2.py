#This is a travel agency run by Jar Jar Binks :) , so it speaks in a funny way. It can recommend a random
# destination, or you can choose a climate, and it recommends you places based
# on your choice and writes the results in a txt.

#This module is used for randomizing and selecting a planet for a surprise holiday.
# You can install the  module using the Python package manager called pip.

import random

#This module is used for making HTTP requests to the SWAPI (Star Wars API) to retrieve planet data.
import requests

#  SWAPI URL for planets
swapi_planets_url = "https://swapi.dev/api/planets/"

# Initialize a list to store planet data
all_planets = []

# Initialize the initial page URL
next_page_url = swapi_planets_url

# Retrieving planet data
while next_page_url:
    response = requests.get(next_page_url)

    if response.status_code == 200:
        planet_page_data = response.json()
        all_planets.extend(planet_page_data['results'])
        next_page_url = planet_page_data['next']
    else:
        print("Failed to retrieve planet data")
        break

# List of available climates from the API
planet_climates = ["frozen", "temperate", "tropical", "arid", "arctic", "murky"]

#function for  offering a surprise holiday or
# helping the user choose a holiday based on climate
def holiday():
    if FavHoliday == "yes":
        def surprise_holiday():
            randomholiday = random.choice(all_planets)
            return randomholiday["name"]

        with open("destination.txt", "w+") as text_file:
            destination = surprise_holiday()
            text_file.write(destination)
            print(f"Meesa recommendin' a bombad holiday destination for you, {client_name} : " + destination + "!")


    elif FavHoliday == "no":
        while True:
            print(
                "Yousa gotta choose from one of these climates: frozen, temperate, tropical, arid, arctic, or murky. Which one yousa likin?")
            # Get input from the user and convert it to lowercase for case-insensitive comparison
            FavClimate = input(f"Yousa like da hot or da cold weather, {client_name}?").lower()

            if FavClimate in planet_climates:
                break  # Exit the loop if the input is valid
            else:
                print(f"Choose from: {', '.join(planet_climates)} you should, {client_name}")

        print("So yousa would likin' to have " + FavClimate + " climate on your holiday.")
#The function checks the all_planets list for planets matching the selected climate and returns a list of matching planet names.
        def good_Climate_Planets(all_planets, FavClimate):
            ideal_planets = []  # Create an empty list to store matching planets

            for planet in all_planets:
                if planet['climate'] == FavClimate:
                    planet_info = f"Planet : {planet['name']}"
                    ideal_planets.append(planet_info)

            if ideal_planets:
                return ideal_planets
            else:
                return ["No planets with this climate"]

        matching_planets = good_Climate_Planets(all_planets, FavClimate)

        if matching_planets != ["No planets with this climate"]:
            print("Yousa should travel to:")
            for planet_info in matching_planets:
                print(planet_info)
            with open("destination.txt", "w+") as text_file:
                for planet_info in matching_planets:
                    text_file.write(planet_info + "\n")
        else:
            print("No planets with this climate")
            with open("destination.txt", "w+") as text_file:
                text_file.write("No planets with this climate")


print("Welcome to Jar Jar Binks Travel Agency")
client_name = input("Whosa yousa name?")
#Jar Jar Binks shortens words :)
client_name = client_name[0:3]
print(f"Meesa greetin' you, {client_name}! Yousa bein' a nice person, meesa think!")

while True:
    # Get input from the user and convert it to lowercase for case-insensitive comparison
    FavHoliday = input("Yousa want a big surprise trip? Mesa thinkin' it gonna be muy muy excitin'!").lower()

    # Check if the input is either "yes" or "no"
    if FavHoliday == "yes" or FavHoliday == "no":
        break  # Exit the loop if the input is valid
    else:
        print(f"Type 'yes' or 'no,' you should, {client_name}")

holiday()

print("Meesa wish you a bombad journey, okeyday? And thank yousa for usin' my travel agency! Yousa come back anytime, "
      "meesa always here to help!!")





