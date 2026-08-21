def update_var(datatype, name, val):
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

variables = {}

with open("main.man", "r") as f:
    code = f.read().split("\n")

for line in code:
    if line == "":
        continue

    tokens = line.split(" ", 1)

    first = tokens[1].split(" ", 1)[0]
    second = tokens[1].split(" ", 1)[1]

    match tokens[0]:
        case "shout":
            mode = first
            to_print = second

            match mode:
                case "normal":
                    print(to_print.replace('"', ""))
                case "special":
                    ...
        case "words" | "number" | "yesno":
            update_var(tokens[0], first, second)

print(variables)