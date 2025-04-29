import os
import datetime
os.system('cls' if os.name == 'nt' else 'clear') # cleaning terminal
chat = list()
while True:
    message = input("""\033[1m -----------------------------------------------------------------------------------
                   \033[0m  \033[93m MESSAGE COUNTER
                     \033[1m \033[91m  EXIT \033[0m to close counter
                     \033[1m \033[91m  COUNT \033[0m to count messages so far
                     \033[1m \033[91m  LOG \033[0m to show previous messages\033[0m
                     \033[1m \033[91m  CLEAR \033[0m to delete history\033[0m
                   	 \033[1mEnter new message: \033[0m""") # base message
    Time = datetime.datetime.now()
    Time = (Time.strftime("%H:%M:%S"))  # actual time for each message    
    if message.upper() == "EXIT":
        exit_confirmation = input("\033[103m\033[90m\033[1m Are you sure? (y/n): \033[0m") # Clearing terminal
        if exit_confirmation.upper() == "Y":
            print("\033[103m\033[90m\033[1mTHANKS FOR COMING!\033[0m")
            break
        elif exit_confirmation.lower() == "n":
            print("\033[103m\033[90m\033[1mNOT CLOSED\033[0m")
        else:
            print("\033[103m\033[90m\033[1mINVALID INPUT, ABORTING\033[0m")
    elif message.upper() == "CLEAR":
        clear_confirmation = input("\033[103m\033[90m\033[1m Are you sure? (y/n): \033[0m") # Clearing terminal
        if clear_confirmation.upper() == "Y":
            chat.clear()
            print("\033[103m\033[90m\033[1mCLEARED\033[0m")
        elif clear_confirmation.lower() == "n":
            print("\033[103m\033[90m\033[1mNOT CLEARED\033[0m")
        else:
            print("\033[103m\033[90m\033[1mINVALID INPUT, ABORTING\033[0m")
    elif message.upper() == "COUNT":
        print(F"\033[103m\033[90m\033[1m******{len(chat)} MESSAGES SENT SO FAR******\033[0m") # count message
    elif message.upper() == "LOG":
        if len(chat) == 0:
            print("\033[103m\033[90m\033[1m==== CHAT LOG EMPTY ====\033[0m")
        else:
            print("\033[103m\033[90m\033[1m==== CHAT LOG ====\033[0m") # show previous messages
            for message in chat:
                print(message)
    else:
        chat.append(f"{Time} - {message}")  # adding message to the log with message time
    