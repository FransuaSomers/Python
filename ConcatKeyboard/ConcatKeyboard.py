hotkeys = []
for i in range(1, 13):
    for j in range(1, 13):
        if i != j:  # eliminate cases where a button combines with itself
            hotkeys.append(str(i) + str(j))

with open("hotkeys.txt", "w") as file:
    for hotkey in hotkeys:
        file.write(hotkey + "\n")
