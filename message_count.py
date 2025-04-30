import os
import datetime
os.system('cls' if os.name == 'nt' else 'clear')                                                                         # clearing terminal to begin from scratch
chat = list()
c_reset = "\033[0m"
c_yellow = "\033[93m"
c_red = "\033[1m \033[91m"
c_title = "\033[103m\033[90m\033[1m"
c_danger = "\033[97m\033[101m\033[1m"
                                    # for copy and paste {c_reset} {c_red} {c_title} {c_yellow}
def confirm():                                                                                                           # defining confirmation function
     confirmation = input(f"{c_danger}Are you sure? (y/n): {c_reset}") 
     if confirmation.upper() == "Y":
        return True
     elif confirmation.upper() == "N":
        print(f"{c_title}-------------------------------------CANCELLED-------------------------------------{c_reset}")
        return False
     else:
        print(f"{c_title}-----------------------------------INVALID INPUT-----------------------------------{c_reset}")
        return False
         
while True:
    message = input(f"""-----------------------------------------------------------------------------------
                     {c_yellow}\t MESSAGE MANAGER
                     {c_red}  EXIT {c_reset} to close counter
                     {c_red}  COUNT {c_reset} to count messages so far
                     {c_red}  SEARCH {c_reset} to search inside Log
                     {c_red}  LOG {c_reset} to show previous messages\033[0m
                     {c_red}  CLEAR {c_reset} to delete history\033[0m
                   	 \033[1mEnter new message: {c_reset}""")                                                                  # base message
    time_now = datetime.datetime.now()
    time_now = (time_now.strftime("%H:%M:%S"))                                                                              # actual time for each message    
    if message.upper() == "EXIT":
        if confirm():
            print(f"{c_title}--------------------------------THANKS FOR COMING!--------------------------------{c_reset}")
            break
    elif message.upper() == "CLEAR":                                                                                         # clearing log
        if confirm():
            chat.clear()
            print(f"{c_title}CLEARED{c_reset}")
    elif message.upper() == "COUNT":
        print(f"{c_title}******{len(chat)} MESSAGES SENT SO FAR******{c_reset}")                                             # count message
    elif message.upper() == "LOG":
        if len(chat) == 0:
            print(f"{c_title}================================== CHAT LOG EMPTY =================================={c_reset}")
        else:
            print(f"{c_title}===================================== CHAT LOG ====================================={c_reset}") # show previous messages
            for message in chat:
                print(message)
            print(f"{c_title}===================================================================================={c_reset}")
    elif message.upper() == "SEARCH":                                                                                        #search engine
        search = input("Enter words to search: ")
        search_results = list(filter(lambda results: search.upper() in results.upper(), chat))
        if len(search_results) == 0:
            print(f"{c_title}================================= SEARCH LOG EMPTY ================================{c_reset}")
        else:
            print(f"{c_title}==================================== SEARCH LOG ==================================={c_reset}") 
            for search in search_results:
                print(search)
            print(f"{c_title}===================================================================================={c_reset}")
    elif message.strip():
        chat.append(f"{time_now} - {message}")  # adding message to the log with message time

# I'm satisfied with this practice, I'm going yo do something else