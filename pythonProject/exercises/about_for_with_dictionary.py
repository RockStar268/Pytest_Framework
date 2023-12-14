def my_info():
    some_info = {
        "Birthcity: ": "Eindhoven",
        "Car: ": "LynkCo",
        "Favourite Genre: ": "Reggae",
        "Lucky Number: ": "7"
    }

    for keys, values in some_info.items():
        print(keys, values)
        print("===")
        print(f"{keys} {values}")
        print("===")

    print("I am printing only the lucky number, retrieved from given dictionary: " + str(some_info["Lucky Number: "]))


my_info()
