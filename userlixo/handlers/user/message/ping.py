# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2021 Amano Team

from datetime import datetime

from pyrogram import Client, filters


@Client.on_message(filters.su_cmd("ping"))
async def onping(c, m):
    before = datetime.now()
    await m.reply_chat_action("typing")
    after = datetime.now()
    diff_ms = (after - before).microseconds / 1000

    keyb = [[("🏓", "ping")]]
    await m.reply(f"<b>Pong!</b> <code>{diff_ms}</code><code>ms</code>", keyb)
