
message = input("Enter the Messsage: ")

key = int(input("Enter the Key: "))

encrypted_message = ""
for c in message:
    bit = ord(c) # ascii value
    encry_bit = bit^key
    encry_char = chr(encry_bit)
    encrypted_message+=encry_char
    print(c,encry_bit,encry_char)
    # print(c)


print("Original Message: ",message,"\nEncrypted Message: ",encrypted_message)