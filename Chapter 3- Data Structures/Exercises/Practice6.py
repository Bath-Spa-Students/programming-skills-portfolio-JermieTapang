guest =  ['Vince', 'Cassy', 'Tydus']
names = guest[0].title()
print (names + " Would you like to go to dinner with me?")

names = guest[1].title()
print (names + " Would you like to go to dinner with me?")

names = guest[2].title()
print (names + " Would you like to go to dinner with me?")

name = guest[1].title()
print ("\nSorry, " + name + " I'm not available right now.")

del(guest[1])
guest.insert(1, 'Saya')

name =  guest[0].title()
print ("\n" + name + " Would you like to go to dinner with me?")

names = guest[1].title()
print (names + " Would you like to go to dinner with me?")

names = guest[2].title()
print (names + " Would you like to go to dinner with me?")

print ("\n We got extra seats!")
guest.insert(0, 'Sean')
guest.insert(2, 'Jiben')
guest.append('Zhep')

names = guest[0].title()
print (names + " Would you like to go to dinner with me?")

names = guest[1].title()
print (names + " Would you like to go to dinner with me?")

names = guest[2].title()
print (names + " Would you like to go to dinner with me?")

names = guest[3].title()
print (names + " Would you like to go to dinner with me?")

names = guest[4].title()
print (names + " Would you like to go to dinner with me?")

names = guest[5].title()
print (names + " Would you like to go to dinner with me?")

print ("\n Forgive us, but we can only invite two people to dinner.")

name = guest.pop()
print ("Sorry, " + name.title() + "There is no seat left")

name = guest.pop()
print ("Sorry, " + name.title() + "There is no seat left")

name = guest.pop()
print ("Sorry, " + name.title() + "There is no seat left")

name = guest.pop()
print ("Sorry, " + name.title() + "There is no seat left")  

names = guest[0].title()
print (names + " Would you like to go to dinner with me?")

names = guest[1].title()
print (names + " Would you like to go to dinner with me?")

del(guest[0])
del(guest[0])

print (guest)