import time
import random

lyrics = '''
I go to church, not for the word, just to leave with a guaranteed freak
Slide to the city, then swerve to the burbs, head to the boonies, the trenches for drinks
Not in Arkansas, but shoutout to herb when I'm outta state he gon' hold down the heat
In Baltimore we was 19, never serve
Left with some boxer some pints and some P's
I close my eyes for a lil' more space
Could believe in a god, still can't bе safe
You roll your eyes whеn I talk this way
Me and my friends went separate ways
Might add a lil' red in the Fanta for the flavor
America taught me how to behave
Shit, you want it, it's yours to take
Put it all on line, know what's at stake
Fuck all that talk, ain't no debates
Ran into my old ting while I'm on a date
Say what you want, know I got good taste
Good Cheese Cake then back to the basics
After I bust on her she get replaced
My momma calling me, she know my ways
Might pick up, but there's nothing to say
Mind on a million different lil' thangs
Like what to put through it, intrude or persuade?
I go to church, not for the word, just to leave with a guaranteed freak
Slide to the city, then swerve to the burbs, head to the boonies, the trenches for drinks
Not in Arkansas, but shoutout to herb when I'm outta state he gon' hold down the heat
In Baltimore we was 19, never serve
Left with some boxer some pints and some P's
Fuck all that he say she say shit
Fuck all that he say she say shit
Fuck all that he say she say shit
I close my eyes for a lil' more space
Could believe in a god, still can't be safe
You roll your eyes when I talk this way
Me and my friends went separate ways
Might add a lil' red in the Fanta for the flavor
America taught me how to behave
Shit, you want it, it's yours to take
Put it all on line, know what's at stake
Fuck all that talk, ain't no debates
I ain't too sure about having blind faith
Really you'd think they'd want us to see
I'd take your word if you rose from the grave
'Til then it's lookin' like pyramid schemes
I know it's good and it's evil in me
You defined by your actions and hardly your speech
I don't know shit and I can't be naive
Tryna be balanced, in tune and in sync
I don't know shit, but I can't be naive
Tryna be balanced, in tune and in sync
Balanced, in tune and in sync
Tryna be balanced, in tune and in sync
Tryna be balanced, in tune and in sync
Tryna be balanced, in tune and in sync
'''

splitLyrics = lyrics.split("\n")
currentIter = 0

for i in range(len(splitLyrics)):
    splitLyrics[i] = splitLyrics[i] + " FUCK THE BLACKS\n"
    
print(splitLyrics)