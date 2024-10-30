import random as r
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Una cara riendo",
            "RANDOM": "Algo aleatorio",
            "ESTA MUY ROTO": "Cuando algo tiene mucho poder",
            "COOL": "Cuando algo es muy increible, impresionante o grandioso"
            }
print(meme_dict.keys())
word = input("Escribe una palabra que no entiendas:").upper()

if word in meme_dict.keys():
    print("Significa:", meme_dict[word])
else:
    print("Por el momento no se a agregado esya palabra al diccionario")
