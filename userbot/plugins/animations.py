# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.8.html

from asyncio import sleep
import requests
import random

from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from .help import add_command_help


textded = '''<b> Я дед инсайд </b>
<b> Мне 9 лет </b>
<b> И я хочу в Психокидс </b>'''


@Client.on_message(filters.command("dead", prefixes=".") & filters.me)
async def dead(_, message):
    txt = textded.split("\n")
    for i in txt:
        try:
            await message.edit(f'❤️{i} ❤️')
            await sleep(0.8)
            await message.edit(f'🧡 {i} 🧡')
            await sleep(0.8)
            await message.edit(f'💛 {i} 💛')
            await sleep(0.8)
            await message.edit(f'💚 {i} 💚')
            await sleep(0.8)
            await message.edit(f'💙 {i} 💙')
            await sleep(0.8)
            await message.edit(f'💜 {i} 💜')
            await sleep(0.8)
            await message.edit(f'🖤 {i} 🖤')
            await sleep(0.8)
            await message.edit(f'🤍 {i} 🤍')
            await sleep(0.8)
        except:
            pass


jopa = '''
           <b>ВЗЛОМ ЖОПЫ</b> 
           <b><i>Loading...</i></b> 
    10%  █▒▒▒▒▒▒▒▒▒▒▒▒
    30%  ███▒▒▒▒▒▒▒▒▒▒    
    50%  █████▒▒▒▒▒▒▒▒
    66%  ██████▒▒▒▒▒▒▒
    79%  ████████▒▒▒▒▒
    04%  █████████▒▒▒▒
    09%  ██████████▒▒▒
    95%  ████████████▒
    99%  █████████████
    100% █████████████
    <b> ВАША ЖОПА ВЗЛОМАНА </b>
    <b><i>Создатель: "Прощайте"</i></b>
    <b><i>Создатель: "Прощайте"</i></b>
    <b><i>Создатель: "Прощайте"</i></b>
'''


@Client.on_message(filters.command("jopa", prefixes=".") & filters.me)
async def sjopa(client, message):
    txt = jopa.split("\n")
    for i in txt:
        try:
            await message.edit(f'{i}')
            await sleep(0.8)
            await message.edit(f'{i}')
            await sleep(0.8)
            await message.edit(f'{i}')
            await sleep(0.8)
            await message.edit(f'{i}')
            await sleep(0.8)
            await message.edit(f'{i}')
            await sleep(0.8)
            await message.edit(f'{i}')
            await sleep(0.8)
            await message.edit(f'{i}')
            await sleep(0.8)
            await message.edit(f'{i}')
            await sleep(0.8)
        except:
            pass


