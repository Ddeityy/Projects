import os
import threading
import discord
import asyncio
from dotenv import load_dotenv
from datetime import datetime
from discord.ext import tasks
from init_func import get_names, get_scroffi, get_scrim_time, get_maps, get_pregame, get_enemy

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  

bot = discord.Client()

@tasks.loop(minutes=1) #20 Scrim/Official                
async def update_20():
    threading.Timer(60, update_20).start()
    channel = await bot.fetch_channel('569944018482364438')
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    pregame = get_pregame()
    if current_time == "20:00" and pregame == None:
        scrim_time = get_scrim_time()
        if scrim_time != None:
            roster = get_names()
            scroffi = get_scroffi()
            scrim_time = get_scrim_time()
            maps = get_maps()
            enemy = get_enemy()
            await channel.send(f"@everyone\nWe have {scroffi} at {scrim_time} against {enemy}.\nWe're playing {maps}.\n{roster}")
            print(f"20:  {scroffi} at {scrim_time} against {enemy}.\nWe're playing {maps}.\n{roster}")
            await asyncio.sleep(360)
        else:
            pass
    
@tasks.loop(minutes=1) # 21 Scrim/Official             
async def update_21():
    threading.Timer(60, update_21).start()
    channel = await bot.fetch_channel('569944018482364438')
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    pregame = get_pregame()
    if current_time == "21:00" and pregame == None:
        scrim_time = get_scrim_time()
        if scrim_time == None:
            pass
        else:
            roster = get_names()
            scroffi = get_scroffi()
            maps = get_maps()
            enemy = get_enemy()
            await channel.send(f"@everyone\nWe have {scroffi} today at {scrim_time} against {enemy}.\nWe're playing {maps}.\n{roster}")
            print(f"21:  {scroffi} at {scrim_time} against {enemy}.\nWe're playing {maps}.\n{roster}")
            await asyncio.sleep(360)
            
@tasks.loop(minutes=1) #Scrim + Official                 
async def update_scroffi(): 
    threading.Timer(60, update_scroffi).start()
    channel = await bot.fetch_channel('569944018482364438')
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    pregame = get_pregame()                  
    if current_time == "20:00" and pregame != None:
        scrim_time = get_scrim_time()
        roster = get_names()
        scroffi = get_scroffi()
        scrim_time = get_scrim_time()
        maps = get_maps()
        enemy = get_enemy()
        await channel.send(f"@everyone\nWe have a pregame/maptalk at {pregame}\n{scroffi} at {scrim_time} against {enemy}.\nWe're playing {maps}.\n{roster}")
        print(f"20+21:  Pregame/maptalk at {pregame}\n{scroffi} at {scrim_time} against {enemy}.\nWe're playing {maps}.\n{roster}")
        await asyncio.sleep(360)

         
@tasks.loop(minutes=1) #Timer            
async def update_timer():
    threading.Timer(60, update_scroffi).start()
    channel = await bot.fetch_channel('569944018482364438')
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)   

update_timer.start()   
update_20.start()
update_scroffi.start()
update_21.start()

             
bot.run(TOKEN, reconnect=True)

     
        
        
    




