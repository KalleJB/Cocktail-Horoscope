# API-project-Cocktail Horoscope

## Bakgrund

Denna README är skriven i markdown. Den är till för att ge komplimenterande information till programmet "Cocktail Horoscope".

Syftet med projektet är att skapa ett program som ger användaren ett namn på en drink utifrån dess födelsedatum.

## Teknik

Programmet är skrivet i Python och använder endast biblioteket "requests". Det använder även ett API från https://www.thecocktaildb.com/api.php.

## Användning

Programmet startar i temrinalen för visual studio code Python. Där får användaren en rad där hen ska skriva in ett datum på formen mm/dd. Om denna formalia inte fullföljs så får användaren en till chans att skriva in ett datum till formalian uppnåts.

När programmet fått in ett datum genom användaren så används funktioner för att göra om strängen till användbar data. Denna data används sedan för att skapa ett index på en lista full med olika drinkar. Efter det skrivs drinken för datumet ut i terminalen så att användaren kan läsa av det.

## Installation

Kör följande kommando för att installera biblioteket som krävs för programmet.

"""
pip install requests
"""

Programmet är testat i python 3.10.2 64-bit vilket du kan ladda ned på (https://www.python.org/downloads/).

## Contribution

Då bedömning ännu ej är gjord på uppgiften så tillåts inga pull requests. Så fort bedömning är gjord kommer detta tillåtas. 

## License

MIT License

Copyright (c) [2022] [Karl Järvitalo Beckérus]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.