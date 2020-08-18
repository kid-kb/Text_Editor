from tkinter import *
from tkinter import filedialog
from tkinter.font import Font


class TextEditor:
    curr_open_file = "no_file"

    def open_file(self, event=""):
        file = filedialog.askopenfile(title="Select file to open")
        if file is None:
            return
        self.text_area.delete(1.0, END)
        for line in file:
            self.text_area.insert(END, line)
        self.curr_open_file = file.name
        file.close()

    def save_as_file(self, event=""):
        s_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if s_file is None:
            return
        text2save = self.text_area.get(1.0, END)
        self.curr_open_file = s_file.name
        s_file.write(text2save)
        s_file.close()

    def save_file(self):
        if self.curr_open_file == 'no_file':
            self.save_as_file()
        else:
            fi = open(self.curr_open_file, 'w+')
            fi.write(self.text_area.get(1.0, END))
            fi.close()

    def new_file(self, event=""):
        self.text_area.delete(1.0, END)
        self.curr_open_file = "no_file"

    def copy_txt(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut_txt(self):
        self.copy_txt()
        self.text_area.delete("sel.first", "sel.last")

    def paste_txt(self):
        self.text_area.insert(INSERT, self.text_area.clipboard_get())

    def __init__(self, master):
        self.master = master
        self.master.title("Textpad")

        my_font = Font(family="Comic Sans Ms", size=14)
        self.text_area = Text(self.master, undo=TRUE,font=my_font)
        self.text_area.pack(fill=BOTH, expand=1)

        self.main_menu = Menu(self.master)
        self.master.config(menu=self.main_menu)

        # creating file menu
        self.file_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New   ⌘+N", command=self.new_file)
        self.file_menu.add_command(label="Open  ⌘+O", command=self.open_file)

        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save as   ⌘+S", command=self.save_as_file)

        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=self.master.quit)

        # creating edit menu
        self.edit_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut   ⌘+X", command=self.cut_txt)
        self.edit_menu.add_command(label="Copy  ⌘+C", command=self.copy_txt)
        self.edit_menu.add_command(label="Paste ⌘+V", command=self.paste_txt)

        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)


root = Tk()
te = TextEditor(root)
root.bind('<Command-n>', te.new_file)
root.bind('<Command-o>', te.open_file)
root.bind('<Command-s>', te.save_as_file)

root.mainloop()
