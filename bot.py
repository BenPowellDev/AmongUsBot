import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('as the imposter'))
    print('Bot is Ready.')

#Help Command
@client.command()
async def help(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(
        description = 'This is a helper bot, use the commands as you please!',
        colour = discord.Colour.orange()
    )

    embed
    embed.set_author(name="Help")
    embed.add_field(name ='.ping', value='Returns Latency in ms', inline= False)
    embed.add_field(name ='.fortune', value='The Bot will give some Among Us wisdom', inline= False)
    embed.add_field(name ='.amongus', value='Summon the hordes for some fun', inline= False)
    embed.add_field(name ='.whosus', value='The bot knows who is sus.', inline= False)
    embed.add_field(name ='.developer', value='Shows the Developer credits', inline= False)

# DM the user the help commands.
    await ctx.author.send(author, embed=embed)

# Ping Command
@client.command()
async def ping(ctx):
    await ctx.send(f'Latency = {round(client.latency * 1000)}ms')

# Clear Command
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

# Among us
@client.command()
async def amongus(ctx):
    emb = discord.Embed(title="Anybody want to play Among Us?", description="Pls react to this message with your answer!\n @everyone", color=0xff00d4)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')
    
# The Bot tells a Fortune
@client.command()
async def fortune(ctx):
    responses = ["I saw Yellow vent.",
                 "How do I go in the vents like Blue?",
                 "I want to kill people like purple.",
                 "Is White the only one who can kill?",
                 "Why does Brown keep jumping in vents?",
                 "Purple, how do I Kill?",
                 "Why is my name red?",
                 "Why is mine and Yellow's name red?",
                 "I'm stuck in a vent",]
    await ctx.send(f'{random.choice(responses)}')

# The Bot tells U who's sus
@client.command()
async def whosus(ctx):
    responses = ["Red",
                 "Blue",
                 "Green",
                 "Orange",
                 "Yellow",
                 "Black",
                 "White",
                 "Purple",
                 "Brown",
                 "Cyan",
                 "Lime",]
    await ctx.send(f'{random.choice(responses)} is sus.')

# DM's User the Dev Credit
@client.command()
async def developer(ctx):
    await ctx.author.send('This bot was created by Ben Powell (2020)')


client.run('TOKEN REMOVED FOR SECURITY REASONS')