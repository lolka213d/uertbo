# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import sqlite3
from asyncio import sleep
import os

from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType

from .help import add_command_help


def convert_to_binary_data(filename):
	# Преобразование данных в двоичный формат
	with open(filename, 'rb') as file:
		blob_data = file.read()
	return blob_data

def write_to_file(data, filename):
    # Преобразование двоичных данных в нужный формат
	with open(filename, 'wb') as file:
		file.write(data)

class pictures_():
	def __init__(self):
		self.conn = sqlite3.connect(r'userbot/base/databases/pictures.db')
		self.cur = self.conn.cursor()

		self.cur.execute("""CREATE TABLE IF NOT EXISTS pictures(
			id INT,
   			desc TEXT,
	  		photo BLOB,
			format TEXT);
		""")
		self.conn.commit()

	def get_format(self, id_):
		self.cur.execute("SELECT format FROM pictures WHERE id = ?", id_)
		format_ = self.cur.fetchone()

		return format_[0]

	def get_all_desc(self):
		self.cur.execute("SELECT id, desc FROM pictures")
		rows = self.cur.fetchall()

		return rows

	def get_photo(self, id_):
		self.cur.execute("SELECT photo FROM pictures WHERE id=?", (id_,))
		row = self.cur.fetchone()
		return row[0]
	
	def get_id(self):
		id_ = self.cur.execute("SELECT max(id) FROM pictures").fetchone()[0]
		if id_ is None:
			return 1
		else:
			return int(id_) + 1

	def add_photo(self, id, desc, filename, format_):
		photo = convert_to_binary_data(filename)
		self.cur.execute("INSERT INTO pictures (id, desc, photo, format) VALUES (?, ?, ?, ?)", (id, desc, photo, format_))
		self.conn.commit()


@Client.on_message(filters.command("addpic", ".") & filters.me)
async def add_picture(client, message):
	print(message.reply_to_message.animation)
	desc = ' '.join(message.command[1:])

	if desc == "":
		await message.edit(
			f"🖼️ `Pictures`: \n"
			f"└ <i>Нет описания для картинки, или сообщение не является ответом на картинку.</i>\n\n"
		)

	elif message.reply_to_message.animation != None:
		pictures = pictures_()

		id_ = pictures.get_id()
		filename = f"{message.reply_to_message.animation.file_id}.gif"
		await client.download_media(message.reply_to_message.animation.file_id, filename)

		pictures.add_photo(id_, desc, f"userbot/downloads/{filename}", ".gif")

		if os.path.isfile(f"userbot/downloads/{filename}"):
			os.remove(f"userbot/downloads/{filename}")

			try: os.rmdir("userbot/downloads")
			except: pass

		await message.edit(
			f"🖼️ `Pictures`: \n"
			f"└ <i>Гифка добавленна!</i>\n\n"
		)

	elif message.reply_to_message.photo:
		pictures = pictures_()

		id_ = pictures.get_id()
		filename = f"{message.reply_to_message.photo.file_id}.jpg"
		await client.download_media(message.reply_to_message.photo.file_id, filename)

		pictures.add_photo(id_, desc, f"userbot/downloads/{filename}", ".jpg")

		if os.path.isfile(f"userbot/downloads/{filename}"):
			os.remove(f"userbot/downloads/{filename}")

			try: os.rmdir("userbot/downloads")
			except: pass

		await message.edit(
			f"🖼️ `Pictures`: \n"
			f"└ <i>Изображение добавленно!</i>\n\n"
		)
	
	else:
		await message.edit(
			f"🖼️ `Pictures`: \n"
			f"└ <i>Нет описания для картинки, или сообщение не является ответом на картинку.</i>\n\n"
		)
	
	await sleep(5)
	await message.delete()

@Client.on_message(filters.command("allpic", ".") & filters.me)
async def all_picture(client, message):
	pic = pictures_()

	text = (
		f"🖼️ `Pictures`: \n"
		f"└ <i>Список сохранённых картинок:</i>\n\n"
	)
	for x in pic.get_all_desc():
		text += (
			f"📄**Номер**: `{x[0]}`\n"
			f"└ <i>{x[1]}</i>\n"
		)
		await message.edit(text)

	await sleep(10)
	await message.delete()


@Client.on_message(filters.command("sendpic", ".") & filters.me)
async def send_pic(client, message):
	try:
		id_ = ' '.join(message.command[1:])
		pic = pictures_()
		write_to_file(pic.get_photo(id_), f"{id_}{pic.get_format(id_)}")

		await message.delete()

		if pic.get_format(id_) == ".gif":
			await message.reply_animation(f'{id_}{pic.get_format(id_)}')
			os.remove(f'{id_}{pic.get_format(id_)}')
			try: os.rmdir("userbot/downloads")
			except: pass
			
		else:
			await message.reply_photo(f'{id_}{pic.get_format(id_)}')
			os.remove(f'{id_}{pic.get_format(id_)}')
			try: os.rmdir("userbot/downloads")
			except: pass

	except Exception as e:
		await message.edit(
			f"🖼️ `Pictures`: \n"
			f"└ <i>Изображений нет для отправки</i>\n\n"
		)

add_command_help(
	"pictures",
	[
		[".addpic [Описание]", "Сохранить изображение(Использывать ответом на сообщение)"],
		[".sendpic [Номер]", "Отправить сохранённое изображенние"],
		[".allpic", "Список всех сохранёных изображений"]
	]
)