import os

path = input("Enter directory path: ")

for i, filename in enumerate(os.listdir(path)):
    old = os.path.join(path, filename)
    new = os.path.join(path, f"file_{i}.txt")
    os.rename(old, new)

print("Files renamed successfully.")
