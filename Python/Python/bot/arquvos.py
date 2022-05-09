
adivinhe = ['abobora', 'melão']

data = ''


@client.event
async def oie(ctx):
  zois(ctx)



@client.command()
async def game(ctx, numero=0):
  await ctx.send('Iniciando game...')
  vct = False
  sleep(1)
  await ctx.send('Isso pode demorar um pouco aguarde')
  sleep(4)
  comp = 25
  await ctx.send('>j "sua jogada"')
  while vct != True:
    @client.command()
    async def jogada(ctx, jog):
      play = int(jog)
      if play < 0 and play > 50:
        await ctx.send('Numero invalido!')
      if play == comp:
        await ctx.send('Vitoria!')
        vct = True

  await ctx.send('Jogo finalizado')




@client.command()
async def adivinhe(ctx):
  a = choice(adivinhe)
  await ctx.send(a)



@client.command()
async def Comando(ctx):
  await ctx.send(file=discord.File('load.jpg'))




@client.command()
async def finalizar(ctx):
  await ctx.send('Finalizando BOT...')
  sleep(7)
  await ctx.send('AGUARDE...')
  sleep(9)
  await ctx.send('Isso esta demorando mais que o esperado.')
  sleep(11)
  await ctx.send('BOT finalizado com sucesso!')




@client.command()
async def ma(ctx):
  pedro = client.get_user(785497461207859221)
  await ctx.author.send(f'Comando temporario sugerido por {pedro}.')
  sleep(2)
  await ctx.author.send('Mama eu')
  sleep(1)
  await ctx.author.send(';-;')



#####################  EMBED  ###################


@client.command()
async def e(ctx):
  embed = discord.Embed(
    title = 'TITULO',
    description = 'Descrição',
    colour = 16711680
  )

  embed.set_author(name='Criador: ABOBORA', icon_url='https://www.tibiawiki.com.br/images/5/5c/Mining_Helmet.gif')

  embed.set_thumbnail(url='https://www.tibiawiki.com.br/images/c/ce/The_Epic_Wisdom.gif')

  embed.set_image(url='https://www.minecraft.net/content/dam/games/minecraft/marketplace/updates-catspandas_latest.jpg')

  embed.set_footer(text='Footer')

  embed.add_field(name='Nome', value='VALOR', inline=True)
  embed.add_field(name='Nome', value='VALOR', inline=True)
  embed.add_field(name='Nome', value='VALOR', inline=True)
  await ctx.send(embed = embed)

  await ctx.send('''comandos:

Funções Ativas:
!Bot em funcionamento
!novo Membro #apresenta erro

Comandos:
>oie #indisponivel
>ola
>dado 99 
>game #em desenvolvimento
    >jogada #funcionalidade extra do >game
>adivinhe #jogo de adivinhaçao incompleto
>comandos #criar um embed 
>finalizar #reinicia o Bot
>ping
>ajuda
>e
>fig
>comand

Versão 0.0.5

V0.0.6
Limpar o codigo
''')