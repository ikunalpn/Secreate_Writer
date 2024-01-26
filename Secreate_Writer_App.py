from tkinter import *

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

go_btn = Button(root,text="Magic")

root.mainloop()