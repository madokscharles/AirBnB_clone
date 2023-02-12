0x00. AirBnB clone - The Console


Project Description
**********************
The console is the first of all the AirBnB clone projects. The goal of this project is to:
	- Create a data model
	- Manage (create, update, destroy, etc) objects via a console / command interpreter
	- Store and persist objects to a file (JSON file)


Command Interpreter description
**********************************
The command interpreter is like a CLI with specific commands like the AirBnB website. It is how we would interact with our project like a user interface (front-end)

	- How to start it?
****************************
Installation
**************
git clone https://github.com/OMmienu/AirBnB_clone.git

cd into directory and run "console.py"

	How to use it?
*************************
Use the commands given:
- Create: create CLASS
	- Creates a new object and saves it

- Show: show CLASS ID
	- Displays a specific object
- Destroy: destroy CLASS ID
	- Destroys a specific object
- All: all [CLASS]
	- Displays all objects in storage (of a particular class or the entire storage)
- Update: update CLASS ID NAME
	- Updates attributes of a specific object

Authors
**********
Isaac Edzie Edzie
Madoks Dokubo
*******************

### Storage

All the classes are handled by the `Storage` engine in the `FileStorage` Class.

<!-- Style guidelines -->
* Style guidelines:
  * [pycodestyle (version 2.7.*)](https://pypi.org/project/pycodestyle/)
  * [PEP8](https://pep8.org/)

### Execution

In interactive mode

```bash
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

in Non-interactive mode

```bash
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


### Documentation

* Modules:

```python
python3 -c 'print(__import__("my_module").__doc__)'
```

* Classes:

```python
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```

* Functions (inside and outside a class):

```python
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```

and

```python
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

### Python Unit Tests

* unittest module
* File extension ``` .py ```
* Files and folders star with ```test_```
* Organization:for ```models/base.py```, unit tests in: ```tests/test_models/test_base.py```
* Execution command: ```python3 -m unittest discover tests```
* or: ```python3 -m unittest tests/test_models/test_base.py```

### run test in interactive mode

```bash
echo "python3 -m unittest discover tests" | bash
```

### run test in non-interactive mode

To run the tests in non-interactive mode, and discover all the test, you can use the command:

```bash
python3 -m unittest discover tests
```
