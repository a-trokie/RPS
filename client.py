import socket
import sys

def start_client(player_name, host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, int(port)))
    print(f"Connected to server {host}:{port}")

    client.sendall(player_name.encode())  # Send your name to the server
    opponent_name = client.recv(1024).decode()  # Receive opponent's name

    print(f"Your opponent is {opponent_name}.")

    while True:
        # Receive opponent's choice
        opponent_choice = client.recv(1024).decode()
        if opponent_choice == "quit":
            print(f"{opponent_name} ended the game.")
            break

        # Get player's choice
        choice = input(f"{player_name}, enter your choice ((r)ock, (p)aper, (s)cissors, quit to exit): ").strip().lower()
        if choice == "quit":
            client.sendall("quit".encode())
            print("Game ended.")
            break
        if choice not in ["rock", "paper", "scissors","r","p","s"]:
            print("Invalid choice. Try again.")
            continue

        if choice in ["r","p","s"]:
            match (choice):
                case "r":
                    choice = "rock"
                case "p":
                    choice = "paper"
                case "s":
                    choice = "scissors"
                case _:
                    break # don't really need this because im already error handling uptop

        # Send player's choice to the server
        client.sendall(choice.encode())

        # Display the result
        print("\n" + "*" * 20)
        print("~~~~RPS~~~~")
        print(f"YOU ({player_name}): {choice} ||| OPPONENT ({opponent_name}): {opponent_choice}")
        determine_winner(player_name, opponent_name, opponent_choice, choice)
        print("*" * 20 + "\n")

    client.close()

def determine_winner(player_name, opponent_name, choice1, choice2):
    if choice1 == choice2:
        print("Result: It's a draw!")
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "scissors" and choice2 == "paper") or \
         (choice1 == "paper" and choice2 == "rock"):
        print(f"Result: {opponent_name} wins!")
    else:
        print(f"Result: {player_name} wins!")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python client.py <Your Name> <Server Host> <Server Port>")
        sys.exit(1)
    player_name = sys.argv[1]
    server_host = sys.argv[2]
    server_port = sys.argv[3]
    start_client(player_name, server_host, server_port)
