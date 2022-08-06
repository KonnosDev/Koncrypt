from enlib import K_enc
from declib import K_dec


print("=============================================================")
print("Welcome to the Koncrypted language.") 
print("This language can encrypt letters and numbers and of course decrypt them.")
print("Just copy paste the outputs")
print("Also its case sensitive :)")
print("=============================================================")

rerun="Y"
while rerun=="Y" or rerun=="y":
    for i in range(3):
        print ("")
    print("Do you want to encrypt or decrypt a phrase?")
    print("1. Encrypt")
    print("2. Decrypt")

    option= input("--->")

    while option !="1"  and option!="2":
        print("Please choose a correct option(1 or 2)")
        option= input("--->")

    print("Input a phrase please")
    phrase= input("--->")
    
    if option == "1":
        final_word= K_enc(phrase)
        print ("")
        
        print(final_word)
    elif option == "2":
        final_word= K_dec(phrase)
        print ("")
        print(final_word)
    print("Want encrypt or decrypt anything else? Y/N")
    rerun=input("--->")

exit=input("Press enter to kill me :(")
