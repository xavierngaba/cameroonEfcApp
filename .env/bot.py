from discord.ext import commands

class DocBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur")
