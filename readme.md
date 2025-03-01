# Codefest 2025 Draft Repo

Here I am just gonna make a django app and maybe a frontend to play around with Gemini API

## Repo setup

To setup this repo on your machine, you need python and node

## Backend setup

This repo uses Django Python for the backend, and venv for python library management.

To run the python django server on your own machine, you need to have python installed and create your own virtual environment.

First create a virtual environment like this (once you have python installed)
```
python3 -3.12 -m venv .venv
```

then activate the environment in your terminal:

Mac
```
source ./venv/bin/activate
```

Windows powershell
```
./venv/Scripts/Activate.ps1
```


then install the libraries like this:
```
pip install -r requirements.txt
```

## Frontend Setup

If you want to run the frontend on your machine, you need to have node installed on your machine. I am using node version v22.12.0 so you may want to install that version. I recommend installing a node version manager on your machine to do this, on windows I use NVM.

Once you have node installed, I recommend using pnpm instead of npm.

To install pnpm for Windows powershell, just run this command:

```
Invoke-WebRequest https://get.pnpm.io/install.ps1 -UseBasicParsing | Invoke-Expression
```