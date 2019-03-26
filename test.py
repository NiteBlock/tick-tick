import discord, chalk, asyncio, random, time, datetime, ast, os
from discord.ext import commands

from datetime import datetime as dt

bot = commands.Bot(command_prefix="-", status=discord.Status.idle, activity=discord.Game(name="Starting up..."))
client = discord.Client()

bot.remove_command("help")

@bot.event
async def on_ready():
    global ver
    print(chalk.green("Ready to go!"))
    print(chalk.blue(f"Serving: {len(bot.guilds)} guilds."))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Tick Tick"))
    ver = "1.0.0 Testing"

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount:int=None):
    await ctx.message.delete()
    if amount == None:
        await ctx.send("Please tell me an amount")
    else:
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title=f"Cleared {amount} messages", colour=discord.Colour(0x9adc86))
        embed.set_footer(text="Message will delete in 10 seconds.")
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(1)
        embed.set_footer(text="Message will delete in 9 seconds.")
        await msg.edit(embed=embed)
        await asyncio.sleep(1)
        embed.set_footer(text="Message will delete in 8 seconds.")
        await msg.edit(embed=embed)
        await msg.edit(embed=embed)
        await asyncio.sleep(1)
        embed.set_footer(text="Message will delete in 7 seconds.")
        await msg.edit(embed=embed)
        await asyncio.sleep(1)
        embed.set_footer(text="Message will delete in 6 seconds.")
        await msg.edit(embed=embed)
        await asyncio.sleep(1)
        embed.set_footer(text="Message will delete in 5 seconds.")
        await msg.edit(embed=embed)
        await msg.edit(embed=embed)
        await asyncio.sleep(1)
        embed.set_footer(text="Message will delete in 4 seconds.")
        await msg.edit(embed=embed)
        await asyncio.sleep(1)
        embed.set_footer(text="Message will delete in 3 seconds.")
        await msg.edit(embed=embed)
        await asyncio.sleep(1)
        embed.set_footer(text="Message will delete in 2 seconds.")
        await msg.edit(embed=embed)
        await msg.edit(embed=embed)
        await asyncio.sleep(1)
        embed.set_footer(text="Message will delete in 1 seconds.")
        await msg.edit(embed=embed)     
        await asyncio.sleep(1)
   
        await msg.delete()



