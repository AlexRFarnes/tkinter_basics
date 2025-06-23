# Tkinter Basics

Repository to keep track of what I've learned about the basics of Tkinter.

## Como usar este repositorio

Si deseas trabajar localmente necesitarás:

1. Clonar este repositorio
2. Crear un entorno virtual de python
3. Instalar los paquetes necesarios
4. ¡Escribir tu código!

La manera recomendada de manejar tus entornos virtuales es con la herramienta `uv` [docs](https://docs.astral.sh/uv/)
en Mac/Linux

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

en Windows

```shell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Clonar el repositorio

Utiliza `git`

```shell
git clone https://github.com/AlexRFarnes/tkinter_basics
```

### Crear un entorno virtual de python

Entra al repositorio **c**ambiando de **d**irectorio (`cd`) y ejecuta uv sync

```shell
cd tkinter_basics
uv sync
```

Esto va a crear un entorno virtual en `.venv/` e instalar los paquetes necesarios

Si deseas usar `venv` (el paquete incluido con tu python)

```shell
cd tkinter_basics
python3 -m venv .venv
```
