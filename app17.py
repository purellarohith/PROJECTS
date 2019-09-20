command  = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print( "car already sterted")
        else:
            started = True
            print('car started...')
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car stoped...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - quit
        """)
    elif command == "exit":
        print("bye")
        break

    else :
        print("sorry i don't understand")