@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    global ver
    channel = ctx.channel
    async with channel.typing():

        embed = discord.Embed(title="Are you ready to set things up", description="This will take less than a minute, Reply with `yes` or `no`")
        
        embed.set_footer(text=f"Tick Tick | {ver}")
        msg = await ctx.send(embed=embed)

        channel = ctx.channel
        author = ctx.author

        def check(m):
            return m.channel == channel and m.author == author

        



        waited = await bot.wait_for('message', check=check)
        await waited.delete()
        await msg.delete()

        if waited.content == "yes" or waited.content == "Yes":
            embed = discord.Embed(title="Do you want me to setup all the categories and roles?", description="Reply with `yes` or `no`")

            embed.set_footer(text=f"Tick Tick | {ver}")
            msg = await ctx.send(embed=embed)

            waited = await bot.wait_for('message', check=check)

            await msg.delete()
            await waited.delete()

            if waited.content == "yes" or waited.content == "Yes":

                embed = discord.Embed(title="Creating everything for you", description="Just a second.") 

                embed.set_footer(text=f"Tick Tick | {ver}")
                msg = await ctx.send(embed=embed)

                guild = ctx.message.guild
                
                filepath = os.path.exists(f'./data/{ctx.message.guild.id}-channels.txt')

                if filepath == True:
                    f = open(f"./data/{ctx.message.guild.id}-channels.txt", "r")
                    data = f.read()
                    f.close()
                else:
                    data = None
                    

                if data == None:
                    tickets = None
                    applications = None
                    logs = None
                else:
                    channels = ast.literal_eval(data)
                    tickets = channels["tickets"]
                    logs = channels["logs"]
                    applications = channels["applications"]
                
                if tickets == None:
                    ticketschannel = await guild.create_category_channel("Tickets")
                    await ticketschannel.set_permissions(guild.default_role, read_messages=False)
                    tickets = ticketschannel.id
                
                if logs == None:
                    logschannel = await guild.create_text_channel("logs")
                    await logschannel.set_permissions(guild.default_role, read_messages=False)
                    logs = logschannel.id

                if applications == None:
                    applicationschannel = await guild.create_category_channel("Applicatons")
                    await applicationschannel.set_permissions(guild.default_role, read_messages=False)
                    applications = applicationschannel.id

                embed = discord.Embed(title="Creating everything for you", description="Just a second..") 

                embed.set_footer(text=f"Tick Tick | {ver}")
                await msg.edit(embed=embed)

                filepath = os.path.exists(f'./data/{ctx.message.guild.id}-roles.txt')


                if filepath == True:
                    f = open(f"./data/{ctx.message.guild.id}-roles.txt", "r")
                    data = f.read()
                    f.close()
                else:
                    data = None
                    

                if data == None:
                    support = None
                else:
                    channels = ast.literal_eval(data)
                    support = channels["support"]

                if support == None:
                    supportrole = await guild.create_role(name="Support")
                    support = supportrole.id
                    logschannel.set_permissions(support, read_messages=True, send_messages=False)
                    ticketschannel.set_permissions(support, read_messages=True, send_messages=True)
                    applicationschannel.set_permissions(support, read_messages=True, send_messages=True)



                
                embed = discord.Embed(title="Creating everything for you", description="Just a second...") 

                embed.set_footer(text=f"Tick Tick | {ver}")
                await msg.edit(embed=embed)
                await asyncio.sleep(1)
                embed = discord.Embed(title="Saving the data", description="Just a second.") 

                embed.set_footer(text=f"Tick Tick | {ver}")
                await msg.edit(embed=embed)

                f = open(f"./data/{ctx.message.guild.id}-channels.txt", "w")
                channels = {"tickets": tickets, "applications": applications}
                f.write(str(channels))
                f.close()

                embed = discord.Embed(title="Saving the data", description="Just a second..") 

                embed.set_footer(text=f"Tick Tick | {ver}")
                await msg.edit(embed=embed)

                f = open(f"./data/{ctx.message.guild.id}-roles.txt", "w")
                roles = {"support": support}
                f.write(str(roles))
                f.close()


                embed = discord.Embed(title="Saving the data", description="Just a second...") 

                embed.set_footer(text=f"Tick Tick | {ver}")
                await msg.edit(embed=embed)
                
                await asyncio.sleep(1)
                
                embed = discord.Embed(title="Done! Do you want custom messages?", description="Reply with `yes` or `no`") 

                embed.set_footer(text=f"Tick Tick | {ver}")
                await msg.delete()
                msg = await ctx.send(embed=embed)

                channel = ctx.channel
                author = ctx.author
                waited = await bot.wait_for('message', check=check)
                await waited.delete()
                await msg.delete()
                
                if waited.content == "Yes" or waited.content == "yes":
                    embed = discord.Embed(title="What should be the title when you open a new ticket", description="Reply with your answer, use `creator` to put the name of the creator of the ticket and `reason` for the reason and `reason` for the reason") 

                    embed.set_footer(text=f"Tick Tick | {ver}")
                    msg = await ctx.send(embed=embed)

                    waited = await bot.wait_for('message', check=check)

                    amount = len(waited.content)
                    await msg.delete()
                    await waited.delete()
                    if amount > 256:
                        await ctx.channel.send("Your title title cant be longer than 256")
                    else:
                        ticketheader = waited.content
                        embed = discord.Embed(title="What should be the description when you open a new ticket", description="Reply with your answer, use `creator` to put the name of the creator of the ticket and `reason` for the reason and `reason` for the reason") 

                        embed.set_footer(text=f"Tick Tick | {ver}")
                        
                        msg = await ctx.send(embed=embed)
                        waited = await bot.wait_for('message', check=check)

                        amount = len(waited.content)
                        await msg.delete()
                        await waited.delete()
                        
                        if amount > 256:
                            await ctx.channel.send("Your descrition cant be longer than 256")
                        else:
                            ticketdescription = waited.content

                            embed = discord.Embed(title="What should be the title when you open a new application", description="Reply with your answer, use `creator` to put the name of the creator of the application and `reason` for the reason") 

                            embed.set_footer(text=f"Tick Tick | {ver}")
                            
                            msg = await ctx.send(embed=embed)

                            waited = await bot.wait_for('message', check=check)

                            amount = len(waited.content)
                            await msg.delete()
                            await waited.delete()
                            if amount > 256:
                                await ctx.channel.send("Your title cant be longer than 256")
                            else:
                                appheader = waited.content

                                embed = discord.Embed(title="What should be the description when you open a new application", description="Reply with your answer, use `creator` to put the name of the creator of the application and `reason` for the reason") 

                                embed.set_footer(text=f"Tick Tick | {ver}")
                                
                                msg = await ctx.send(embed=embed)
                                waited = await bot.wait_for('message', check=check)

                                amount = len(waited.content)
                                await msg.delete()
                                await waited.delete()

                                if amount > 256:
                                    await ctx.channel.send("Your description cant be longer than 256")
                                else:
                                    appdescription = waited.content
                                    embed = discord.Embed(title="Saving the data", description="Just a second.") 

                                    embed.set_footer(text=f"Tick Tick | {ver}")
                                    
                                    msg = await ctx.send(embed=embed)
                                    filepath = os.path.exists(f'./data/{ctx.message.guild.id}-message-tickets.txt')
                                    if filepath == True:
                                        f = open(f"./data/{ctx.message.guild.id}-message-tickets.txt", "r")
                                        data = f.read()
                                        f.close()
                                        tickets = ast.literal_eval(data)
                                    else:
                                        tickets = None

                                    tickets = {
                                            "custom" : "True",
                                            "header" : ticketheader ,
                                            "description" : ticketdescription

                                        }
                                    f = open(f"./data/{ctx.message.guild.id}-message-tickets.txt", "w")
                                    f.write(str(tickets))
                                    f.close()

                                    embed = discord.Embed(title="Saving the data", description="Just a second..") 

                                    embed.set_footer(text=f"Tick Tick | {ver}")
                                    await msg.edit(embed=embed)

                                    filepath = os.path.exists(f'./data/{ctx.message.guild.id}-message-applications.txt')
                                    if filepath == True:
                                        f = open(f"./data/{ctx.message.guild.id}-message-applications.txt", "r")
                                        data = f.read()
                                        f.close()
                                        tickets = ast.literal_eval(data)
                                    else:
                                        applications = None

                                    applications = {
                                            "custom" : "True",
                                            "header" : appheader ,
                                            "description" : appdescription
                                        }

                                    f = open(f"./data/{ctx.message.guild.id}-message-applications.txt", "w")
                                    f.write(str(tickets))
                                    f.close()
                                    embed = discord.Embed(title="Saving the data", description="Just a second...") 

                                    embed.set_footer(text=f"Tick Tick | {ver}")
                                    await msg.edit(embed=embed)

                                    asyncio.sleep(1)

                                    await msg.delete()

                                    embed = discord.Embed(title="Done! Your all setup", colour=discord.Colour(0x00ff7d), description="Your all done. Do -help for a list of commands") 

                                    embed.set_footer(text=f"Tick Tick | {ver}")
                                    
                                    msg = await ctx.send(embed=embed)




                    




                elif waited.content == "No" or waited.content == "no":
                    f = open(f"./data/{ctx.message.guild.id}-message-applications.txt", "w")
                    applications = {"custom": False}

                    f.write(str(applications))
                    f.close()
                    f = open(f"./data/{ctx.message.guild.id}-message-tickets.txt", "w")
                    tickets = {"custom": False}

                    f.write(str(tickets))
                    f.close()

                    embed = discord.Embed(title="Done!", description="Do `-help` for a list of commands") 

                    embed.set_footer(text=f"Tick Tick | {ver}")
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="Error", colour=discord.Colour(0xff0000), description="``Ìnvalid response```") 

                    embed.set_footer(text=f"Tick Tick | {ver}")
                    await ctx.send(embed=embed)


            elif waited.content == "No" or waited.content == "no":
                
                embed = discord.Embed(title="This isnt fully supported yet...", description="Please use my automated system") 
 
                embed.set_footer(text=f"Tick Tick | {ver}")
                msg = await ctx.send(embed=embed)


        elif waited.content == "no" or waited.content == "No":
            await msg.edit("Ok :smiley:")
        else:
            await msg.edit("Invalid response")



