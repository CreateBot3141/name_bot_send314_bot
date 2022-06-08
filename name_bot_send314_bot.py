

def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import iz_func
    import iz_game
    import iz_main
    import time
    import iz_telegram


    print ('=====================================')

    if message_in == 'Включить':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Система включена','S',message_id)  

        user_id  = '590719271'
        variable = 'Статус бота'
        namebot  = '@send314_bot'
    
        #iz_telegram.save_variable (user_id,namebot,"Статус бота",'ON')
        iz_func.save_variable (user_id,"Статус бота",'ON',namebot)
        status = ""        
   
    if message_in == 'Выключить':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Система выключена','S',message_id)

        user_id  = '590719271'
        variable = 'Статус бота'
        namebot  = '@send314_bot'
    
        #iz_telegram.save_variable (user_id,namebot,"Статус бота",'ON')
        iz_func.save_variable (user_id,"Статус бота",'OFF',namebot)


        #iz_telegram.save_variable (user_id,namebot,"Статус бота",'OFF')
        status = ""

    if message_in == 'TEST':
        answer = iz_telegram.save_tovar (user_id,namebot,"TEST","","","")
        #print ("[+] TEST:",TEST)


    if message_in.find ('TEST') != -1:                    
        status_bota =  iz_func.load_variable (user_id,"Статус бота",namebot)
        message_send = iz_func.send_message (user_id,status_bota,'S',namebot)

    if message_in == '/add_user_grup':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Введите новый каталог для чтения','S',message_id)
        iz_telegram.save_variable (user_id,namebot,"status",'Ввод каталога')

    if status == 'Ввод каталога':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Информация записана','S',message_id)
        iz_telegram.save_variable (user_id,namebot,"status",'')
        db,cursor = iz_func.connect ()
        sql = "INSERT INTO send314_bot_catalog_read (name,status,user_id) VALUES ('{}','','{}')".format (message_in,user_id)
        cursor.execute(sql)
        db.commit()
        lastid = cursor.lastrowid        

    if message_in == '/list_user_grup':
        #message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Список рабочик каталог','S',message_id)
        #iz_telegram.save_variable (user_id,namebot,"status",'Ввод каталога')
        db,cursor = iz_func.connect ()
        message_out,menu = iz_telegram.get_message (user_id,'Список рабочик каталог',namebot)
        message_out = message_out + '\n\n\n'
        #message_out = message_out.replace('%%Процент%%',str(minmin))   
        #message_out = message_out.replace('%%Заявка%%',str(command))
        markup = ''

        sql = "select id,name from send314_bot_catalog_read where 1=1;".format(namebot)
        cursor.execute(sql)
        data = cursor.fetchall()
        for rec in data: 
            id,name = rec.values() 
            message_out = message_out + name + '\n'


        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)        

