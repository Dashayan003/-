def send_email(message, recipient, *, sender="university.help@gmail.com"):
    email_domains = [".com", ".ru", ".net"]
    if "@" not in recipient or not (recipient.endswith(domain) for domain in email_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
