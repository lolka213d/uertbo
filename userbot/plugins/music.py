# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.enums import ChatAction

from .help import add_command_help


@Client.on_message(filters.command("showdown", prefixes=".") & filters.me)
async def showdown(client, message):
	for x in range(13, 0, -1):
		await message.edit(f"Начало через: {x}s")
		await sleep(0.6)
	await sleep(0.2)
	await message.edit(f"<b>Бу, блять! Ха-ха</b>") 
	await sleep(1.2)
	await message.edit(f"<b>Просыпайтесь нахуй (Let's go!)</b>")
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Головы сияют на моей едкой катане</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Голоса этих ублюдков по пятам бегут за нами</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Погружённый в Изанами, все колёса под глазами</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Её взгляд убьёт любого, её взгляд убьёт цунами</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Похоронный марш гулей, на часах последний тик</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Моя тати — Бравл Шелли, я несу ей дробовик</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Ваши головы — мишени, я снесу их в один миг</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Никаких резких движений — ваш хилбар на один хит</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Динамайк трипл килл, ха, нервы на пределе</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Voice в моих ушах — я позабыл все дни недели</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Как на лезвии ножа и шквал патрон, летят шрапнели</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Psychokilla — весь мой шарм, вся эта мапа поредели</b>
	''')
	await sleep(1.5)
	await client.send_message(message.chat.id, f'''
	<b>Эй, погоди, мои парни на Стокгольме</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Мой showdown 1x1, и мои демоны все в форме</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Если я зайду к вам в лобби — оно станет вам могилой</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Если ты зайдешь — мне похуй, я не стартану и выйду, а-ха</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>По приказу Генерала Гавса!</b>
	''')
	await sleep(1.4)
	await client.send_message(message.chat.id, f'''
	<b>— Бро, тут вообще сложная ситуация, все границы позакрывали нахуй. Ваще пиздец полный. Ща просто едем ближе ко Львову, но во Львове тоже пиздец начался, поэтому хуй знает</b>
	''')
	await sleep(1.9)
	await client.send_message(message.chat.id, f'''
	<b>— Бля, чуваки, шутки шутками, но не занимайтесь хуйнёй, я вас умоляю. А-а-а!</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Эй, я как Вольт — называй неуловимый</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Я в showdown'е, как Кольт — твои патроны летят мимо</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Ты на этой мапе — ноль, ты не скрывайся — тебя видно</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Я как Рико, дал обойму, мой лайфстайл — psychokilla</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>De-Dead inside mode, я бегу по головам</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Оверсайз весь шмот, я на трапе тут и там</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Весь твой скилл — шаблон, я по рофлу на битах</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Зачем мне октагон? Могу выйти на финдах, ха</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Головы сияют на моей едкой катане</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Голоса этих ублюдков по пятам бегут за нами</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Погружённый в Изанами, все колёса под глазами</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Её взгляд убьёт любого, её взгляд убьёт цунами</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Генерал Гавс, ха, вижу вас без гема</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Я отдал приказ, и все умрут от реквиема</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Дота-рэп — топ чарт, ха, наебал систему</b>
	''')
	await sleep(1.3)
	await client.send_message(message.chat.id, f'''
	<b>Mute all chat, я на лям скупил все гемы, ха-ха</b>
	''')
	await sleep(1.4)
	await client.send_message(message.chat.id, f'''
	<b>Ха-а, бля</b>
	''')

	await sleep(5)
	await message.delete()


@Client.on_message(filters.command("versus", ".") & filters.me)
async def versus(client, message):
	await client.send_message(message.chat.id, f'''
	<b>Гавно</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Залупа</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Пенис</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Хер</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Давалка</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Хуй</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Блядина</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Галовка</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Шлюха</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Жопа</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Член</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Еблан</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Петух</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Мудила</b>
	''')
	await sleep(0.7)
	await client.send_message(message.chat.id, f'''
	<b>Рукаблуд</b>
	''')
	await sleep(0.5)
	await client.send_message(message.chat.id, f'''
	<b>Ссанина</b>
	''')
	await sleep(0.5)
	await client.send_message(message.chat.id, f'''
	<b>Очко</b>
	''')
	await sleep(0.5)
	await client.send_message(message.chat.id, f'''
	<b>Блядун</b>
	''')
	await sleep(0.5)
	await client.send_message(message.chat.id, f'''
	<b>Вагина</b>
	''')
	await sleep(0.4)
	await client.send_message(message.chat.id, f'''
	<b>Сука</b>
	''')
	await sleep(0.4)
	await client.send_message(message.chat.id, f'''
	<b>Ебланище</b>
	''')
	await sleep(0.4)
	await client.send_message(message.chat.id, f'''
	<b>Влагалеще</b>
	''')
	await sleep(0.4)
	await client.send_message(message.chat.id, f'''
	<b>Пердун</b>
	''')
	await sleep(0.4)
	await client.send_message(message.chat.id, f'''
	<b>Дрочила</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Пидор</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Пизда</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Туз</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Малафья</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Гомик</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Мудила</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Пилотка</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Манда</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Анус</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Вагина</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Путана</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Педрила</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Шалава</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Хуила</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Мошонка</b>
	''')
	await sleep(0.3)
	await client.send_message(message.chat.id, f'''
	<b>Елда</b>
	''')
	await sleep(0.8)
	await client.send_message(message.chat.id, f'''
	<b>Раунд!</b>
	''')

	await sleep(5)
	await message.delete()


@Client.on_message(filters.command("zoo", ".") & filters.me)
async def zoo(client, message):
	await client.send_message(message.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Мне собачку тр*хнуть утром мало</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Надо утром вечером и днем</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>У меня вчера змея сосала</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>А сегодня я е*усь с ежом!</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Мама принесла вчера котенка</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>На ночь я его к себе забрал</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сразу во все дыры отъе*ал!</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')

	await sleep(5)
	await message.delete()


@Client.on_message(filters.command("stars", ".") & filters.me)
async def stars(client, message):
	await client.send_message(message.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Да я скорей подохну, чем заговорю с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я точно буду одинок до конца своих дней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Парней так много, и чем я могу запомниться?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я сброшусь с крыши, лишь бы мне не опозориться</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Покинуть город, лишь бы не говорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Разбиться насмерть, лишь бы не говорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Потерять память, лишь бы не говорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Пропасть бесследно, лишь бы не говорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Её глаза прекрасны, детка LovelyLove</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Её волосы достойны самых преданных баллад, а</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Таких красивых мало просто поискать</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Она сияет ярче звёзд, и освещается Земля</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>«Привет, как день?» — щас подойду и скажу ей</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Но я скорей… Скорей подохну, чем заговорю</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Мой батя скажет мне, что я ёбаное ссыкло</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>В мои годы был женат на маме и служил в ОМОН</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Но зачем мне кто-то? Одинокий музыкант</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Презираю всё, что вижу, тут Марголдин — реальный панк, я</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Тёлки не нужны — мы и без них справимся</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Нет лучше пизды, чем очко товарища</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Её глаза прекрасны, детка LovelyLove</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Её волосы достойны самых преданных баллад, а</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Таких красивых мало просто поискать</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Она сияет ярче звёзд, и освещается Земля</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сбросится с крыши или заговорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сбросится с крыши или заговорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сбросится с крыши или заговорить с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сбросится с крыши или заговорить с ней</b>
	''')
	await sleep(1)

	await sleep(5)
	await message.delete()


