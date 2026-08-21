import os

def update_var(datatype, name, val: str):
    value = val

    match datatype:
        case "words":
            value = remove_quotes(value)
        case "number":
            value = int(value)
        case "yesno":
            value = True if value == "yes" else False

    variables.update({
        name: value
    })

def remove_quotes(text: str):
    return text.replace('"', "")

def is_valid_string(text: str):
    return (text[0] == '"') and (text[-1] == '"')

### stuff ###

os.system("clear")

variables = {}

with open("main.man", "r") as f:
    code = f.read().split("\n")

for line in code:
    if line == "":
        continue

    tokens = line.split(" ", 1)

    match tokens[0]:
        case "shout":
            first = tokens[1].split(" ", 1)[0]
            second = tokens[1].split(" ", 1)[1]

            mode = first
            to_print = second

            match mode:
                case "normal":
                    if is_valid_string(to_print):
                        print(to_print.replace('"', ""))
                    else:
                        if variables[to_print] == True:
                            print("yes")
                        elif variables[to_print] == False:
                            print("no")
                        else:
                            print(variables[to_print])
                case "special":
                    if is_valid_string(to_print):
                        to_print = to_print.replace('"', "").replace("([", "{").replace("])", "}")
                        print(to_print.format_map(variables)) # yesno breaks
                    else:
                        if variables[to_print] == True:
                            print("yes")
                        elif variables[to_print] == False:
                            print("no")
                        else:
                            print(variables[to_print])
        case "words" | "number" | "yesno":
            first = tokens[1].split(" ", 1)[0]
            second = tokens[1].split(" ", 1)[1]

            update_var(tokens[0], first, second)
        case "what":
            first = tokens[1].split(" ", 2)[0]
            second = tokens[1].split(" ", 2)[1]
            third = tokens[1].split(" ", 2)[2]

            temp = input(third.replace('"', ""))
            update_var(first, second, temp)