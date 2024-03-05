import tkinter as tk
from tkinter import messagebox
import instaloader

def baixar_video_instagram():
    url = entry_url.get()
    nome_arquivo = entry_nome_arquivo.get()

    
    if not url or not nome_arquivo:
        messagebox.showerror("Erro", "Por favor, insira o URL do vídeo e o nome do arquivo.")
        return

    # Crie uma instância do Instaloader
    loader = instaloader.Instaloader()

    # Baixe apenas o vídeo
    try:
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
        
        # Verificar se há vídeos na postagem
        if post.typename == "GraphVideo":
            # Baixar o vídeo

            loader.download_post(post, target=f'{nome_arquivo}', post_filter=lambda post: post.typename == "GraphVideo")
            messagebox.showinfo("Sucesso", f"Download concluído. Arquivo de vídeo salvo como: {nome_arquivo}")
        else:
            messagebox.showerror("Erro", "Nenhum vídeo encontrado nesta postagem.")
    except instaloader.exceptions.InvalidArgumentException:
        messagebox.showerror("Erro", "O URL fornecido é inválido.")
    except instaloader.exceptions.ProfileNotExistsException:
        messagebox.showerror("Erro", "O perfil do Instagram não existe.")
    except instaloader.exceptions.PostChangedException:
        messagebox.showerror("Erro", "A postagem foi alterada.")
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        messagebox.showerror("Erro", "Este é um perfil privado e você não está seguindo.")
    except instaloader.exceptions.InstaloaderException as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")




# Configurações da janela principal
root = tk.Tk()
root.title("Download de Vídeo do Instagram")

# Tutorial de como usar
tutorial_text = """
Instruções:
1. Cole o URL do vídeo do Instagram no campo apropriado.
2. Escolha um nome para o arquivo de saída.
3. Clique no botão 'Baixar Vídeo' para iniciar o download.
"""

label_tutorial = tk.Label(root, text=tutorial_text, justify="left", padx=10, pady=10)
label_tutorial.grid(row=0, column=0, columnspan=2)

# Widgets
label_url = tk.Label(root, text="URL do vídeo do Instagram:")
label_url.grid(row=1, column=0, sticky="w", padx=10, pady=(0,5))
entry_url = tk.Entry(root, width=50, bd=2, relief="groove")
entry_url.grid(row=1, column=1, padx=10, pady=(0,5))

label_nome_arquivo = tk.Label(root, text="Nome do arquivo de saída:")
label_nome_arquivo.grid(row=2, column=0, sticky="w", padx=10, pady=(0,5))
entry_nome_arquivo = tk.Entry(root, width=50)
entry_nome_arquivo.grid(row=2, column=1, padx=10, pady=(0,5))

button_baixar = tk.Button(root, text="Baixar Vídeo", command=baixar_video_instagram, bg="#4CAF50", fg="white", padx=20)
button_baixar.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
