import json

# Additional HP Questions
hp_more = {
    "easy": [
        {"question": "Who represents Hufflepuff in the Triwizard Tournament?", "options": ["Cedric Diggory", "Zacharias Smith", "Ernie Macmillan", "Justin Finch-Fletchley"], "answer": "Cedric Diggory"},
        {"question": "What kind of creature is Aragog?", "options": ["Acromantula", "Basilisk", "Hippogriff", "Blast-Ended Skrewt"], "answer": "Acromantula"},
        {"question": "Who is the ghost of Slytherin house?", "options": ["The Bloody Baron", "Nearly Headless Nick", "The Fat Friar", "The Grey Lady"], "answer": "The Bloody Baron"},
        {"question": "What is the name of Hagrid's boarhound?", "options": ["Fang", "Fluffy", "Norbert", "Buckbeak"], "answer": "Fang"},
        {"question": "What magical sport is played on flying broomsticks?", "options": ["Quidditch", "Gobstones", "Wizard's Chess", "Exploding Snap"], "answer": "Quidditch"},
        {"question": "Which family does Dobby originally serve?", "options": ["The Malfoys", "The Blacks", "The Lestranges", "The Crouches"], "answer": "The Malfoys"},
        {"question": "What is the name of the wizarding bank in London?", "options": ["Gringotts", "The Leaky Cauldron", "Ollivanders", "Borgin and Burkes"], "answer": "Gringotts"},
        {"question": "What color is the Gryffindor house crest?", "options": ["Red and Gold", "Blue and Bronze", "Green and Silver", "Yellow and Black"], "answer": "Red and Gold"},
        {"question": "Who leaves Harry the Invisibility Cloak?", "options": ["Albus Dumbledore", "Sirius Black", "Severus Snape", "Remus Lupin"], "answer": "Albus Dumbledore"},
        {"question": "What phrase activates the Marauder's Map?", "options": ["I solemnly swear that I am up to no good", "Mischief managed", "Lumos Maxima", "Open Sesame"], "answer": "I solemnly swear that I am up to no good"}
    ],
    "medium": [
        {"question": "What ingredient is not in a Polyjuice Potion?", "options": ["Dittany", "Fluxweed", "Knotgrass", "Boomslang skin"], "answer": "Dittany"},
        {"question": "What is the real name of Voldemort?", "options": ["Tom Marvolo Riddle", "Gellert Grindelwald", "Lucius Malfoy", "Salazar Slytherin"], "answer": "Tom Marvolo Riddle"},
        {"question": "Who wrote 'Advanced Potion-Making'?", "options": ["Libatius Borage", "Severus Snape", "Arsenius Jigger", "Phyllida Spore"], "answer": "Libatius Borage"},
        {"question": "What position does Ginny Weasley play on the Gryffindor Quidditch team professionally?", "options": ["Chaser", "Seeker", "Keeper", "Beater"], "answer": "Chaser"},
        {"question": "What is the incantation for the Patronus Charm?", "options": ["Expecto Patronum", "Expelliarmus", "Riddikulus", "Accio"], "answer": "Expecto Patronum"},
        {"question": "Who destroys the Ravenclaw Diadem horcrux?", "options": ["Crabbe (via Fiendfyre)", "Harry Potter", "Ron Weasley", "Hermione Granger"], "answer": "Crabbe (via Fiendfyre)"},
        {"question": "What magical object reveals your deepest desires?", "options": ["The Mirror of Erised", "The Pensieve", "The Remembrall", "The Marauder's Map"], "answer": "The Mirror of Erised"},
        {"question": "Which Peverell brother received the Resurrection Stone?", "options": ["Cadmus", "Antioch", "Ignotus", "Gellert"], "answer": "Cadmus"},
        {"question": "Where does the Dumbledore's Army meet?", "options": ["The Room of Requirement", "The Shrieking Shack", "The Gryffindor Common Room", "The Owlery"], "answer": "The Room of Requirement"},
        {"question": "Who takes Hermione to the Yule Ball?", "options": ["Viktor Krum", "Ron Weasley", "Harry Potter", "Neville Longbottom"], "answer": "Viktor Krum"}
    ],
    "hard": [
        {"question": "What number is Harry's vault at Gringotts?", "options": ["687", "713", "394", "422"], "answer": "687"},
        {"question": "What is the password to the prefects' bathroom?", "options": ["Pine Fresh", "Caput Draconis", "Mimbulus Mimbletonia", "Fairy Lights"], "answer": "Pine Fresh"},
        {"question": "Who was the Muggle Studies teacher murdered by Voldemort?", "options": ["Charity Burbage", "Alecto Carrow", "Quirinus Quirrell", "Silvanus Kettleburn"], "answer": "Charity Burbage"},
        {"question": "How many staircases are there at Hogwarts?", "options": ["142", "112", "163", "128"], "answer": "142"},
        {"question": "What type of wood is Ron's second wand made of?", "options": ["Willow", "Ash", "Cherry", "Mahogany"], "answer": "Willow"},
        {"question": "What does S.P.E.W. stand for?", "options": ["Society for the Promotion of Elfish Welfare", "Society for the Protection of Elfish Workers", "Secret Potion Enforcement Wizards", "Students Protecting Endangered Wildlife"], "answer": "Society for the Promotion of Elfish Welfare"},
        {"question": "Who is the author of 'Magical Drafts and Potions'?", "options": ["Arsenius Jigger", "Libatius Borage", "Bathilda Bagshot", "Newt Scamander"], "answer": "Arsenius Jigger"},
        {"question": "What is the name of Dumbledore's younger sister?", "options": ["Ariana", "Kendra", "Honoria", "Aberforth"], "answer": "Ariana"},
        {"question": "What is the command to make a wand emit a burst of green sparks?", "options": ["Verdimillious", "Periculum", "Lumos", "Incendio"], "answer": "Verdimillious"},
        {"question": "How much does a ticket on the Knight Bus from Little Whinging to London cost?", "options": ["11 Sickles", "10 Galleons", "15 Knuts", "5 Sickles"], "answer": "11 Sickles"}
    ]
}

