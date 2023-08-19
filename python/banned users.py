"""banned_users=["eve","fred","gary","helen"]
prompt="\nAdd a player to your team"
prompt+="\nEnter 'quit' when you're done"
players=[]
while True:
    player=input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:
        print(player + "is banned!")
        continue
    else:
        players.append(player)
player("\nYour team:")
for player in players:
    print(player)"""
"""pets=["cat","dog","rabbit","fish"]
print("original format:\n",pets)
while "cat" in pets:
    pets.remove('cat')
print("after changed format:\n",pets)"""
"""for i in range(5):
    for k in range(4-i):
        print("",end="  ")
    for j in range(i+1):
        print("* ",end="")
    print("")
for i in range(5):
    for k in range(i+1):
        print("",end="  ")
    for j in range(4-i):
        print("* ",end="")
    print(" ")"""
"""def build_person(first,last):
    person={"first name":first,"last name":last}
    print(person)
    print(person["first name"])
build_person("jimiki","ponnu")"""
"""alien={'color':'green',"points":5}
print(alien["color"])
print(alien["points"])
power={222:"naruto",333:"kakashi","s":556}
print(power[222])
print(power[333])
print(power["s"])"""
"""def lovers():pass
print(type(lovers))
lovers.devaraj="jeevisha"
print(lovers.__name__)
print(lovers.__dict__)"""
fav_numbers={17:"eric",7:"ever"}
for name,number in fav_numbers.items():
    print(str(name)+" loves a name "+number)


