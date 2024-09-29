n = int(input().strip())

phoneBook = {}
try:
    for i in range(n):
        name, phone = input().split()

        if phone != "":
            phoneBook[name] = phone

    for i in range(n):
        name = input()

        if phoneBook.get(name) is not None:
            print(f"{name}={phoneBook.get(name)}")
        else:
            print("Not found")
except Exception:
    pass

    # Time Complexity: O(n)
    # Space Complexity: O(n)
