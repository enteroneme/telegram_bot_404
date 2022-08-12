#from distutils.log import info
import sqlite3
import telebot
import config
from telebot import types



con = sqlite3.connect('users.db', check_same_thread=False)
cursor = con.cursor()


client = telebot.TeleBot(config.config['token'])


cursor.execute(""" CREATE TABLE IF NOT EXISTS PythonTeacher(
    photo BLOB,
    description TEXT
    )""")

con.commit()

cursor.execute(""" CREATE TABLE IF NOT EXISTS WebDesignTeacher(
    photo BLOB,
    description TEXT
    )""")

con.commit()



cursor.execute(""" CREATE TABLE IF NOT EXISTS WebProgramm(
    photo BLOB,
    description TEXT
    )""")

con.commit()


cursor.execute(""" CREATE TABLE IF NOT EXISTS CyberSport(
    photo BLOB,
    description TEXT
    )""")

con.commit()


cursor.execute(""" CREATE TABLE IF NOT EXISTS Photo_and_video(
    photo BLOB,
    description TEXT
    )""")

con.commit()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Rooms(
    id TEXT,
    address TEXT,
    description TEXT
    )""")

con.commit()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Studens(
    name TEXT
    )""")

con.commit()







@client.message_handler(commands = ['info'])
def get_main_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_gaid = types.InlineKeyboardButton('гайд перваша' , callback_data= 'gaid')
    item_material = types.InlineKeyboardButton('учебный материал' , callback_data= 'material')
    item_rooms = types.InlineKeyboardButton('найти кабинет' , callback_data= 'rooms')
    item_was_first = types.InlineKeyboardButton('я тоже был первашом' , callback_data= 'first')
    item_kbty = types.InlineKeyboardButton('мемы кбту' , callback_data= 'kbty')

    markup_inline.add(item_gaid, item_material, item_rooms, item_was_first, item_kbty)
    client.send_message(message.chat.id, 'привет ученик 404 education',
        reply_markup= markup_inline
    )

@client.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'gaid':
        markup_reply_1 = types.ReplyKeyboardMarkup(one_time_keyboard= True, resize_keyboard=True)
        item_text = types.KeyboardButton('text')
        item_video = types.KeyboardButton('video')
        item_back = types.KeyboardButton('вернуться назад')

        markup_reply_1.add(item_text, item_video, item_back)
        client.send_message(call.message.chat.id, 'тут ты можешь почитать гайд и посмотреть видео о 404',
            reply_markup= markup_reply_1
    )



    elif call.data == 'material':
        markup_reply_2 = types.ReplyKeyboardMarkup(one_time_keyboard= True, resize_keyboard=True)
        item_material_lesson = types.KeyboardButton('Материал по предметам')
        item_choose_teacher = types.KeyboardButton('Выбор преподавателя')
        item_back = types.KeyboardButton('вернуться назад')

        markup_reply_2.add(item_material_lesson, item_choose_teacher, item_back)
        client.send_message(call.message.chat.id, 'выбор материала или же учителя',
            reply_markup= markup_reply_2
        )



    elif call.data == 'rooms':
        markup_reply_3 = types.ReplyKeyboardMarkup(one_time_keyboard= True, resize_keyboard=True)
        item_toiled = types.KeyboardButton('туалеты')
        item_find_room = types.KeyboardButton('поиск кабинета')
        item_useful_rooms = types.KeyboardButton('Полезные кабинеты')
        item_back = types.KeyboardButton('вернуться назад')

        markup_reply_3.add( item_toiled,  item_find_room, item_useful_rooms, item_back)
        client.send_message(call.message.chat.id, 'тут ты можешь найти рассположения комнат',
            reply_markup= markup_reply_3
        )



    elif call.data == 'first':
        markup_reply_4 = types.ReplyKeyboardMarkup(one_time_keyboard= True, resize_keyboard=True)
        item_ask_question = types.KeyboardButton('Задать вопрос старшаку')
        item_back = types.KeyboardButton('вернуться назад')
        
        markup_reply_4.add(item_ask_question, item_back)
        client.send_message(call.message.chat.id, 'тебе рандомно будет дан аккаунт старшека',
            reply_markup= markup_reply_4
        )
    


    elif call.data == 'kbty':
        markup_reply_5 = types.ReplyKeyboardMarkup(one_time_keyboard= True, resize_keyboard=True)
        item_memi = types.KeyboardButton('мемы КБТУ')
        item_back = types.KeyboardButton('вернуться назад')
        
        markup_reply_5.add(item_memi, item_back)
        client.send_message(call.message.chat.id, 'бооооооот',
            reply_markup= markup_reply_5
        )




    if call.data == 'python':
        for value in cursor.execute("SELECT * FROM PythonTeacher"):
            client.send_photo(call.message.chat.id, value[0], caption=value[1])
            

    elif call.data == 'web design':
        for value in cursor.execute("SELECT * FROM WebDesignTeacher"):
            client.send_photo(call.message.chat.id, value[0], caption=value[1])


    elif call.data == 'web programming':
        for value in cursor.execute("SELECT * FROM WebProgramm"):
            client.send_photo(call.message.chat.id, value[0], caption=value[1])

    elif call.data == 'кибер спорт':
        for value in cursor.execute("SELECT * FROM CyberSport"):
            client.send_photo(call.message.chat.id, value[0], caption=value[1])


    elif call.data == 'фото и видео':
        for value in cursor.execute("SELECT * FROM Photo_and_video"):
            client.send_photo(call.message.chat.id, value[0], caption=value[1])


    if call.data == 'random student':
        query = """SELECT * FROM Studens ORDER BY RANDOM() LIMIT 1 """
        arr = [str(i) for i in cursor.execute(query).fetchone()]

        s = " ".join(arr)
        client.send_message(call.message.chat.id, s)


    

