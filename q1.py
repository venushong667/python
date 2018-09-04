import re

countries = ["Singapore","USA","Malaysia","Indonesia","Dubai","Australia","Europe","Argentia","Belgium","China",
            "Brazil","Brunei","Colombia","Croatia","Denmark","France","Germany","Iceland","Italy","Japan"]

def search(country):
    if country in countries:
            print(country)
    else:
        print("Not Found")

search("Colombia")
search("Wakanda")