@bot.command()
async def new(ctx, *, reason=None):
    global ver
    if reason == None:
        embed = discord.Embed(title="Please tell us what you need", colour=discord.Colour(0xff0000), description="eg. -new Discord Bot")

        embed.set_footer(text=f"Tick Tick | {ver}")
        await ctx.channel.send(embed=embed)
    
    else:
        filepath = os.path.exists(f'./data/{ctx.message.guild.id}-channels.txt')
        if filepath == True:
            embed = discord.Embed(title="Opening your ticket", description="Just a sec.")

            embed.set_footer(text=f"Tick Tick | {ver}")
            msg = await ctx.send(embed=embed)


            f = open(f"./data/{ctx.message.guild.id}-channels.txt", "r")
            data = f.read()
            f.close()
            channels = ast.literal_eval(data)
            ticketsid = channels["tickets"]

            tickets = bot.get_channel(ticketsid)
            guild = ctx.message.guild
            filepath = os.path.exists(f'./data/{ctx.message.guild.id}-ticket-num.txt')
            if filepath == True:
                f = open(f"./data/{ctx.message.guild.id}-ticket-num.txt", "r")
                number_ = int(f.read())
                number_ += 1
                number_ = int(number_)
                number = int(number_)

                f.close()
            else:
                number = 1
            
            if number < 10:
                num = f"00{number}"
            elif number < 100:
                num = f"0{number}"
            else:
                num = number

            newchannel = await guild.create_text_channel(f"ticket-{num}", category=tickets)
            await newchannel.set_permissions(ctx.message.author, read_messages=True, send_messages=True)
            filepath = os.path.exists(f'./data/{ctx.message.guild.id}-message-tickets.txt')
            if filepath == True:
                f = open(f"./data/{ctx.message.guild.id}-message-tickets.txt", "r")
                data = f.read()
                f.close()
                messages = ast.literal_eval(data)

            else:
                embed = discord.Embed(title="Error", colour=discord.Colour(0xf6ff), description="```Messages are not defined; contact an administrator```")

                embed.set_footer(text=f"Tick Tick | {ver}")
                await ctx.channel.send(embed=embed)

            custom = messages["custom"]
            if custom == False:
                embed = discord.Embed(title=f"Thank you for creating a ticket {ctx.author.name}", colour=discord.Colour(0xf6ff), description="We will get right back to you")

                embed.set_footer(text=f"Tick Tick | {ver}")
                await ctx.channel.send(embed=embed)
            else:
                title = messages["header"]
                title = title.replace("creator", ctx.author.name)
                title = title.replace("reason", reason)
                description = messages["description"]
                description = description.replace("creator", ctx.author.name)
                description = description.replace("reason", reason)

                embed = discord.Embed(title=title, colour=discord.Colour(0xf6ff), description=description)
                    
                embed.set_footer(text=f"Tick Tick | {ver}")

            await newchannel.send(embed=embed)
            embed = discord.Embed(title="Your channel has been sucsessfully created.", colour=discord.Colour(0xf6ff), description=f"Your ticket is located in {newchannel.mention}")
                    
            embed.set_footer(text=f"Tick Tick | {ver}")
            await msg.edit(embed=embed)

            filepath = os.path.exists(f'./data/{ctx.message.guild.id}-ticket-num.txt')

            f = open(f"./data/{ctx.message.guild.id}-ticket-num.txt", "w")
            f.write(str(number))
            f.close()
                


            ticketinfo = {
                    "guild" : ctx.guild.id,
                    "owner" : ctx.author.id ,
                    "reason" : reason,
                    "channelcreated" : ctx.channel.id,
                    "ticketnum" : num,
                    "ticketchannel" : newchannel.id
                }
            f = open(f"./data/tickets/{ctx.message.guild.id}-ticket-{num}.txt", "w")
            f.write(str(ticketinfo))
            f.close()
            
            



        else:
            embed = discord.Embed(title="Error", colour=discord.Colour(0xf6ff), description="```Categories are not defined; contact an administrator```")

            embed.set_footer(text=f"Tick Tick | {ver}")
            await ctx.channel.send(embed=embed)



