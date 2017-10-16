#! /usr/bin/python3
import random
import datetime

notes = {
    "do": 'c',
    're': 'd',
    'mi': 'e',
    'fa': 'f',
    'sol': 'g',
    'la': 'a',
    'si': 'b'
}

score = 0
totaltime = datetime.timedelta(0, 0, 0)
num = 10

av_notes = {}

for x in range(0,num):

    if not av_notes:
        av_notes = notes.copy()

    rnote = random.choice(list(av_notes.keys()))
    av_notes.pop(rnote, None)

    print(notes[rnote])
    begintime = datetime.datetime.now()
    answer = input()

    finaltime = datetime.datetime.now() - begintime

    if answer.lower() == rnote:
        score += 1
        totaltime += finaltime
    else:
        print("NO: " + rnote)


print("Score: " + str(score) + "/" + str(num))
print('Time per good answer: ' + str(totaltime.total_seconds() / score))