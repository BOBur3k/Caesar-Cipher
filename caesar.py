import sys


def main(): #first we create a function that we will be using for this project
    print('Welcome to Cesar Cypher encryption system!') #welcome the end user and ask them what they want to do
    choice = input("First, let's decide what do you want to do, if you wanna encrypt type <E>, if you want to decrypt a secret message type <D>  ")
    response1 = "E" #define the options, either decrypt or encrypt 
    response2 = "D"
    if choice == response1: #depending on end user response, we will initiate the sub function. First is encryption
        message = input ("Please type a message to encode: ") #collecting the message n
        print("NOTE: PLEASE REMEBER THE FOLLOWING CODE TO DECRYPT THIS MESSAGE LATER") #notifying the end user to remember the key#
        key_input = input("Please insert your desired encryption number: ") #asking end user for a special key number for encryption, user can use any numeric value
        key = int(key_input) #transforming the string formated number to the integer format 
#encryption begins
        encryption = []
        for z in message: #firsr we launch for loop
            progress = (ord(z)- 32 + key)% 95 + 32 #goal is tranform each letter to the numeric value and then adding the key number.
            part1 = chr(progress) #afterwards change the numeric values to the charaters
            encryption.append(part1) #placing our answer to the encryption slot 
        result1 = ''.join(encryption) #to make the end message more  apealing and not in a list format we use this function
        print("               ")
        print("We are done!") #making end message more appealing 
        print("Here is your encrypted message : ", result1) #providng result and asking to copy it
        print("DO NOT FORGET TO COPY IT") 
        print("            ")
        return end() #encryption is done and user end up with encrypted message that can be used for decrpytion
    #users will be directed to the end function 
#decryption beginss
    elif choice == response2: #if end user choose to decrypt, this code will be initiate 
        message = input ("Please type a message to decode: ") #asking to paste the encrypted message
        print("I HOPE YOU SAVED THE ENCRYPTION NUMBER") #reminding the importance of the encryption key
        key_input = input("Please insert your the encryption number: ") #place to put the encryption key
        key = int(key_input) #changing the format of the key from string to integer
        decryption = [] #here we will place the decrypted message
        for z in message: #for loop activation
            progress = (ord(z)- 32 - key) % 95 + 32  #changing every character in the list to the corresponging number and subtracting the key
            part2 = chr(progress) #changing our numeric values to the corresponding characters
            decryption.append(part2) #placing our results in appropriate slot
        result2 = ''.join(decryption)#making end message more appealing by removing the list format 
        print("               ")
        print("We are done!") #making end message more appealing 
        print("Here is your encrypted message: ", result2) #demonstating the decrypted message
        print("             ")
        return end() #reffering to the end message
    else: #if end user couldn't follow the orders/instructions the following message will be displayed
            print("Well, looks like someone can't read or follow the directions correctly, Caesar is dissapointed and will not help you...")
            return end () #reffering to the end function 
def end():   #end function  
    print(" That's it! if you wanna decode or encode another message, answer to the following message: ")
    final_choice = input("Wanna use Caesar Cypher again? Y/N   ") #giving the choice to encode or decode again
    if  final_choice == "Y": #if yes we return to the main function 
        main()
    else: #if use do not wish to continue, we end the program 
        print("Thank you for using Ceaser Cypher encoding tool")

if __name__ == "__main__": #this function intiate our code
    main()