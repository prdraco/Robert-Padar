#Print the head 'The Trivia Program'
#Get the user's name, age and wieght (in kg)
#welcome the user by name
#convert the user age in years to a number of seconds
#print 'Did you know...?'
#print 'You are nnnn seconds old!' Where the nnnn is the calculated number of second
#Calculate your Moon weight as (user weight / Earth gravity (9.81) * Moon ravity (1.622))
#print 'You would weight nn.nnn kilos on the Moon!' Where nn.nnn is the calculated Moon weight
#Calculate your Mars weight as (user weight / Earth gravity * Mars gravity (3.711))
#Print 'You would weight nn.nnn kilos on the Mars!' Where nn.nnn is the calculated Mars weight
#Calculate your Venus weight as (user weight / Earth gravity * Venus gravity (8.87))
#Print 'You would weight nn.nnn kilos on the Venus!' Where nn.nnn is the calculated Venus weight
#calculate the difference in weight between Earth and Moon
#Print the user name and 'Here is some great advice...'
#print 'Fly to the Moon and lose nn.nnn kilos!' Where nn.nnn is the calculated difference in weight
print('\n\t\tThe Trivia Program\n\n')
name = input('What is your name? ')
age = input('What is your age? ')
weight = input('What is your weight (kg)? ')
name = name.capitalize()
print('Welcome ' + name)
age = float(age)
weight = float(weight)
ageSec = age * 31536000
ageSec = str(ageSec)
print('Did you know...? ')
print('You are ' + ageSec + ' seconds old! ')
moonWeight = (weight/9.81*1.622)
print('You would weight %.4f kilos on the Moon! ' % moonWeight)
marsWeight = (weight/9.81*3.711)
print('You would weight %.4f kilos on the Mars! ' % marsWeight)
venusWeight = (weight /9.81*8.87)
print('You would weight %.4f kilos on the Venus! ' % venusWeight)
difWeight = weight - moonWeight
print(name + ' Here is some great advice... ')
print('Fly to the moon and loose %.4f kilos! ' % difWeight)