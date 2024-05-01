import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Empate"
    elif (player_choice == "piedra" and computer_choice == "tijeras") or \
         (player_choice == "papel" and computer_choice == "piedra") or \
         (player_choice == "tijeras" and computer_choice == "papel"):
        return "¡Ganaste!"
    else:
        return "¡La computadora ganó!"

def rock_paper_scissors():
    choices = ["piedra", "papel", "tijeras"]

    print("¡Bienvenido al juego de piedra, papel o tijeras!")
    print("Selecciona tu jugada: piedra, papel o tijeras.")
    player_choice = input("Tu elección: ").lower()

    while player_choice not in choices:
        print("Elección inválida. Por favor, elige entre piedra, papel o tijeras.")
        player_choice = input("Tu elección: ").lower()

    computer_choice = random.choice(choices)
    print("La computadora eligió:", computer_choice)

    winner = determine_winner(player_choice, computer_choice)
    print(winner)

rock_paper_scissors()
