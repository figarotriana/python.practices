import datetime

chat = list()
while True:
    message = input("""\033[1m -----------------------------------------------------------------------------------
                   \033[0m  \033[93m MESSAGE COUNTER
                     \033[1m \033[91m EXIT \033[0m to close counter
                     \033[1m \033[91m COUNT \033[0m to count messages so far
                     \033[1m \033[91m LOG \033[0m to show previous messages\033[0m
                   	\033[1m Enter new message: \033[0m""")
    Time = datetime.datetime.now()
    Time = (Time.strftime("%H:%M:%S"))  # actual time for each message    
    if message.upper() == "EXIT":
        print("\033[103m\033[90m\033[1mTHANKS FOR COMING!\033[0m")
        break
    elif message.upper() == "COUNT":
        print(F"\033[103m\033[90m\033[1m******{len(chat)} MESSAGES SENT SO FAR******\033[0m")
    elif message.upper() == "LOG":
        print("\033[103m\033[90m\033[1m==== CHAT LOG ====\033[0m")
        for message in chat:
            print(message)
    else:
        chat.append(f"{Time} - {message}")  # adding message to the log with message time
    