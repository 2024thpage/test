import time
import random

lyrics = '''
Check
Okay
Alright
I Been that Nigga since like
Been that Nigga since like 17
My money evergreen
I see niggas tryna ride the wave it don’t mean nothing to me
I can’t even hit my old girl up she said she done with me
Know I’m toxic but she ain’t gonna stop it she have fun with me
In my prime like Optimus she said I change like bumblebee
Way too cocky need it ASAP rocky shorty humble me
Let’s run it back
Touchdown in your city just don’t fumble me
Hit it raw and now her Nigga salty want to rumble me
I ain’t fighting about no bitch
I be writing bout yo bitch
Sending pictures to the group chat they be typing bout your bitch
Ain’t no wifing out yo bitch
I’m one nighting out yo bitch
I’m a good guy but I do her nasty triflin bout yo bitch
OK let’s go
Who want smoke with E you ain’t controlling me
Hit it once and now she need that shit girl this that OCD
In KY you know that Nigga fly that boy like CVG
Here’s my number treat me like a plumber give her PVC
Been that Nigga since like 17
My money evergreen
I see niggas tryna ride the wave it don’t mean nothing to me
I can’t even hit my old girl up she said she done with me
Know I’m toxic but she ain’t gonna stop it she have fun with me
In my prime like Optimus she said I change like bumblebee
Way too cocky need it ASAP rocky shorty humble me
Let’s run it back
Touchdown in your city just don’t fumble me
Hit it raw and now her Nigga salty want to rumble me
I ain’t fighting bout no bitch
What
Boy I ain’t fighting bout no
Okay
Boy I ain’t
Alright
Alright
Alright
'''

splitLyrics = lyrics.split("\n")

for i in range(len(splitLyrics)):
    splitLyrics[i] = splitLyrics[i] + "\n"
    
print(splitLyrics)