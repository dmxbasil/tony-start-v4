class script(object):
    START_TXT = """𝑯𝒆𝒍𝒍𝒐 {},
𝑴𝒚 𝒏𝒂𝒎𝒆 𝒊𝒔 <a href=https://t.me/{}>{}</a> 𝑰 𝒄𝒂𝒏 𝒑𝒓𝒐𝒗𝒊𝒅𝒆 𝒎𝒐𝒗𝒊𝒆𝒔 𝒊𝒏 𝒈𝒓𝒐𝒖𝒑, 𝑱𝒖𝒔𝒕 𝒂𝒅𝒅 𝒎𝒆 𝒕𝒐 𝒖𝒓 𝒈𝒓𝒐𝒖𝒑 𝒂𝒔 𝒂𝒅𝒎𝒊𝒏😍"""
    HELP_TXT = """𝑯𝒆𝒚 {}
𝑯𝒆𝒓𝒆 𝒊𝒔 𝒎𝒚 𝒉𝒆𝒍𝒑 𝒄𝒐𝒎𝒎𝒂𝒏𝒅𝒔."""
    ABOUT_TXT = """✯ ᴍʏ ɴᴀᴍᴇ » {}
✯ ᴄʀᴇᴀᴛᴏʀ » <a href=https://t.me/dmx_bots/4>ᴛᴇᴀᴍ ᴅᴍx</a>
✯ ʟɪʙʀᴀʀʏ » <a href=https://docs.pyrogram.org/>ᴘʏʀᴏɢʀᴀᴍ</a>
✯ ʟᴀɴɢᴜᴀɢᴇ » <a href=https://www.python.org/>ᴘʏᴛʜᴏɴ</a>
✯ ᴠᴇʀsɪᴏɴ » 3
✯ ᴅᴀᴛᴀʙᴀsᴇ » <a href=https://www.mongodb.com>ᴍᴏɴɢᴏ ᴅʙ</a>
✯ sᴇʀᴠᴇʀ » <a href=https://signup.heroku.com/login>ʜᴇʀᴏᴋᴜ</a>
✯ ᴍʏ sᴛᴀᴛᴜs » v8.0.2 [ ᴏɴ ʙᴇᴛᴀ ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- 𝒓𝒆𝒂𝒍𝒍𝒚 𝒔𝒐𝒓𝒓𝒚 𝒊𝒂𝒎 𝒏𝒐𝒕 𝒓𝒆𝒂𝒅𝒚 𝒕𝒐 𝒈𝒊𝒗𝒆 𝒎𝒚 𝒔𝒐𝒖𝒄𝒓𝒆
- 𝑮𝒓𝒐𝒖𝒑 - https://dmx_chating_2_0 

<b>ᴄʀᴇᴀᴛᴏʀs »</b>
- <a href=https://t.me/dmx_bots/4>ᴛᴇᴀᴍ ᴅᴍx</a>"""
    MANUELFILTER_TXT = """ʜᴇʟᴘ » <b>Fɪʟᴛᴇʀs</b>

- 𝑴𝒂𝒏𝒖𝒍 𝑭𝒊𝒍𝒕𝒆𝒓 𝒊𝒔 𝒕𝒉𝒆 𝒇𝒆𝒂𝒕𝒖𝒓𝒆 𝒘𝒆𝒓𝒆 𝒖𝒔𝒆𝒓𝒔 𝒄𝒂𝒏 𝒔𝒆𝒕 𝒂𝒖𝒕𝒐 𝒓𝒆𝒑𝒍𝒊𝒆𝒔 𝒇𝒐𝒓 𝒑𝒂𝒓𝒕𝒊𝒄𝒖𝒍𝒂𝒓 𝒌𝒆𝒚𝒘𝒐𝒓𝒅𝒔 𝒂𝒏𝒅 𝒊 𝒘𝒊𝒍𝒍 𝒓𝒆𝒔𝒑𝒐𝒏𝒅 𝒘𝒉𝒆𝒏 𝒆𝒗𝒆𝒓 𝒕𝒉𝒂𝒕 𝒌𝒆𝒚𝒘𝒐𝒓𝒅 𝒇𝒐𝒖𝒏𝒅 𝒊𝒏 𝒚𝒐𝒖𝒓 𝒄𝒉𝒂𝒕..

<b>Nᴏᴛᴇ »</b>
1. 𝑰𝒂𝒎 𝒔𝒉𝒐𝒖𝒍𝒅 𝒃𝒆 𝒂 𝒂𝒅𝒎𝒊𝒏 𝒐𝒇 𝒚𝒐𝒖𝒓 𝒈𝒓𝒐𝒖𝒑
2. 𝑶𝒏𝒍𝒚 𝒂𝒅𝒎𝒊𝒏𝒔 𝒄𝒂𝒏 𝒇𝒊𝒍𝒕𝒆𝒓 𝒊𝒏 𝒎𝒚 𝒑𝒎
3. 𝑪𝒐𝒏𝒏𝒆𝒄𝒕 𝒈𝒓𝒐𝒖𝒑 𝒊𝒏 𝒎𝒚 𝒑𝒎 [𝒖𝒔𝒆 » `/connect - group id]\n𝒇𝒐𝒓 𝒆𝒙𝒂𝒎𝒑𝒍𝒆 `/connect -1234567890`
4. 𝑨𝒍𝒆𝒓𝒕 𝒃𝒖𝒕𝒕𝒐𝒏𝒔 𝒉𝒂𝒗𝒆 𝒍𝒊𝒎𝒊𝒕 64 𝒄𝒉𝒂𝒓𝒂𝒄𝒕𝒆𝒓𝒔

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ »</b>
• /filter ᴏʀ /add - <code>ᴀᴅᴅ ғɪʟᴛᴇʀ ɪɴ ɢʀᴏᴜᴘ</code>
• /filters ᴏʀ /viewfilters - <code>ʟɪsᴛ ᴏғ ᴀʟʟ ғɪʟᴛᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ</code>
• /del - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ғɪʟᴛᴇʀ ɪɴ ɢʀᴏᴜᴘ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴡʜᴏʟᴇ ғɪʟᴛᴇʀs ɪɴ ɢʀᴏᴜᴘ (ᴀᴅᴍɪɴ ᴏɴʟʏ)</code>"""
    BUTTON_TXT = """ʜᴇʟᴘ:» <b>Buttons</b>

- ɪᴀᴍ sᴜᴘᴘᴏʀᴛᴇᴅ ᴏɴ ʙᴏᴛʜ ʙᴜᴛᴛᴏɴs (ᴜʀʟ , ᴀʟᴇʀᴛ)

<b>ɴᴏᴛᴇ »</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴀᴅᴅ ᴀɴʏ ᴛᴇxᴛ , ᴘʜᴏᴛᴏ,ᴇᴛᴄᴄ ᴏɴ ʙᴜᴛᴛᴏɴ ғɪʟᴛᴇʀɪɴɢ.
2. ɪ sᴜᴘᴘᴏʀᴛ ᴏɴ ᴀɴʏ ᴍᴇᴅɪᴀ ᴛʜᴀᴛ ᴛᴇʟᴇɢʀᴀᴍ sᴜᴘᴘᴏʀᴛs
3. ʙᴜᴛᴛᴏɴ sʜᴏᴜʟᴅ ʙᴇ ɪɴ ᴄᴏʀʀᴇᴄᴛ ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ

<b>Uʀʟ ʙᴜᴛᴛᴏɴs »</b>
<code>[Button Text](buttonurl:https://t.me/dmx_chating)</code>

<b>Aʟᴇʀᴛ ʙᴜᴛᴛᴏɴs »</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """ʜᴇʟᴘ » <b>ᴀᴜᴛᴏ ғɪʟᴛᴇʀ</b>

