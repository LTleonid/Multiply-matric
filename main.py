from tkinter import *
 
root = Tk()
root.geometry("250x200")
root1 = Tk()
root1.geometry("200x250")
entX = Entry(root)
entX.pack()
entY = Entry(root1,)
entY.pack()
entx = Entry()
enty = Entry()
entx.pack()
enty.pack()
def work(): 
    need = 0
    mult_mat = [ [0]*int(entX.get()) for i in range(int(entY.get()))]
    maty = [ [0]*int(entX.get()) for i in range(int(entY.get()))]
    matx = [ [0]*int(entX.get()) for i in range(int(entY.get()))]
    matyENT = str(enty.get()).split("/")
    matxENT = str(entx.get()).split(" ")
    for y in range(int(entY.get())):
        for x in range(int(entX.get())):
            maty[y][x] = matyENT[need]
            need += 1
    print(maty)
    need = 0
    for y in range(int(entY.get())):
        for x in range(int(entX.get())):
            matx[y][x] = matxENT[need]
            need += 1
    print(matx)
    for y in range (int(entY.get())):
        for x in range(int(entX.get())):
            mult_mat[y][x] = int(matx[y][x]) * int(maty[x][y])
            print(f"{matx[y][x]} * {maty[x][y]} = {mult_mat[y][x]}")
    lbl["text"] = mult_mat
btn = Button(text="WORK PLEASE",command= work)
btn.pack()
lbl = Label(text = " ")
lbl.pack()
root1.mainloop()
root.mainloop()