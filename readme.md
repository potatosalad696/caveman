# Caveman
Caveman is a programming language that ***tries*** to sound as close to a stereotypical caveman as possible. Therefore, it uses **a lot of** unconventional names, and it is simpler than other programming languages.

**This programming language should not be used for anything serious.**

The sections below are the learning guides for Caveman.

## Chapter 1 - Shouting, Screaming, Saying
There are two functions that can be used to print in Caveman. ```scream``` is used purely for text. If you want to print variables in any way, you have to use ```shout``` (to learn more, read Chapter 2).
```
scream [text] !!!
shout [text] !!
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

## Chapter 2 - Things and Stuff, I Guess
Variable declaration in Caveman is shown below:
```
[type] [name] [value] !
```

Variables should not use a used keyword (for example, `shout`). For example, to declare a variable named `rock` with a value of `7`, write this line below:
```
fingers rock 7 !
```

### Variable Types
There are different variable types in Caveman, and all of them use unconventional names.

#### say
`say` is used to store text, and therefore is similar to the `string` datatype used in other languages. An example is shown below:
```
say want_eat "meat" !
```

#### fingers
`fingers` is used to store numbers, whether they are integers or decimals (since cavemen *probably* don't understand the concept of decimals). Therefore, it is similar to the `int` and `float` datatypes found in Python. An example is shown below:
```
fingers animals 100 !
fingers days 1.5 !
```

#### yesno
`yesno` is used to store `yes` or `no`, and thus is equivalent to the `bool` datatype. Instead of using `true` or `false`, Caveman uses `yes` and `no`. An example is *probably* shown below:
```
yesno have_meat yes !
```

### `shout`
`shout` is used to print variables, whether they are by themselves or combined with text. To combine variables with text, variables have to be enclosed in `[[]]` (called a double blanket). An example is shown below:
```
say want_eat "meat" !

shout want_eat !!
shout "me want eat [[want_eat]]" !!
```

Output:
```
meat
me want eat meat
```

`shout` does not support operations within a double blanket.

### Input
`what` is used for input. To get input from the user, use this syntax:
```
what [type] [name] [text] ?
```

`what` will immediately assign the input to a variable with the same name and the same datatype. An example is shown below:
```
what fingers age "Age? " ?
shout "You [[age]]" !!
```

Output:
```
Age? 25
You 25
```

## Chapter 3 - Operations by Operators
`give` and `take` are used to do additions and subtractions respectively in Caveman. The syntax is shown below:
```
give [first] [second] [result] !!
take [first] [second] [result] !!
```

`first` and `second` can be variables or numbers, meanwhile result is always a variable. An example is shown below.
```
fingers old_meat 7 !
fingers new_meat 14 !

shout old_meat !!
give old_meat new_meat old_meat !!
shout old_meat !!
```

Output:
```
7
21
```

## Appendix A - Endings
There are different types of endings in Caveman.
- `!`
    - This is the default ending in Caveman. When in doubt, use this.
- `!!`
    - This is used for `shout`, `give`, and `take`. Think of it as an emphasizer.
- `!!!`
    - This is used for `scream`. It's basically an emphasize-emphasizer.
- `?`
    - This is used for `what`. It's a question mark, so it's used for questions.