@Client.on_message(filters.command('ziga', prefixes='.') & filters.me)
async def betaloves(client, message):
    try:
        hearts = [
         '🧡', '💛', '💚', '💙', '💜']
        try:
            mode = int(message.text.split('.ziga', maxsplit=1)[1])
            if mode > 2:
                await message.edit('<b> У команды всего 2 режима!</b>')
            if mode == 2:
                time = 0.6
                for i in range(1):
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(2)

            if mode == 1:
                time = 0.6
                for i in range(1):
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍❤️❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️❤️🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️❤️❤️🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🧡🧡🧡🧡🤍🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🤍🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🤍🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🤍🧡🧡🧡🧡🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💛💛💛💛🤍💛💛🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍🤍🤍🤍💛🤍🤍💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛🤍🤍💛🤍🤍🤍🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍💛💛🤍💛💛💛💛🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💚💚💚💚🤍💚💚🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍🤍🤍🤍💚🤍🤍💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚🤍🤍💚🤍🤍🤍🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍💚💚🤍💚💚💚💚🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💙💙💙💙🤍💙💙🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍🤍🤍🤍💙🤍🤍💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙🤍🤍💙🤍🤍🤍🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍💙💙🤍💙💙💙💙🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💜💜💜💜🤍💜💜🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍🤍🤍🤍💜🤍🤍💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜🤍🤍💜🤍🤍🤍🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍💜💜🤍💜💜💜💜🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🧡🧡🧡🧡🤍🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🤍🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🤍🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🤍🧡🧡🧡🧡🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💛💛💛💛🤍💛💛🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍🤍🤍🤍💛🤍🤍💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛🤍🤍💛🤍🤍🤍🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍💛💛🤍💛💛💛💛🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💚💚💚💚🤍💚💚🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍🤍🤍🤍💚🤍🤍💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚🤍🤍💚🤍🤍🤍🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍💚💚🤍💚💚💚💚🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💙💙💙💙🤍💙💙🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍🤍🤍🤍💙🤍🤍💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙🤍🤍💙🤍🤍🤍🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍💙💙🤍💙💙💙💙🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💜💜💜💜🤍💜💜🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍🤍🤍🤍💜🤍🤍💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜🤍🤍💜🤍🤍🤍🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍💜💜🤍💜💜💜💜🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🧡🧡🧡🧡🤍🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🤍🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🤍🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🤍🧡🧡🧡🧡🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💛💛💛💛🤍💛💛🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍🤍🤍🤍💛🤍🤍💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛🤍🤍💛🤍🤍🤍🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍💛💛🤍💛💛💛💛🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💚💚💚💚🤍💚💚🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍🤍🤍🤍💚🤍🤍💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚🤍🤍💚🤍🤍🤍🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍💚💚🤍💚💚💚💚🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💙💙💙💙🤍💙💙🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍🤍🤍🤍💙🤍🤍💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙🤍🤍💙🤍🤍🤍🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍💙💙🤍💙💙💙💙🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💜💜💜💜🤍💜💜🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍🤍🤍🤍💜🤍🤍💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜🤍🤍💜🤍🤍🤍🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍💜💜🤍💜💜💜💜🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🧡🧡🧡🧡🤍🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🤍🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🤍🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🤍🧡🧡🧡🧡🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💛💛💛💛🤍💛💛🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍🤍🤍🤍💛🤍🤍💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛🤍🤍💛🤍🤍🤍🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍💛💛🤍💛💛💛💛🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💚💚💚💚🤍💚💚🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍🤍🤍🤍💚🤍🤍💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚🤍🤍💚🤍🤍🤍🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍💚💚🤍💚💚💚💚🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💙💙💙💙🤍💙💙🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍🤍🤍🤍💙🤍🤍💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙🤍🤍💙🤍🤍🤍🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍💙💙🤍💙💙💙💙🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💜💜💜💜🤍💜💜🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍🤍🤍🤍💜🤍🤍💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜🤍🤍💜🤍🤍🤍🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍💜💜🤍💜💜💜💜🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️❤️❤️🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍❤️❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️❤️🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
                    await sleep(time)
                    await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')

        except Exception as e:
            try:
                await message.edit('<b>Вы не указали режим .ziga!\nПример:</b><code> .ziga 1</code>')
            finally:
                e = None
                del e

    except FloodWait as e:
        try:
            await sleep(e.x)
        finally:
            e = None
            del e


