import socket
import sys

def start_server(player_name, host="127.0.0.1"):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, 0))  # Use port 0 to let OS pick a random available port
    server.listen(1)

    # Get the port the OS assigned
    port = server.getsockname()[1]
    print(f"Server started on {host}:{port}. Waiting for a connection...")

    conn, addr = server.accept()
    print(f"Connection established with {addr}")

    opponent_name = conn.recv(1024).decode()
    conn.sendall(player_name.encode())  # Send your name to the opponent

    print(f"Your opponent is {opponent_name}.")

    while True:
        # Get player's choice
        choice = input(f"{player_name}, enter your choice ((r)ock, (p)aper, (s)cissors, quit to exit): ").strip().lower()
        if choice == "quit":
            conn.sendall("quit".encode())
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


        # Send player's choice to opponent
        conn.sendall(choice.encode())

        # Receive opponent's choice
        opponent_choice = conn.recv(1024).decode()
        if opponent_choice == "quit":
            print(f"{opponent_name} quit the game.")
            break

        # Display the result
        print("\n" + "*" * 20)
        print("~~~~RPS~~~~")
        print(f"YOU ({player_name}): {choice} ||| OPPONENT ({opponent_name}): {opponent_choice}")
        determine_winner(player_name, opponent_name, choice, opponent_choice)
        print("*" * 20 + "\n")

    conn.close()

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
    if len(sys.argv) < 2:
        print("Usage: python server.py <Your Name>")
        sys.exit(1)
    player_name = sys.argv[1]
    start_server(player_name)
