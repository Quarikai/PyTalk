import random
import datetime

class Talk_with_consumer_eng:
        def hello(self):
            list_of_words = ['Hi!', 'Hello!', 'Hallo!', 'Salut!', 'Good day!', 'Good afternoon!', 'Greetings!',
            'Hullo!', 'Hiya!', 'Hey!', 'Howdy!', 'Greet!', 'Yo!']
            print(random.choice(list_of_words))
        def how_are_you_ans(self):
            list_of_words = ['Fine!', 'Great!', 'Good!', 'Pretty good!', 'I’m fine, thank you.', 'I’m doing well',
                             'Not too bad', 'I’ve been better', 'Can’t complain', 'Same old, same old']
            print(random.choice(list_of_words))
        def how_are_you_que(self):
            list_of_words = ['How are you doing?', 'What’s up?', 'How are you getting on?', 'How are you bearing up?', 
            'How’s it going?', 'How’s life?', 'How are things?', 'How’s everything?', 'What’s new?']
            print(random.choice(list_of_words))
        def bye(self):
            list_of_words = ['Bye', 'Goodbye', 'Adieu', 'Arrivederci', 'Good Day', 'So far', 'So long', 'Cheerio']
            print(random.choice(list_of_words))