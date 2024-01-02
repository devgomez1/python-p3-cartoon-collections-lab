CHEESE = ["cheddar", "gouda", "camembert"]

def roll_call_dwarves(dwarfes):
    for i in range(len(dwarfes)):
        print(f"{i+1}. {dwarfes[i]}")
    return dwarfes

def summon_captain_planet(elements):
    for i in range(len(elements)):
        elements[i] = elements[i].capitalize() + "!"
    return elements

def long_planeteer_calls(list):
    for i in range(len(list)):
        if len(list[i]) > 4:
            return True
    return False
        

def find_the_cheese(list):
    for i in range(len(list)):
        if list[i] in CHEESE:
            return list[i]
    return None

