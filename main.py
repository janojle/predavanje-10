import  json
#r - read
with open("data/user.json", "r") as file:
    data = json.load(file)
    #data i file su varijable
    data.append({
        "name": "Petar Petrovic",
        "age": 29,
        "height": 187,
        "gender": "male"
    })

print(data)

# w -write
with open("data/user.json", "w") as file:
    json.dump(data, file, indent=4)