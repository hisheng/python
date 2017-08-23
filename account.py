passwords = {
    'email':'fafjscpzkx',
    'blog':'dqwdsdA2w',
    'sns':'2rrcszc'
}

import sys,pyperclip

if len(sys.argv) < 2 :
    print ('usage : account.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in passwords :
    pyperclip.copy(passwords[account])
    print ('account copied to clipboard')
else:
    print ("no accout")