import os
import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop

bot =  telepot.aio.Bot( os.environ["bot_token"] )

async def handle( msg ):
    flance = telepot.flance( msg )
    if flance[0] != "chat":
        return
    if flance[1][0] == "new_chat_member":
        name = msg["new_chat_member"]["first_name"]
        chat = msg["chat"]["id"]
        await bot.sendMessage( chat,
        """        Hello recruit! \n
        I see in here that your name is """ + name + """, is it correct?\n
        Well, let's get started. I need you to send me your recruitment code, it's the 6 leter code (XXX XXX) atop you /me tab.\n
        You can just paste it in here or forward you /me tab to this chat, either is fine.\n
        After that, I want you to take a look at our recruit guide: http://telegra.ph/Highnest-castle-guide-12-15\n
        Everything you need to know should be there, but if any doubts shall fill this little helm of yours, just let us know.\n
        Now fly high, recruit!""" )

loop = asyncio.get_event_loop()
loop.create_task( MessageLoop( bot, handle ).run_forever() )
loop.run_forever()
