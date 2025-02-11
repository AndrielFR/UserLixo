# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2021 Amano Team

from pyrogram import Client, filters

from userlixo.handlers.bot.restart import on_restart_u


@Client.on_message(filters.sudoers & filters.su_cmd("restart"))
async def on_restart(c, m):
    await on_restart_u(c, m)
