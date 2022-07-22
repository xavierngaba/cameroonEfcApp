import discord

default_intents = discord.Intents.default()

default_intents.members = True

client = discord.Client(intents=default_intents)


@client.event
async def on_ready():
    print("Le bot est prêt à l'action.")


@client.event
async def on_message(message):
    if message.content.lower() == "ping":
        await message.channel.send("pong", delete_after=5)


@client.event
async def on_member_join(member):
    buvette_channel: discord.TextChannel = client.get_channel(780837396417347614)
    await buvette_channel.send(content=f"Bienvenue sur le serveur {member.display_name}")


client.run("OTU0MDM4MzA1MjQxMDY3NTIx.GXKl7v.8BhS3FRm9AwELxuWjZTC68NhfFuuk1Qugr8ESQ")
