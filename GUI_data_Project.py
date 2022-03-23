from tkinter import * 
from tkinter import messagebox
#import CSV_Read

def work():
    file=file_value.get()
    import pandas as pd


    file=str(input())

    df = pd.read_csv(file)

    print(df.to_string())


window=Tk()
window.title('DATA ANALYTICS ')
window.geometry('1000x500')
lab=Label(window,text="ENTER THE FILE:",fg='black')
lab.place(x=100,y=50)
file_value=Entry(window,width=250)
file_value.place(x=100,y=100)

button=Button(window,text="ENTER",fg="blue",command=work)
button.pack()



window.mainloop()