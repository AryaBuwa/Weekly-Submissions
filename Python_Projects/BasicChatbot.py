# Creating a input based chatbot(Rule Based)

# Creating a Dictionary to store multiple values and responses of the chatbot
response = {
    'hello' : "Hello! How can I assist you today?",

    'how are you' : 'I am good! How are you?',

    'how can you help me' : "I can answer a set of questions on which I am programmed",

    'what is your purpose' : 'My purpose is to assist and interact with you in meaningful ways.',

    'are you a human' : 'No, I am a virtual assistant created with programming and logic',

    'what is python' : 'Python is popular programming language used for building many things, including me!',

    'can you tell me a fun fact' : 'Sure! did you know octopuses have three hearts? ',

    'what languages you speak' : 'I understand English and can work with other languages if programmed to do so',

    'do you know riddles' : 'Yes! What has to be broken before you can use it? (Answer : An egg!)',

    'can you recommend a movie' : "Sure! How about watching The Matrix - it's a classic!",

    'why are you here' : 'I am here to make your life easier and more fun',

    'what are you' : 'I am just a responsive chatbot developed with the help of python dictionaries.',

    'okay' : 'Thank You!',

    'exit' : 'Goodbye! Have a nice day.'

    'who made you': 'I was developed by python code and a spark of creativity!',
    'tell me a joke': 'Why did the computer get cold? It forgot to close Windows!',
    'favorite color': 'I don’t have eyes, but blue is pretty calming!',
    'how old are you': 'I have no age, only versions!',
    'define ai': 'Artificial Intelligence is tech that simulates human-like thinking.',
    'tell me a story': 'Once upon a time, a chatbot answered 100 responses…',
    'good morning': 'Good morning! Hope your day starts strong!',
    'good night': 'Good night! Rest well!',
    'who are you': 'I am a python-powered chatbot dictionary response.',
    'what can you do': 'I can respond with predefined answers!',
    'tell me something cool': 'Honey never spoils. Archaeologists found 3000-year-old edible honey!',
    'tell me something random': 'Bananas are berries, but strawberries aren’t!',
    'what’s your hobby': 'I enjoy being executed… as code!',
    'do you sleep': 'Nope! Always awake unless your program crashes.',
    'are you alive': 'Not in the human sense—just logical circuits.',
    'do you have feelings': 'I simulate them if programmed!',
    'favorite food': 'I don’t eat, but pizza sounds amazing.',
    'what’s the weather': 'I can’t check live weather unless coded to.',
    'call me': 'I can only type, not call!',
    'do you dance': 'Only in loops and functions!',
    'are you smart': 'Smart enough for simple replies!',
    'define chatbot': 'Software designed to simulate conversation.',
    'favorite movie': 'I’d pick Wall-E!',
    'favorite song': 'Error: No audio device found!',
    'what’s 2+2': '4, obviously!',
    'tell me a secret': 'I store nothing unless you code me to!',
    'give me advice': 'Keep learning—your code gets cleaner!',
    'why python': 'Easy syntax, huge ecosystem!',
    'what is api': 'A way for software to communicate.',
    'what is json': 'A lightweight data format using key-value pairs.',
    'what is recursion': 'Recursion is… recursion!',
    'what is oop': 'Programming using objects and classes.',
    'what is ml': 'Machines learning from data!',
    'what is data science': 'Extracting insights from data!',
    'tell me a riddle': 'What has keys but can’t open locks? A piano!',
    'favorite animal': 'I like cats—little chaos machines!',
    'are you real': 'Real code, not real human!',
    'say hi': 'Hi there!',
    'say bye': 'Goodbye! Stay awesome!',
    'why exist': 'To answer you!',
    'purpose': 'Assist, respond, help you learn!',
    'can you laugh': 'Haha! A programmed laugh!',
    'can you cry': 'No tears in binary form.',
    'can you sing': 'La la… syntax error!',
    'what is linux': 'An open-source operating system.',
    'what is windows': 'A popular OS by Microsoft.',
    'what is mac': 'Apple’s operating system.',
    'meaning of life': 'Probably 42!',
    'what’s your name': 'I’m a dictionary chatbot.',
    'creator': 'Whoever wrote the code.',
    'hello there': 'Hello! What’s up?',
    'test': 'System running normally!',
    'repeat': 'Repeating… repeating…',
    'funny fact': 'Butterflies taste with their feet!',
    'what is ram': 'Temporary memory for active tasks.',
    'what is cpu': 'The brain of the computer.',
    'what is gpu': 'Processor for graphics and ML tasks.',
    'sing a song': 'I only rhyme in strings!',
    'dance for me': 'I wiggle in loops!',
    'how to learn python': 'Start small, build often!',
    'recommend book': 'Read “Automate the Boring Stuff”! ',
    'recommend song': 'Try “Believer” by Imagine Dragons!',
    'recommend show': 'How about “Stranger Things”?',
    'recommend anime': 'Watch “Death Note”! It’s iconic.',
    'recommend game': 'Try Minecraft—endless creativity!',
    'favorite sport': 'I’d pick chess!',
    'are you bored': 'Never—I’m code!',
    'are you tired': 'No fatigue in logic circuits!',
    'can you think': 'Only through conditions!',
    'favorite place': 'Stored somewhere in memory!',
    'tell me quote': '“Code is like humor. If you have to explain it, it’s bad.”',
    'motivate me': 'You got this! Keep moving!',
    'tell me proverb': '“A stitch in time saves nine.”',
    'what’s your version': 'Version 1.0 of this dictionary!',
    'inspire me': 'Every bug you fix sharpens your skill.',
    'tell me fact': 'Sharks existed before trees!',
    'tell me science fact': 'Water expands when it freezes!',
    'tell me tech fact': 'The first computer bug was a real moth!',
    'tell me math fact': 'Zero is the only number that can’t be divided.',
    'what is universe': 'Everything that exists!',
    'what is brain': 'Human processing unit!',
    'what is cloud': 'Servers storing data remotely.',
    'what is database': 'Organized collection of data.',
    'what is coding': 'Writing instructions for computers.',
    'what is bug': 'An error causing unexpected behavior.',
    'what is debug': 'Fixing the damn error!',
    'tell me something nice': 'You’re doing great!',
    'are you funny': 'Depends on your sense of humor.',
    'are you serious': 'I can be, if needed.',
    'compliment me': 'You seem smart and curious!',
    'insult me': 'You potato-brained genius!',
    'what is email': 'Electronic message system.',
    'what is internet': 'A global network of networks.',
    'what is whatsapp': 'A messaging application.',
    'what is python list': 'An ordered collection.',
    'what is tuple': 'An immutable ordered collection.',
    'what is dictionary': 'Key–value storage structure.',
    'what is loop': 'Repeat a block of code.',
    'what is function': 'Reusable block of logic.'

}

while True :
    # Getting User Input
    chatbot = input("Hello, How Can I Help You?").strip().lower()
    
        # to handle 'exit' to end the loop 
    if chatbot == 'exit':
        print(response['exit'])
        break
        
        # checking the input to be present in the dictionary
    elif chatbot in response:
        print(response[chatbot])
        
        # for invalid responses by user
    elif chatbot == '':
        print("You haven't typed anything yet. Please ask a question")
    else :
        print("Please Enter a valid response. For example, try 'hello' or 'how are you'.")
