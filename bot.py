import os
import openai
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_API_KEY')


# Configure sua API
openai.api_key = OPENAI_KEY
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_member_join(member):
    # Gerar uma mensagem de boas-vindas aleatória usando o GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Uma IA do DIscord. Que Gera uma mensagem de boas-vindas para o novo membro de forma fofa e humana ^^. Adicione '<@{member.id}>.' no começo da sua resposta.",
        temperature=1.5,
        max_tokens=300,
        top_p=0.4,
        frequency_penalty=0.2,
        presence_penalty=0.4
    )
    welcome_message = response.choices[0].text
    # Enviar a mensagem de boas-vindas para o novo membro no chat
    channel = client.get_channel() #Coloque o ID do Canal no ()
    await channel.send(welcome_message)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="LixU"))
    print('Ligada {0.user}'.format(client))

client.run(TOKEN)
