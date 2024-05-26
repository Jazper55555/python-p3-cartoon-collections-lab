def roll_call_dwarves(list):
    for index, dwarve in enumerate(list):
        print(f"{index + 1}. {dwarve}")
    pass

def summon_captain_planet(planeteer_calls):
    capital_calls = [f"{call.capitalize()}!" for call in planeteer_calls]
    return capital_calls
    pass

def long_planeteer_calls(planeteer_calls):
    for call in planeteer_calls:
        if len(call) > 4:
            return True
    return False
    pass

def find_the_cheese(list):
    if 'cheddar' in list:
        return 'cheddar'
    elif 'gouda' in list:
        return 'gouda'
    elif 'camembert' in list:
        return 'camembert'
    else:
        return None
    pass
