# bot.py
import os, discord

from discord.ext import commands
from dotenv import load_dotenv
import yfinance as yf
import plotly.graph_objects as go



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if not os.path.exists("images"):
    os.mkdir("images")

bot = commands.Bot(command_prefix='!!')

def getData(CRYPTO, CURRENCY, TIME, INTERVAL):
    data = yf.download(tickers=f'{CRYPTO}-{CURRENCY}', period=TIME, interval=INTERVAL)
    return data

def get_graph(CRYPTO, CURRENCY, TIME, INTERVAL):
    crypto_data = getData(CRYPTO, CURRENCY, TIME, INTERVAL)

    # Candlestick
    fig = go.Figure(
        data = [
            go.Candlestick(
                x = crypto_data.index,
                open = crypto_data.Open,
                high = crypto_data.High,
                low = crypto_data.Low,
                close = crypto_data.Close
            ),

        ]
    )


    fig.update_layout(
        title = f'The graph of {CRYPTO} during {TIME} with an intervall of {INTERVAL}',
        xaxis_title = 'Time',
        yaxis_title = f'Price ({CURRENCY})',
        xaxis_rangeslider_visible = False
    )
    fig.update_yaxes(tickprefix='€')
    fig.write_image("images/fig1.png")

@bot.event
async def on_ready():
  print('bot is active')


@bot.command(name='crypto', help='!!crypto <CRYPTO> <CURRENCY> <TIME> <INTERVAL>')
async def crypto_graph(ctx, CRYPTO, CURRENCY, TIME, INTERVAL):
    get_graph(CRYPTO, CURRENCY, TIME, INTERVAL)
    await ctx.send(file=discord.File("images/fig1.png"))

bot.run(TOKEN)
