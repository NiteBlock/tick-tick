from discord.ext import commands
import discord, chalk, asyncio, random, time, datetime, logging, aiohttp
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
        elif type == "show":
            if name == "guilds":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"{len(bot.guilds)} servers"))
                await ctx.channel.send(f"Set the status to **watching `guild amount` servers**")
        else:
            await ctx.channel.send("Not a valid type of status")
    else:
        await ctx.channel.send("Oops, you cant to that")

@bot.event
async def on_ready():
    global ver
    print(chalk.green("Ready to go!"))
    print(chalk.blue(f"Serving: {len(bot.guilds)} guilds."))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Tick Tick"))
    ver = "Beta 1.0.0"

@bot.command()
@commands.has_permissions(manage_guild=True)
async def setup(ctx):

    guild = ctx.message.guild
    embed = discord.Embed(title="Setting things up", color=discord.Colour(0xFF0000))
    msg = await ctx.channel.send(embed=embed)
    tickets = discord.utils.get(guild.categories, name="Tickets")
    await asyncio.sleep(1)
    if tickets == None:
        embed = discord.Embed(title="Making ticket category", color=discord.Colour(0xFF0000))
        
        await msg.edit(embed=embed)
        tickets = await guild.create_category_channel("Tickets")
    else:
        embed = discord.Embed(title="Making ticket category", color=discord.Colour(0xFF0000))
        
        await msg.edit(embed=embed)
        await asyncio.sleep(0.3)

        embed = discord.Embed(title="Category already made", color=discord.Colour(0xFF0000))
        await msg.edit(embed=embed)

    apps = discord.utils.get(guild.categories, name="Applications")
    if apps == None:
        embed = discord.Embed(title="Making applications category", color=discord.Colour(0xFF0000))
        
        await msg.edit(embed=embed)
        await guild.create_category_channel("Applications")
    else:
        embed = discord.Embed(title="Making applications category", color=discord.Colour(0xFF0000))
        
        await msg.edit(embed=embed)
        await asyncio.sleep(0.3)

        embed = discord.Embed(title="Category already made", color=discord.Colour(0xFF0000))
        await msg.edit(embed=embed)
    support = discord.utils.get(guild.roles, name="Support")
    if support != None:
        await asyncio.sleep(0.5)

        embed = discord.Embed(title="Making support role", color=discord.Colour(0xFF0000))
        
        await msg.edit(embed=embed)
        await asyncio.sleep(0.6)

        embed = discord.Embed(title="Category already made", color=discord.Colour(0xFF0000))
        await msg.edit(embed=embed)
        await ctx.message.author.add_roles(support)
    else:
        await asyncio.sleep(0.4)

        embed = discord.Embed(title="Making applications category", color=discord.Colour(0xFF0000))
        await asyncio.sleep(0.7)

        await msg.edit(embed=embed)
        support = await guild.create_role(name="Support")
        await ctx.message.author.add_roles(support)


    embed = discord.Embed(title="Done! make sure you set the permsissions for the categories", color=discord.Colour(0x00ff00), description="Do -help to get started")
    embed.set_footer(text="We have finished setting things up for you")

    await msg.edit(embed=embed)







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
async def close(ctx):

    channel = bot.get_channel(ctx.channel.id)
    if channel.category.name == "Tickets":
        await ctx.channel.send("Please type **-confirm** to close your ticket")
        
        def check(m):
            return m.content == '-confirm' and m.channel == channel


        msg = await bot.wait_for('message', check=check)

        await channel.send('Your ticket will be closed')
        await channel.delete()
        embed = discord.Embed(title="Your ticket has been closed", colour=discord.Colour(0xf6ff), description=f"Thank you for using {ctx.message.guild.name}")
        await user.send(embed=embed)
    else:
        await ctx.channel.send("This is not a ticket...")

@bot.command()
async def withdraw(ctx):
    channel = bot.get_channel(ctx.channel.id)       

    if channel.category.name == "Applications":
        await ctx.channel.send("Please type `confirm` if you wish to close this application")
        def check(m):
            global response
            response = m.content.lower()
            print(response) 
            return m.channel == channel

        await asyncio.sleep(0.1)
        msg = await client.wait_for('message', check=check)

        if response == "confirm":
            await channel.delete()
            embed = discord.Embed(title="Your application has been closed", colour=discord.Colour(0xf6ff), description=f"Thank you for using {ctx.message.guild.name}")
            await user.send(embed=embed)
        else:
            await ctx.channel.send("Your application wasn't closed")
    else:
        await ctx.channel.send("This is not a application...")



