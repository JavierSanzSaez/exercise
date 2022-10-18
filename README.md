# Unimover - An open Python module for an exercise

## Installation
This repository only contains the source code, so you will need to build the package itself.

Firstly install the requirements for Python...

```bash
pip install -r requirements.txt
```
...as well as the Debian dependencies:

```bash
sudo apt-get install build-essential devscripts debhelper debmake
```

Then, locate yourself on the parent directory and build the package with the `build` package

```bash
python -m build
```

Untar the file inside `dist`:

```bash
cd dist && tar -xzmf unimover-1.0.tar.gz 
```

For debian package building, you will have to enter the `unimover-1.0` folder and create the Makefile:

```bash
cd unimover-1.0 && debmake
```

On the `debian` folder, apply any needed changes to the `control`, `rules` or other files and finish building the package:

```bash
debuild
```

After it is finished, you can easily install the package via `apt-get`:

```bash
sudo apt-get install ./unimover-1.0-*.deb -y
```

## Usage 
Unimover can be imported either via a simple Python import or via a Debian import

### Via Python
Simply import the package

```python
from unimover import main as unimover_main

unimover_main(group= "group", destination="destination path")
```

### Via apt-get
The `setup.py` file allows you to create a symbolic link so that you can avoid using `python -m`. Therefore, you can call the script with:

```bash
unimover <group> <destination_path>
```

## Logging
This program will output logs for all the duration of the execution. An example of such logging is in [this file](output.log), where several executions have been made with correct and incorrect parameters.

For now the script will log every level. If you want to change this behaviour, it can be changed by changing this line:

```python
logging.basicConfig(format='%(asctime)s - %(levelname)s -%(message)s', filename='output.log', filemode='a', level=logging.DEBUG)
```

And altering the parameter `level` for the level desired. See more information at the [logging documentation](https://docs.python.org/3/library/logging.html#logging-levels)