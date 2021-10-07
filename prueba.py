import os

path = os.path.join(os.pardir, "images", "player", "walk")
for element in os.scandir(os.pardir):
    print(element)

pass
