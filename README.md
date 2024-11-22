# Rock Paper Scissors Networking Game

A simple command-line multiplayer Rock-Paper-Scissors game implemented in Python using basic networking principles. One player acts as the server, while the other connects as the client. The game exchanges choices between players over a socket connection and determines the winner for each round.

---

## Features
- Multiplayer gameplay over a network.
- Human-readable output for clear round results.
- Randomized server port to avoid port reuse issues.
- Easy-to-use command-line interface.

---

## How It Works
1. The server starts and listens for a connection on a randomly assigned port.
2. The client connects to the server using the provided IP and port.
3. Players take turns making their choices (`rock`, `paper`, `scissors`, or `quit`).
4. Choices are exchanged, and the results are displayed after each round in a clear and formatted output.
5. The game ends when either player chooses `quit`.

---

## Installation
1. Clone this repository or download the source code.
2. Ensure you have Python 3 installed on your system.

---

## How to Run

### Server
- Run the server with: 
    ``` python server.py <Your Name> ```
- Example: 
    ``` python server.py Alice ```
- The server will display its randomly assigned port for the client to connect.

### Client
- Run the client with:
    ``` python client.py <Your Name> <Server Host> <Server Port> ```
- Example;
    ``` python client.py Bob 127.0.0.1 54321 ```
- Replace ```<Server Host>``` and ```<Server Port>``` with the values shown by the server.

## Gameplay Example

### Server:
```
Server started on 127.0.0.1:54321. Waiting for a connection...
Connection established with ('127.0.0.1', 12345)
Your opponent is Bob.

********************
RPS
YOU (Alice): rock ||| OPPONENT (Bob): scissors
Result: Alice wins!
********************
```

### Client:
```
Connected to server 127.0.0.1:54321
Your opponent is Alice.

********************
RPS
YOU (Bob): scissors ||| OPPONENT (Alice): rock
Result: Alice wins!
********************
```

## Future Improvements
- Add a scoring system to track wins, losses, and ties.
- Implement a rematch feature without restarting the program.
- Encrypt communication between server and client for added security.