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