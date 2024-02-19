from tool import *

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', None)
root.mainloop()