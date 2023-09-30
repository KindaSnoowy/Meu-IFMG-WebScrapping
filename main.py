import threading
from config import *
from discord.discordapi import discordhear
from web.webhear import webhear

print("turning on discordhear...")
thread = threading.Thread(target=discordhear)
thread.start()

print("turning on webhear...")
thread = threading.Thread(target=webhear, args=(tagsdisc, disciplinas,))
thread.start()