#Declaration of required variables
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
choice=input("Type 'encode' to encrpt and decode to decrypt:\n").lower()
text=input(f"Enter text to {choice}:\n").lower()
shift=int(input("Enter shift number:\n"))

#Encrypt
def Encrypt(original_text,shift_amount):
    encrypted_text=""
    for letter in original_text:
        shifted_position=alphabets.index(letter)+shift_amount
        encrpted_text+=alphabets[shifted_position]
    print(encrypted_text)
                
if choice=="encode":
    Encrypt(text,shift)
            