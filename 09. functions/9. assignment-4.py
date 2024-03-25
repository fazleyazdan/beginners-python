# Messages: Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

def show_messages(messages_p):
    for message in messages_p:
        print(f"\n{message}")

messages = ['Hi ! how are you?', 'what\'s up', 'everything okay?']
show_messages(messages)