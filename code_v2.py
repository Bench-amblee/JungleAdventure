rarebirds = {
    'Gold-Crested Toucan': {
        'Height (m)': 1.1,
        'Weight (kg)': 35,
        'Color': 'Gold',
        'Endangered': True,
        'Aggresive': True  },
    'Pearlescent Kingfisher': {
        'Height (m)': 0.25,
        'Weight (kg)': 0.5,
        'Color': 'White',
        'Endangered': False,
        'Aggresive': False     },
    'Four-Metre Hummingbird': {
        'Height (m)': 0.6,
        'Weight (kg)': 0.5,
        'Color': 'Blue',
        'Endangered': True,
        'Aggresive': False    },
    'Giant Eagle':{
        'Height (m)': 1.5,
        'Weight (kg)': 52,
        'Color': 'Black and White',
        'Endangered': True,
        'Aggresive': True },
    'Ancient Vulture': {
        'Height (m)': 2.1,
        'Weight (kg)': 70,
        'Color': 'Brown',
        'Endangered': False,
        'Aggresive': False }
}
# Create a list of bird locations base on our position
birdlocation = ["In the canopy directly above our heads.",
    "Between my 6 and 9 o'clock above.",
    "Between my 9 and 12 o'clock above.",
    "Between my 12 and 3 o'clock above.",
    "Between my 3 and 6 o'clock above.",
    "In a nest on the ground.",
    "Right behind you."
]
codes = { '001': birdlocation[0],
    '010': birdlocation[1],
    '011': birdlocation[2],
    '100': birdlocation[3],
    '101': birdlocation[4],
    '110': birdlocation[5],
    '111': birdlocation[6]
}
actions = ['Back Away',
    'Cover our Heads',
    'Take a Photograph'
]
import time
intro = """
***************
Welcome to Jungle Safari! 
We're looking to take pictures of rare birds today.
There are the birds we're looking for: 

- Gold-Crested Toucan
- Pearlescent Kingfisher
- Four-Metre Hummingbird
- Giant Eagle
- Ancient Vulture

Before we take a picture, you'll have to tell me 
where the bird is using one of our codes
"""
print(intro)
time.sleep(5)
print('Codes:')
for k, v in codes.items():
    print(k, v)
print()
for k, v in rarebirds.items():
    v['Seen'] = False
print('Now lets go! Let me know if you see a bird')
encounter = True
rarebirdslist = []
for bird in rarebirds.keys():
    rarebirdslist.append(bird.lower())
while encounter:
    sighting = input('What did you see? ').lower()
    if sighting in (rarebirdslist):
        print("This is one of the birds we're looking for!")
        break
    else:
        print("That's not one of the birds we're looking for.")
code = input("Where did you see it? Input the correct code:")
location = codes[code]
print("So you've seen a", sighting.title(), location, "My goodness.")
if rarebirds[sighting.title()]['Aggresive']:
    print('The', sighting.title(), 'is aggresive.', actions[0], 'and', actions[1],'.')
    print(actions[2], 'of the', sighting.title(), codes[code].lower())
elif rarebirds[sighting.title()]['Endangered']:
    print(actions[2], 'of the', sighting.title(), codes[code].lower())
else:
    print(actions[2], 'of the', sighting.title(), codes[code].lower())
