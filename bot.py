# bot.py - CIOO NOTIFIER BOT - FULL
from flask import Flask, request
import requests

app = Flask(__name__)

# === ISI DI SINI, CIOO! ===
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1574043020423073862/U8w1JPDc3RzQQRzc0vGS6GVtVc7P0xrZiHwnhAWXmr7b3ITiEQx469PHifVe0Eoi8Y0a"
# Contoh: https://discord.com/api/webhooks/123456/abcdef

GAME_LINK = "https://www.roblox.com/games/107778070777162/Steal-an-Egg"
WA_CHANNEL_ID = "0029Vb9IYpxKGGGLvms1D93K"

def buat_teks(data, platform):
    rarity = data['rarity']
    if rarity == "DIVINE":
        judul = "*📢ANNOUNCEMENT*\n*‼️⚡🔥 DIVINE HAS SPAWNED 🔥⚡‼️*"
    else:
        judul = "*📢ANNOUNCEMENT*\n*‼️🔥 ETERNAL HAS SPAWNED 🔥‼️*"
    
    teks = f"""{judul}

{data['emoji']}Pet : {data['pet']}"""
    if platform == "discord":
        teks += f"\n*⚖️ Pet weight : {data['weight']}*"
        teks += f"\n*Pet price : {data['price']}*"
    teks += f"""
*📍 Area : {data['area']}*
*🏃 Recommend Speed : {data['speed']}*

*🎮 JOIN GAME:*
*{GAME_LINK}*

_*🔥 Buruan join game & steal sebelum keduluan orang lain‼️*_
_*👀 Pantengin terus spawn berikutnya ‼️*_

*🚫 Dilarang keras mengcopy apapun disini tanpa izin dari admin.*
> cioo Notifier"""
    return teks

@app.route('/spawn', methods=['POST'])
def spawn():
    data = request.json
    print(f"SPAWN: {data['pet']} - {data['rarity']}")
    
    # 1. KIRIM KE DISCORD
    teks_dc = buat_teks(data, "discord")
    requests.post(DISCORD_WEBHOOK, json={"content": teks_dc})
    
    # 2. KIRIM KE SALURAN WA - LEWAT BOT TIDUR
    teks_wa = buat_teks(data, "wa")
    kirim_ke_wa_channel(teks_wa)
    
    return {"status": "OK - Kirim 2 Sekaligus!"}

def kirim_ke_wa_channel(teks):
    # Bot WA bangun 10 detik, kirim ke Channel, tidur lagi!
    # Sambungin ke Evolution API / Waha di sini!
    print("KIRIM KE WA CHANNEL: " + teks)
    print("Channel ID: " + WA_CHANNEL_ID)

@app.route('/', methods=['GET'])
def home():
    return "CIOO NOTIFIER AKTIF!"

import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
