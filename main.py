import sys

try:
    script = sys.argv[1]
except IndexError:
    raise ValueError("Missing file (how am I supposed to run nothing?)")

class Instance:
    def __init__(self, lines: list[str], variables: dict, functions: dict):
        self.lines = [_line.strip("    ") for _line in lines]
        self.variables = variables
        self.functions = functions
        self.ignore = []

    def comparisons(self, mode, first, second, result):
        val = True

        match mode:
            case "less":
                val = first < second
            case "more":
                val = first > second
            case "same":
                val = first == second
            case "nosame":
                val = first != second
            case "and":
                val = first and second
            case "or":
                val = first or second

        val = "yes" if val == True else "no"
        self.update_var("yesno", result, val)

    def update_var(self, datatype, name, val: str):
        match datatype:
            case "say":
                if not is_valid_string(val):
                    raise SyntaxError(f"Invalid text")
                
                val = remove_quotes(val)
            case "fingers":
                val = remove_quotes(val)
                
                if val.count(".") != 0:
                    val = float(val)
                else:
                    val = int(val)
            case "yesno":
                val = remove_quotes(val)

                if val == "yes":
                    val = True
                elif val == "no":
                    val = False
                else:
                    raise ValueError("Invalid value for yesno")

        self.variables.update({
            name: val
        })

    def parse_yesno(self, val: str):
        if val == "yes":
            return True
        elif val == "no":
            return False
        else:
            return self.variables[val]

    def run(self):
        for idx, line in enumerate(self.lines):
            if line == "":
                continue
            if idx in self.ignore:
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
                        values = remove_quotes(double_blanket(values)).format_map(self.variables)
                        print(values)
                    else:
                        print(self.variables[values])
                case "say" | "fingers" | "yesno":
                    tokens = values.split(" ", 1)

                    name = tokens[0]
                    value = tokens[1]

                    self.update_var(command, name, value)
                case "what":
                    tokens = values.split(" ", 2)

                    datatype = tokens[0]
                    name = tokens[1]
                    to_ask = tokens[2]

                    if not is_valid_string(to_ask):
                        raise SyntaxError(f"Invalid text")

                    value = input(to_ask.replace('"', ""))
                    self.update_var(datatype, name, f'"{value}"')
                case "give" | "take":
                    tokens = values.split(" ", 2)

                    first = tokens[0]
                    second = tokens[1]
                    result = tokens[2]

                    first = self.variables[first] if not str(first).isnumeric() else float(first)
                    second = self.variables[second] if not str(second).isnumeric() else float(second)

                    output = first + second if command == "give" else first - second
                    self.update_var("fingers", result, str(output))
                case "less" | "more" | "same" | "nosame" | "and" | "or":
                    tokens = values.split(" ", 2)

                    first = tokens[0]
                    second = tokens[1]
                    result = tokens[2]

                    first = self.variables[first] if not str(first).isnumeric() else float(first)
                    second = self.variables[second] if not str(second).isnumeric() else float(second)

                    self.comparisons(command, first, second, result)
                case "times":
                    start = idx + 1
                    future = self.lines[start:]
                    end = future.index("again !") + start

                    new_lines = self.lines[start:end]
                    for i in range(start, end + 1):
                        self.ignore.append(i)

                    new_instance = Instance(new_lines, self.variables, self.functions)
                    times = self.variables[values] if not str(values).isnumeric() else int(values)
                    
                    for _ in range(times):
                        new_instance.run()
                case "when":
                    tokens = values.split(" ", 1)

                    start = idx + 1
                    future = self.lines[start:]
                    end = future.index("done !") + start

                    new_lines = self.lines[start:end]
                    for i in range(start, end + 1):
                        self.ignore.append(i)

                    new_instance = Instance(new_lines, self.variables, self.functions)
                    val1 = self.parse_yesno(tokens[0])
                    val2 = self.parse_yesno(tokens[1])

                    if val1 == val2:
                        new_instance.run()
                case "start":
                    start = idx + 1
                    future = self.lines[start:]
                    end = future.index("go !") + start

                    new_lines = self.lines[start:end]
                    for i in range(start, end + 1):
                        self.ignore.append(i)

                    self.functions.update({
                        values: new_lines
                    })
                case "do":
                    new_lines = self.functions[values]
                    new_instance = Instance(new_lines, self.variables, self.functions)
                    new_instance.run()
                case "uhh":
                    continue

## TODO: "yes" instead of "True"

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
        "give": " !!",
        "take": " !!",
        "less": " ?",
        "more": " ?",
        "same": " ?",
        "nosame": " ?",
        "and": " ?",
        "or": " ?",
        "times": " ,",
        "again": "!",
        "when": " ,",
        "done": "!",
        "start": " ,",
        "go": "!",
        "do": " !!",
        "uhh": " .",
        "bring": " !!", # variables that are taken in by a function
        "here": " !" # return
    }

    if val.endswith(endings[com]):
        return [True, endings[com]]
    else:
        return [False, endings[com]]
    
with open(script, "r") as f:
    code = f.read().split("\n")

main = Instance(code, {}, {})
main.run()