@bot.event
async def on_guild_join(guild):
    global ver
    embed = discord.Embed(title="Thank you for adding me", colour=discord.Colour(0xffff), description="This is the commands availible:")

    embed.set_footer(text=f"Tick tick | {ver}")

    embed.add_field(name="-new <name>", value="Makes a new ticket", inline=True)
    embed.add_field(name="-close", value="Closes an open ticket", inline=True)
    embed.add_field(name="-add <user>", value="Adds a user to your ticket", inline=True)
    embed.add_field(name="-remove <user>", value="removes a user from your ticket", inline=True)
    embed.add_field(name="-apply <job>", value="Applies you for a job", inline=True)
    embed.add_field(name="-withdraw", value="withdraws your application for a job", inline=True)
    embed.add_field(name="-setup", value="Sets up the server with all channels, etc.", inline=True)
    user = bot.get_user(guild.owner.id)
    await user.send(embed=embed)
    channel = bot.get_channel(557474056371437568)
    embed = discord.Embed(title="Added to a server", colour=discord.Colour(0xffff), description=f"Total servers {len(bot.guilds)}")

    embed.set_footer(text=f"Tick tick | {ver}")

    embed.add_field(name=f"Name: {guild.name}", value=f"Id: {guild.id}")
    embed.add_field(name=f"Owner: {user.name}", value=f"Id: {user.id}")
    await channel.send(embed=embed)

@bot.event
async def on_guild_remove(guild):
    embed = discord.Embed(title="Hey there,  sorry to here that you removed me", colour=discord.Colour(0xffff), description="(Click here to leave a review)[https://]")


    user = bot.get_user(guild.owner.id)
    await user.send(embed=embed)
    channel = bot.get_channel(557474056371437568)
    embed = discord.Embed(title="Removed to a server", colour=discord.Colour(0xFF0000), description=f"Total servers {len(bot.guilds)}")

    embed.set_footer(text=f"Tick tick | {ver}")

    embed.add_field(name=f"Name: {guild.name}", value=f"Id: {guild.id}")
    embed.add_field(name=f"Owner: {user.name}", value=f"Id: {user.id}")
    await channel.send(embed=embed)


@bot.command(aliases=["app", "application"])
async def apply(ctx, *, type = None):
    if type != None:

        num = random.randint(0,999)
        if num < 10:
            num = f"00{num}"
        if num < 100:
            num = f"0{num}"
        guild = ctx.message.guild
        tick = discord.utils.get(guild.categories, name='Applications')

        channel = await guild.create_text_channel(f"application-{num}", category=tick)
        await channel.set_permissions(ctx.message.author, read_messages=True, send_messages=True)

        embed = discord.Embed(title="Your application has been created ", colour=discord.Colour(0xf6ff), description=f"We created a channel for your application in {channel.mention}")
        
        await ctx.channel.send(embed=embed)
        embed = discord.Embed(title=f"{ctx.message.author.name}, We will get right back to you ", colour=discord.Colour(0xff00), description="Your application has been created. We will come right back to you! In the mean time please describe what you can do and why your applying.")

        embed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
        embed.set_author(name=f"{type}")
        embed.set_footer(text=f"Thank you for choosing {ctx.message.guild.name}")
        await channel.send(embed=embed)

    else:
        embed = discord.Embed(title="Please tell us what you want to apply for", colour=discord.Colour(0xf6ff), description="eg. -apply Configuring plugins")

        await ctx.channel.send(embed=embed)

@bot.command()
async def add(ctx, person:discord.User):
    channel = bot.get_channel(ctx.channel.id)
    if user == None:
        await ctx.channel.send("Please mention a user to add")
    else:
        if channel.category.name == "Tickets":
            await channel.set_permissions(person, read_messages=True, send_messages=True)
            await ctx.channel.send(f"Added {person.mention} to this ticket")
        else:
            await ctx.channel.send("This is not a ticket...")

@bot.command()
async def remove(ctx, person:discord.User):
    channel = bot.get_channel(ctx.channel.id)
    if user == None:
        await ctx.channel.send("Please mention a user to remove")
    else:
        if channel.category.name == "Tickets":
            await channel.set_permissions(person, read_messages=False, send_messages=False)
            await ctx.channel.send(f"Removed {person.name} from this ticket")
        else:
            await ctx.channel.send("This is not a ticket...")




@bot.command(aliases=["tickets", "ticket", "make", "order"])
async def new(ctx, *, type = None):
    if type != None:

        num = random.randint(0,999)
        if num < 10:
            num = f"00{num}"
        if num < 100:
            num = f"0{num}"
        guild = ctx.message.guild
        tick = discord.utils.get(guild.categories, name='Tickets')
        channel = await guild.create_text_channel(f"ticket-{num}", category=tick)
        await channel.set_permissions(ctx.message.author, read_messages=True, send_messages=True)

        embed = discord.Embed(title="Your ticket has been created ", colour=discord.Colour(0xf6ff), description=f"We created a channel for your ticket in {channel.mention}")
        
        await ctx.channel.send(embed=embed)
        embed = discord.Embed(title=f"{ctx.message.author.name}, We will get right back to you ", colour=discord.Colour(0xff00), description="Your ticket has been created. We will come right back to you! In the mean time please describe your questions thoroughly.")


        embed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
        embed.set_author(name=f"{type}")
        embed.set_footer(text=f"Thank you for choosing {ctx.message.guild.name}")
        role = discord.utils.get(guild.roles, name='Support')

        await channel.send(content=f"<@&{role.id}>",embed=embed)



    else:
        embed = discord.Embed(title="Please tell us what you need", colour=discord.Colour(0xf6ff), description="eg. -new Discord Bot")

        await ctx.channel.send(embed=embed)




