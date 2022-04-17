# discord-bot-cryptocurrency

With the use of a discord bot, it will create and send custom graph of : a crypto, in a currency, for a period, with an intreval

## Setup

### You will need to create a discord bot, get his token and make it join your server :

> This site will help you : [How-to-create-discord-bot](https://github.com/peterthehan/create-discord-bot#create-discord-bot)

### You have to install libraries :
> You can paste this command into the terminal

```
pip install discord yfinance plotly kaleido
```
> You have to create a folder **images** or the program will make it.

> In the **.env** file you have to put your bot token, in this way it will by secure.

## Use

> When the bot is online, you can make a command in discord with this patern :

**!!crypto "CRYPTO" "CURRENCY" "TIME" "INTERVAL"**

> For example if I tipe --> !!crypto BTC EUR 5d 30m
> 
![image](https://user-images.githubusercontent.com/83816499/163731653-95a62578-fd0c-4992-ace7-af575dc1e2d0.png)

> For example if I tipe --> !!crypto ETH USD 1y 1d
> 
![image](https://user-images.githubusercontent.com/83816499/163731782-3f236793-1f79-4756-89e1-dd0530c4a904.png)

The image is send on average ender 2sec.