<b>ɴᴏᴛᴇ ᴛᴏ ɪɴᴅᴇx »</b>

ʏᴏᴜ ᴅᴏɴᴛ ᴛʜɪɴᴋ ᴀʙᴏᴜᴛ ɪᴛ ʙᴇᴀᴄᴀᴜsᴇ ɪᴀᴍ ᴀʟʀᴇᴀᴅʏ ᴀᴅᴅᴇᴅ ᴍᴏʀᴇ ᴛʜᴀɴ 2ᴍ ғɪʟᴇs ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ sᴏ ʏᴏᴜ ᴅᴏɴᴛ ɴᴇᴇᴅ ᴛᴏ ᴀᴅᴅ ғɪʟᴇs ᴀɴʏᴍᴏʀᴇ

1. ᴍᴀᴋᴇ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ɪғ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ɪs ᴘʀɪᴠᴀᴛᴇ
2. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴ ᴀɴʏ ᴘʀᴏɴ ᴏʀ ᴀɴʏ ғᴀᴋᴇ ғɪʟᴇs ( ɪғ ɪ ғɪɴᴅ ʟɪᴋᴇ ᴛʜᴀᴛ ɪ ᴡɪʟʟ ʙᴀɴ ʏᴏᴜ ɪɴ ᴍʏ ᴅʙ ᴀɴᴅ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴍʏ ғᴇᴅ)
3. ᴛʜᴇɴ ғᴏʀᴡᴀʀᴅ ᴍᴇ ᴛʜᴇ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴡɪᴛɢ ғᴏʀᴡᴀʀᴅ ᴛᴀɢs (ǫᴜᴏᴛᴇs)
 ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ғɪʟᴇs ᴛᴏ ᴍʏ ᴅʙ"""
    CONNECTION_TXT = """ʜᴇʟᴘ » <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴs</b>

- ᴜsᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ᴘᴍ ɪɴ ɢʀᴏᴜᴘ
- ɪᴛ ʜᴇʟᴘs ᴛᴏ ᴘʀᴇᴠᴇɴᴛ ᴛʜᴇ ᴏᴠᴇʀ sᴘᴀᴍᴍɪɴɢ ᴏғ ɢʀᴏᴜᴘ

<b>ɴᴏᴛᴇ »</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ
3. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ɪᴀᴍ ᴀᴅᴍɪɴ ᴛʜᴇʀᴇ
2. sᴇɴᴅ <code>/connect (ɢʀᴏᴜᴘ ɪᴅ)</code> ᴛᴏ ᴄᴏɴɴᴇᴄᴛ

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ »</b>
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ᴍʏ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪssᴄᴏɴɴᴇᴄᴛ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪsᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴs</code>"""
    EXTRAMOD_TXT = """ʜᴇʟᴘ »<b>ᴇxᴛʀᴀ ᴍᴏᴅs</b>

<b>ɴᴏᴛᴇ »</b>
ᴛʜᴇsᴇ ᴀʀᴇ sᴏᴍᴇ ᴇxᴛʀᴀ ᴍᴏᴅs ᴛʜᴀᴛ ɪ ʜᴀᴠᴇ

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ »</b>
• /id - <code>ɢᴇᴛ ɪᴅ ᴏғ ᴀ sᴘᴇᴄɪғᴇᴅ ᴜsᴇʀ</code>
• /info  - <code>ɢᴇᴛ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ</code>
• /imdb  - <code>ɢᴇᴛ ғɪʟᴍ ɪɴғᴏ ɪɴ ɪᴍᴅʙ sᴏᴜᴄʀᴇ</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏ ɪɴ ᴠᴀʀɪᴏᴜs sᴏᴜᴄʀᴇ </code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>ɴᴏᴛᴇ »</b>
This module only works for my admins

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ »</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
