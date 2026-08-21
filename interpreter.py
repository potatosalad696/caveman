with open("main.man", "r") as f:
    code = f.read().split("\n")

for line in code:
    if line.startswith("say "): # printing
        to_print = line.split(" ", 1)[1].replace('"', "")
        print(to_print)