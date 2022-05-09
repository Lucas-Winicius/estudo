import discord
from discord.ext import commands
from random import randint, choice
from time import sleep
from datetime import *

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='>', case_insensitive=True)

@client.event
async def on_ready():
  print('Entramos como {0.user}'.format(client))

# NÃO ESTA FUNCIONANDO
@client.event
async def on_member_join(member):
  print('EXECUTANDO...')
  canal_boas_vindas = client.get_channel(939350630785507359)
  regras = client.get_channel(713066571609931796)
  mensagem = await canal_boas_vindas.send(f'<:emoji_17:834904386911076424>Olá, {member.mention}! Leia as regras em {regras}')

@client.command()
async def ola(ctx):
  await ctx.send(f'Olá, {ctx.author}')

@client.command()
async def dado(ctx, numero=6):
  v = randint(1, int(numero))
  await ctx.send('Girando dado...')
  sleep(2.3)
  await ctx.send(f'DADO: {v}')

@client.command()
async def ping(ctx):
  await ctx.send(f"PONG! {round(client.latency * 1000)}ms")

@client.command()
async def ajuda(ctx):
  await ctx.send(file=discord.File('load.jpg'))

@client.command()
async def fig(ctx):
  await ctx.send('<:emoji_19:834904563702038529> <:emoji_16:834904337028481074> <:emoji_2:834892118039592980> <:emoji_21:834904681569583125>')

@client.command()
async def hora(ctx):
  data = str(f'{datetime.today().day}/{datetime.today().month}/{datetime.today().year}  {datetime.today().hour}:{datetime.today().minute}')
  await ctx.send(data)
  await ctx.send(f'Bot online desde {data}')

@client.command()
async def comandos(ctx):
  data = str(f'{datetime.today().day}/{datetime.today().month}/{datetime.today().year}  {datetime.today().hour}:{datetime.today().minute}')

  comandos = discord.Embed(
    title = 'Lista de comandos:',
    description = 'Lembre-se de sempre colocar ">" para o comando ser executado',
    colour = 16729600
  )

  comandos.set_author(name='Abobora')#, icon_url='https://i.imgur.com/pxirbXg.jpg')

  comandos.set_thumbnail(url='https://c.tenor.com/15iA-FBQhuAAAAAd/pumpkin-dancing-pumpkin.gif')

  comandos.add_field(name='OLA', value='Te da um oizinho.', inline=False)
  comandos.add_field(name='DADO "Valor"', value='Retorna um numero aleatorio contando desde o 1 ate o seu numero escolhido.', inline=False)
  comandos.add_field(name='PING', value='Exibe o atual ping do Bot.', inline=False)
  comandos.add_field(name='HORA', value='Mostra o horario atual do servidor.', inline=False)

  comandos.set_footer(text= data)

  await ctx.send(embed= comandos)
  

client.run('')
