variants = ('.com', '.ru', '.net')


def send_email(message: str, recipient: str, *, sender='university.help@gmail.com'):
    global variants
    if '@' not in recipient and sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if recipient.endswith(variants) and sender.endswith(variants) == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com' and recipient.endswith(variants) and sender.endswith(variants) == True:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif recipient.endswith(variants) and sender.endswith(variants) == True:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
