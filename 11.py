connection = True
is_correct = False
is_dot = False
is_at = False
while connection == True:
    while is_correct == False:
        mail_adress = input("Введите адресс электронной почты: ")
        if "@" in mail_adress:
            is_at = True
        else:
            continue
        if "." in mail_adress:
            is_dot = True
        else:
            continue
        if is_at == True and is_dot == True:
            is_correct = True
            print("Ответ записан")