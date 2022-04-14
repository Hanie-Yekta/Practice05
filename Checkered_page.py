def Checkered_page(s,v):
    # chaap be surat shatranji
    for j in range(s):
        if j % 2 == 0:
            for i in range(v):
                if i % 2 == 0:
                    print("🟩", end="")
                else:
                    print("🟨", end="")
            print()

        else:
            for i in range(v):
                if i % 2 == 0:
                    print("🟨", end="")
                else:
                    print("🟩", end="")
            print()


# dayaft aabaad safhe
print("Enter the dimensions of the array.")
n = int(input("row:"))
m = int(input("col:"))

Checkered_page(n,m)