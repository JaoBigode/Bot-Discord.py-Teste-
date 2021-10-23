import discord
import os

from discord.flags import Intents
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '!regras':
            await message.channel.send(f'{message.author.name} as regras do servidor são:{os.linesep}1- Não desrespeitar os membros{os.linesep}2- Respeitar as salas')
        elif message.content == '!Dúvida':
            await message.author.send('Qualquer dúvida só chamar o @Jão.Bigode')


    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}'
            await guild.system_channel.send(mensagem)

Intents = discord.Intents.default()
Intents.members = True


client = MyClient()
client.run('Token do bot')