# add your code here
# function to adjust the index based on the provided shift
def adjust_index(original_index : int, shift : int) -> int:
    adjusted_index = original_index + shift
    if adjusted_index >= 26 or adjusted_index <= -26:
        adjusted_index = adjusted_index % 26
            
    return adjusted_index

# function to encrypt a sentence
def encrypt(original_sentence : str, shift : int) -> str:
    alpha = "abcdefghijklmnopqrstuvwxyz"
    encrypted_sentence = ""

    for letter in original_sentence:
        if letter in alpha:
            letter_index = alpha.index(letter)
            adjusted_letter_index = adjust_index(letter_index, shift)
            encrypted_sentence += alpha[adjusted_letter_index]
        else:
            encrypted_sentence += letter
    
    return encrypted_sentence


# ask the user for the sentence to encrypt and convert it to lower case
original_sentence = input("Enter a sentence:")
original_sentence = original_sentence.lower()


# ask for the number of characters to shift and convert it to a number
# shift = input("Number of characters to shift:")
# shift = int(shift)
shift = 5

# encrypt the sentence
encrypted_sentence = encrypt(original_sentence, shift)

# print out the result
print(f"Encrypted sentence is: {encrypted_sentence}")