# Additional ST Questions
st_more = {
    "easy": [
        {"question": "What is the name of Dustin's girlfriend he meets at Camp Know Where?", "options": ["Suzie", "Chrissy", "Heather", "Eden"], "answer": "Suzie"},
        {"question": "What color are the Demogorgon's teeth?", "options": ["White/Grey", "Yellow", "Black", "Green"], "answer": "White/Grey"},
        {"question": "What toy does Eleven levitate in Mike's basement?", "options": ["Millennium Falcon", "X-Wing", "TIE Fighter", "Death Star"], "answer": "Millennium Falcon"},
        {"question": "What does Joyce use to talk to Will in Season 1?", "options": ["Christmas lights", "A walkie-talkie", "A telephone", "A Ouija board"], "answer": "Christmas lights"},
        {"question": "Who says 'Mornings are for coffee and contemplation'?", "options": ["Jim Hopper", "Bob Newby", "Mike Wheeler", "Joyce Byers"], "answer": "Jim Hopper"},
        {"question": "What is Max's arcade username?", "options": ["MADMAX", "MAXIMUM", "REDHEAD", "SKATERGIRL"], "answer": "MADMAX"},
        {"question": "Who is Will's older brother?", "options": ["Jonathan", "Steve", "Billy", "Mike"], "answer": "Jonathan"},
        {"question": "What does Eleven call Jim Hopper?", "options": ["Hop", "Dad", "Jim", "Chief"], "answer": "Hop"},
        {"question": "What kind of business does Bob Newby manage?", "options": ["RadioShack", "Family Video", "Scoops Ahoy", "A hardware store"], "answer": "RadioShack"},
        {"question": "Who is Barb's best friend in Season 1?", "options": ["Nancy", "Joyce", "Robin", "Carol"], "answer": "Nancy"}
    ],
    "medium": [
        {"question": "What is the password to Castle Byers?", "options": ["Radagast", "Gandalf", "Elrond", "Mirkwood"], "answer": "Radagast"},
        {"question": "What song do Dustin and Suzie sing together?", "options": ["The NeverEnding Story", "Total Eclipse of the Heart", "Material Girl", "Africa"], "answer": "The NeverEnding Story"},
        {"question": "What is the name of the D&D monster in Season 1?", "options": ["The Demogorgon", "The Thessalhydra", "The Mind Flayer", "Vecna"], "answer": "The Demogorgon"},
        {"question": "Who cracked the Russian code in Season 3?", "options": ["Robin", "Dustin", "Erica", "Steve"], "answer": "Robin"},
        {"question": "How long was Will missing in the Upside Down?", "options": ["A week", "Three days", "Two weeks", "One month"], "answer": "A week"},
        {"question": "What does Billy do during the summer in Hawkins?", "options": ["He's a lifeguard", "He works at Scoop's Ahoy", "He delivers newspapers", "He runs a gym"], "answer": "He's a lifeguard"},
        {"question": "What happens to objects when they enter the Upside Down?", "options": ["They become cold and decayed", "They turn invisible", "They burst into flames", "They become indestructible"], "answer": "They become cold and decayed"},
        {"question": "Who is the first person Vecna kills in Season 4?", "options": ["Chrissy Cunningham", "Fred Benson", "Patrick McKinney", "Barb Holland"], "answer": "Chrissy Cunningham"},
        {"question": "What is the flavor of the Slurpee Alexei specifically asks for?", "options": ["Cherry", "Strawberry", "Blue Raspberry", "Cola"], "answer": "Cherry"},
        {"question": "What does Erica Sinclair want in exchange for crawling through the vents?", "options": ["Free ice cream for life", "A new bicycle", "100 dollars", "A walkie-talkie"], "answer": "Free ice cream for life"}
    ],
    "hard": [
        {"question": "What was the date Will Byers disappeared?", "options": ["November 6, 1983", "October 31, 1983", "November 11, 1984", "October 28, 1983"], "answer": "November 6, 1983"},
        {"question": "What is the brand of the hairspray Steve uses?", "options": ["Farrah Fawcett", "Aqua Net", "L'Oreal", "Vidal Sassoon"], "answer": "Farrah Fawcett"},
        {"question": "What was the name of the Hawkins middle school science teacher?", "options": ["Mr. Clarke", "Mr. Henderson", "Mr. Harris", "Mr. Wheeler"], "answer": "Mr. Clarke"},
        {"question": "In what city was Eleven's sister Kali operating?", "options": ["Chicago", "New York", "Los Angeles", "Detroit"], "answer": "Chicago"},
        {"question": "What classical composer's music is played by Dr. Brenner?", "options": ["Brahms", "Beethoven", "Mozart", "Bach"], "answer": "Brahms"},
        {"question": "What is the specific address of the Byers house?", "options": ["149 Corliss", "4819 Cherry Lane", "12 Grimmauld Place", " Elm Street"], "answer": "149 Corliss"},
        {"question": "What does a 'Code Red' mean to the party?", "options": ["Immediate danger", "Meet at the basement", "Parents are listening", "Aliens attack"], "answer": "Immediate danger"},
        {"question": "What is the name of the D&D character played by Eddie Munson?", "options": ["Kas", "Loridas", "Elminster", "Drizzt"], "answer": "Kas"},
        {"question": "Who was the editor of the Hawkins Post?", "options": ["Tom Holloway", "Bruce Lowe", "Murray Bauman", "Donald Chapman"], "answer": "Tom Holloway"},
        {"question": "What color was the hazmat suit Hopper found in the tunnels in Season 2?", "options": ["Yellow", "Orange", "White", "Blue"], "answer": "Yellow"}
    ]
}

def update_trivia(filename, new_data):
    with open(filename, 'r') as f:
        data = json.load(f)
    
    for difficulty in ['easy', 'medium', 'hard']:
        data[difficulty].extend(new_data[difficulty])
        
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

update_trivia('hp_trivia.json', hp_more)
update_trivia('st_trivia.json', st_more)
print("Trivia files successfully updated with more questions.")
