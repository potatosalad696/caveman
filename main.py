import sys

try:
    script = sys.argv[1]
except IndexError:
    print("How am I supposed to run nothing?")

class Instance:
    pass
    
with open(script, "r") as f:
    file = f.read().split("\n")

main = Instance()
main.run()