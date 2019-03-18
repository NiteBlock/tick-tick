from discord.ext import commands
import discord, chalk, asyncio, random, time, datetime
from datetime import datetime

bot = commands.Bot(command_prefix="-", status=discord.Status.idle, activity=discord.Game(name="Starting up..."))
client = discord.Client()

bot.remove_command("help")


@bot.command()
async def setstatus(ctx, type, *, name):
    user = bot.get_user(445556389532925952)
    user2 = bot.get_user(394174323117654036)
    if ctx.message.author == user or ctx.message.author == user2:

        if type == "listening":
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{name}"))
            await ctx.channel.send(f"Set the status to **Listening to {name}**")
        elif type == "watching":
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{name}"))
            await ctx.channel.send(f"Set the status to **Watching {name}**")
        elif type == "playing":
            await bot.change_presence(activity=discord.Game(name=f"{name}"))
            await ctx.channel.send(f"Set the status to **playing {name}**")
        else:
            await ctx.channel.send("Not a valid type of status")
    else:
        await ctx.channel.send("Oops, you cant to that")

@bot.event
async def on_ready():
    print(chalk.green("Ready to go!"))
    print(chalk.blue(f"Serving: {len(bot.guilds)} guilds."))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Tick Tick"))



@bot.command()
async def botver(ctx):
    await ctx.channel.send(f"{discord.__version__}")

bot.launch_time = datetime.utcnow()

@bot.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")






        
@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    embed = discord.Embed(title=f"The bots ping is {ping}ms :ping_pong: ", colour=discord.Colour(0x9adc86),)

    await ctx.channel.send(embed=embed)









@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx):
    deleted = await ctx.channel.purge(limit=10000)
    embed = discord.Embed(title=f"Cleared all of the messages", colour=discord.Colour(0x9adc86))
    embed.set_footer(text="Message will delete in 10 secs with all other messages sent.")
    await ctx.channel.send(embed=embed)
    await asyncio.sleep(10)
    deleted2 = await ctx.channel.purge(limit=10000)




bot.run("NTU3MjI0MDU4NDY3Mzg1MzU1.D3FK_Q.noTfu0GM47Ee3IMN54LRS5GTSzg")