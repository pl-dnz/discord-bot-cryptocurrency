# discord-bot-cryptocurrency

With the use of a discord bot, it will create and send custom graph of : a crypto, in a currency, for a period, whith an intreval

## Setup

### You will need to create a discord bot, get his token and make it join your server :

> This site will help you : [How-to-create-discord-bot](https://github.com/peterthehan/create-discord-bot#create-discord-bot)

### You have to install libraries :
> you can paste this command into the terminal

```
pip install discord yfinance plotly
```
> you have to create a folder **images** or add this to the program

```
import os

if not os.path.exists("images"):
    os.mkdir("images")
```
