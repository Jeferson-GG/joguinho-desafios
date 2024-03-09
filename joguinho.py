import tkinter as tk
import random

# Cores
BACKGROUND_COLOR = "#722f37"
TEXT_COLOR = "#ffffff"
BUTTON_COLOR = "#9b5069"
BUTTON_TEXT_COLOR = "#ffffff"

# Configurações dos Widgets
BUTTON_STYLE = {"bg": BUTTON_COLOR, "fg": BUTTON_TEXT_COLOR, "padx": 10, "pady": 5, "borderwidth": 0, "relief": tk.FLAT}
LABEL_STYLE = {"bg": BACKGROUND_COLOR, "fg": TEXT_COLOR}
FRAME_STYLE = {"bg": BACKGROUND_COLOR}

# Variáveis globais
players = []
current_player_index = 0

# Início da configuração das variáveis globais da GUI
root = tk.Tk()
root.title("Gerador de Desafios")
root.configure(bg=BACKGROUND_COLOR)  # Define a cor de fundo da janela principal

# Definindo um tamanho fixo para a janela e impedindo o redimensionamento
window_width = 600
window_height = 400
root.geometry(f"{window_width}x{window_height}")
root.resizable(False, False)  # Impede o redimensionamento da janela

players_text = tk.StringVar()
challenge_text = tk.StringVar()
main_players_list_text = tk.StringVar()

def generate_challenge():
    challenges = [
        "Escreva um programa para calcular a soma de uma lista de números.",
        "Implemente um jogo da forca.",
        "Crie um gerador de senhas seguras.",
        "Desenvolva um programa para contar quantas vezes cada palavra aparece em um texto.",
        "Projete um sistema de cadastro de alunos para uma escola.",
        "Escreva um algoritmo para encontrar o maior número em uma lista.",
        "Crie uma calculadora que realize operações básicas (adição, subtração, multiplicação, divisão).",
        "Desenvolva um programa para verificar se uma palavra é um palíndromo.",
        "Implemente o jogo da velha.",
        "Crie um programa para converter temperatura de Celsius para Fahrenheit e vice-versa."
    ]
    return random.choice(challenges)

def show_challenge():
    global current_player_index
    if players:
        current_player = players[current_player_index]
        challenge_text.set(f"{current_player}, seu desafio é:\n\n{generate_challenge()}")
        current_player_index = (current_player_index + 1) % len(players)
    else:
        challenge_text.set("Adicione jogadores para começar.")

def add_player():
    player_name = player_entry.get()
    if player_name:
        players.append(player_name)
        player_entry.delete(0, tk.END)
        update_players_list()

def update_players_list():
    players_text.set("Jogadores:\n" + "\n".join(players))
    main_players_list_text.set("Jogadores:\n" + "\n".join(players))

def show_add_players_screen():
    main_frame.pack_forget()  # Esconde a tela de desafios
    add_players_frame.pack(padx=20, pady=20)  # Mostra a tela para adicionar jogadores novamente

def show_start_screen():
    start_frame.pack_forget()  # Esconde a tela de início
    add_players_frame.pack(padx=20, pady=20)  # Mostra a tela para adicionar jogadores

def start_game():
    add_players_frame.pack_forget()  # Esconde a tela de adicionar jogadores
    main_frame.pack(padx=20, pady=20)  # Mostra a tela principal de desafios

def setup_start_screen():
    global start_frame
    start_frame = tk.Frame(root, **FRAME_STYLE)
    start_frame.pack(padx=20, pady=20)
    start_game_button = tk.Button(start_frame, text="Iniciar Jogo", command=show_start_screen, **BUTTON_STYLE)
    start_game_button.pack(pady=10)

def setup_add_players_screen():
    global add_players_frame, player_entry
    add_players_frame = tk.Frame(root, **FRAME_STYLE)
    player_entry = tk.Entry(add_players_frame, width=30, relief=tk.FLAT, borderwidth=0, insertbackground=TEXT_COLOR)
    player_entry.pack(pady=5)
    add_player_button = tk.Button(add_players_frame, text="Adicionar Jogador", command=add_player, **BUTTON_STYLE)
    add_player_button.pack(pady=5)
    players_label = tk.Label(add_players_frame, textvariable=players_text, **LABEL_STYLE)
    players_label.pack(pady=5)
    start_button = tk.Button(add_players_frame, text="Começar", command=start_game, **BUTTON_STYLE)
    start_button.pack(pady=10)

def setup_main_screen():
    global main_frame
    main_frame = tk.Frame(root, **FRAME_STYLE)
    players_list_label = tk.Label(main_frame, textvariable=main_players_list_text, **LABEL_STYLE)
    players_list_label.pack(pady=10)
    challenge_label = tk.Label(main_frame, textvariable=challenge_text, wraplength=300, **LABEL_STYLE)
    challenge_label.pack(pady=10)
    generate_button = tk.Button(main_frame, text="Novo Desafio", command=show_challenge, **BUTTON_STYLE)
    generate_button.pack(pady=5)
    back_button = tk.Button(main_frame, text="Voltar", command=show_add_players_screen, **BUTTON_STYLE)
    back_button.pack(pady=10)

setup_start_screen()
setup_add_players_screen()
setup_main_screen()

root.mainloop()