@bot.command()
async def help(ctx):
    global ver
    embed = discord.Embed(title="Help for tickets", colour=discord.Colour(0xffff), description="This is all you need to know for making tickets")

    embed.set_footer(text=f"Tick Tick | {ver}")

    embed.add_field(name="-new <name>", value="Makes a new ticket", inline=True)
    embed.add_field(name="-close", value="Closes an open ticket", inline=True)
    embed.add_field(name="-add <user>", value="Adds a user to your ticket", inline=True)
    embed.add_field(name="-remove <user>", value="removes a user from your ticket", inline=True)
    embed.add_field(name="-apply <job>", value="Applies you for a job", inline=True)
    embed.add_field(name="-withdraw", value="withdraws your application for a job", inline=True)
    await ctx.channel.send(embed=embed)

@bot.command()
async def bug(ctx, *, name):
    channel = bot.get_channel(557505096557264896)
    await ctx.send(f"Your bug has been sent to {channel.mention}")
    embed = discord.Embed(title=f"{ctx.mesage.author.name} reported a bug", colour=discord.Colour(0xffff), description=f"{name}")
    await channel.send(embed=embed)


@bot.command()
async def invite(ctx):
    global ver
    embed = discord.Embed(title="Invite the bot", colour=discord.Colour(0x29ff00), description="[Click here to invite the bot](https://discordapp.com/api/oauth2/authorize?client_id=557154903563304960&permissions=268823672&redirect_uri=https%3A%2F%2Fdiscord.gg%2FY5ereeE&scope=bot)")

    embed.set_footer(text=f"Tick tick | {ver}")
    await ctx.send(embed=embed)


@bot.command()
async def support(ctx):
    global ver
    embed = discord.Embed(title="Get support for the bot", colour=discord.Colour(0x29ff00), description="[Click here to go into our support server](https://discord.gg/Ks43Av4)")

    embed.set_footer(text=f"Tick tick | {ver}")
    await ctx.send(embed=embed)

@bot.command(alias=["site"])
async def website(ctx):
    global ver
    embed = discord.Embed(title="This is our website", colour=discord.Colour(0x29ff00), description="[Click here to go to our website](https://tick-tick.netlify.com/)")

    embed.set_footer(text=f"Tick tick | {ver}")
    await ctx.send(embed=embed)

@bot.command()
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = "Their"
    name = f"{member.name}#{member.discriminator}"
    mention = member.mention
    status = member.status
    joined = member.joined_at
    role = member.top_role
    await ctx.channel.send(f"{pronoun} name is {name} and thier id is {member.id}. {pronoun} status is {status}. They joined at {joined}. {pronoun} rank is {role}.")


@bot.command()
@commands.has_any_role("Support")
async def clear(ctx):
    deleted = await ctx.channel.purge(limit=10000)
    embed = discord.Embed(title=f"Cleared all of the messages", colour=discord.Colour(0x9adc86))
    embed.set_footer(text="Message will delete in 10 secs with all other messages sent.")
    await ctx.channel.send(embed=embed)
    await asyncio.sleep(10)
    deleted2 = await ctx.channel.purge(limit=10000)



@bot.command()
@commands.has_any_role("Support")
async def cr(ctx, id:int, *, name):
    guild = ctx.message.guild

    cat = bot.get_channel(id)
    channel = await guild.create_text_channel(f"{name}", category=cat)



class DiscordBotsOrgAPI:
    """Handles interactions with the discordbots.org API"""

    def __init__(self, bot):
        self.bot = bot
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjU1NzE1NDkwMzU2MzMwNDk2MCIsImJvdCI6dHJ1ZSwiaWF0IjoxNTUzMTYyMjc3fQ.uK77F1zPIWnsZ-bPhLIWNJmsHpqq54YLjfM2npgtfas'  #  set this to your DBL token
        self.dblpy = dbl.Client(self.bot, self.token)
        self.bot.loop.create_task(self.update_stats())

    async def update_stats(self):
        """This function runs every 30 minutes to automatically update your server count"""

        while True:
            logger.info('attempting to post server count')
            try:
                await self.dblpy.post_server_count()
                logger.info('posted server count ({})'.format(len(self.bot.guilds)))
            except Exception as e:
                logger.exception('Failed to post server count\n{}: {}'.format(type(e).__name__, e))
            await asyncio.sleep(1800)


def letsgo(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(DiscordBotsOrgAPI(bot))

bot.run("NTU3MTU0OTAzNTYzMzA0OTYw.D3ELQg.687msGFGIfKnJk8ra8AGF0YpxSc")

