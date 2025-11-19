import tkinter as tk
window = tk.Tk()

for i in range(8):
    for j in range(8):
        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=2)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f'Row {i} \n {j}')
        label.pack()

        window.mainloop()