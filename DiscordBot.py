import discord
from discord.ext import commands
import asyncio

import youtube_dl


intents = discord.Intents().all()

bot_token = "MTA4NTk2NzUzNTM5Mzk5Njg4NQ.G-bbba.yishvDfHm2C2xmkTJIgoIzYMcjYs6uA6vaWN5I"
bot = commands.Bot(command_prefix='!', token=bot_token, intents=intents)




@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")


@bot.command()
async def play(ctx, url):
    # Check if the user is in a voice channel
    if not ctx.author.voice:
        await ctx.send("You are not connected to a voice channel.")
        return

    # Get the user's voice channel
    channel = ctx.author.voice.channel

    # Connect to the voice channel
    await channel.connect()

    # Download the audio from the YouTube link
    ydl_opts = {'format': 'bestaudio/best'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['url']

    # Play the audio in the voice channel
    voice_client = ctx.voice_client
    source = await discord.FFmpegOpusAudio.from_probe(URL, method='fallback')
    voice_client.play(source)

    # Send a message to confirm that the audio is playing
    await ctx.send("Now playing: {}".format(info['title']))


if __name__ == "__main__":
    asyncio.run(bot.run(bot_token))