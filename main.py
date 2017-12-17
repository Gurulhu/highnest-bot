import os
import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

bot =  telepot.aio.Bot( os.environ["bot_token"] )

async def on_chat( msg ):
    flance = telepot.flance( msg )
    if flance[0] != "chat":
        return
    if flance[1][0] == "new_chat_member":
        name = msg["new_chat_member"]["first_name"]
        chat = msg["chat"]["id"]
        await bot.sendMessage( chat,
        """Hello recruit! \n
I see in here that your name is """ + name + """, is it correct?\n
Well, let's get started. I need you to send me your recruitment code, it's the 6 letter code (ABC DEF) at top of your  [🏅Me] tab\n
You can just paste it in here or forward you [🏅Me] tab to this chat, either is fine.\n
After that, I want you to take a look at our recruit guide: http://telegra.ph/Highnest-castle-guide-12-15\n
Everything you need to know should be there, but if any doubts shall fill this little helm of yours, just let us know.\n
Now fly high, recruit!""" )
    elif flance[1][0] == "text":
        chat = msg["chat"]["id"]
        if msg["text"].find("/call") == 0:
            global inline_message
            global count
            global clicked
            keyboard = InlineKeyboardMarkup( inline_keyboard = [ [ InlineKeyboardButton( text="Sir, yes sir!", callback_data="click" ) ] ] )
            inline_message = await bot.sendMessage( chat, "Call to Arms!", reply_markup=keyboard )
            count = 0
            clicked = []


async def on_callback( msg ):
    global inline_message
    global count
    global clicked
    _, from_id, data = telepot.glance(msg, flavor='callback_query')
    if data == "click":
        count = count + 1
        if inline_message:
            msg = telepot.message_identifier( inline_message )
            keyboard = InlineKeyboardMarkup( inline_keyboard = [ [ InlineKeyboardButton( text="Not yet sir!", callback_data="unclick" ) ] ] )
            await bot.editMessageText( msg, "Call to Arms!\n\n" + str( count ) + " soldiers are ready!", reply_markup=keyboard )
    if data == "unclick":
        count = count - 1
        if inline_message:
            msg = telepot.message_identifier( inline_message )
            keyboard = InlineKeyboardMarkup( inline_keyboard = [ [ InlineKeyboardButton( text="Sir, yes sir!", callback_data="click" ) ] ] )
            await bot.editMessageText( msg, "Call to Arms!\n\n" + str( count ) + " soldiers are ready!", reply_markup=keyboard )



loop = asyncio.get_event_loop()
loop.create_task( MessageLoop( bot, { "chat" : on_chat,
                                      "callback_query" : on_callback } ).run_forever() )
loop.run_forever()
