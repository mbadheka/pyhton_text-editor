import tkinter as tk
from tkinter import Label, image_types, ttk
from PIL import Image,ImageTk
from tkinter import filedialog,font,colorchooser,messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x720') #setting up resolution of main application 
main_application.title('Text Editor')

#codding of Main Menu
main_menu = tk.Menu(main_application)

# Import Icon Filemenu
new_icon = ImageTk.PhotoImage(Image.open(r'D:\python_code\text_editor\icon_pack/new.png').resize((24,24),Image.ANTIALIAS))
open_icon = ImageTk.PhotoImage(Image.open(r'D:\python_code\text_editor\icon_pack/open.png').resize((24,24),Image.ANTIALIAS))
save_icon = ImageTk.PhotoImage(Image.open(r'D:\python_code\text_editor\icon_pack/save.png').resize((24,24),Image.ANTIALIAS))
save_as_icon = ImageTk.PhotoImage(Image.open(r'D:\python_code\text_editor\icon_pack/save_as.png').resize((24,24),Image.ANTIALIAS))
exit_icon = ImageTk.PhotoImage(Image.open(r'D:\python_code\text_editor\icon_pack/exit.png').resize((24,24),Image.ANTIALIAS))

file =tk.Menu(main_menu, tearoff=False)

# Import Icon Edit menu
copy_icon = ImageTk.PhotoImage(Image.open(r'D:\python_code\text_editor\icon_pack/copy.png').resize((24,24),Image.ANTIALIAS))
cut_icon = ImageTk.PhotoImage(Image.open(r'D:\python_code\text_editor\icon_pack/cut.png').resize((24,24),Image.ANTIALIAS))
paste_icon = ImageTk.PhotoImage(Image.open(r'D:\python_code\text_editor\icon_pack/paste.png').resize((24,24),Image.ANTIALIAS))
clear_icon = ImageTk.PhotoImage(Image.open(r'D:\python_code\text_editor\icon_pack/clear.png').resize((24,24),Image.ANTIALIAS))
find_icon = ImageTk.PhotoImage(Image.open(r'D:\python_code\text_editor\icon_pack/find.png').resize((24,24),Image.ANTIALIAS))

edit =tk.Menu(main_menu, tearoff=False)

# Import Icon View menu
toolbar_icon = ImageTk.PhotoImage(Image.open(r'D:\python_code\text_editor\icon_pack/tool_bar.png').resize((24,24),Image.ANTIALIAS))
statusbar_icon = ImageTk.PhotoImage(Image.open(r'D:\python_code\text_editor\icon_pack/status_bar.png').resize((24,24),Image.ANTIALIAS))

view = tk.Menu(main_menu, tearoff=False)

# Import Icon Theme menu
light_default = tk.PhotoImage(file=r'D:\python_code\text_editor\icon_pack/light_default.png')
dark = tk.PhotoImage(file=r'D:\python_code\text_editor\icon_pack/dark.png')
red = tk.PhotoImage(file=r'D:\python_code\text_editor\icon_pack/red.png')
night_blue = tk.PhotoImage(file=r'D:\python_code\text_editor\icon_pack/night_blue.png')
monokai = tk.PhotoImage(file=r'D:\python_code\text_editor\icon_pack/monokai.png')
light_plus = tk.PhotoImage(file=r'D:\python_code\text_editor\icon_pack/light_plus.png')     

color_theme=tk.Menu(main_menu, tearoff=False) 

color_icon = (light_default,dark,red,night_blue,monokai,light_plus)
theme_dict = {
    'Light default':('#000000','#ffffff'),
    'Dark':('#00e0e0','#292928'),
    'Red':('#2d2d2d','#c90000'),
    'Night blue':('#f7fcff','#3e80b3'),
    'Monokai':('#66ff00','#4f4e4e'),
    'Light plus':('#474747','#e0e0e0')
}

Theme_choice = tk.StringVar()

main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Themre',menu=color_theme)

# ----------------------Coding of toolbar-------------------
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)
# ------fontbox------#
font_tuple = tk.font.families()
font_family =tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)
# ------font Size------#

size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width=10,textvariable=size_var,state='readonly')
font_size['values'] = tuple(range(8,62,2))
font_size.current(2)
font_size.grid(row=0,column=1,padx=5)

# bold button 
bold_icon = tk.PhotoImage(file=r'D:\python_code\text_editor\icon_pack/bold.png')
bold_button = ttk.Button(tool_bar,image=bold_icon)
bold_button.grid(row=0,column=2,padx=5)

# italic button 
italic_icon = tk.PhotoImage(file=r'D:\python_code\text_editor\icon_pack/italic.png')
italic_button = ttk.Button(tool_bar,image=italic_icon)
italic_button.grid(row=0,column=3,padx=5)

# underline button 
underline_icon = tk.PhotoImage(file=r'D:\python_code\text_editor\icon_pack/underline.png')
underline_button = ttk.Button(tool_bar,image=underline_icon)
underline_button.grid(row=0,column=4,padx=5)

# font color

font_color_icon = tk.PhotoImage(file=r'D:\python_code\text_editor\icon_pack/font_color.png')
font_button = ttk.Button(tool_bar,image=font_color_icon)
font_button.grid(row=0,column=5,padx=5)

# allignleft
alighnleft_icon = tk.PhotoImage(file=r'')
# allighn center
# align right

# coding of Main status bar

# -------------------------- Menus funcality Funcanality------------------------- 

# files Command --- 
file.add_command(label='New', image=new_icon, compound=tk.LEFT,accelerator='Ctrl+N')
file.add_command(label='Open', image=open_icon, compound=tk.LEFT,accelerator='Ctrl+O')
file.add_command(label='Save', image=save_icon, compound=tk.LEFT,accelerator='Ctrl+S')
file.add_command(label='Save as', image=save_as_icon, compound=tk.LEFT,accelerator='Ctrl+Alt+S')
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT,accelerator='Ctrl+Q')
# Edit Command ---
edit.add_command(label='Copy', image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C')
edit.add_command(label='Paste', image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V')
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X')
edit.add_command(label='Clear All',image=clear_icon,compound=tk.LEFT,accelerator='Ctrl+X')
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F')
# Vire Commnad-- 
view.add_checkbutton(label='Toolbar',image=toolbar_icon,compound=tk.LEFT)
view.add_checkbutton(label='StatusBar',image=statusbar_icon,compound=tk.LEFT)
# Theme Command
count = 0
for i in theme_dict:
    color_theme.add_radiobutton(label=i,image=color_icon[count], variable=Theme_choice,compound=tk.LEFT)
    count+=1

main_application.config(menu=main_menu)
main_application.mainloop()





