from tkinter import *


def readit():
    message = txt_msg.get("1.0",END) # take all data from textbox
    print("Read it: \n",message)

    key = int(txt_key.get("1.0",END))
    print("Key is: ",key)

    encrypted_message = ""
    for c in message:
        bit = ord(c)  # ascii value
        encry_bit = bit ^ key
        encry_char = chr(encry_bit)
        encrypted_message += encry_char
        # print(c, encry_bit, encry_char)
        # print(c)

    # print("Encrypted Message is: ",encrypted_message)
    txt_encry_msg.insert(END,encrypted_message)
root = Tk()
root.title("Screate Writer")
root.geometry('500x500+250+10')

main_label = Label(root,text="Message Here")
main_label.pack()

txt_msg = Text(root,height=10,width=30)
txt_msg.pack()


key_label = Label(root,text="Enter Key Here: ")
key_label.pack()

txt_key = Text(root,height=1,width=10)
txt_key.pack()

go_btn = Button(root,text="Magic",command=readit)
go_btn.pack()

txt_encry_msg = Text(root,height=10,width=30)
txt_encry_msg.pack()

root.mainloop()