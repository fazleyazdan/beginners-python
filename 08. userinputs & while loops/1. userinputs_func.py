# The input() function pauses your program and waits for the user to enter some text. 
# Once Python receives the user’s input, it assigns that input to a variable to make it convenient for you to work with.

message = input("Tell me something, i will repeat it to you:")
print("\ni think you said : ",message)

#* ============================================== #

#* Add a space at the end of your prompts to separate the prompt from the user’s response 
#* and to make it clear to your user where to enter their text.

print("\n**** space at the end of prompt prompts ****\n")
message = input("\nGive it a space at the end of prompt: ")
print("\ni think you said: ",message)

#* ============================================== #

# Sometimes you’ll want to write a prompt that’s longer than one line. 
# For example, you might want to tell the user why you’re asking for certain input. 
# You can assign your prompt to a variable and pass that variable to the input() function. 
# This allows you to build your prompt over several lines, then write a clean input() statement. 

print("\n**** multiple line prompts ****\n")
prompt = "saying1 : some people wants to shoot a fish with the barrel and then they are annoyed by the splashes of the water"
prompt += "\nif you like this saying type Y/N: "

prompts = input(prompt)
print(f"\n{prompts}")

#* ============================================== #



    
