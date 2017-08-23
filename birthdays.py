birthdays = {
    'alice':'apr 1',
    'bob':'dec 12',
    'carlon':'mar 4'
}

while True :
    print ('enter a name :' )
    name = input()
    if name == '':
        break
    if name in birthdays :
        print (birthdays[name] + 'is the birthday of ' + name)
    else:
        print ('we dont have for ' + name)
        print ('the birthday of ' + name )
        bday = input()
        birthdays[name] = bday
        print ('hava add ' + name)
