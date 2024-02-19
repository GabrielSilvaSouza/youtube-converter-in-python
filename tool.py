from tkinter import *
from tkinter import ttk, filedialog, Entry
from conversor import *

def assembling(*args):
    try:
        video_name = download_video(url.get(), filepath.get())
        audio_name = convert_to_mp3(video_name, filepath.get())
        os.remove(f'{filepath.get()}/{video_name}')
        return audio_name
    
    except ValueError:
        pass

def select_folder():
    Tk().withdraw()
    selection = filedialog.askdirectory()
    entry.delete(0, 'end')
    entry.insert(0, selection)
    filepath.set(selection)

    return selection



root = Tk()
root.title("Youtube Conveter")

entry = Entry(root)


mainframe = ttk.Frame(root, padding="3 3 200 200")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

url = StringVar()
link_entry = ttk.Entry(mainframe, width=50, textvariable=url, justify='center')
link_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Link").grid(column=1, row=1, sticky=E)


button = Button(mainframe, text="Select Folder", command=select_folder)
button.grid(column=2, row=2, sticky=W)

filepath = StringVar()
label_path = Label(mainframe, textvariable=filepath).grid(column=1, row=2, sticky=E)


ttk.Button(mainframe, text='Converter', command=assembling).grid(column=3, row=3, sticky=W)