@Client.on_message(filters.command("landisi", ".") & filters.me)
async def landisi(client, message):
	await client.send_message(message.chat.id, f'''
	<b>Ты вчера мне преподнес</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Толстый х*й под самый нос</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>И сказал, что это ландыши</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Но меня не проебешь</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Х*й на ландыш не похож</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Х*й — большой</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>А ландыш — маленький</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Это весенние цветы</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Их подарил мне ты</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты вчера мне преподнес</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Мех с п*зды, клочек волос</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>И сказал, что это ландыши</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Но меня не наебешь</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Клок на ландыш не похож</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Клок — большой</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>А ландыш — маленький</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Это весенние цветы</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Их подарил мне ты</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Мы забрались в камыши</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Нае*ались от души</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Нах*я нам эти ландыши?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты и так, б*ядь, хороша</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ну и что</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Что ландыш маленький?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Теплого мая привет</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Девушка юноше</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Делает м*нет</b>
	''')

	await sleep(5)
	await message.delete()


@Client.on_message(filters.command("neverenough", ".") & filters.me)
async def neverenough(client, message):
	await client.send_message(message.chat.id, f'''
	<b>MUPP broken your heart</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Ха-а, ха-а, а-а</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Крики necromastery и вопли подо мной</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Руки дезоляторы и shadow nevermore</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Ха-а</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Трипл рэйз в ебало, твоя сука вся течёт</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Она говорит ей мало, но я продолжу ход</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Твоё сердце так пылает, его превращаю в лёд</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Как Лелуш управляю этой сукой — она орёт</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Я бегу ща как Соник, попробуй поймай</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Эта сука не знает, как подойти — отступай</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>На мне ща куча дури (А-а) и это не манта</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Вдавил шб и таунт трайни (А-а), один из ста</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Записал тебя в тетрадку и я не Ягами</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Zero reasons to talk, ублюдки, это цунами</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Я, бля, Тобирама — все бастарды за бортами</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Я неуязвим, моя клятва — это синигами (Ага)</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Fear — это страх, а страх — это я</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Под баффом агилы берсерк mode Киллуа</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Эй, я как Вольт — называй неуловимый</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Я в showdown'е, как Кольт — твои патроны летят мимо</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Ты на этой мапе — ноль, ты не скрывайся — тебя видно</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Я как Рико, дал обойму, мой лайфстайл — psychokilla</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>De-Dead inside mode, я бегу по головам</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Оверсайз весь шмот, я на трапе тут и там</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Весь твой скилл — шаблон, я по рофлу на битах</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Зачем мне октагон? Могу выйти на финдах, ха</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Sla-Sla-Slayer убийца, Рефреш обновился</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Реквием в сердце — ты болью проникся</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>За спиной нет крыльев, но я лечу</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Butterfly на руке и я его точу (А)</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Emotional emptiness — совсем не грущу</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Why do you even try? Заживо сожру</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Я-Я не под спидами, просто под хастой</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Су-Су-Супер Сайян, so slow — это штрафной</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Выпал крит, это не Кристалис</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Моб Психо сто, но мы не сыгрались</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Зеницу Агацума — называй меня скорость</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Меня не остановить, тревела на ноги полная готовность</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>See you later на полу следы от ног остались навсегда</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Позади меня нет жара, only холода</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Не оставлю тебе выбора, творя, бля, чудеса</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Never enough даю те полчаса, убив всех enemy, ну да-да</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Ха-а, продолжай, ха-а (Yeah, ho)</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Демоны в башке, рэйзы на тебе</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Кричишь от боли, приклонись судьбе</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Поток Акаши, ты вставший на колени</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Не посмел бы даже думать о замене</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>У меня нет кагуне, просто я ебанутый</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Feel no pain — и я стал культом</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Тысячи гулей узнают по никнейму</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Чекай телеграм, там весь сквад Антейку</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Если у тя бабочка — я не миссую</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Если у тя мкб — ты вовсе не хитуешь</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>W/W — сияю ярче Иллидана (А-а)</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Парень ставит паузу и я достаю катану</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>**Ха-а, ха-а, а-а**</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>**Крики Necromastery и вопли подо мной**</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>**Руки дезоляторы, shadow nevermore**</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Залетаю с автоматом, ставлю лазер коллиматор</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Твоя тати — моя тати, со мной едет в Maserati</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Фиолетовая shawty, её тело на кровати</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Я снёс им всем ебало — это стиль аннигилятор</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Третий глаз как шинигами, в темноте не вижу свет</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Venom orb в моём пресете, замедляю в интернете</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Вооружён зубами, я их отправлю на тот свет</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Они стреляют в моё тело, мой armor бронежилет (Арата)</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Мо-Моя катана самехада — поедает этих тварей</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Холодает в моём теле, бью — я будто Гаара</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Один hit по тебе — ты пропал с радара</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>Один hit по тебе — ты пропал с радара</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>**Крики Necromastery и вопли подо мной**</b>
	''')
	await sleep(0.6)
	await client.send_message(message.chat.id, f'''
	<b>**Руки дезоляторы, shadow nevermore**</b>
	''') 
	await sleep(1)
	await client.send_sticker(message.chat.id, "CAACAgIAAxkBAAEENvNiNs_MoD7fFverk1v5wqoX2Fd-tQACxgoAAiu8OUlTcsBdvR5J0iME")

	await sleep(5)
	await message.delete()


