# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

from asyncio import sleep

from pyrogram import Client, filters, enums

from userbot.utils.logger import logger
from .help import add_command_help

@Client.on_message(filters.command("updst", ".") & filters.me)
async def update_status_handler(client, message):
    cmds = ' '.join(message.command[1:])
    try:
        text = cmds.split("|")
        await message.edit(f"Статус будет успешно обновлятся")
        while True:
            for x in text:
                await client.update_profile(bio = x.strip())
                await sleep(5)
        
    except Exception as e:
        await message.edit(f"Ошибка: {e}")
        
    await sleep(5)
    await message.delete()

@Client.on_message(filters.command("calc", ".") & filters.me)
async def calc(client, message):
    cmds = ' '.join(message.command[1:])
    
    try:
        await message.edit(eval(cmds))
    except NameError:
        await message.edit(
            f"🔴 Неправильное использование команды.\n"
            f"└ Команда принимает только \"+\" \"-\" \"*\" \"**\" \"/\" (плюс, минус, умножение, степень, деление)\n\n"
            f"Пример: .calc 2 + 3 - 4 * 5 ** 6 / 7",
            parse_mode = enums.ParseMode.DISABLED
        )
        await sleep(5)
        await message.delete()
    except Exception as e:
        logger.error(f"Error: {e}")
        await message.edit(
            f"🔴 Ошибка, или неправильное использование команды.\n"
            f"└ Команда принимает только \"+\" \"-\" \"*\" \"**\" \"/\" (плюс, минус, умножение, степень, деление)\n\n"
            f"Пример: .calc 2 + 3 - 4 * 5 ** 6 / 7",
            parse_mode = enums.ParseMode.DISABLED
        )
        await sleep(5)
        await message.delete()

add_command_help(
    "misc",
    [
        [
            ".calc [пример]",
            "Калькулятор. (Пример: .calc 2 + 3)"
        ],
        [
            ".updst [Текст 1 | Текст 2 | Текст 3 и тд.]", 
            f"Автоматическая смена статуса каждые 5 секунд.\n"
            f"Чтобы остановить, закройте консоль с помощью Ctrl+C"
            f"(в таком случае закроется весь юзербот, и его надо будет запустить заного)"
        ]
    ],
)