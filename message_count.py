chat = list()
while True:
    message = input("""MESSAGE COUNTER
                     EXIT to close counter
                     COUNT to count messages so far
                     LOG to show previous messages
                    enter new message: """)
    if message.upper() == "EXIT":
        print("THANKS FOR COMING!")
        break
    elif message.upper() == "COUNT":
        print(F"******{len(chat)} MESSAGES SENT SO FAR******")
    elif message.upper() == "LOG":
        print("==== CHAT LOG ====")
        for message in chat:
            print(message)
    else:
        chat.append(message)