@client.message_handler(content_types = ['text'])
def get_gaid_block(message):
    if message.text == 'text':
        client.send_message(message.chat.id, 'тут будет текст')

    elif message.text == 'video':
        client.send_message(message.chat.id, 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')


    #как-то сделал, с горем по полам

    if message.text == 'вернуться назад':
        client.send_message(message.chat.id, 'выберите предмет')



    if message.text == 'Материал по предметам':
        
        client.send_message(message.chat.id, 'тут будет ссылка на материал')


    elif message.text == 'Выбор преподавателя':
        markup_inline_2 = types.InlineKeyboardMarkup()
        item_python = types.InlineKeyboardButton('python' , callback_data= 'python')
        item_web_design = types.InlineKeyboardButton('web design' , callback_data= 'web design')
        item_web_programm = types.InlineKeyboardButton('web programming' , callback_data= 'web programming')
        item_cyber_sport = types.InlineKeyboardButton('кибер спорт' , callback_data= 'кибер спорт')
        item_photo_video = types.InlineKeyboardButton('фото и видео' , callback_data= 'фото и видео')

        markup_inline_2.add(item_python,item_web_design, item_web_programm, item_cyber_sport, item_photo_video)
        client.send_message(message.chat.id, 'выберите предмет',
            reply_markup= markup_inline_2
        )



    if message.text == 'туалеты':
        client.send_message(message.chat.id, 'мне скинут текст с туалет, эта часть готова к работе',)
    



#осталось сделать только input
    elif message.text == 'поиск кабинета':
        client.send_message(message.chat.id, 'введите номер кабинета',)
        
        
        query = f"""SELECT * from Rooms
        WHERE id like(id)"""
        arr = [str(i) for i in cursor.execute(query).fetchone()]

        s = " ".join(arr)
        client.send_message(message.chat.id, s)


                
        


    elif message.text == 'Полезные кабинеты':
        for value in cursor.execute("SELECT * FROM Rooms"):
            client.send_message(message.chat.id, value[1])
            client.send_message(message.chat.id, value[2])
        


    if message.text == 'Задать вопрос старшаку':
        markup_inline_3 = types.InlineKeyboardMarkup()
        item_random = types.InlineKeyboardButton('рандом' , callback_data= 'random student')

        markup_inline_3.add(item_random)
        client.send_message(message.chat.id, 'рандон учеников',
            reply_markup= markup_inline_3
        )



    if message.text == 'мемы КБТУ':
        markup_inline_3 = types.InlineKeyboardMarkup()
        item_channel = types.InlineKeyboardButton('перейти на канал ➡️' , callback_data= 'channel')

        markup_inline_3.add(item_channel)
        client.send_message(message.chat.id, 'перейти на канал',
            reply_markup= markup_inline_3
        )






client.polling(none_stop = True, interval = 0)