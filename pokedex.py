#!/usr/bin/env python3

import requests
import json
import os

f = open("json/test.json", "w", encoding="utf-8")

r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10000").json()

mons = list()

for i in r["results"]:
    pokemon = requests.get(i["url"]).json()
    species = requests.get(pokemon["species"]["url"]).json()
    species_name = [x["name"] for x in species["names"] if x["language"]["name"] == "en"][0]
    forms = list()
    c = pokemon["id"]-1
    while c <= 1025:
        for form in pokemon["forms"]:
            if form["name"] == pokemon["name"]:
                continue
            else:
                forms.append(form["name"])
        for variety in species["varieties"]:
            if variety["pokemon"]["name"] == pokemon["name"]:
                continue
            else:
                forms.append(variety["pokemon"]["name"])

        match pokemon["name"]:
            case "tauros":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": pokemon["name"], "name": species_name, "forms": [p.removesuffix("-breed") for p in forms] })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "burmy":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": pokemon["name"], "name": species_name, "forms": forms, "default": "burmy-plant" })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "wormadam-plant":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": "wormadam", "name": species_name, "forms": forms+["wormadam-plant"], "default": "wormadam-plant" })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "cherrim":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": pokemon["name"], "name": species_name, "forms": forms, "default": "cherrim-overcast" })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "shellos" | "gastrodon":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": pokemon["name"], "name": species_name, "forms": forms, "default": pokemon["name"]+"-west" })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "darmanitan-standard":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": "darmanitan", "name": species_name, "forms": [p.removesuffix("-standard") for p in forms] })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "deerling" | "sawsbuck":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": pokemon["name"], "name": species_name, "forms": forms, "default": pokemon["name"]+"-spring" })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "genesect":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": pokemon["name"], "name": species_name, "forms": forms+["genesect-no-drive"], "default": "genesect-no-drive" })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "xerneas":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": pokemon["name"], "name": species_name, "forms": forms, "default": "xerneas-neutral" })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "zygarde-50":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": species["name"], "name": species_name, "forms": forms+[pokemon["name"]], "default": pokemon["name"] })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "zacian" | "zamazenta":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"],"species": species["name"], "name": species_name, "forms": forms+[pokemon["name"]+"-hero"], "default": pokemon["name"]+"-hero" })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "maushold":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": species["name"], "name": species_name, "forms": forms, "default": "maushold-family-of-three" })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "squawkabilly":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": species["name"], "name": species_name, "forms": forms, "default": "squawkabilly-green-plumage" })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "palafin":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": species["name"], "name": species_name, "forms": forms, "default": "palafin-zero" })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "tatsugiri":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": species["name"], "name": species_name, "forms": forms, "default": "tatsugiri-curly" })
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "dudunsparce":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": species["name"], "name": species_name, "forms": forms, "default": "dudunsparce-two-segment"})
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "gimmighoul":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": species["name"], "name": species_name, "forms": forms, "default": "gimmighoul-chest"})
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "ogerpon":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": species["name"], "name": species_name, "forms": forms+["ogerpon-teal-mask"], "default": "ogerpon-teal-mask"})
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "toxtricity-amped":
                fixed_forms = []
                for form in forms:
                    if "gmax" not in form:
                        fixed_forms.append(form)
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": species["name"], "name": species_name, "forms": fixed_forms+["toxtricity-gmax", "toxtricity-amped"], "default": "toxtricity-amped"})
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "calyrex":
                fixed_forms = []
                for form in forms:
                    fixed_forms.append(form+"-rider")
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": species["name"], "name": species_name, "forms": fixed_forms, "default": "calyrex-rider"})
                print("put: ", pokemon["name"])
                print(mons[c])
                break
            case "giratina-altered" | "shaymin-land" | "basculin-red-striped" | "tornadus-incarnate" | "thundurus-incarnate" | "landorus-incarnate" | "keldeo-ordinary" | "meloetta-aria" | "oricorio-baile" | "lycanroc-midday" | "wishiwashi-solo" | "minior-red-meteor" | "mimikyu-disguised" | "eiscue-ice" | "morpeko-full-belly" | "urshifu-single-strike" | "enamorus-incarnate" | "deoxys-normal" | "indeedee-male" | "aegislash-shield" | "basculegion-male" | "meowstic-male" | "pumpkaboo-average" | "gourgeist-average":
                mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": species["name"], "name": species_name, "forms": forms+[pokemon["name"]], "default": pokemon["name"] })
                print("put: ", pokemon["name"])
                print(mons[c])
                break

        mons.append({ "pokedex_number": species["pokedex_numbers"][0]["entry_number"], "species": species["name"], "name": species_name, "forms": forms })
        print("put: ", pokemon["name"])
        print(mons[c])
        break
    else:
        f.write(json.dumps(mons, ensure_ascii=False, indent=4))
        check = input("Is this the correct output (y/n): ")
        if check == "y":
            f = open("json/pokedex.json", "w", encoding="utf-8")
            f.write(json.dumps(mons, ensure_ascii=False, indent=4))
            os.remove("json/test.json")
            f.close()
            break
        elif check == "n":
            f.close()
            os.remove("json/test.json")
            break