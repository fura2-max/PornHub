"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 12)

    input_str = event.pattern_match.group(1)

    if input_str == "baalaji":

        await event.edit(input_str)

        animation_chars = [
        
            "`Your bot is running\n\nTelethon version: 1.9.0\Python: 3.7.3\nUser: @r4v4n4\nDatabase Status: Databases functioning normally!`",
            "`Connecting To github.com...`",
            "`Deleting Balaji Repo....`",
            "`Forking Uniborg... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Forking Uniborg... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Forking Uniborg... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Forking Uniborg... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Forking Uniborg... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Forking Uniborg... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Forking Uniborg... 84%\n█████████████████████▒▒▒▒ `",
            "`Forking Uniborg... 100%\n█████████████████████████\nTask Completed... `",
            "`Forking Completed\n\n@UniBorg ( Custom Built By @r4v4n4 ) \nVerified Account: ✅\nOfficial Website: https://ravanaisdrunk.site.live\n\nPython 3.6.8 (default, Jan 29 2019, 19:35:16)\n[GCC 7.3.0]\nTelethon 1.8.0\n\nCustom Built Fork: https://github.com/ravana69/UniBorg`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
