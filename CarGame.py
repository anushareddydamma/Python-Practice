user_input = ""
started = False
while True:
    user_input = input("> ").lower()
    if user_input == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started")
    elif user_input == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Car stopped")
    elif user_input == "help":
        print('''
        start : to start the car
        stop : to stop the car
        quit : to exit the car
                ''')
    elif user_input == "quit":
        break
    else:
        print("Sorry i don't understand your command")

