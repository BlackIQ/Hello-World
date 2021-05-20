# ~English
~English ("NOT English") was an esoteric attempt at using a natural
 language as programming language.
This repository hosts a second, revised version of the language.
This updated version generalizes many language concepts and introduces
 a number of new features. 

New language features (will) include: ([X] means implemented)
* New function call syntax [X]
* Generalization of "Display" (it is now a function) [X]
* Comments [X]
* Constants for often used values. [X]
* Introduce "it" (and possibly "its") as a reference to the
 last-used variable.
* User-defined functions/subroutines [X]
* User-defined functions take arguments by reference [X]
* Return statement
* Sentences can end in "!" or "?".
* Built-in objects and variable generalization
* User-created libraries (using C/C++)
* User-created libraries (using Python)
* Built-ins moved to "standard" library.
* Arrays and array library.
* String library.
* Socket library.

## Practical information
* Compile with -std=c++11.
* boost::any, boost::variant and boost::lexical_cast are being used
 (these do not require linking though)

The source code is based upon the old source code, although it has been
 (somewhat) cleaned up.

## Overview of new features

### New function call syntax
The new syntax for calling functions is as following (example):

    Display "First argument", a newline, "Second argument"
     and another newline.

(Where display is a function.)
And in expressions:

    Set the value of name to the result of getInput.

### Comments
Anything starting with "Note:" or "Note" is considered a comment, eg.:

    Create a variable called name. Note: name holds the username.
    Set the value of name to "undefined". Note that "undefined" is only
     a placeholder.

Synonyms for "Note"/"Note:" include "Notice", "Notice:" and "Mind".

### Constants for often used values
Example:

    Set the value of i to one.
    Dipslay i and a newline.

### User-defined functions
To use a user-defined function, you must first declare it and then define
 it.

Example:

    Note: the following line is the declaration. Mind the "with" construct.
    Create a function called Greet with argument name.
    Notice: the next line is the implementation.
    Upon calling Greet do:
    Display "Hello", the name and a newline.
    That's all.
    Note that the next line is not a part of the definition (it's a call).
    Greet "world".

Synonyms for "When" include "Upon" and "Whenever". Synonyms for "calling"
 include "executing", "running" and "evaluating".
Note also that arguments are by default passed by-reference in ~English.
This means hat if you modify an argument, that modification is not bound to
 the scope of the function.
