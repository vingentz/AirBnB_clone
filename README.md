# AirBnB clone - The console
---

![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

---

## Description of the project:

This project involves developing an AirBnb clone using python scripts adhering to specific coding standards. Created clsses ,functions and modules a adhering to strict code style quidelines (pycodestyle) alongside their documnetation.Unit tests are organized in the 'tests' folder,following the project's structure, and executed using 'python3-m unittest discover tests.

---

## Description of the command interpreter:

The interface of the application is just like the Bash shell except that this has a limited number of accepted commands  defined for the purposes of the usage of the AirBnB website.

This command line interpreter serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

 The  console will  perform the folloewing:
-   Creating new objects (ex: a new User or a new Place)
-   Retrieving an object from a file, a database etc…
-   Doing operations on objects (count, compute stats, etc…)
-   Updating attributes of an object
-   Destroying an object

---

## How to use it

* It can work in two different modes interactive and non-interactive.

    * In **Interactive mode**, a program allows real-time user interaction. It provides a prompt where users can input commands, receive immediate feedback, and make further inputs based on the program's responses. 
    * This mode is highly engaging and facilitates dynamic exploration, debugging, and experimentation.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

    * In **Non-interactive mode**,a program executes predefined tasks without requiring constant user input. It operates autonomously, following a predetermined sequence of commands or instructions.
    * This mode is often used for automated processes, batch operations, or when user interaction is not necessary or feasible.


```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
---

## Author :black_nib:
* **Kevin Kariuki** [vingentz](https://github.com/vingentz)
* **BenieShann** [Shann](https://github.com/BenieShann)
