import bot

import discord

from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

doc_bot = bot.DocBot()

@doc_bot.command(name='del')
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for each_message in messages:
             await each_message.delete()


#calendrier


#match
@doc_bot.command(name='match')
async def match(ctx, date_match: datetime, adversaire: string)

#presence
@doc_bot.command(name='presence')

#react on message
@doc_bot.event
async  def on_reaction_add()