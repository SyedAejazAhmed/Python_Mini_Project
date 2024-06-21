import sqlite3
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog

KV = '''
ScreenManager:
    LoginScreen:
    ChatScreen:

<LoginScreen>:
    name: 'login'

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "Welcome to ChatBot"
            halign: 'center'
            theme_text_color: 'Primary'
            font_style: 'H4'
            size_hint_y: None
            height: self.texture_size[1]

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(20)

            MDTextField:
                id: username
                hint_text: "Username"
                mode: "rectangle"
                on_text_validate: app.login(username.text, password.text)

            MDTextField:
                id: password
                hint_text: "Password"
                password: True
                mode: "rectangle"
                on_text_validate: app.login(username.text, password.text)

            MDRaisedButton:
                text: "Login"
                pos_hint: {'center_x': 0.5}
                size_hint: (None, None)
                size: dp(100), dp(50)
                on_press: app.login(username.text, password.text)

            MDRaisedButton:
                text: "Register"
                pos_hint: {'center_x': 0.5}
                size_hint: (None, None)
                size: dp(100), dp(50)
                on_press: app.register(username.text, password.text)

<ChatScreen>:
    name: 'chat'

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        MDLabel:
            id: chat_history
            text: "Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.\\n"
            size_hint_y: None
            height: dp(400)
            theme_text_color: 'Primary'

        MDBoxLayout:
            size_hint_y: None
            height: dp(50)
            spacing: dp(10)

            MDTextField:
                id: user_input
                hint_text: "Type your message here"
                mode: "rectangle"
                on_text_validate: app.on_button_press(user_input.text)

            MDRaisedButton:
                id: send_button
                text: "Send"
                size_hint: (None, None)
                size: dp(80), dp(50)
                on_press: app.on_button_press(user_input.text)
'''

def create_user_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
    return True

def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None

def chatbot_response(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I help you today?"
    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm here to help you!"
    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day!"
    elif 'name' in user_input:
        return "I am a simple chatbot created to assist you."
    elif 'help' in user_input:
        return "Sure! How can I assist you today?"
    elif 'weather' in user_input:
        return "I can't check the weather right now, but you can try asking a weather service."
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

class LoginScreen(Screen):
    pass

class ChatScreen(Screen):
    pass

class ChatBotApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.screen_manager = Builder.load_string(KV)
        return self.screen_manager

    def login(self, username, password):
        if authenticate_user(username, password):
            self.show_chat_screen()
        else:
            self.show_dialog("Login failed", "Invalid username or password")

    def register(self, username, password):
        if add_user(username, password):
            self.show_dialog("Registration successful", "You can now login with your credentials")
        else:
            self.show_dialog("Registration failed", "Username already exists")

    def show_dialog(self, title, message):
        dialog = MDDialog(title=title, text=message, size_hint=(0.8, 1))
        dialog.open()

    def show_chat_screen(self):
        self.screen_manager.current = 'chat'

    def on_button_press(self, user_message):
        if user_message.lower() == 'bye':
            self.update_chat_history("Goodbye! Have a great day!")
            self.screen_manager.get_screen('chat').ids.user_input.disabled = True
            self.screen_manager.get_screen('chat').ids.send_button.disabled = True
        else:
            response = chatbot_response(user_message)
            self.update_chat_history(f"You: {user_message}")
            self.update_chat_history(f"Chatbot: {response}")
            self.screen_manager.get_screen('chat').ids.user_input.text = ""

    def update_chat_history(self, message):
        chat_history = self.screen_manager.get_screen('chat').ids.chat_history
        chat_history.text += message + "\n"
        chat_history.height += 20

if __name__ == "__main__":
    create_user_table()
    ChatBotApp().run()
