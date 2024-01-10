import sys

def main():
    print('Welcome to Cesar Cypher encryption system!')
    choice = input("First, let's decide what do you want ot do, if you wanna encrypt type <E>, if you want to decrypt a secret message type <D>  ")
    response1 = "E"
    response2 = "D"
    if choice == response1: 
        message = input ("Please type a message to encode: ")
        print("NOTE: PLEASE REMEBER THE FOLLOWING CODE TO ENCRYPT MESSAGES")
        key_input = input("Please insert your desired encryption number: ")
        key = int(key_input)

        encryption1 = []
        for z in message:
            progress = ord(z) +  key
            encryption1.append(progress) 

        encryption2 = []
        for z in encryption1:
            progress1 = z
            answer = chr(progress1)
            encryption2.append(answer)
        result = ''.join(encryption2)
        encryption_result = print("Please copy Your encrypted message : ", result)
        return encryption_result
    elif choice == response2:
        message = input ("Please type a message to decode: ")
        print("I HOPE YOU SAVED THE ENCRYPTION NUMBER")
        key_input = input("Please insert your THE encryption number: ")
        key = int(key_input)
        keyword = list(message)
        home = []
        for z in message:
            progress = ord(z) 
            home.append(progress) 
        stage1 = []
        for z in home: 
            part1 = z - key
            stage1.append(part1)
        stage2 = []
        for z in stage1: 
            part2 = chr(z)
            stage2.append(part2)
        decrypted = ''.join(stage2)
        encryption_result = print("Your decrepted message is: ", decrypted)
        return encryption_result
    else: 
            print("Well, looks like someone can't read or follow the directions correctly, Caesar is dissapointed and will not help you...")
    
    print("That's it! if you wanna decode or encode another message, run this program again!")
    final_choice = input("Wanna use Caesar Cypher again? Y/N   ")
    if  final_choice == "Y": 
        main()
    elif final_choice == "N":
        print("Thank you for using Ceaser Cypher encoding tool")

if __name__ == "__main__":
    main()