import requests
cityName = input("nom de votre ville")
langage="fr"
clef="8da70054636bb534bcace716b97cf5f4"
part="hourly"
def hel_to_cel(kelvin):
    cel=kelvin-273.15
    return cel
api_lien=f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={clef}&lang={langage}"
json= requests.get(api_lien).json()
response=json["weather"][0]["description"]
temp= json["main"]["temp"]
temp_cel=hel_to_cel(temp)
name=json["name"]
print(f"name:{name} descri: {response} tmp: {temp_cel:.2f}°C")