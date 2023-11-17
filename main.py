import os
try:
	import discord
	from discord.ext import commands
	from colorama import init, Fore;init()
	import requests
except:
	os.system('pip install -U discord.py-self colorama requests')
	import discord
	from discord.ext import commands
	from colorama import init, Fore;init()
	import requests
import json
cmd = "mode 90, 45"
with open("config.json", "r", encoding="utf-8-sig") as f:
	config = json.load(f)
Intro=Fore.MAGENTA +"""
    
██████╗..█████╗..█████╗.████████╗  ████████╗.█████╗..█████╗.██╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝  ╚══██╔══╝██╔══██╗██╔══██╗██║
██████╔╝██║..██║██║..██║...██║...  ...██║...██║..██║██║..██║██║
██╔══██╗██║..██║██║..██║...██║...  ...██║...██║..██║██║..██║██║
██║..██║╚█████╔╝╚█████╔╝...██║...  ...██║...╚█████╔╝╚█████╔╝███████╗
╚═╝..╚═╝.╚════╝..╚════╝....╚═╝...  ...╚═╝....╚════╝..╚════╝.╚══════╝
"""+Fore.RED + "SUBNORMAL AND MISSMIRD\n" + Fore.GREEN
clear=lambda: os.system(f'cls && title ROOT TOOL' if os.name == 'nt' else 'clear')
clear()
print(Intro)
pref=config['Prefix']
bot = commands.Bot(command_prefix=pref, case_insensitive=True, self_bot=True)
bot.remove_command('help')
version=0.2
update=''

@bot.event
async def on_connect():
	for filename in os.listdir():
		if filename.endswith('.txt'):
			os.remove(filename)
	print(Fore.MAGENTA + f"Аккаунт: {Fore.YELLOW}{bot.user}{Fore.MAGENTA}\nID: {Fore.YELLOW}{bot.user.id}{Fore.MAGENTA}\nPrefix: {Fore.YELLOW}{pref}")
	if float(requests.get('https://roottool.tb.ru/mainmenu').text)>version:
		global update
		update=f':warning: Приятного использования {pref}bot**\n**'
		print(f'{Fore.CYAN}**ROOT** {pref}bot{Fore.RED}\n')
		return
	print(Fore.RED)
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		print(Fore.RED + f"[ERROR] Недостаточно аргументов!")
	elif isinstance(error, commands.CommandNotFound):
		print(Fore.RED + f"[ERROR] Данной команды не существует!")
	elif isinstance(error, commands.BadArgument):
		print(Fore.RED + f"[ERROR] Неправильный аргумент!")
	else:
		print(Fore.RED + f"[ERROR] {error}")

@bot.command(aliases=['хелп', 'помощь'])
async def help(ctx, cat=None):
	if cat==None:
		await ctx.message.edit(content=f'>>> **ROOT TOOL\n{update}\n<{pref}help Tools> - Полезные команды\n<{pref}help Info> - Команды для получения информации\n<{pref}help Fun> - Развлекательные команды\n<{pref}help Nuke> - Команды краша\n\n{pref}bot - Получение ссылки на сайт селф бота**')
		return
	cat=cat.lower()
	if cat=='tools':
		await ctx.message.edit(content=f'>>> **ROOT TOOL\n{update}\n<{pref}status> [Тип статуса] [Текст] - Изменяет статус\n<{pref}purge> [Количество] - Удаляет ваши сообщения\n<{pref}masspin> [Количество] - спам закреплением сообщений\n<{pref}spam> [Количество] [Текст] - Спам сообщениями\n<{pref}lag> [Тип лагов] [Количество] - Делает очень сильные лаги в канале\n<{pref}messages> [Количество] - Сохраняет сообщения в файл**')
	if cat=='info':
		await ctx.message.edit(content=f'>>> **ROOT TOOL\n{update}\n<{pref}server> - Информация о сервере\n<{pref}user> [ID/Пинг] - Информация об аккаунте**')
	if cat=='fun':
		await ctx.message.edit(content=f'>>> **ROOT TOOL\n{update}\n<{pref}troll> [ID/Пинг] - Удаление всех сообщений пользователя\n<{pref}untroll> - Выключение команды troll\n<{pref}reaction> [Эмодзи] [Количество] - Спамит реакциями\n<{pref}trollreaction> [ID/Пинг] [Эмодзи] - Ставка реакций на все сообщения пользователя\n<{pref}trollrepeat> [ID/Пинг] - Повторение всех сообщений пользователя**')
	if cat=='nuke':
		await ctx.message.edit(content=f'>>> **ROOT TOOL\n{update}\n<{pref}nuke> - Уничтожение сервера\n<{pref}spamchannels> [Имя] - Спам каналами\n<{pref}spamroles> [Имя] - Спам ролями\n<{pref}spamwebhooks> [Сообщение] - Спам вебхуками\n<{pref}deleteall> - Удаление всего\n\n<{pref}deletechannels> - Удаляет каналы\n<{pref}deleteroles> - Удаляет роли\n<{pref}deleteemojis> - Удаляет эмодзи**')
@bot.command(name='bot', aliases=['selfbot', 'бот', 'селфбот'])
async def __bot(ctx):
	await ctx.message.edit(content='> **ROOT TOOL**\n\n**Ссылка: https://root-tool.tb.ru/mainmenu**')
for filename in os.listdir("./modules"):
	if filename.endswith(".py"):
		bot.load_extension(f"modules.{filename[:-3]}")
try: bot.run(config["Token"])
except:
	while True:
		input("Инвалид токен!")