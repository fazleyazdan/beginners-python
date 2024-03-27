# Messages: Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

print("\n==================== Task 1 ====================\n")
def show_messages(messages_p):
    for message in messages_p:
        print(f"{message}")

messages = ['Hi ! how are you?', 'what\'s up', 'everything okay?']
show_messages(messages)

#! ==================== Task 2 ==================== #
'''Sending Messages: Start with a copy of your program from above. 
Write a function called send_messages() that prints each text message and 
moves each message to a new list called sent_messages as it's printed. After 
calling the function, print both of your lists to make sure the messages were 
moved correctly'''

print("\n==================== Task 2 ====================\n")

def send_messages(messages_list, sent_messages):
    while messages_list:
        pop_message = messages_list.pop()
        print(f"sending message... {pop_message}")
        sent_messages.append(pop_message)         

messages_list = ['Hi ! how are you?', 'what\'s up', 'everything okay?']
sent_messages = []

send_messages(messages_list,sent_messages)

print(f"\n*** send message list ***")
show_messages(messages_list)
print(f"\n*** sent message list ***")
show_messages(sent_messages)


#! ==================== Task 3 ==================== #
'''Archived Messages: Start with your work from above Exercise. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.'''

print("\n==================== Task 3 ====================\n")

messages_list = ['Hi ! how are you?', 'what\'s up', 'everything okay?']
sent_messages = []

send_messages(messages_list[:], sent_messages)

print(f"\n*** send message list ***")
show_messages(messages_list)
print(f"\n*** sent message list ***")
show_messages(sent_messages)
