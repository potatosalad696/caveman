import os

## TODO: NEWLINE CHARS
## ? FOR WHAT
## ! FOR SHOUT
## . FOR ELSE

variables = {}

def update_var(datatype, name, val: str):
    match datatype:
        case "words":
            if not is_valid_string(val):
                raise SyntaxError(f"Invalid text")
            
            val = remove_quotes(val)
        case "number":
            if val.count(".") != 0:
                val = float(val)
            else:
                val = int(val)
        case "yesno":
            if val == "yes":
                val = True
            elif val == "no":
                val = False
            else:
                raise ValueError("Invalid value for yesno")

    variables.update({
        name: val
    })

def is_valid_string(val: str):
    return (val[0] == '"') and (val[-1] == '"')

def remove_quotes(val: str):
    return val.removeprefix('"').removesuffix('"')

def has_right_ending(com: str, val: str):
    endings = {
        "scream": " !!!",
        "shout": " !!",
        "words": " !",
        "number": " !",
        "yesno": " !"
    }

    if val.endswith(endings[com]):
        return [True, endings[com]]
    else:
        return [False, endings[com]]

### stuff ###

os.system("clear")
with open("main.man", "r") as f:
    code = f.read().split("\n")

for line in code:
    if (line == "") or (line.startswith(">> ")):
        continue

    command = line.split(" ", 1)[0]
    values = line.split(" ", 1)[1]

    is_valid_ending = has_right_ending(command, values)[0]
    ending = has_right_ending(command, values)[1]

    if not is_valid_ending:
        raise SyntaxError(f"Incorrect ending ('{command}' uses '{ending}')")
    
    values = values.removesuffix(ending)

    match command:
        case "scream":
            if not is_valid_string(values):
                raise SyntaxError(f"Invalid text")
            
            values = remove_quotes(values)
            print(values)
        case "shout":
            pass
        case "words" | "number" | "yesno":
            name = values.split(" ", 1)[0]
            value = values.split(" ", 1)[1]

            update_var(command, name, value)
        case "what":
            first = values.split(" ", 2)[0]
            second = values.split(" ", 2)[1]
            third = values.split(" ", 2)[2]

            temp = input(third.replace('"', ""))
            update_var(first, second, temp)

print(variables)