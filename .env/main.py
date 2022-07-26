import discord

default_intents = discord.Intents.default()

default_intents.members = True

client = discord.Client(intents=default_intents)


@client.event
async def on_ready():
    print("Le bot est prêt à l'action.")


@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()

        for each_message in messages:
            await each_message.delete()


@client.event
async def on_member_join(member):
    buvette_channel: discord.TextChannel = client.get_channel(780837396417347614)
    await buvette_channel.send(content=f"Bienvenue sur le serveur {member.display_name}")


client.run("OTU0MDM4MzA1MjQxMDY3NTIx.GU-zxN.aYlAoaaNtzDM5QxnVvomExi8e5Hz9VKXOFbIQs")
