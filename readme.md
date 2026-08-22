# Caveman
Caveman is a programming language that ***tries*** to sound as close to a stereotypical caveman as possible. Therefore, it uses **a lot of** unconventional names, and it is simpler than other programming languages.

**This programming language should not be used for anything serious.**

The sections below are the learning guides for Caveman.

## Chapter 1 - Printing
There are two functions that can be used to print in Caveman. ```scream``` is used purely for text. If you want to print variables in any way, you have to use ```shout``` (to learn more, read Chapter 2).
```
scream [value] !!!
shout [value] !!
```

For example, to print `Hello World` in Caveman, write this line below:
```
scream "Hello World" !!!
```

Output:
```
Hello World
```

`shout` can be used in this case, but `scream` is preferred. Double quotation marks (`"`) **must** be used, as the language does not recognize single quotation marks (`'`).

## Chapter 2 - Variables
Variable declaration in Caveman is shown below:
```
[type] [name] [value] !
```

Variables should not use a used keyword (for example, `shout`). For example, to declare a variable named `rock` with a value of `7`, write this line below:
```
number rock 7 !
```

### Variable Types
There are different variable types in Caveman, and all of them use unconventional names.

#### words
`words` is used to store text, and therefore is similar to the `string` datatype used in other languages. An example is shown below:
```
words want_eat "meat" !
```

#### number
`number` is used to store numbers, whether they are integers or decimals (since cavemen *probably* don't understand the concept of decimals). Therefore, it is similar to the `int` and `float` datatypes found in Python. An example is shown below:
```
number animals 100 !
number days 1.5 !
```

#### yesno
`yesno` is used to store `yes` or `no`, and thus is equivalent to the `bool` datatype. Instead of using `true` or `false`, Caveman uses `yes` and `no`. An example is *probably* shown below:
```
yesno have_meat yes !
```

### `shout special`
`shout special` is used to combine text and variables. It is similar to an f-string in Python. To use it, variables have to be enclosed in `([])` (called a double blanket). An example is shown below:
```
words want_eat "meat"

shout normal want_eat
shout special "me want eat ([want_eat])"
```

Output:
```
meat
me want eat meat
```

`shout special` does not support operations within a double blanket.

### Input
To get input from the user, use this syntax:
```
what [type] [name] [value]
```

`what` will immediately assign the input to a variable with the same name and the same datatype. An example is shown below:
```
what number age "Age? "
shout special "You ([age])"
```

Output:
```
Age? 25
You 25
```