
rooms = input("Enter status of rooms (0 clean, 1 dirty): ").split()

for i in range(len(rooms)):
    if rooms[i] == "1":
        print("Room", i + 1, "is dirty")
        print("Cleaning room", i + 1)
        rooms[i] = "0"
    else:
        print("Room", i + 1, "is clean")

print("All rooms cleaned")
