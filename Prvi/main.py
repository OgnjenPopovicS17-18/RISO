import http.client
import json

conn = http.client.HTTPSConnection("getpantry.cloud")
predmet = ["Sql programiranje","C programiranje","C# programiranje"]

class kontakt: 
    adresa = "Vojacka 51",
    mesto = "Zemun",
    telefon = "065 555 333"

kontakt = kontakt()

payload = json.dumps({
  "id" : "112233",
  "ime": "Ognjen",
  "prezime":"Popovic",
  "smer": "Informacione tehnologije",
  "predmet": predmet,
  "prosek" : "7.6",
  "kontakt": [kontakt.adresa,kontakt.mesto,kontakt.telefon] 

})

headers = {
  'Content-Type': 'application/json'
}

conn.request("POST", "/apiv1/pantry/491f191d-617b-4175-902c-83667f32fa23/basket/Ognjen", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))