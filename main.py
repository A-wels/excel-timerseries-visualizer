from pandas import read_excel
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, simpledialog
from functools import partial

df = ""
variables = []
buttons = []
class GUI:
    def __init__(self, master):
        tk.Button(master, text="Andere Datei wählen", command = partial(load_table, master)).pack(padx=10,pady=10, side=tk.TOP)
        tk.Label(master,
            text="Wähle zu visualisierende Spalten",
            padx = 20).pack()
        build_layout(master)

def fit_data(df):
    # fit data and return it
    df=(df-df.mean())/df.std()

    return df

def load_table(widget=""):
    global df
    global buttons

    dialog = tk.Tk()
    path = filedialog.askopenfilename()
    dialog.withdraw()
    df = read_excel(path)
    
    if widget != '':
        build_layout(widget)

def build_layout(widget):
    global variables
    global buttons

    for btn in buttons:
        btn.destroy()
    buttons.clear
    variables.clear()

    master = widget


   
    variables = []


    for index, c in enumerate(df.columns):
        variables.append(tk.IntVar(widget))
        btn = tk.Checkbutton(widget, text=c, padx=10, variable=variables[index])
        buttons.append(btn)
        btn.pack()

    vis = tk.Button(widget, text="Visualisieren", command = partial(visualize, df.columns))
    buttons.append(vis)
    vis.pack(padx=5, pady = 10, side=tk.LEFT)


    close = tk.Button(widget, text="Beenden", command=widget.quit)
    buttons.append(close)
    close.pack(padx=10, pady=10,side=tk.RIGHT)
            


def visualize(column_names):
    global variables
    global df
    selected = []
    for i in range(len(variables)):
        if variables[i].get() == 1:
            selected.append(column_names[i])
    scatter_plot(df,selected)




def scatter_plot(dataframe, column_names):
    colors = ['b','r','g']
    i = 0
    for df in column_names:
        plt.scatter(x=range(len(dataframe[df])), y=dataframe[df], c=colors[i], label=df)
        i+=1

    plt.legend()
    plt.show()


if __name__ == '__main__':
    load_table()
    df = fit_data(df)
    root = tk.Tk()
    root.title("Data visualizer")
    gui = GUI(root)
    root.mainloop()

