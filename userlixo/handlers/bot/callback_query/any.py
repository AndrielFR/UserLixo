# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2021 Amano Team

import os

from pyrogram import Client

from userlixo.config import langs


# Getting the language to use
@Client.on_callback_query(group=-2)
async def deflang(c, cq):
    cq._lang = langs.get_language(os.getenv("LANGUAGE"))
