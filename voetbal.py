
scorer1 = 'Demyanenko'
scorer2 = 'Lytovchenko'
scorer3 = 'Jan Wouters'
scorer4 = 'Khidiyatullin'
scorer5 = 'Berry van Aerle'
goaltime1 = '31'
goaltime2 = '33'
goaltime3 = '37'
goaltime4 = '42'
goaltime5 = '50'

# dit moet handiger kunnen met een 1 tot 5 tellertje oid.
# naam en goaltijd is altijd gekoppeld, waarom 2 variabelen maken

scorers = scorer1 + ' scored in the ' + goaltime1 + 'st minute', scorer2 + ' ' + goaltime2, scorer3 + ' ' + goaltime3, scorer4 + ' ' + goaltime4, scorer5 + ' ' + goaltime5
print (scorers)


print ('---------------------------\n')

print (f'{scorer1} scored in the {goaltime1}st minute \n')
print (f'{scorer2} scored in the {goaltime2}rd minute \n')
print (f'{scorer3} scored in the {goaltime3}th minute \n')
print (f'{scorer4} scored in the {goaltime4}nd minute \n')
print (f'{scorer5} scored in the {goaltime5}th minute \n')


print ('---------------------------\n')
report = (f'{scorer1} scored in the {goaltime1}st minute \n')+(f'{scorer2} scored in the {goaltime2}rd minute \n')+(f'{scorer2} scored in the {goaltime2}rd minute \n')+(f'{scorer3} scored in the {goaltime3}th minute \n')+(f'{scorer4} scored in the {goaltime4}nd minute \n')+(f'{scorer5} scored in the {goaltime5}th minute \n')
print (report)

print ('---------------------------\n')

player = 'Berry van Aerle'
eerstespatie = player.find(' ')
firstname = (player[slice(eerstespatie)])
print ('voornaam: \t',firstname)

# Jan Jaap van den Brugge zal dus lastig worden maar die speelde gelukkig niet mee
# nu de achternaam isoleren. alles na de eerste spatie. Werkt internationaal niet trouwens, Brugge van den. Maar die speelde ook niet mee.

lengte = len (player)
# vanaf eerstespatie teruggeven. lengte maakt niks uit, dus 99 voor alles
tweededeel = (player[(eerstespatie+1):99])
#spatie mag weg dus +1

print ('achternaam: \t',tweededeel)
last_name_len = len(tweededeel)

print ('karakters in de achternaam is: ', last_name_len)
# inclusief de spatie, noemen we dat een karakter?
    
print ('---------------------------\n')    
# voorletter ipv hele naam maken

name_short = player [0]
print (name_short,'.',tweededeel)

chant = firstname +'!'
print (chant)
times = len (firstname)
print ((chant + ' ') * times)


if chant[-1] != ' ':
    print ('Great Chant!')
    
    