@bot.command()
async def apply(ctx, *, reason=None):
    global ver
    if reason == None:
        embed = discord.Embed(title="Please tell us what you want to apply for", colour=discord.Colour(0xff0000), description="eg. -apply Developer")

        embed.set_footer(text=f"Tick Tick | {ver}")
        await ctx.channel.send(embed=embed)
    
    else:
        filepath = os.path.exists(f'./data/{ctx.message.guild.id}-channels.txt')
        if filepath == True:
            embed = discord.Embed(title="Opening your application", description="Just a sec.")

            embed.set_footer(text=f"Tick Tick | {ver}")
            msg = await ctx.send(embed=embed)


            f = open(f"./data/{ctx.message.guild.id}-channels.txt", "r")
            data = f.read()
            f.close()
            channels = ast.literal_eval(data)
            applicationsid = channels["applications"]

            applications = bot.get_channel(applicationsid)
            guild = ctx.message.guild
            filepath = os.path.exists(f'./data/{ctx.message.guild.id}-app-num.txt')
            if filepath == True:
                f = open(f"./data/{ctx.message.guild.id}-app-num.txt", "r")
                number_ = int(f.read())
                number_ += 1
                number_ = int(number_)
                number = int(number_)

                f.close()
            else:
                number = 1
            
            if number < 10:
                num = f"00{number}"
            elif number < 100:
                num = f"0{number}"
            else:
                num = number

            newchannel = await guild.create_text_channel(f"application-{num}", category=applications)
            await newchannel.set_permissions(ctx.message.author, read_messages=True, send_messages=True)
            filepath = os.path.exists(f'./data/{ctx.message.guild.id}-message-applications.txt')
            if filepath == True:
                f = open(f"./data/{ctx.message.guild.id}-message-applications.txt", "r")
                data = f.read()
                f.close()
                messages = ast.literal_eval(data)

            else:
                embed = discord.Embed(title="Error", colour=discord.Colour(0xf6ff), description="```Messages are not defined; contact an administrator```")

                embed.set_footer(text=f"Tick Tick | {ver}")
                await ctx.channel.send(embed=embed)

            custom = messages["custom"]
            if custom == False:
                embed = discord.Embed(title=f"Thank you for creating a ticket {ctx.author.name}", colour=discord.Colour(0xf6ff), description="We will get right back to you")

                embed.set_footer(text=f"Tick Tick | {ver}")
                await ctx.channel.send(embed=embed)
            else:
                title = messages["header"]
                title = title.replace("creator", ctx.author.name)
                title = title.replace("reason", reason)
                description = messages["description"]
                description = description.replace("creator", ctx.author.name)
                description = description.replace("reason", reason)

                embed = discord.Embed(title=title, colour=discord.Colour(0xf6ff), description=description)
                    
                embed.set_footer(text=f"Tick Tick | {ver}")

            await newchannel.send(embed=embed)
            embed = discord.Embed(title="Your application has been sucsessfully created.", colour=discord.Colour(0xf6ff), description=f"Your ticket is located in {newchannel.mention}")
                    
            embed.set_footer(text=f"Tick Tick | {ver}")
            await msg.edit(embed=embed)

            filepath = os.path.exists(f'./data/{ctx.message.guild.id}-ticket-num.txt')

            f = open(f"./data/{ctx.message.guild.id}-app-num.txt", "w")
            f.write(str(number))
            f.close()
                


            appinfo = {
                    "guild" : ctx.guild.id,
                    "owner" : ctx.author.id ,
                    "reason" : reason,
                    "channelcreated" : ctx.channel.id,
                    "ticketnum" : num,
                    "ticketchannel" : newchannel.id
                }
            f = open(f"./data/apps/{ctx.message.guild.id}-app-{num}.txt", "w")
            f.write(str(appinfo))
            f.close()
            
            



        else:
            embed = discord.Embed(title="Error", colour=discord.Colour(0xf6ff), description="```Categories are not defined; contact an administrator```")

            embed.set_footer(text=f"Tick Tick | {ver}")
            await ctx.channel.send(embed=embed)

