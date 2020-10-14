# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from SaitamaRobot import telethn


@telethn.on(events.NewMessage(pattern="/tagall"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Hello"
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


@telethn.on(events.NewMessage(pattern="/administrator"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Administrators : "
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

__help__ = """
*Song Download*
 x /song <text>: Downloads and Uploads The song!
*Youtube Search*
 x /yt <text>: perform a youtube search
 
 *Youtube Downloader*
 x /ytaudio <link> : Gives you direct mp3 audio 
 x /ytvideo <link>: Gives you direct mp4 video 
*NOTE*
Bot Downloads to server then uploads to the telegram . so have patience !
Only group admins will able to use this command , others simply can use in bot's pm[!](https://telegra.ph/file/74b9a1bf04e93fc774d7b.png)
"""
__mod_name__ = "tagall"
