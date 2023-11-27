import re

def vate(objective):
    bot = "Vou até "
    for obj in objective[0]:
        if obj:
            bot += str(obj)
    
    return bot

intent_dict = {
    r"\b(?:v[áa] para|dirja-se ao|me leve para|v[áa] pro|me leve at[ée])\s+(?:a\s+)?(\w+)": "vate",
}

action_dict = {
    "vate": vate,
}

print('fala tu (escreve "sair" pra sair)')
while True:
    command = input().lower()

    if command == "sair": break

    for key, value in intent_dict.items():
        pattern = re.compile(key)
        groups = pattern.findall(command)
        if groups:
            print(action_dict[value](groups))
    print()