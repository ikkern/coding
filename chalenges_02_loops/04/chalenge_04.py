for num in range(10, 0, -1):  # Countdown from 10 to 1
    print(num)
    user_input = input('Enter "stop" to cancel or press Enter to continue: ').strip().lower()
    if user_input == "stop":
        print("Countdown stopped!")
        break
