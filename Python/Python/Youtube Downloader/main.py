from pytube import YouTube

link = input('URL: ')
path = input('Onde salvar o video: ')

yt = YouTube(link)

result = {
    "Titulo":yt.title,
    "Numero de Views":yt.views,
    "Tamanho do video":yt.length,
    "Avaliação de video":yt.rating
}

# print(f'''Titulo: {result["Titulo"]} 
# Views: {result["Numero de Views"]}
# Tamanho: {result["Tamanho do video"]}
# Avaliação: {result["Avaliação de video"]}''')

ys = yt.streams.get_highest_resolution()

print('Baixando...')

ys.download(path)
print('Download completo!')