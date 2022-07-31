import os

import discord

import bot

from datetime import tzinfo, timedelta, datetime, date, time

from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

doc_bot = bot.DocBot()

@doc_bot.command(name='del')
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for each_message in messages:
             await each_message.delete()


#match
@doc_bot.command(name='match')
async def match(ctx, jour_match: str, heure_match: str, adversaire: str):
    message = await ctx.send(f":calendar: Match du {jour_match} à {heure_match} :vs: {adversaire}. Veuillez valider vos présences : :white_check_mark: présent ou :x: absent")
    await message.add_reaction("✅")
    await message.add_reaction("❌")

    def checkEmoji(reaction, user):
        return message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

    def add_user_reaction(user_list):
        user_list_str = ""
        for u in user_list:
            user_list_str += u + " :white_check_mark:" + "\n"
        return user_list_str

    def del_user_reaction(user_list):
        user_list_str = ""
        for u in user_list:
            user_list_str -= u + " :x:" + "\n"
        return user_list_str

    user_list = []
    try:
        reaction, user = await doc_bot.wait_for("reaction_add", check = checkEmoji)
        print(reaction)
        print(user)
    except:

    # user_list.append(user.name)
    #
    # if reaction.emoji == "✅":
    #     await ctx.send(add_user_reaction(user_list))
    # else:
    #     await ctx.send(del_user_reaction(user_list))

#today = datetime.today()

#print("aujourd'hui nous sommes ", today)

doc_bot.run(os.getenv("TOKEN"))