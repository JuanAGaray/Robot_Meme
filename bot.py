import discord
from genPass import gen_pass


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send(":P")
    elif message.content.startswith("$memeaudio"):
        await message.channel.send(file = discord.File("amarillo.mp3")  )
    elif message.content.startswith("$foto"):
        await message.channel.send(file = discord.File("foto.png"))
    elif message.content.startswith("$anime"):
        await message.channel.send(file = discord.File("anime.mp4"))
    elif message.content.startswith("$rock"):
        await message.channel.send(file = discord.File("kino.mp3"))
    elif message.content.startswith("$Contraseña-"):
        try:
            x = int(message.content[12:])
            if x >= 1500:
                await message.channel.send("No puedes pasar de los 1500 ")
            else:
                await message.channel.send(gen_pass(int(x)))
        except:
            await message.channel.send("debes colocar un numero despues del guón. Example : $Contraseña-15 ")
 
client.run("")
