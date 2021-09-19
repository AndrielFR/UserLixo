import os

from pyrogram import Client, filters

from userlixo.config import langs


# Getting the language to use
@Client.on_message(group=-2)
async def deflang(c, m):
    m._lang = langs.get_language(os.getenv("LANGUAGE"))


# Define what updates to reject
@Client.on_message(filters.edited)
async def reject(c, m):
    m.stop_propagation()
