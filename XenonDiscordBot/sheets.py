import os
import threading
import discord
import asyncio
from dotenv import load_dotenv
from datetime import datetime
from discord.ext import commands, tasks
from init_func import get_names, get_scroffi, get_scrim_time, get_maps, get_pregame

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  

bot = discord.Client()
   
@tasks.loop(seconds=1)                
async def update():
    channel = await bot.fetch_channel('958745386825170974')
    threading.Timer(60, update).start()
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    pregame = get_pregame()
    if pregame != None:
        if current_time == "20:00":
            pregame = get_pregame()
            scrim_time = get_scrim_time()
            if scrim_time == None:
                pass
            else:
                if pregame == None:
                    roster = get_names()
                    scroffi = get_scroffi()
                    maps = get_maps()
                    await channel.send(f"@everyone\nWe have {scroffi} today at {scrim_time}.\nWe're playing {maps}.\n{roster}")
                    await asyncio.sleep(60)
                else:
                    roster = get_names()
                    scroffi = get_scroffi()
                    scrim_time = get_scrim_time()
                    maps = get_maps()
                    await channel.send(f"@everyone\nWe have a pregame/maptalk at {pregame}\n{scroffi} at {scrim_time}.\nWe're playing {maps}.\n{roster}")  
                    await asyncio.sleep(60)
    else:
        if current_time == "21:00":
            pregame = get_pregame()
            scrim_time = get_scrim_time()
            if scrim_time == None:
                pass
            else:
                if pregame == None:
                    roster = get_names()
                    scroffi = get_scroffi()
                    maps = get_maps()
                    await channel.send(f"@everyone\nWe have {scroffi} today at {scrim_time}.\nWe're playing {maps}.\n{roster}")
                    await asyncio.sleep(60)
                else:
                    roster = get_names()
                    scroffi = get_scroffi()
                    scrim_time = get_scrim_time()
                    maps = get_maps()
                    await channel.send(f"@everyone\nWe have a pregame/maptalk at {pregame}\n{scroffi} at {scrim_time}.\nWe're playing {maps}.\n{roster}")  
                    await asyncio.sleep(60)
    print(current_time)
    
update.start() 
 
                
bot.run(TOKEN)
        
        
        
    




