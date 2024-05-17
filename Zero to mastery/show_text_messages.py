def show_text_messages(text_messages_phone, sent_messages):
    while text_messages_phone:
        moved_messages = text_messages_phone.pop()
        sent_messages.append(moved_messages)

def send_messages(sent_messages):
    for message in sent_messages:
        print(message)


text_messages_phone = ['Good morning', 'Good afternoon', 'Good night', 'Good evening', 'Have a nice day', 'Be well',
                       'How are you?', 'What is your']
sent_messages = []

show_text_messages(text_messages_phone[:], sent_messages)
send_messages(sent_messages)

# print(text_messages_phone)
# print(sent_messages)








