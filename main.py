import sys

try:
    script = sys.argv[1]
except IndexError:
    raise ValueError("Missing file (how am I supposed to run nothing?)")

variables = {}

def update_var(datatype, name, val: str):
    match datatype:
        case "say":
            if not is_valid_string(val):
                raise SyntaxError(f"Invalid text")
            
            val = remove_quotes(val)
        case "fingers":
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

def double_blanket(val: str):
    return val.replace("[[", "{").replace("]]", "}")

def has_right_ending(com: str, val: str):
    endings = {
        "scream": " !!!",
        "shout": " !!",
        "say": " !",
        "fingers": " !",
        "yesno": " !",
        "what": " ?",
        "give": " !",
        "take": " !"
    }

    if val.endswith(endings[com]):
        return [True, endings[com]]
    else:
        return [False, endings[com]]
    
with open(script, "r") as f:
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
            if is_valid_string(values):
                values = remove_quotes(double_blanket(values)).format_map(variables)
                print(values)
            else:
                print(variables[values])
        case "say" | "fingers" | "yesno":
            name = values.split(" ", 1)[0]
            value = values.split(" ", 1)[1]

            update_var(command, name, value)
        case "what":
            datatype = values.split(" ", 2)[0]
            name = values.split(" ", 2)[1]
            to_ask = values.split(" ", 2)[2]

            if not is_valid_string(to_ask):
                raise SyntaxError(f"Invalid text")

            value = input(to_ask.replace('"', ""))
            update_var(datatype, name, value)
        case "give" | "take":
            first = values.split(" ", 2)[0]
            second = values.split(" ", 2)[1]
            result = values.split(" ", 2)[2]

            first = variables[first]
            second = variables[second]

            output = first + second if command == "give" else first - second
            update_var("fingers", result, str(output))