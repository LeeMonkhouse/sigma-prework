user_list = []
stop_loop = False

print("Input one number at a time to build a list of numbers.")
print("When your list is complete, enter 'stop' to find the min and max.")

while stop_loop == False:
    user_input = input("Enter a number or 'stop' to stop.: ")
    if not user_input == "stop":
        if user_input.lstrip("-").isdigit():
            user_list.append(user_input)
        else:
            print("Not a proper number.")
    else:
        stop_loop = True

print("Your list of numbers is:", user_list)
minmax = [min(user_list), max(user_list)]
print("Min/Max:", minmax)
