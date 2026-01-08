import random

def main():
    print("Random Quote Generator : ")
    print("--------------------------------")
    print("Generate Random Quote")
    print("Exit.")

def generate():
    quotes = [
    "Believe you can, and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Even if you’re on the right track, you’ll get run over if you just sit there.",
    "You are braver than you believe, stronger than you seem, and smarter than you think.",
    "Challenges are what make life interesting, and overcoming them is what makes life meaningful.",
    "Do what you can, with what you have, where you are.",
    "Happiness is not something ready-made. It comes from your own actions.",
    "The difference between ordinary and extraordinary is that little extra.",
    "Strive not to be a success, but rather to be of value.",
    "Your time is limited, so don’t waste it living someone else’s life.",
    "Fall seven times and stand up eight.",
    "The only difference between success and failure is the ability to take action.",
    "Go as far as you can see; when you get there, you’ll be able to see farther.",
    "Don’t let the fear of losing be greater than the excitement of winning.",
    "Be so good they can’t ignore you.",
    "Do what you can with all you have, wherever you are.",
    "The only person you are destined to become is the person you decide to be.",
    "Work hard in silence, let your success be your noise.",
    "Don't stop when you're tired. Stop when you're done.",
    "Be a voice, not an echo.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Don’t watch the clock; do what it does. Keep going.",
    "If opportunity doesn’t knock, build a door.",
    "Push yourself, because no one else is going to do it for you.",
    "It’s not whether you get knocked down, it’s whether you get up.",
    "Failure will never overtake me if my determination to succeed is strong enough.",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
    "The best way to predict your future is to create it.",
    "The man who has confidence in himself gains the confidence of others.",
    "You don’t have to see the whole staircase, just take the first step.",
    "Great things never come from comfort zones.",
    "Little things make big days.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Dream it. Wish it. Do it.",
    "The key to success is to focus on goals, not obstacles.",
    "Wake up with determination. Go to bed with satisfaction.",
    "It always seems impossible until it’s done.",
    "Set your goals high, and don’t stop till you get there.",
    "It’s going to be hard, but hard does not mean impossible.",
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "Don’t be afraid to give up the good to go for the great.",
    "Do something today that your future self will thank you for.",
    "The way to get started is to quit talking and begin doing.",
    "Don’t limit your challenges. Challenge your limits.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "In the middle of every difficulty lies opportunity.",
    "Hustle until you no longer have to introduce yourself.",
    "Start where you are. Use what you have. Do what you can.",
    "I am not a product of my circumstances. I am a product of my decisions.",
    "You miss 100% of the shots you don’t take.",
    "Be yourself; everyone else is already taken.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "Try not to become a person of success, but rather try to become a person of value.",
    "Do what you love and the money will follow.",
    "Success doesn’t just find you. You have to go out and get it.",
    "What we achieve inwardly will change outer reality.",
    "Good things come to people who wait, but better things come to those who go out and get them.",
    "Work until your idols become your rivals.",
    "There are no limits to what you can accomplish, except the limits you place on your own thinking.",
    "Stay hungry, stay foolish.",
    "Perseverance is not a long race; it is many short races one after the other.",
    "Don’t raise your voice, improve your argument.",
    "The best revenge is massive success.",
    "The question isn’t who is going to let me; it’s who is going to stop me.",
    "The only way to achieve the impossible is to believe it is possible.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "You are never too old to set another goal or to dream a new dream.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "Don’t wait. The time will never be just right.",
    "Go confidently in the direction of your dreams. Live the life you have imagined.",
    "Act as if what you do makes a difference. It does.",
    "With the new day comes new strength and new thoughts.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Opportunities don't happen. You create them.",
    "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Don’t let yesterday take up too much of today.",
    "Do one thing every day that scares you.",
    "Your limitation—it’s only your imagination.",
    "Dream big and dare to fail.",
    "Keep your eyes on the stars and your feet on the ground.",
    "All our dreams can come true if we have the courage to pursue them.",
    "What we think, we become.",
    "Success is not how high you have climbed, but how you make a positive difference to the world.",
    "When the going gets tough, the tough get going.",
    "If you can dream it, you can achieve it.",
    "It’s never too late to be what you might have been.",
    "Don't count the days, make the days count.",
    "Life isn’t about finding yourself. It’s about creating yourself.",
    "Do not wait to strike till the iron is hot; but make it hot by striking."
]

    random_quote = random.choice(quotes)
    print("\nRandom Quote: ", random_quote)
    print("\nDo you want to generate another quote? (yes/no): ")
    user_choice = input().lower()
    
    if user_choice == "yes":
        generate()
    elif user_choice == "no":
        print("\nThank you for using the Random Quote Generator!")
        exit()

if __name__ == "__main__":
    main()
    generate()


