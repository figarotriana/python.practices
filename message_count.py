import datetime

chat = list()
while True:
    message = input("""vvvvv
                    MESSAGE COUNTER
                     EXIT to close counter
                     COUNT to count messages so far
                     LOG to show previous messages
                    enter new message: """)
    Time = datetime.datetime.now()
    Time = (Time.strftime("%H:%M"))  # actual time for each message    
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
        chat.append(f"{Time} - {message}")  # adding message to the log with message time
        