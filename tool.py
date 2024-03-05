from tkinter import *
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Youtube Converter")
        self.master.geometry("800x250")
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        self.url = StringVar()
        self.filepath = StringVar()
        style = ttk.Style()

        self.creditos_texto = 'Desenvolvido por: Bergs'
        self.creditos_label = Label(self, text=self.creditos_texto, justify='left', wraplength=400)
        self.creditos_label.grid(column=3, row=7, rowspan=4, padx=10, pady=10, sticky=(N, E, S, W))


        self.url_entry = ttk.Entry(self, width=50, textvariable=self.url, justify='center')
        self.url_entry.grid(column=1, row=2, columnspan=2, sticky=(W, E), padx=10, pady=5)
        ttk.Label(self, text="Link do Vídeo").grid(column=1, row=1, sticky=(W, E), padx=10)

        self.select_folder_button = ttk.Button(self, text="Selecione a Pasta", command=self.select_folder)
        self.select_folder_button.grid(column=1, row=4, columnspan=2, sticky=(W, E), padx=10, pady=5)

        self.convert_button = ttk.Button(self, text="Converter", command=self.assembling)
        self.convert_button.grid(column=1, row=6, columnspan=2, sticky=(W, E), padx=10, pady=5)

        self.progress_bar = ttk.Progressbar(self, orient=HORIZONTAL, length=100, mode='determinate')
        self.progress_bar.grid(column=1, row=7, columnspan=2, sticky=(W, E), padx=10, pady=5)

        self.tutorial_text = "Bem-vindo ao Youtube Converter!\n\nPara começar, cole o link do vídeo do YouTube no campo ao lado esquerdo. Em seguida, clique em 'Selecione a Pasta' para escolher onde salvar o arquivo de áudio convertido. Por fim, clique em 'Converter'."
        self.tutorial_label = Label(self, text=self.tutorial_text, justify='left', wraplength=400)
        self.tutorial_label.grid(column=3, row=2, rowspan=4, padx=10, pady=10, sticky=(N, E, S, W))

        self.label_path = Label(self, textvariable=self.filepath).grid(column=1, row=5, columnspan=2, sticky=(W, E), padx=10, pady=5)

        style.configure('My.TButton', foreground='green', background='white')

    def download_video(self, url, filepath):
        yt = YouTube(url, on_progress_callback=self.progress_callback)
        video = yt.streams.get_highest_resolution()
        video.download(f'{filepath}')
        return video.default_filename

    def progress_callback(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        self.progress_bar['value'] = percentage_of_completion
        self.update_idletasks()

    def convert_to_mp3(self, video_name, filepath):
        video = AudioFileClip(f'{filepath}/{video_name}')
        video.write_audiofile(f'{filepath}/{video_name[:-4]}.mp3')
        return video_name[:-4]
    
    def assembling(self):
        try:
            video_name = self.download_video(self.url.get(), self.filepath.get())
            audio_name = self.convert_to_mp3(video_name, self.filepath.get())
            os.remove(f'{self.filepath.get()}/{video_name}')
            self.show_message("Conversão concluída com sucesso!")
            self.progress_bar['value'] = 0  # Reset the progress bar
            self.update_idletasks()  # Update the GUI
            return audio_name
        except ValueError as e:
            self.show_message(f"Erro: {str(e)}")

    def select_folder(self):
        self.folder_selected = filedialog.askdirectory()
        self.filepath.set(self.folder_selected)

    def show_message(self, message):
        messagebox.showinfo("Youtube Converter", message)

    def update_progress(self, progress):
        self.progress_bar['value'] = progress

root = Tk()
myapp = App(root)
myapp.mainloop()
    
