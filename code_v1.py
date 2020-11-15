rarebirds = {
    'Gold-Crested Toucan': {
        'Height (m)': 1.1,
        'Weight (kg)': 35,
        'Color': 'Gold',
        'Endangered': True,
        'Aggressive': True},
    'Pearlescent Kingfisher': {
        'Height (m)': 0.25,
        'Weight (kg)': 0.5,
        'Color': 'White',
        'Endangered': False,
        'Aggressive': False},
    'Four-Metre Hummingbird': {
        'Height (m)': 0.6,
        'Weight (kg)': 0.5,
        'Color': 'Blue',
        'Endangered': True,
        'Aggressive': False},
    'Giant Eagle': {
        'Height (m)': 1.5,
        'Weight (kg)': 52,
        'Color': 'Black and White',
        'Endangered': True,
        'Aggressive': True},
    'Ancient Vulture': {
        'Height (m)': 2.1,
        'Weight (kg)': 70,
        'Color': 'Brown',
        'Endangered': False,
        'Aggressive': False}
}
birdlocation = [
    "In the canopy directly above our heads.",
    "Between my 6 and 9 o'clock above.",
    "Between my 9 and 12 o'clock above.",
    "Between my 12 and 3 o'clock above.",
    "Between my 3 and 6 o'clock above.",
    "In a nest on the ground.",
    "Right behind you."
]
codes = {
    '111': birdlocation[0],
    '110': birdlocation[1],
    '101': birdlocation[2],
    '100': birdlocation[3],
    '011': birdlocation[4],
    '010': birdlocation[5],
    '001': birdlocation[6]}
actions = ['Back Away','Cover our Heads','Take a Photograph']
# Your photographer has heard that the Giant Eagle has killed adult gorillas before. She wants to know if it's aggressive. Using your rarebirds dictionary, print out the Giant Eagle’s value for the "Aggressive" key within the nested dictionary (hint: you should be printing out the Boolean True).
print(rarebirds['Giant Eagle']['Aggressive'])
# Your colleague is now nervous, and you’re even more so. She wants the low-down on the rest of the birds you may encounter. Using a for loop that goes through the keys and the values of your rarebirds dictionary: Print out a string specifying the names of all the birds we’re looking for. If a bird is aggressive, print out a string advising us to cover our heads. Make use of the actions list in this print statement. If a bird is endangered, print out a string advising us to back away. Make use of the actions list in this print statement.
for birds in rarebirds:
    if rarebirds[birds]['Aggressive'] == True:
        print(birds + ' - This bird is aggressive. ' + actions[1])
    if rarebirds[birds]['Endangered'] == True:
        print(birds + ' - This bird is endangered. ' + actions[0])
# Your photographer wants a reminder of what the binary codes that you've come up with mean. Using a for loop, iterate through the keys and the values of the codes dictionary. Print out a statement that specifies what each code means.
for index, code in enumerate(codes):
    print(code + ' - ' + birdlocation[index])
# Using a for loop, add an extra bird attribute (to go with with height, weight, etc) called 'seen', and set its value to False for all birds.
for birds in rarebirds:
    rarebirds[birds]['seen'] = False
# Make a new variable called encounter, and set its value to True.
encounter = True
# Ask the user for an input, and give them the prompt: ‘What do you see?’. Store this input in a variable called sighting. Make this input all lowercase with a built-in function.
# Make a list called rarebirdsList of the names of the rare birds, using your dictionary rarebirds and the built-in method keys().
rarebirdslist = []
for bird in rarebirds.keys():
    rarebirdslist.append(bird.lower())
# Write some code that checks whether the sighting is in rarebirdsList. If it isn’t, print out the statement: “that’s not one of the birds we’re looking for”. If it is, print out the statement: “this is one of the birds we’re looking for!”
# Ask the user for an input, and give them the prompt: ‘What do you see?’. Store this input in a variable called sighting.
while encounter == True:
    sighting = input('What do you see? ').lower()
    if sighting in rarebirdslist:
        print("this is one of the birds we're looking for!")
        break
    print("that's not one of the birds we're looking for")
    continue
# Ask the user for another input, with the prompt: ‘Where do you see it? Input the correct code.’, and store this input in a variable called code.
code = input('Where do you see it? Input the correct code. ')
# Make a new variable called location that gets the correct location from the dictionary codes using the key code.
location = codes[code]
# Make a printout summarizing which bird has been seen and its location, making use of the variables sighting and location. This could look like:
print("So you've seen a " + sighting + ' ' + location.lower() + ' My goodness.')
# In the if-statement, check whether the sighting is aggressive. If it is, print out that it’s aggressive, and that we need to back away and cover our heads. In addition, print out that we need to photograph the sighting at its location.In the elif-statement, check whether the sighting is endangered. If it is, print out that it’s endangered, and that we need to back away. Also, print out that we need to photograph the sighting at its location. In the else statement (i.e, the sighting is neither aggressive nor endangered) print out that we need to photograph the ultra rare sighting at its location. In all of these blocks, make use of the actions list and the variables sighting and location in your printouts.
if rarebirds[sighting.title()]['Aggressive'] == True:
    print ('That creature is aggresive, we need to ' + actions[0].lower() + ' and ' + actions[1].lower() + '.')
    print( actions[2] + ' ' + location.lower())
elif rarebirds[sighting.title()]['Endangered'] == True:
    print('That creature is endangered, we need to ' + actions[0].lower())
    print( actions[2] + ' ' + location.lower())
else:
    print('That ' + sighting + ' is ultra rare! We need to ' + actions[2].lower() + ' ' + location.lower())
