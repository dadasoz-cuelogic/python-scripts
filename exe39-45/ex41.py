import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):"
    :
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}


if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False


for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        
        for word in class_names:
            result = result.replace("%%%", word, 1)

        
        for word in other_names:
            result = result.replace("***", word, 1)

        
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results



try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"


'''
it123@it123:~/Documents/exe39-45$ python ex41.py english
From dinosaurs get the direction attribute and set it to 'believe'.
> 
ANSWER:  dinosaurs.direction = 'believe'


class Church has-a __init__ that takes self and cracker parameters.
> 
ANSWER:  class Church(object):
    def __init__(self, cracker)


Make a class named Control that is-a Desk.
> 
ANSWER:  class Control(Desk):


class Bee has-a function named calendar that takes self and band, base parameters.
> class bee(object):
ANSWER:  class Bee(object):
    def calendar(self, band, base)


From curve get the dust function, and call it with parameters self, ball.
> 
ANSWER:  curve.dust(ball)


Set cannon to an instance of class Debt.
> 
ANSWER:  cannon = Debt()


From division get the dust function, and call it with parameters self, creator.
> 
ANSWER:  division.dust(creator)


Set coach to an instance of class Attempt.
> 
ANSWER:  coach = Attempt()


Make a class named Ball that is-a Chin.
> 
ANSWER:  class Ball(Chin):

'''