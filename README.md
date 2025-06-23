# Tkinter Basics

Repository to keep track of what I've learned about the basics of Tkinter.

## How to use this repository

1. Clone this repository
2. Create a Python virtual environment
3. Play with the code!

The recommended way to manage your virtual environments is with the tool `uv` [docs](https://docs.astral.sh/uv/)
in Mac/Linux

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

in Windows

```shell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Clone the repository

Use `git`

```shell
git clone https://github.com/AlexRFarnes/tkinter_basics
```

### Create your Python virtual environment

Change into the repository **c**hange **d**irectory (`cd`) and execute command `uv sync`

```shell
cd tkinter_basics
uv sync
```

This will create a virtual environment in `.venv/`

If you prefer to use `venv` (the module included with Python)

```shell
cd tkinter_basics
python3 -m venv .venv
```
