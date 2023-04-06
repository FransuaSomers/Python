import discord
from discord.ext import commands
import os

TOKEN = os.getenv('MTA4NTk2NzUzNTM5Mzk5Njg4NQ.GsuroZ.fWABC5okKX37gmz-y3zKNAOajn2OllvNANReyw')

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True


#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='/', intents=intents)

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with our token
print(TOKEN)
bot.run(TOKEN)
