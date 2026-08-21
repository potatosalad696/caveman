# Caveman
Caveman is a programming language that ***tries*** to use as few symbols as possible, replacing common symbols such as `=`, `==`, and others to `is`, `equals`, and others. It also tries to sound as close to a stereotypical caveman as possible.

**This programming language should not be used for anything serious.**

The sections below are the learning guides for Caveman.

## Chapter 1 - Printing
The syntax for printing in Caveman is shown below:
```
shout normal [val]
shout special [val]
```

For example, to print ```Hello World``` in Caveman, write this line below:
```
shout normal "Hello World"
```

Output:
```
Hello World
```

To see how to use ```shout special```, read Chapter 2

## Chapter 2 - Variables
Variable declaration in Caveman is shown below:
```
[type] [name] [value]
```

Variables should not use a used keyword (for example, `shout`). For example, to declare a variable named `rock` with a value of `7`, write this line below:
```
number rock 7
```

### Variable Types
There are different variable types in Caveman, and most of them use unconventional names.

#### words
`words` is used to store text, and therefore is similar to the `string` datatype used in other languages. An example is shown below:
```
words want_eat "meat"
```

#### number
```number``` is used to store numbers, whether they are integers or decimals (since cavemen *probably* don't understand the concept of decimals). Therefore, it is similar to the `int` and `float` datatypes found in Python. An example is shown below:
```
number animals 100
```

#### yesno
```yesno``` is used to store ```yes``` or ```no```, and thus is equivalent to the `bool` datatype. Instead of using ```true``` or ```false```, Caveman uses ```yes``` and ```no```. An example is *probably* snown below:
```
yesno have_meat yes
```