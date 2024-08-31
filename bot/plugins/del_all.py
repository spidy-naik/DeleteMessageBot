#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import filters
from pyrogram.errors import (
    ChatAdminRequired
)
from pyrogram.raw.functions.channels import DeleteHistory
from pyrogram.types import Message
from bot import (
    ADMINS,
    AUTH_GROUP,
    BEGINNING_DEL_ALL_MESSAGE,
    DEL_ALL_COMMAND,
)
from bot.bot import Bot
from bot.helpers.custom_filter import allowed_chat_filter
from bot.helpers.get_messages import get_messages


@Bot.on_message( filters.command(DEL_ALL_COMMAND) & allowed_chat_filter &  filters.chat(AUTH_GROUP) &  filters.user(ADMINS) )
async def del_all_command_fn(client: Bot, message: Message):
    try:
        status_message = await message.reply_text(
            BEGINNING_DEL_ALL_MESSAGE
        )
    except ChatAdminRequired:
        status_message = None

    await get_messages(
        client.USER,
        message.chat.id,
        0,
        status_message.id if status_message else message.id,
        []
    )

    if status_message:
        await message.delete()
        await status_message.delete()
