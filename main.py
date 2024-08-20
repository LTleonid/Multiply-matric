import tkinter as tk
root = tk.Tk()

def result():
    matrix_x = int(matrix_X.get())
    matrix_y = int(matrix_Y.get())
    matrix1 = [["0" if entry_vars1[row][col].get() == "" else entry_vars1[row][col].get() for col in range(matrix_x)] for row in range(matrix_y)]
    matrix2 = [["0" if entry_vars1[row][col].get() == "" else entry_vars1[row][col].get() for col in range(matrix_x)] for row in range(matrix_y)]
    mult_mat = [[0]*matrix_x for i in range(matrix_y)]
    
    for y in range (matrix_y):
        for x in range(matrix_x):
            mult_mat[y][x] = int(matrix1[y][x]) * int(matrix2[x][y])
            print(f"{matrix1[y][x]} * {matrix2[x][y]} = {mult_mat[y][x]}")
    for row in range(matrix_y):
        for col in range(matrix_x):
            entry = tk.Entry(result_window, width=5)
            entry.insert(0,mult_mat[row][col])
            entry.grid(row=row, column=col, padx=5, pady=5)
def create_matrix():
    global entry_vars1, entry_vars2
    matrix_x = int(matrix_X.get())
    matrix_y = int(matrix_Y.get())
    
    entry_vars1 = [[tk.StringVar() for _ in range(matrix_x)] for _ in range(matrix_y)]
    entry_vars2 = [[tk.StringVar() for _ in range(matrix_x)] for _ in range(matrix_y)]
    
    for row in range(matrix_y):
        for col in range(matrix_x):
            entry = tk.Entry(matrix1_window, textvariable=entry_vars1[row][col], width=5)
            entry.grid(row=row, column=col, padx=5, pady=5)
    
    for row in range(matrix_y):
        for col in range(matrix_x):
            entry = tk.Entry(matrix2_window, textvariable=entry_vars2[row][col], width=5)
            entry.grid(row=row, column=col, padx=5, pady=5)
        
matrix1_window = tk.Toplevel(root)
matrix2_window = tk.Toplevel(root)
result_window = tk.Toplevel(root)
entry_vars1= []
entry_vars2= []
matrix_X = tk.Entry(root)
matrix_X.insert(0, 0)
matrix_Y = tk.Entry(root)
matrix_Y.insert(0, 0)
create_matrixs = tk.Button(root,text="Create Matrixs", command=create_matrix)
get_result = tk.Button(root, command=result, text = "Result")

matrix_X.pack()
matrix_Y.pack()
create_matrixs.pack()
get_result.pack()
root.mainloop()

