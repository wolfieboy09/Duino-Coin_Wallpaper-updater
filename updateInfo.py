print("-= Update Configuration =-")

options = ["Username"]

def listOptions() -> None:
  print("Options:")
  for index, option in enumerate(options):
    print(f"{index}. {option}")

def edit(key: str, value: str) -> None:
  with open("config.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
      


while True:
  inp = input("Enter list number (press Q to quit): ")
  if inp == "1":
    newUsername = input("Enter your Duino-Coin username: ")
    edit("username", newUsername)

exit()
