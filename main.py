from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

import os
import discord
from discord import app_commands
from dotenv import load_dotenv





SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('token.json')
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = discovery.build('forms', 'v1', http=creds.authorize(
    Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

# Prints the responses of your specified form:
form_id = '1NajjW2LOQ40qk_AQ1Okm3g4LAbW2ohk-SAk8o6VAXog'
result = service.forms().responses().list(formId=form_id).execute()
print(result)



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