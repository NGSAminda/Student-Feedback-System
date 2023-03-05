from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Crypto.Cipher import AES
import os
import secrets

key = secrets.token_bytes(32)  # 32 bytes for AES-256
iv = secrets.token_bytes(16)  # 16 bytes for AES


root = Tk()
frame_header = ttk.Frame(root)
frame_header.pack()
headerlabel = ttk.Label(frame_header, text='STUDENT FEEDBACK SYSTEM', foreground='blue',
                        font=('Arial', 24))
headerlabel.grid(row=0, column=1)
messagelabel = ttk.Label(frame_header,
                         text='PLEASE TELL US WHAT YOU THINK ABOUT LECTURERS',
                         foreground='Red', font=('Arial', 10))
messagelabel.grid(row=1, column=1)

frame_content = ttk.Frame(root)
frame_content.pack()
#     def submit():
#     username = entry_name.get()
#     print(username)
myvar = StringVar()
var = StringVar()
# cmnt= StringVar()
namelabel = ttk.Label(frame_content, text='Index No')
namelabel.grid(row=0, column=0, padx=5, sticky='sw')
entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar)
entry_name.grid(row=1, column=0)

emaillabel = ttk.Label(frame_content, text='Lecture ID')
emaillabel.grid(row=0, column=1, sticky='sw')
entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=var)
entry_email.grid(row=1, column=1)

commentlabel = ttk.Label(frame_content, text='Your Feedback', font=('Arial', 10))
commentlabel.grid(row=2, column=0, sticky='sw')
textcomment = Text(frame_content, width=55, height=10)
textcomment.grid(row=3, column=0, columnspan=2)


textcomment.config(wrap ='word')
# def clear():
#     textcomment.delete(1.0,'end')
def clear():
    global entry_name
    global entry_email
    global textcomment
    messagebox.showinfo(title='clear', message='Do you want to clear?')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)


def submit():
    global entry_name
    global entry_email
    global textcomment
    global encrypted_feedback

    # print("\n")
    print("\n")
    print("Tihs information shows only Lecture UI")
    print("\n")
    print('Name:{}'.format(myvar.get()))
    print('Lecture ID:{}'.format(var.get())) 
    feedback = textcomment.get(1.0, END)
    encrypted_feedback = encrypt_feedback(feedback, key, iv)
    messagebox.showinfo(title='Encrypted Feedback',message='Thank you for your Feedback')
    message=encrypted_feedback
    print(message)
    
    # print("\n")
    print("\n")
    print("*****************************************************************")
    print("Tihs Decypted Message show only for Admin UI")
    print('Student Feedback:',feedback)
    # dmessage= decrypted_feedback
    # print(dmessage)
    # entry_name.delete(0, END)
    # entry_email.delete(0, END)
    # textcomment.delete(1.0, END)
    #feedback = textcomment.get(1.0,END)



def encrypt_feedback(feedback, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    feedback_bytes = feedback.encode()
    padded_feedback_bytes = feedback_bytes + b' ' * (AES.block_size - len(feedback_bytes) % AES.block_size)
    ciphertext = cipher.encrypt(padded_feedback_bytes)
    return ciphertext


def decrypt_feedback(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_feedback_bytes = cipher.decrypt(ciphertext)
    feedback_bytes = padded_feedback_bytes.rstrip(b' ')
    feedback = feedback_bytes.decode()
    return feedback

# def  decrypt_feedback():
#     global encrypted_feedback
#     feedback = decrypt_feedback(encrypted_feedback, key, iv)
#     print(feedback)


submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=4, column=0, sticky='e')
clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=4, column=1, sticky='w')
# test_decrypt_feedback()


mainloop()
