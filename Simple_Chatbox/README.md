# ChatBot App with User Authentication
This repository contains a Kivy-based application that implements a simple chatbot with user authentication using SQLite. The chatbot responds to basic text inputs, and users can register and log in to use the chatbot.

## Features
1. User registration and login system using SQLite.
2. Simple chatbot that responds to specific keywords and phrases.
3. Kivy-based graphical user interface.

## Getting Started
### Prerequisites
1. Python 3.x
2. Kivy
3. SQLite

Clone the repository: 
```bash
git clone https://github.com/SyedAejazAhmed/Python_Mini_Project.git
cd Simple_Chatbox
```

## Code Explanation
### SQLite Database Functions
1. create_user_table(): Creates the users table if it does not exist.
2. add_user(username, password): Adds a new user to the database.
3. authenticate_user(username, password): Authenticates a user based on provided credentials.

## Chatbot Response Function
chatbot_response(user_input): Generates a response to user input based on predefined keywords and phrases.

## Kivy App
1. LoginRegisterScreen: A Kivy layout for user login and registration.
2. ChatBotApp: The main Kivy application class that manages screens and handles user interactions.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
This project is inspired by the need for simple user authentication and chatbot interaction, serving as an educational example for learning Python, Kivy, and SQLite integration.
