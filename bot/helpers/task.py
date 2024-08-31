import asyncio
from bot import AUTO_DELETE_TIME, AUTH_GROUP, DEL_ALL_COMMAND

async def delete_task(USER):
    while AUTO_DELETE_TIME and AUTH_GROUP:
        await asyncio.sleep(AUTO_DELETE_TIME)
        try:
            for group_id in AUTH_GROUP:
                await USER.send_message(group_id, f"/{DEL_ALL_COMMAND}")
        except Exception as e:
            print(e)
