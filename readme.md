# Caveman
***AI is not used in this project.***<br>
**1.0.0 Iteration 1** (read [changelog](changelog.md) for more)

Caveman is a programming language that ***tries*** to sound as close to a stereotypical caveman as possible. Therefore, it uses **a lot of** unconventional names, and it is simpler than other programming languages.

**This programming language should not be used for anything serious.**

The sections below are the learning guides for Caveman.

## Chapter 0 - How to Stay Alive
To run a Caveman program, you need to have **Python 3.10 and up**. Install the interpreter, and create your Caveman file in the same folder as the interpreter. The Caveman file should end in `.cave`.

To run the file, run this command:
```
(python3 / python) main.py [file].cave
```

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

### Comments
To add comments in Caveman, use this syntax:
```
>> [comments]
```

This will be ignored by the interpreter.

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

## Chapter 3 - Take the Bigger One
The way Caveman does math is *very* weird (but that's what makes it special).

### Operations
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

### Comparisons
There are 6 types of comparisons, listed below:
```
less [first] [second] [result] ?
more [first] [second] [result] ?
same [first] [second] [result] ?
nosame [first] [second] [result] ?
and [first] [second] [result] ?
or [first] [second] [result] ?
```

They are equivalent to `<`, `>`, `==`, `!=`, `and` / `&&`, and `or` / `||` respectively. The result will be stored in the variable under `[result]`, and it will be either `yes` or `no`. `first` and `second` can either be a variable or a number, **but not a string**. You know where the example is.
```
fingers age 20 !
more age 21 is_more_21 ?
shout is_more_21 !!
```

Output _(note: this is a bug and should output `no`. We're still working on it.)_:
```
False
```

## Chapter 4 - Clap Twice If You're Happy
Loops, functions, and conditionals are not left out in Caveman.

### Loops
To loop in Caveman, use this syntax:
```
times [times] ,
    [code]
again !
```
Loops **cannot** be nested with other loops, and the same thing is true for conditionals. This is similar to the `for` loop (not including `foreach`).

Although indentation does not matter, it is common etiquette to include one, preferrably 4 spaces per tab.

### Conditionals
To do conditionals in Caveman, use this syntax below:
```
when [val1] [val2] ,
    [code]
done !
```

`val1` and `val2` can either be booleans (`yes` or `no`) or variables. `when` checks if both of the values are the same.

Although one can use `same`, the creator decided to be nice for once.

### Functions
Functions are integral in Caveman. To declare a function and call it, use this syntax:
```
start [name] ,
    [code]
go !

do [name] !!
```

## Appendix A - Exclamation Questions
There are different types of endings in Caveman.
- `!`
    - This is the default ending in Caveman. When in doubt, use this.
- `!!`
    - This is used for `shout`, `give`, and `take`. Think of it as an emphasizer.
- `!!!`
    - This is used for `scream`. It's basically an emphasize-emphasizer.
- `?`
    - This is used for `what` and the Comparison family (notably And Comparison). It's a question mark, so it's used for questions.
- `,`
    - This is used for `start`, `when`, and `times`. Used for lines that contain other codes.

## Appendix B - What is a "Double Blanket?"
There are many unique Caveman terminologies that people might not understand. Here are some common ones:

- **double blanket** - `[[]]`, used for `shout`
- **endings** - see Appendix A
- **fingers** - integers, floats
- **says** - strings
- **things** - variables