@Client.on_message(filters.command(["console"], prefixes="."))
async def brain(client, message):
    await message.edit("`>_`")
    await sleep(0.1)
    await message.edit("`>  `")
    await sleep(0.1)
    await message.edit("`>_`")
    await sleep(0.1)
    await message.edit("`>  `")
    await sleep(0.1)
    await message.edit("`>_`")
    await sleep(0.1)
    await message.edit("`>c_`")
    await sleep(0.1)
    await message.edit("`>cd`")
    await sleep(0.1)
    await message.edit("`>cd _`")
    await sleep(0.1)
    await message.edit("`>cd p`")
    await sleep(0.1)
    await message.edit("`>cd pr_`")
    await sleep(0.1)
    await message.edit("`>cd pro`")
    await sleep(0.1)
    await message.edit("`>cd proj_`")
    await sleep(0.1)
    await message.edit("`>cd proje`")
    await sleep(0.1)
    await message.edit("`>cd projec_`")
    await sleep(0.1)
    await message.edit("`>cd project`")
    await sleep(0.6)
    await message.edit("`>cd project`\n" + "`project>_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>g`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>gi_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git i_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git in`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git ini_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`")
    await sleep(0.6)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>g_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>gi`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git a_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git ad`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [=---------] 3%`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [=---------] 5%`")
    await sleep(0.3)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [===-------] 30%`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [===-------] 36%`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [====------] 41%`")
    await sleep(0.4)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [======----] 67%`")
    await sleep(0.2)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>g_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>gi`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git c`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git co_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git com`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git comm_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commi`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -a_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"I`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`")
    await sleep(2)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>g_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>gi`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git p`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git pu_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git pus`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push h`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push he_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push her`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push hero_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push herok`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku m`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku ma_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku mas`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku mast_`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku maste`")
    await sleep(0.1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`")
    await sleep(2)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`\n" + "`  Counting objects: 100% (5/5), done.`")
    await sleep(1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`\n" + "`  Counting objects: 100% (5/5), done.\n  Writing objects: 100% (3/3), 364 bytes | 364.00 KiB/s, done.`")
    await sleep(1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`\n" + "`  Counting objects: 100% (5/5), done.\n  Writing objects: 100% (3/3), 364 bytes | 364.00 KiB/s, done.\n  remote: Compressing source files... done.`")
    await sleep(1)
    await message.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`\n" + "`  Counting objects: 100% (5/5), done.\n  Writing objects: 100% (3/3), 364 bytes | 364.00 KiB/s, done.\n  remote: Compressing source files... done.\n  remote: Verifying deploy... done.`")


@Client.on_message(filters.command("др", prefixes=".") & filters.me)
async def dr_anim(client, message):
    await message.edit(f'С днём рождения! Желаю тебе...')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    👑 чтобы вся жизнь была полна радости
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    ☀️ счастья
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    🏋️‍♂️ здоровья
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    🌈 улыбок
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    💚 любви
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    🔥 приятных сюрпризов
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    🥇 Высоких достижений
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    🍃 Душевной гармонии
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    🌹 Процветания
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    📈 Карьерного роста
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    🤝 Хороших друзей
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    💪 Больше силы, чувств, смелости
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    🎲 Везения, мира, добра
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    🌃 Чтобы сбывались даже самые необычные желания
    ''')
    await sleep(0.8)
    await client.send_message(message.chat.id, f'''
    🎇 И чтобы каждое начатое дело заканчивалось успешно!
    ''')


@Client.on_message(filters.command("zaika", prefixes=".") & filters.me)
async def zaika(client, message):
    zaika = 0
    zaika2 = 0
    while zaika < 100:
        await message.edit(f'''
            💖 Поиск зайки... {zaika}%''')
        zaika += 1
    if zaika >= 100:
        await message.edit(f'''
            ✅ Зайка успешно найдена!''')
        await sleep(1)
        while zaika2 < 100:
            await message.edit(f'''
                🤔 Подбираю слова что-бы описать тебя... {zaika2}%''')
            zaika2 += 1
        if zaika2 >= 100:
            await message.edit(f'''
                ❤ Ты самый лучший человек которого я видел!''')
            await sleep(5)
            await message.delete()


@Client.on_message(filters.command("type", prefixes=".") & filters.me)
async def valentine(client, message):
    orig_text = message.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "█"
    while (tbp != orig_text):
        try:
            await message.edit(tbp + typing_symbol)
            await sleep(0.05)

            tbp = tbp + text[0]
            text = text[1:]

            await message.edit(tbp)
            await sleep(0.05)

        except FloodWait as e:
            sleep(e.x)


@Client.on_message(filters.command("wink", ".") & filters.me)
async def wink(client, message):
    try:
        hmm_s = "https://api.waifu.pics/sfw/wink"
        r = requests.get(url=hmm_s).json()
        image_s = r["link"]
        await client.send_video(message.chat.id, image_s)
        await message.delete()
    except Exception as e:
        await message.edit("Ошибка на стороне сайта. Попробуйте позже")
        await sleep(1)
        await message.delete()


@Client.on_message(filters.command("hug", ".") & filters.me)
async def hug(client, message):
    try:
        hmm_s = "https://api.waifu.pics/sfw/hug"
        r = requests.get(url=hmm_s).json()
        image_s = r["url"]
        await client.send_video(message.chat.id, image_s)
        await message.delete()
    except Exception as e:
        await message.edit("Ошибка на стороне сайта. Попробуйте позже")
        await sleep(1)
        await message.delete()
    
    
@Client.on_message(filters.command("pat", ".") & filters.me)
async def pat(client, message):
    try:
        hmm_s = "https://api.waifu.pics/sfw/pat"
        r = requests.get(url=hmm_s).json()
        image_s = r["url"]
        await client.send_video(message.chat.id, image_s)
        await message.delete()
    except Exception as e:
        await message.edit("Ошибка на стороне сайта. Попробуйте позже")
        await sleep(1)
        await message.delete()
        
@Client.on_message(filters.command("kiss", ".") & filters.me)
async def kiss(client, message):
    try:
        hmm_s = "https://api.waifu.pics/sfw/kiss"
        r = requests.get(url=hmm_s).json()
        image_s = r["link"]
        await client.send_video(message.chat.id, image_s)
        await message.delete()
    except Exception as e:
        await message.edit("Ошибка на стороне сайта. Попробуйте позже")
        await sleep(1)
        await message.delete()


@Client.on_message(filters.command("tea", ".") & filters.me)
async def tea_handler(client, message):
    text = ' '.join(message.command[1:])
    await message.edit(f"▀▄▄▄▄▄▀▀")
    await sleep(0.2)
    await message.edit(f"█░░░░░█─█\n▀▄▄▄▄▄▀▀")
    await sleep(0.2)
    await message.edit(f"█▀▀▀▀▀█▄\n█░░░░░█─█\n▀▄▄▄▄▄▀▀")
    await sleep(0.2)
    await message.edit(f"──▀──▀\n█▀▀▀▀▀█▄\n█░░░░░█─█\n▀▄▄▄▄▄▀▀")
    await sleep(0.2)
    await message.edit(f"──▀──▀\n─▄▀─▄▀\n█▀▀▀▀▀█▄\n█░░░░░█─█\n▀▄▄▄▄▄▀▀")
    await sleep(0.2)
    for x in range(6):
        await message.edit(f"──▀▄──\n─▄▀▄▀─\n█▀▀▀▀▀█▄\n█░░░░░█─█\n▀▄▄▄▄▄▀▀\n\n {text}")
        await sleep(0.2)
        await message.edit(f"─▀─▀──\n─▄▀─▀─\n█▀▀▀▀▀█▄\n█░░░░░█─█\n▀▄▄▄▄▄▀▀\n\n {text}")
        await sleep(0.2)
        await message.edit(f"──▀─▀─\n▄▀──▄▀\n█▀▀▀▀▀█▄\n█░░░░░█─█\n▀▄▄▄▄▄▀▀\n\n {text}")
        await sleep(0.2)
        await message.edit(f"───▄─▀\n─▄──▄▀\n█▀▀▀▀▀█▄\n█░░░░░█─█\n▀▄▄▄▄▄▀▀\n\n {text}")
        await sleep(0.2)
        await message.edit(f"──▀▄─▀─\n─▄▀─▄▀\n█▀▀▀▀▀█▄\n█░░░░░█─█\n▀▄▄▄▄▄▀▀\n\n {text}")


@Client.on_message(filters.command("dislike", ".") & filters.me)
async def dislike_handler(_, msg):
	for i in range(1):
		await msg.edit(f'''
🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥''')
		await sleep(0.001)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥''')
		sleep(1)
		await msg.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
		sleep(1)
		await msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥
''')
		sleep(1)
		await msg.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')


@Client.on_message(filters.command("like", ".") & filters.me)
async def like_handler(_, msg):
	for i in range(1):
		await msg.edit(f'''      
🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦️''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦️''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦''')
		await sleep(0.001)
		await msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦🟦''')
  
  
@Client.on_message(filters.command("vzlom", prefixes=".") & filters.me)
async def vzlom(app, msg):
	vzlom = 0

	await msg.edit(f'''
		💾 Взлом аккаунта скоро начнётся.''')
	await sleep(1)
	await msg.edit(f'''
		💾 Взлом аккаунта скоро начнётся..''')
	await sleep(1)
	await msg.edit(f'''
		💾 Взлом аккаунта скоро начнётся...''')
	await sleep(1)

	while vzlom < 100:
		await msg.edit(f'''
			❗ Происходит взлом аккаунта... {vzlom}%''')
		vzlom += 1
	if vzlom >= 100:
		await msg.edit(f'''
			✅ Взлом акканута успешно завершен!''')
		await sleep(0.5)
		await msg.edit(f'''
			📲 Передача данных в базу данных.''')
		await sleep(0.5)
		await msg.edit(f'''
			📱 Передача данных в базу данных..''')
		await sleep(0.5)
		await msg.edit(f'''
			📲 Передача данных в базу данных...''')
		await sleep(0.5)
		await msg.edit(f'''
			✅ Аккаунт успешно взломан!''')
		await sleep(5)
		await msg.delete()
  
  
@Client.on_message(filters.command("vzlomip", prefixes=".") & filters.me)
async def vzlomip(app, msg):
	vzlomip = 0

	await msg.edit(f'''
		💾 Поиск айпи начался.''')
	await sleep(1)
	await msg.edit(f'''
		💾 Поиск айпи начался..''')
	await sleep(1)
	await msg.edit(f'''
		💾 Поиск айпи начался...''')
	await sleep(1)

	while vzlomip < 100:
		await msg.edit(f'''
			❗ Происходит поиск IP... {vzlomip}%''')
		vzlomip += 1
	if vzlomip >= 100:
		await msg.edit(f'''
			✅ IP-адрес успешно найдён!''')
		await sleep(5)
		await msg.delete()
  
  
@Client.on_message(filters.command("bank", prefixes=".") & filters.me)
async def vzlombank(_, msg):
	bank = 0
	bank1 = random.randint(1, 2500)

	await msg.edit(f'''
	Идёт взлом банковской карты.''')
	await sleep(0.7)
	await msg.edit(f'''
	Идёт взлом банковской карты..''')
	await sleep(0.7)
	await msg.edit(f'''
	Идёт взлом банковской карты...''')
	await sleep(0.7)
	await msg.edit(f'''
	Получение данных.''')
	await sleep(0.7)
	await msg.edit(f'''
	Получение данных..''')
	await sleep(0.7)
	await msg.edit(f'''
	Получение данных...''')
	await sleep(0.7)
	while bank <= 99:
		bank += 1
		await msg.edit(f'''
		взлом завершён на {bank}%''')
	if bank >= 99:
		await msg.edit(f'''
		Взлом банковской карты успешно завершён!\nСо счёта снято {bank1} руб.''')


@Client.on_message(filters.command("hackpc", prefixes=".") & filters.me)
async def hackpc(_, msg):
	perc = 0
	while(perc < 100):
		try:
			text = "👮‍ Взлом твоего ПК в процессе ... " + str(perc) + "%"
			await msg.edit(text)
			perc += random.randint(1, 3)
			await sleep(0.1)
		except FloodWait as e:
			await sleep(e.x)
	await msg.edit("🟢 Ты успешно взломан!")
	sleep(3)
	await msg.edit("😈 Поиск секретных данных ...")
	perc = 0
	while(perc < 100):
		try:
			text = "😈 Поиск секретных данных ... " + str(perc) + "%"
			await msg.edit(text)
			perc += random.randint(1, 5)
			await sleep(0.15)
		except FloodWait as e:
			await sleep(e.x)
   

@Client.on_message(filters.command("drugs", prefixes=".") & filters.me)
async def _drugs(client, message):
	text = f"<b>💊 Поиск запрещённых препаратов.. </b>"
	await message.edit(str(text))
	await sleep(2)
	kilogramm = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
	text2 = f"<b>🚬 Найдено {random.choice(kilogramm)} кг шпекса</b>"
	await message.edit(str(text2))
	await sleep(3)
	text3 = f"<b>🌿⚗️ Оформляем вкид</b>"
	await message.edit(str(text3))
	await sleep(5)
	drugsss = [f'<b>😳 Вас успешно откачали, пожалуйста, больше не принимайте запрещённые препараты</b>',
			   f'<b>🥴 Вы пожилой наркоман, вас не берёт одна доза, вам необходимо больше, попробуйте  ещё раз оформить вкид</b>',
			   f'<b>😖 Сегодня не ваш день, вы хоть и пожилой, но приняли слишком много. Окончательная причина смерти - передоз</b>',
			   f'<b>😌 Вы оформили вкид, Вам понравилось</b>']
	drug = random.choice(drugsss)
	await message.edit(drug)
        
@Client.on_message(filters.command("onal", prefixes=".") & filters.me)
def onal_handler(_, msg):
	onal = 0
	onal2 = random.randint(0, 325)

	msg.edit(f'''
	Поиск админа.''')
	sleep(0.6)
	msg.edit(f'''
	Поиск админа..''')
	sleep(0.6)
	msg.edit(f'''
	Поиск админа...''')
	sleep(0.6)
	msg.edit(f'''
	Админ найден!''')
	sleep(0.8)
	msg.edit(f'''
	Идёт поиск анального отверстия админа.''')
	sleep(0.6)
	msg.edit(f'''
	Идёт поиск анального отверстия админа..''')
	sleep(0.6)
	msg.edit(f'''
	Идёт поиск анального отверстия админа...''')
	sleep(0.6)
	msg.edit(f'''
	Найдено!''')
	sleep(0.8)
	msg.edit(f'''
	Измерение анального отверстия админа.''')
	sleep(0.6)
	msg.edit(f'''
	Измерение анального отверстия админа..''')
	sleep(0.6)
	msg.edit(f'''
	Измерение анального отверстия админа...''')
	sleep(0.6)
	msg.edit(f'''
	Анальное отверстие админа состовляет {onal2} км''')
	sleep(1)
	while onal <= 55:
		sleep(0.1)
		onal += 1
		msg.edit(f'''
		Анальное проникновение админу выполнено на {onal}%''')
	if onal == 56:
		sleep(0.3)
		onal += 1
		msg.edit(f'''
		Рука устала''')
		sleep(0.6)
		msg.edit(f'''
		Отдых руки.''')
		sleep(0.6)
		msg.edit(f'''
		Отдых руки..''')
		sleep(0.6)
		msg.edit(f'''
		Отдых руки...''')
		sleep(0.6)
		msg.edit(f'''
		Отдых руки.''')
		sleep(0.6)
		msg.edit(f'''
		Отдых руки..''')
		sleep(0.6)
		msg.edit(f'''
		Отдых руки...''')
		sleep(0.6)
		msg.edit(f'''
		Рука отдохнула, можно продолжать...''')
		sleep(0.8)
		while onal >= 57:
			sleep(0.1)
			onal += 1
			msg.edit(f'''
			Анальное проникновение админу выполнено на {onal}%''')
			if onal == 99:
				sleep(0.6)
				msg.edit(f'''
				Жопа админа порвана. Поздравляю!''')
				break
                        
@Client.on_message(filters.command("mum", prefixes=".") & filters.me)
async def mum_command_handler(client, message):
	mamka = [f'<b>❌ Мамаша не найдена</b>',f'<b> ✅ МАМАША НАЙДЕНА</b>' ]
	text = "<b>🔍 Поиск твоей мамки начался...</b>"
	await message.edit(str(text))
	await sleep(3.0)
	text2 = "<b>🔍 Ищем твою мамашу на Авито... </b>"
	await message.edit(str(text2))
	await sleep(1)
	text3 = random.choice(mamka)
	await message.edit(str(text3))
	await sleep(3.0)
	text4 = "<b>🔍 Поиск твоей мамаши на свалке... </b>"
	await message.edit(str(text4))
	await sleep(3.0)
	text5 = random.choice(mamka)
	await message.edit(str(text5))
	await sleep(5.0)

add_command_help(
    "animations",
    [
        [".dead", "Анимация «Я дед инсайд»"],
        [".jopa", "Анимация «Взлом жопы»"],
        [".ziga [1/2]", "Анимация сердца"],
        [".console", "Анимация консоли"],
        [".др", "Анимация «С днём рождения»"],
        [".zaika", "Анимация «Поиск зайки»"],
        [".type [Текст]", "Анимация написания текста"],
        [".tea [Текст]", "Симв. анимация «Чай»"],
        [".like", "Скрипт анимации «Лайк»"],
        [".dislike", "Скрипт анимации «Дизлайк»"],
        [".vzlomip", "Анимация «Взлом IP»"],
        [".vzlom", "Анимация «Взлом аккаунта»"],
        [".bank", "Анимация «Взлом банковской карты»"],
        [".hackpc", "Анимация «Взлом пк»"],
        [".drugs", "Анимация «Вкид н@рко»"],
        [".onal", "Анимация «Aнального проникновения админу»"],
        [".mum", "Анимация «Поиск м@маши»"],
        [".wink", "Присылает рандомную гифку с подмигиванием"],
        [".hug", "Присылает рандомную гифку с обнимашками"],
        [".pat", "Присылает рандомную гифку с поглаживанием по голове"],
        [".kiss", "Присылает рандомную гифку с поцелуем"],
    ]
)
