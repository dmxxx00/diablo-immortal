import discord
import feedparser
import asyncio
import os

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
FEED_URL = 'https://news.blizzard.com/en-us/rss'

intents = discord.Intents.default()
client = discord.Client(intents=intents)

last_entry_link = None

async def check_feed():
    global last_entry_link
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)

    while not client.is_closed():
        feed = feedparser.parse(FEED_URL)
        if feed.entries:
            entry = feed.entries[0]
            if 'Diablo Immortal' in entry.title and entry.link != last_entry_link:
                last_entry_link = entry.link
                await channel.send(f"🔥 Noutate Diablo Immortal: **{entry.title}**\n🔗 {entry.link}")
        await asyncio.sleep(3600)  # verifică o dată pe oră

@client.event
async def on_ready():
    print(f'Botul este conectat ca {client.user}')

client.loop.create_task(check_feed())
client.run(TOKEN)
