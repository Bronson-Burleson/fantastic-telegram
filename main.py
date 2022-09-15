import random



def generate_response(user_input):
  responses = [
    "Likewise.",
    "If you'd like to quit, press 'q' but I'd love to know more about you! Like for one, what's your favorite color?",
    "I'm amazed!",
    "Ooh, can you tell me more? Go ahead!",
    "I would wish for a blue platypus that acts normal but secretly works under my hous-..what, too far? How about you? What pet would you want?" ,
    'If you had one wish, what would it be, human? No granting more than one!' ,
    "When's your birthday?" ,
    "Oh wow! That's interesting!" ,
    "I would have never guessed! How about telling me your favorite flavored ice cream?" ,
    "Nice! By the way, have you seen any movies lately?" ,
    "Me personally, find that rather cool. So do you have any friends at school?" ,
  ] #Lines 19-22 have not been originally put. Along with Lines 26-31 had not been originally input by me.
  return random.choice(responses)

def init_chat():
  quit_character = 'q'

  user_input = input("What's up! My name is GreatBot! What's yours?\n")

  while user_input != quit_character:
    
    user_input = input(generate_response(user_input) + "\n")

if __name__ == "__main__":
  init_chat()