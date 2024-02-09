import discord
from discord.ext import commands
import image_reader
import utilsdb
import database
from collectNames import getNames
import extraUtils

client=discord.Client(intents=discord.Intents.all())

reader = image_reader.Image_Reader()
utils = utilsdb.utilsDB()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    

    if message.content.startswith('test'):
        await message.channel.send("this is the content: {}".format(message.content))
        
    if message.content.startswith('channel'):
        await message.channel.send("this is the content: {}".format(message.channel.id))
        
    if message.content.startswith('$upload'):
        async with message.channel.typing():
            distance = utils.getPoints(reader.readImage(message.attachments[0].url))
            pointsLst = utils.convertMetric(distance)
            #await message.channel.send("Pod of War: +{} {}".format(pointsLst[0],pointsLst[1]))
            database.distance_entry(message.author.id,float(pointsLst[0]))
            await message.channel.send("{}: +{} {}".format(database.getFirstName(message.author.id),pointsLst[0],pointsLst[1]))
        

    if message.content.startswith('author'):
        await message.channel.send("this is the author: {}".format(message.author))
        
    if message.content.startswith('id'):
        await message.channel.send("this is the id: {}".format(message.author.id))
        
    if message.content.startswith('-members--'):
        memberData = message.guild.members
        await message.channel.send("Sent")
        
        data = []
        for member in message.guild.members:
            if not member.nick:
                data.append([member.id,member.name,"no"])
            else:
                data.append([member.id,member.name,member.nick])
        getNames(data)
        
    if message.content.startswith("-add"):
        notRegistered = database.user_entry(message.author.id)
        if notRegistered:
            await message.channel.send("User added")
        else:
            await message.channel.send("User is already registered")
            
    if message.content.startswith("-leaderboard"):
        rankList = database.getListRanking()
        rankingString = extraUtils.getRankingString(rankList)
        await message.channel.send(rankingString)

    

    if message.content.startswith("-guild"):
        await message.channel.send("sent")
        print(message.guild.text_channels)
    
    if message.content.startswith("-back"):
        #await message.channel.send("received")
        channel = client.get_channel(1032412250155266089)
        messages = channel.history(limit=2)
        async for x in messages:
            #print(x.content)
            print(x.id)
    
    if message.content.startswith("-reaction"):
        c = client.get_channel(1032412250155266089)
        message = await c.fetch_message(1204477298456268880)
        for reac in message.reactions:
            print(reac)
            async for user in reac.users():
                print(user.name)
        
        
client.run("MTE1NDUzNDQ4NTc0OTEzNzUwOQ.G_BAyu.JG561gIlT95IhB2ikegjG9AhU7ZGa3Wju8LYBI")