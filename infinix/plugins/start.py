
from .. import bot
from telethon import events
import asyncio

@bot.on(events.NewMessage(incoming = True, pattern = "/start"))
async def start(event):
  await event.reply("Hello This is Infinix Bot")



@bot.on(events.NewMessage(incoming = True, pattern = "/get"))
async def start(event):
  a=await event.reply("Hello This is Get command")
  await asyncio.sleep(3)
  await a.edit("this is edited msg")
  
  
@bot.on(events.NewMessage(incoming = True, pattern = "/eval"))
async def start(event):
  await event.reply("Hello This is Eval command")
    