@Client.on_message(filters.command("kaif", ".") & filters.me)
async def kaif(client, message):
	await client.send_message(message.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты в моих мыслях так плотно засела</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>А я не был грубым, так, просто манера</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Все подружки в шоке, Gucci, Panamera</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>От голоса моего ты опьянела</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Где девочка манит, там так сильно дурманит</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Каждую секунду я звоню, но телеф занят</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты, моя родная, не грусти, не сердись так</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты просто лови, ты лови, ты лови кайф</b>
	''')
	await client.send_message(message.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Кайф ты поймала, тебе всегда мало</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты не представляешь, как мне тебя не хватало</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сильно бьётся сердце, сама не ожидала</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Наконец-то твоя совесть тебя наказала</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Девочка в предвкушении азарта</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Когда встретил тебя, не нашёл пути обратно</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты — моё сокровище, козырная карта</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Мы дошли до финиша, не дойдя до старта</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Что ты забыла у меня на repeat'е?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>В твоих глазах я тону — помогите!</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты, моя родная, не грусти, не сердись так</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты просто лови, ты лови, ты лови кайф</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')

	await client.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEPJ1iOeGaHrwudfx0VAkPdzcJV7rSsAACLBYAAqlr0EsgtENNn-yMxyME")

	await sleep(0.5)
	global number
	number = number + 1


@Client.on_message(filters.command("zelglaz", ".") & filters.me)
async def zelglaz(client, message):
	await client.send_message(message.chat.id, f'''
	<b>Глаз, зеленый глаз, влюбился в тебя так легко</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Носишь оверсайз, встретиться было суждено</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Не спрошу за прайс, ведь это дело не мое</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты будто Пеннивайз, но мнение о себе wow</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Зеленый глаз, влюбился в тебя так легко</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Носишь оверсайз, встретиться было суждено</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Не спрошу за прайс, ведь это дело не мое</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты будто Пеннивайз, но мнение о себе wow</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Строчка горяча — кипяток</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сел ща микро и вые*ал биток</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>У тебя спереди неплохой видок</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты не ровный пацан, ты кидок</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Она красивая, будто модель</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Мне повезло быть вместе с ней</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я не видел девушек горячей</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Такую жизнь мог увидеть во сне (Только там)</b>
	''')
	await client.send_message(message.chat.id, f'''
	<b>Помню, как при встрече сразу же в тебя влюбился</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>С тобою проходили быстро дни и месяца</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Помню из-за ревности сильно на тебя злился</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Но Минин влюбился в твои зеленые глаза</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Зеленый глаз, влюбился в тебя так легко</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Носишь оверсайз, встретиться было суждено</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Не спрошу за прайс, ведь это дело не мое</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты будто Пеннивайз, но мнение о себе wow</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Зеленый глаз, влюбился в тебя так легко</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Носишь оверсайз, встретиться было суждено</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Не спрошу за прайс, ведь это дело не мое</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты будто Пеннивайз, но мнение о себе wow</b>
	''')

	await sleep(5)
	message.edit(f'''
		🍃 author: @tgscriptss''')
	await sleep(5)
	message.delete()

	await sleep(0.5)
	global number
	number = number + 1


@Client.on_message(filters.command("shadowfiend", ".") & filters.me)
async def shadowfiend(client, message):

	await client.send_message(message.chat.id, f'''
	<b>PLVSTIC, ты такой стильный!</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>– shadowraze?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>– Нет, блять, Pavshiy</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>– Mariyaunban?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>– Нет, блять, Prepodobniy, ха-ха-ха</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Коил, коил, коил</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сука, прямо подо мною</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Каждый рэйз наполнен болью</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Кричат души на Стокгольме</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>ZXC и ты покойник</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>В моём лобби ты не воин</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Не рычи, надень намордник</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Реквием, тебе хуёво</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Коил, коил, коил</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сука, прямо подо мною</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Каждый рэйз наполнен болью</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Кричат души на Стокгольме</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>ZXC и ты покойник</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>В моём лобби ты не воин</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Не рычи, надень намордник</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Реквием, тебе хуёво, ха</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Shadow-Shadow Fiend, ха</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Парень без обид</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Твой ugly face уже разбит</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Слышь, ебучий псих, твой playstyle — это стыд, ха</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я, бля, Shadow Fiend, ты — ебучий психокид, ха</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты, блядь, кто такой, а? Сука, чё не нравится?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Трипл рэйз в ебло и твоё эго, блядь, расплавится</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Твоя блядь на пос-пять — она лает и кусается</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я бля perfect player, меня это не касается, сука</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ах-ха-ха, привет, Каспер, помнишь меня?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Как там твой сыночек, безмозглый дегенерат, Стасик,</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>поживает? Никто его ещё не пришиб, как муху ебаную?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>А, броу? Как там твоя мать, шлюха гнилозубая, поживает,</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>тоже, рассказывай</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>До встречи на эпицентре, сын шлюхи</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Коил, коил, коил</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сука, прямо подо мною</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Каждый рэйз наполнен болью</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Кричат души на Стокгольме</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>ZXC и ты покойник</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>В моём лобби ты не воин</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Не рычи, надень намордник</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Реквием, тебе хуёво</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Коил, коил, коил</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Сука, прямо подо мною</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Каждый рэйз наполнен болью</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Кричат души на Стокгольме</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>ZXC и ты покойник</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>В моём лобби ты не воин</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Не рычи, надень намордник</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Реквием, тебе хуёво, ха</b>
	''')
	await client.send_message(message.chat.id, f'''
	<b>Трипл рэйз на шее</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Мне не нужно разрешение, ха</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Убрал тебя с мида, в моём лобби стал мишенью</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Твой Титаник пал, блядь, или сука, потерпел крушение</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты ебучий dead inside интернетных отношений</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Моё лобби ZXC, но я не жду больше минуты</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>В деле топовый SF, мои коилы – терракоты</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Мои коилы — ZXC, мои души — громче всех</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>ZXC — ты отлетаешь от раскаста shadowraze</b>
	''')

	await sleep(0.5)
	global number
	number = number + 1


@Client.on_message(filters.command("astralstep", prefixes=".") & filters.me)
async def astralstep(client, message):
	await client.send_message(message.chat.id, f'''
	<b>Кидаю step, лечу прям вверх</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Мой красный сет убил их всех</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>У них в башке один preset</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я покажу тоннельный свет</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Им не найти меня, я скрылся</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я пропавший в dissimilate</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я не оставлю им и следа</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Из ниоткуда выйду в late</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Разрубаю глефой ноги, я бегу, за спиной Боги (А-а)</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Как на ринге, только в лобби, ты подох, бля (Ха-ха)</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я стреляю — это step, бро, you low</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я быстрее этих lame'ов, you slow, братан</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я use'аю эти spell'ы — это мой lifesteal</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я sip'ую эти step'ы — это жёсткий стиль</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Долбоёб назвал НН-ом, я его простил</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я убил их, даже не завейстил сил</b>
	''')
	await client.send_message(message.chat.id, f'''
	<b>Погасил этих псин, курю бензин, I'm steal</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Показал им старый стиль, добил их всех, а кто спросил?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Astral step поразил долбоёбов и терпил</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>У меня сотка гулей, посмотри — ты вновь один</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Вот ты прикинь, челы чё-то там на Дота-рэп гонят, да</b>
	''')
	await sleep(1.5)
	await client.send_message(message.chat.id, f'''
	<b>А я за один квартал лям рублей получил, бля</b>
	''')
	await sleep(1.5)
	await client.send_message(message.chat.id, f'''
	<b>Лимон за Дота-рэп, ха-ха-ха-ха</b>
	''')
	await sleep(1.5)
	await client.send_message(message.chat.id, f'''
	<b>В моих глазах горит квазар</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Иду вперёд, ни шагу назад</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Кидаю step, бегу на старт</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Весь твой профит идёт на спад</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Стреляю метко, как солдат</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Мой step сияет — это факт</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>И я step'ую прямо в такт</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Им не убить меня, so hard</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Кидаю step, лечу прям вверх</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Мой красный сет убил их всех</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>У них в башке один preset</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я покажу тоннельный свет</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Им не найти меня, я скрылся</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я пропавший в dissimilate</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я не оставлю им и следа</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Из ниоткуда выйду в late</b>
	''')
	await client.send_message(message.chat.id, f'''
	<b>Hunter on ghoul, я убил их всех</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Уворот от пуль, у меня есть вес</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Нахуй граммовка, у меня есть весы</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я не злодей, но у меня свои бесы</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Много валюты, имею и песо</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Много энергии, я будто Тесла</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Стреляю так метко, все пули прям в висок, а</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>В моих глазах горит квазар</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Иду вперёд, ни шагу назад</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Кидаю step, бегу на старт</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Весь твой профит идёт на спад</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Стреляю метко, как солдат</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Мой step сияет — это факт</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>И я step'ую прямо в такт</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Им не убить меня, so hard</b>
	''')

@Client.on_message(filters.command("man", ".") & filters.me)
async def zoo(client, message):
	await client.send_message(message.chat.id, f'''
	<b>И я знаю, что такое страдать</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ведь, я ощущал всё это тысячи раз…</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Раз, два, три, я в квартире один на полу</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Считаю до трёх, чтобы слишком быстро не уснуть</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Кто сказал, что человеку нужен человек?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Всё это пиздеж, я уже давно живу в себе</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Раз, два, три, я в квартире один на полу</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Считаю до трёх, чтобы слишком быстро не уснуть</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Кто сказал, что человеку нужен человек?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Всё это пиздеж, я уже давно живу в себе</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Молчит наш чат</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Говорю только с собой, и только по ночам</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>И пока остывал мой чай</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Ты задавала вопросы, я предпочитал молчать</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>О том, что у меня внутри, о том, что у меня болит</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>О том, что я хотел забыть, но так и не забыл, а-а</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>О том, что я хотел забыть, но так и не забыл, а-а</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Я считаю до трёх и мне не хорошо</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Тысячи ра—</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Раз, два, три, я в квартире один на полу</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Считаю до трёх, чтобы слишком быстро не уснуть</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Кто сказал, что человеку нужен человек?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Всё это пиздеж, я уже давно живу в себе</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Раз, два, три, я в квартире один на полу</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Считаю до трёх, чтобы слишком быстро не уснуть</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Кто сказал, что человеку нужен человек?</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Всё это пиздеж, я уже давно живу в себе</b>
	''')
	await sleep(1)
	await client.send_message(message.chat.id, f'''
	<b>Раз, два, три</b>
	''')

	await sleep(5)
	await message.delete()

add_command_help(
	"music",
	[
		[".showdown", "Showdown - Shadowraze"],
		[".versus", "Версус баттл Oxxxymiron'a "],
		[".zoo", "Ебанько - Я ебу собак "],
		[".stars", "Полматери - Ярче звёзд"],
		[".landisi", "Ебанько - Ландыши "],
		[".neverenough", "Never Enought - ZXCursed"],
		[".astralstep", "Shadowraze - Astral step "],
		[".shadowfiend", "Shadowraze - Shadowfiend"],
		[".zelglaz", "Минин - Зелёный глаз"],
		[".kaif", "Konfuz - Кайф ты поймала "],
		[".man", "cold carti - человеку нужен человек"]
	]
)
