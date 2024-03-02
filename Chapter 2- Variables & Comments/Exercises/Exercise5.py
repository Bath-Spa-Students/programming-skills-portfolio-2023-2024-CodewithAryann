# Defining the price of each USB stick and the total budget

usb_stick= 6
total_budget = 50

# Calculating the max number of USB sticks she can buy

num_usb_sticks = total_budget // usb_stick

# Calculating the pounds left after buying USB sticks
pounds_left = total_budget % usb_stick

# Printing the output
print("She can buy", num_usb_sticks, "USB sticks.")
print("She will have", pounds_left, "pounds left.")
