# Tic Tac Toe App with User Authentication
This repository contains a Kivy-based Tic Tac Toe game application with user authentication using SQLite. The game offers different difficulty levels and allows users to register and log in to play.

## Features
1. User registration and login system using SQLite.
2. Three difficulty levels for the Tic Tac Toe game: Easy, Medium, and Hard.
3. AI opponent with varying difficulty.
4. Kivy-based graphical user interface.

## Getting Started
### Prerequisites
1. Python 3.x
2. Kivy (version 2.0.0 or higher)
3. SQLite

Clone the repository:
```bash
git clone https://github.com/SyedAejazAhmed/Python_Mini_Project.git
cd Tic_Tac_Toe
```

## Code Explanation
### SQLite Database Functions
1. create_user_table(): Creates the users table if it does not exist.
2. add_user(username, password): Adds a new user to the database.
3. authenticate_user(username, password): Authenticates a user based on provided credentials.

### AI and Game Logic Functions
1. check_winner(board): Checks the board for a winner or draw.
2. minimax(board, depth, is_maximizing, alpha, beta): Implements the Minimax algorithm with alpha-beta pruning for the hard difficulty AI.
3. random_move(board): Makes a random move for the AI.
4. ai_move(board, difficulty): Decides the AI move based on the selected difficulty level.

### Kivy App
1. LoginScreen: A Kivy screen for user login and registration.
2. DashboardScreen: A Kivy screen for selecting the game difficulty.
3. GameScreen: A Kivy screen for playing the Tic Tac Toe game.
4. TicTacToeApp: The main Kivy application class that manages screens and handles user interactions.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
1. Kivy for the graphical framework.
2. SQLite for the database.

## Contact
If you have any questions or suggestions, feel free to open an issue or contact me at 'syed.aejaz.ahmed2006@gmail.com'.

Thank you for checking out this project! Have fun playing `Tic Tac Toe!`


