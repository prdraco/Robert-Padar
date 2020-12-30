# The elif allows you to check for different values

country = input('Where do you live? ')
if country == 'CANNADA':
    print('Hello')
elif country == 'GERMANY':
    print('Guten Tag')
elif country == 'FRANCE':
    print('Bonjour')
else:
    print('Hi')


team = input('Enter your favorite hockey team: ').upper()
if team == 'FLYERS':
    print('Best team ever!')
elif team == 'SENATORS':
    print('Go Sens go!')
elif team =='RANGERS':
    print('Go Rangers')
else:
    print('No problem if you prefer the soccer or basketball')