@bot.command()
async def close(ctx):
    channel = ctx.channel
    filepath = os.path.exists(f'./data/tickets/{ctx.message.guild.id}-{channel.name}.txt')
    if filepath == False:
        embed = discord.Embed(title="Error", colour=discord.Colour(0xf6ff), description="```This channel is not a Ticket```")

        embed.set_footer(text=f"Tick Tick | {ver}")
        await ctx.send(embed=embed)
    else:
        filepath = os.path.exists(f'./data/{ctx.message.guild.id}-channels.txt')
        if filepath == False:
            embed = discord.Embed(title="Error", colour=discord.Colour(0xf6ff), description="```The categories are improperly defined```")

            embed.set_footer(text=f"Tick Tick | {ver}")
            await ctx.send(embed=embed)
        else:
            f = open(f"./data/{ctx.message.guild.id}-channels.txt")
            data = f.read()

        await ctx.send()
        channel = ctx.channel
        author = ctx.author

        def check(m):
            return m.channel == channel and m.author == author


        waited = await bot.wait_for('message', check=check)
        await waited.delete()
        if waited.content == "-confirm":
            await ctx.channel.delete()



@bot.command()
async def bug(ctx, *, name):
    channel = bot.get_channel(557505096557264896)
    await ctx.send(f"Your bug has been sent to {channel.mention}")
    embed = discord.Embed(title=f"{ctx.message.author.name} reported a bug", colour=discord.Colour(0xffff), description=f"{name}")
    channel = bot.get_channel(557505096557264896)

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

