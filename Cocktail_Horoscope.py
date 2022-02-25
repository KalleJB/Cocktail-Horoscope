# imports
import requests


# globals
calendar = []


# classes
class Drink:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"


# functions
def make_calender_list(drinks):

    for i in range(8, len(drinks) + 1, 8):
        calendar.append(drinks[i-8:i])


def determine_cocktail(date_list):
    # Lista med drinkar från given månad
    monthly_drinks = calendar[int(date_list[0]) - 1]

    # Datumet dag från input
    day = int(date_list[1])

    # för att få 32 dagar med drinkar
    interval_int = 20

    # Hur många dagar som får samma drink
    interval = interval_int // len(monthly_drinks)
    date_drink = []
    counter = 1
    for drink in monthly_drinks:
        for _ in range(interval):
            #print(f"{counter} : {drink}")
            counter += 1
            date_drink.append(drink)
            date_drink.append(drink)

    #print(day)
    #print(len(date_drink))

    print(f"Drink on the {day}th: {date_drink[day]}")


# main
if __name__ == "__main__":
    response = requests.get("http://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Gin")
    answer = response.json()
    #print(answer['drinks'])
    drinks = []

    # Skapar lista med drink-objekt
    for line in answer['drinks']:
        drinks.append(Drink(line['strDrink']))
        #print(line['strDrink'])
    make_calender_list(drinks)

    date_split_list = []
    # Kollar att input är korrekt
    while True:
        date = input("Skriv in ditt födelsedatum på formen mm/dd :  ")
        if len(date) == 5:
            if date.__contains__("/"):
                date_split_list = date.split("/")
                # Kollar att allt är siffror
                if date_split_list[0].isnumeric() and date_split_list[1].isnumeric():
                    # Tar bort "0" 
                    if int(date_split_list[0]) < 10:
                        date_split_list[0].replace("0", "")
                    if int(date_split_list[1]) < 10:
                        date_split_list[0].replace("0", "")
                    # Kollar att det är inom intervall
                    if 1 <= int(date_split_list[0]) <= 12 and 1 <= int(date_split_list[1]) <= 31:
                        break
                else:
                    print("Skriv datumet enligt formen mm/dd. \n")
        else:
                print("Skriv datumet enligt formen mm/dd. \n")

    determine_cocktail(date_split_list)