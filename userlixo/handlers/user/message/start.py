# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2021 Amano Team

from pyrogram import Client, filters

from userlixo.handlers.bot.start import on_start_u


@Client.on_message(filters.su_cmd("start"))
async def on_start_txt(c, m):
    await on_start_u(c, m)