@bot.command(aliases=["site"])
async def website(ctx):
    global ver
    embed = discord.Embed(title="This is our website", colour=discord.Colour(0x29ff00), description="[Click here to go to our website](https://tick-tick.netlify.com/)")

    embed.set_footer(text=f"Tick tick | {ver}")
    await ctx.send(embed=embed)

@bot.command()
async def setstatus(ctx, status, type, *, name):
    user = bot.get_user(445556389532925952)
    user2 = bot.get_user(394174323117654036)
    if ctx.message.author == user or ctx.message.author == user2:
        
        if type == "listening":
            if status == "Online":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{name}"), status=discord.Status.online)
                await ctx.channel.send(f"Set the status to **Listening to {name}** and **Online**")
            elif status == "dnd":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{name}"), status=discord.Status.dnd)
                await ctx.channel.send(f"Set the status to **Listening to {name}** and **DND**")
            elif status == "idle":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{name}"), status=discord.Status.idle)
                await ctx.channel.send(f"Set the status to **Listening to {name}** and **Idle**")
            else:
                await ctx.send("Not a valid status")
        elif type == "watching":
            if status == "Online":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{name}"), status=discord.Status.online)
                await ctx.channel.send(f"Set the status to **Watching to {name}** and **Online**")
            elif status == "dnd":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{name}"), status=discord.Status.dnd)
                await ctx.channel.send(f"Set the status to **Watching to {name}** and **DND**")
            elif status == "idle":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{name}"), status=discord.Status.idle)
                await ctx.channel.send(f"Set the status to **Watching to {name}** and **Idle**")
            else:
                await ctx.send("Not a valid status")
        elif type == "playing":
            if status == "Online":
                await bot.change_presence(activity=discord.Game(name=f"{name}"), status=discord.Status.online)
                await ctx.channel.send(f"Set the status to **Playing to {name}** and **Online**")
            elif status == "dnd":
                await bot.change_presence(activity=discord.Game(name=f"{name}"), status=discord.Status.dnd)
                await ctx.channel.send(f"Set the status to **Playing to {name}** and **DND**")
            elif status == "idle":
                await bot.change_presence(activity=discord.Game(name=f"{name}"), status=discord.Status.idle)
                await ctx.channel.send(f"Set the status to **Playing to {name}** and **Idle**")
        elif type == "show":
            if name == "guilds":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"{len(bot.guilds)} servers"))
                await ctx.channel.send(f"Set the status to **watching `guild amount` servers** and **Online**")
        else:
            await ctx.channel.send("Not a valid type of status")
    else:
        await ctx.channel.send("Oops, you cant to that")

bot.run("NTU1Mjk0NjM0MDI5NDgxOTk1.D3pDoA.9yW7MLtm-bmysRA4exesPt5-TBs")