import discord
from discord.ext import commands

client=commands.Bot(command_prefix='!')

@client.event
async def on_ready():
     print("ready")


@client.event
async def on_message(message):
    message.content.lower()
    if message.author==client.user:
        return
      
    # react to message with message (not user-specific)
    if 'trigger message here' in message.content:
        await message.channel.send('reaction message here')
        
    # react to user-specific message with message
    if str(message.author) == 'johndoe#0000':
        await message.channel.send('your message here')
        
    # react to user-specific message with emoji reaction
    if str(message.author) == 'johndoe#0000':
        await message.add_reaction('<:emoji_name:>')
        # if you want to use custom server-specific emoji, replace '<:emoji_name:>' with '<:emoji_name:emoji_id_number>'
        
    #reactions are not limited to one
    if str(message.author) == 'janedoe#0000':
        await message.add_reaction('<:emoji_name:>')
        await message.add_reaction('<:emoji_name2:>')
        await message.add_reaction('<:emoji_name3:>')

client.run('place token here')
