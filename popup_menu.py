import tkinter as tk

def popup_menu(entry,root):
    popup_menu = tk.Menu(root, tearoff=False, bg="#f8f8ff", fg="#080808", activebackground="#3F61B0", activeforeground="white")
    popup_menu.add_command(label="Cut", command=lambda: (root.clipboard_append(entry.selection_get()), entry.delete(0, tk.END)))
    popup_menu.add_command(label="Copy", command=lambda: root.clipboard_append(entry.selection_get()))
    popup_menu.add_command(label="Paste", command=lambda: entry.insert(tk.END, root.clipboard_get()))
    popup_menu.add_command(label="Select All", command=lambda: entry.select_range(0, 'end'))

    def show_popup_menu(event):
        try:
            popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            popup_menu.grab_release()

    entry.bind("<Button-3>", show_popup_menu)