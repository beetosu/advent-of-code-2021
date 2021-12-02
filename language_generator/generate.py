import json, random
from datetime import datetime
datetime.today().strftime("%D")

def check_duplicates():
    with open('list.json') as f:
        languages = json.load(f)
        rawLength = len(languages['unused'])
        languages['unused'] = list(set(languages['unused']))
        newLength = len(languages['unused'])
    print(rawLength, newLength)
    #with open('list.json', 'w') as g:
        #json.dump(languages, g)

def pick_language():
    with open('list.json') as f:
        languages = json.load(f)
        chosenLanguage = languages['unused'].pop(random.randrange(len(languages['unused'])))
        day = int(datetime.today().strftime("%d"))
        print(day, chosenLanguage)
        languages['used'].append({"day": day, "language": chosenLanguage})
    with open('list.json', 'w') as g:
        json.dump(languages, g, indent=3)


pick_language()
