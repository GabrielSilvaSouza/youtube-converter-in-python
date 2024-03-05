from tkinter import *
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def download_video(url, filepath):
    yt = YouTube(url, on_progress_callback=progress_callback)
    video = yt.streams.get_highest_resolution()
    video.download(f'{filepath}')
    return video.default_filename

def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress_bar['value'] = percentage_of_completion
    root.update_idletasks() 

def convert_to_mp3(video_name, filepath):
    video = AudioFileClip(f'{filepath}/{video_name}')
    video.write_audiofile(f'{filepath}/{video_name[:-4]}.mp3')
    return video_name[:-4]

def assembling():
    try:
        video_name = download_video(url.get(), filepath.get())
        audio_name = convert_to_mp3(video_name, filepath.get())
        os.remove(f'{filepath.get()}/{video_name}')
        show_message("Conversão concluída com sucesso!")
        progress_bar['value'] = 0  # Reset the progress bar
        root.update_idletasks()  # Update the GUI
        return audio_name
    except ValueError as e:
        show_message(f"Erro: {str(e)}")

def select_folder():
    root.folder_selected = filedialog.askdirectory()
    filepath.set(root.folder_selected)

def show_message(message):
    messagebox.showinfo("Youtube Converter", message)

def update_progress(progress):
    progress_bar['value'] = progress

root = Tk()
root.title("Youtube Converter")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Adicionando um texto de tutorial
tutorial_text = "Bem-vindo ao Youtube Converter!\n\nPara começar, cole o link do vídeo do YouTube no campo ao lado esquerdo. Em seguida, clique em 'Selecione a Pasta' para escolher onde salvar o arquivo de áudio convertido. Por fim, clique em 'Converter'."
tutorial_label = Label(mainframe, text=tutorial_text, justify='left', wraplength=400)
tutorial_label.grid(column=3, row=2, rowspan=4, padx=10, pady=10, sticky=(N, E, S, W))

# Adicionando os créditos
creditos_texto = "Desenvolvido por: Bergs"
creditos_label = Label(mainframe, text=creditos_texto, justify='left', font=('Helvetica', 12, 'bold'))
creditos_label.grid(column=3, row=7, padx=10, pady=10, sticky=(N, E))

url = StringVar()
link_entry = ttk.Entry(mainframe, width=50, textvariable=url, justify='center')
link_entry.grid(column=1, row=2, columnspan=2, sticky=(W, E), padx=10, pady=5)
ttk.Label(mainframe, text="Link do Vídeo").grid(column=1, row=1, sticky=(W, E), padx=10)

button = Button(mainframe, text="Selecione a Pasta", command=select_folder, bg="#007bff", fg="white")
button.grid(column=1, row=4, columnspan=2, sticky=(W, E), padx=10, pady=5)

filepath = StringVar()
label_path = Label(mainframe, textvariable=filepath).grid(column=1, row=5, columnspan=2, sticky=(W, E), padx=10, pady=5)

convert_button = ttk.Button(mainframe, text='Converter', command=assembling, style='My.TButton')
convert_button.grid(column=1, row=6, columnspan=2, sticky=(W, E), padx=10, pady=5)

# Barra de progresso
progress_bar = ttk.Progressbar(mainframe, orient='horizontal', mode='determinate', length=200)
progress_bar.grid(column=1, row=7, columnspan=2, sticky=(W, E), padx=10, pady=5)

# Estilo personalizado para o botão de conversão
style = ttk.Style()
style.configure('My.TButton', background='#28a745', borderwidth=0, lightcolor='#28a745', darkcolor='#28a745')  # Cor de fundo menos transparente

root.mainloop()




