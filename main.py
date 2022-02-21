import tkinter

window = tkinter.Tk()

f = open("./test/Test1.html", "r")
lines = f.readlines()
f.close()

for line in lines:
    line = line.strip()
    if "<h1>" in line:
        h1_content = line[4:-5]
        print(f"Heading 1: {h1_content}")
        var = tkinter.StringVar()
        text = tkinter.Label(window, textvariable=var)
        text.configure(font=("System", 26))
        var.set(h1_content)
        text.pack()
    elif "<h2>" in line:
        h2_content = line[4:-5]
        print(f"Heading 2: {h2_content}")
        var = tkinter.StringVar()
        text = tkinter.Label(window, textvariable=var)
        text.configure(font=("System", 20))
        var.set(h2_content)
        text.pack()
    elif "<p>" in line:
        p_content = line[3:-4]
        print(f"Paragraph: {p_content}")
        var = tkinter.StringVar()
        text = tkinter.Label(window, textvariable=var)
        text.configure(font=("System", 12))
        var.set(p_content)
        text.pack()
    elif "<title>" in line:
        title_content = line[7:-8]
        print(f"Page Title: {title_content}")
        window.title(title_content)

window.mainloop()