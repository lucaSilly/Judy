import os
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

intents = discord.Intents.default()
intents.message_content = True
intents.members= True

class Client(discord.Client):
        def __init__(self):
                super().__init__(intents=intents)
        async def on_ready(self):
                await tree.sync(guild=discord.Object(id= "576840857840386070"))
                print("Judy started")
        #await client.get_channel(692140418405761035).send("https://tenor.com/view/hailee-steinfeld-kate-bishop-dickinson-gif-24083477")


client = Client()
tree = app_commands.CommandTree(client)


@tree.command(name = "supr", description="Supprimer des messages", guild=discord.Object(id="576840857840386070"))
@app_commands.checks.has_permissions(manage_messages = True)
async def delete(interaction, number: int):
        #await interaction.message.delete()
        #t
        deleted = await interaction.channel.purge(limit=number + 1)
        await interaction.response.send_message(f"{len(deleted)} messages supprimés",ephemeral=True)



client.run(os.getenv("TOKEN"))