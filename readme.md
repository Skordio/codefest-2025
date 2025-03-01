# Codefest 2025 Draft Repo

Here I am just gonna make a django app and maybe a frontend to play around with Gemini API

## Repo setup

To setup this repo on your machine, you need python and node

## Backend setup

This repo uses Django Python for the backend, and venv for python library management.

To run the python django server on your own machine, you need to have python installed and create your own virtual environment.

First create a virtual environment like this (run this command in the root of the repo once you have python 3.12 installed):
```
python3 -3.12 -m venv .venv
```

then activate the environment in your terminal (also run this at the root of the repo):

Mac: `source ./venv/bin/activate`

Windows powershell: `./venv/Scripts/Activate.ps1`


then use pip to install the libraries:
```
pip install -r requirements.txt
```

## Frontend Setup

If you want to run the frontend on your machine, you need to have node installed on your machine. I am using node version v22.12.0 so you may want to install that version. I recommend installing a node version manager on your machine to do this, on windows I use NVM.

Once you have node installed, I recommend using pnpm instead of npm.

To install pnpm, just go to the [installation page](https://pnpm.io/installation) and follow the instructions for your system.

Once you have pnpm installed, just run this command while inside the `frontend/` folder:

```
pnpm install
```

this will install all necessary node libraries to run the frontend app on your machine.