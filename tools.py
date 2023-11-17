from distutils.cmd import Command
import discord
from discord.ext import commands
import random, string
from asyncio import sleep
import time
import os
import sys
import json
import requests
import yaml

class Tools(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@commands.command(aliases=['статус', 'activity', 'активность'])
	async def status(self, ctx, cat='ы', *, name='**ROOT TOOL**'):
		cat=cat.lower()
		game=['play', 'playing', 'играть', 'играет', 'game', 'игра', 'играю']
		watching=['watching', 'watch', 'смотреть', 'смотрит', 'смотрю']
		listening=['listening', 'listen', 'слушает', 'слушать', 'слушаю']
		streaming=['streaming', 'stream', 'стрим', 'стримить', 'стримлю', 'стримит']
		reset=['reset', 'remove', 'none', 'off', 'убрать', 'выключить', 'обычный', 'ресет', 'delete', 'удалить']
		reklama=['reklama', 'реклама']
		if cat in game:
			await self.bot.change_presence(activity=discord.Game(name=name))
		elif cat in watching:
			await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
		elif cat in listening:
			await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=name))
		elif cat in streaming:
			await self.bot.change_presence(activity=discord.Streaming(name=name, url="https://www.youtube.com/watch?v=E9MhX2TG06M&t=1142s"))
		elif cat in reklama:
			await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=name, url="https://www.youtube.com/watch?v=E9MhX2TG06M&t=1142s"))
		elif cat in reset:
			await self.bot.change_presence(activity=None)
		else:
			await ctx.message.edit(content="**ROOT TOOL\n\nДоступные варианты: `Watching`, `Listening`, `Playing`, `Streaming` и `Reset`**")
			return
		await ctx.message.edit(content='**ROOT TOOL\n\n:sparkles: Ваш статус был успешно изменён!**')
	@commands.command(alises=['clean', 'clear', 'очистка', 'очистить'])
	async def purge(self, ctx, amount: int):
		await ctx.message.delete()
		messages=await ctx.channel.history(limit=amount).flatten()
		deleted=0
		for message in messages:
			if message.author.id==self.bot.user.id:
				await message.delete()
				deleted+=1
		await ctx.send(f"**ROOT TOOL\n\n:sparkles: Успешно удалил {deleted} сообщений!**")
	@commands.command(aliases=['spampin', 'pinspam', 'pinmass', 'pin', 'закрепить'])
	async def masspin(self, ctx, amount: int=15):
		await ctx.message.delete()
		messages=await ctx.channel.history(limit=amount).flatten()
		pinned=0
		for message in messages:
			try: await message.pin()
			except: pass
			pinned+=1
		await ctx.send(f"**ROOT TOOL\n\n:sparkles: Успешно закрепил {pinned} сообщений!**")
	@commands.command(aliases=['спам', 'flood', 'флуд'])
	async def spam(self, ctx, amount: int, *, text):
		await ctx.message.delete()
		for i in range(amount):
			await ctx.send(f'{text} ||{"".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))}||')
		await ctx.send(f"")
	@commands.command(aliases=['copy', 'сообщения', 'сохранить'])
	async def messages(self, ctx, amount: int=30):
		await ctx.message.delete()
		messages=await ctx.channel.history(limit=amount).flatten()
		messages.reverse()
		saved=0
		with open(f'messages_{ctx.channel.id}.txt', 'w', encoding='utf-8') as f:
			for message in messages:
				f.write(f'[{message.author}]: {message.content}\n')
				saved+=1
		await ctx.send(f"**ROOT TOOL**\n\n``` Успешно сохранил {saved} сообщений!```", file=discord.File(f'messages_{ctx.channel.id}.txt'))
@commands.command(name = "embed")
async def embed(ctx):
  if Command == "embeds":
    embed = requests.post("http://embd.tk/api/createEmbed", json = {
      "title": f"Discord SelfBot Example Help",
      "description": f"""
Command prefix is "g".
 help - shows this text
 play (text) - set Playing status
 stream (text) - set Streaming status
 listen (text) - set Listening to status
 watch (text) - set Watching status
 compet (text) - set Competing status
 type (seconds) - type in a channel N seconds
 status (status) - set provided status (online, idle, dnd, offline)
kill - turn off the bot
Made by SUBNORMAL TEST
""",
      "color": "FF0000",
      "image_url": None
    }).text
    await ctx.send(str(json.loads(embed)['embed']))
  elif Command == "normal":
    await ctx.send(f"""
Discord SelfBot example help;
Command prefix is "".
```
help - shows this text
play (text) - set Playing status
stream (text) - set Streaming status
listen (text) - set Listening to status
watch (text) - set Watching status
compet (text) - set Competing status
type (seconds) - type in a channel N seconds
status (status) - set provided status (online, idle, dnd, offline)
kill - turn off the bot
```
Made by SUBNORMAL TEST
""")

def setup(bot):
	bot.add_cog(Tools(bot))
