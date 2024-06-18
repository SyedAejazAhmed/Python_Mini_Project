from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from kivy.graphics import Color, Rectangle
from kivy.config import Config
from kivy.uix.popup import Popup
import random
import string

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '300')

class PasswordGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"
        self.padding = [20, 20, 20, 20]  # Padding around the layout
        self.spacing = 10  # Spacing between elements
        
        with self.canvas.before:
            Color(0, 0.5, 0.8, 1)  # Background color
            self.blue_rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        # Title label
        self.title_label = Label(
            text="Enter the password length", 
            size_hint=(1, None), 
            height=40,
            font_size='20sp', 
            color=(1, 1, 1, 1)  # White text color for better readability
        )
        self.add_widget(self.title_label)
        
        # Password length input
        self.length_input = TextInput(
            hint_text="Enter password length", 
            size_hint=(1, None), 
            height=40,
            font_size='18sp',
            multiline=False,
            on_text_validate=self.generate_password  # Bind Enter key press to generate_password function
        )
        self.add_widget(self.length_input)
        
        # Generate Password button
        self.generate_button = Button(
            text="Generate Password", 
            size_hint=(1, None), 
            height=40,
            font_size='18sp', 
            background_color=(0.1, 0.6, 1, 1),  # Better button color
            color=(1, 1, 1, 1)  # White text color
        )
        self.generate_button.bind(on_press=self.generate_password)
        self.add_widget(self.generate_button)
        
        # Password display label
        self.password_label = Label(
            text="Your generated password will appear here", 
            size_hint=(1, 1), 
            font_size='18sp', 
            color=(1, 1, 1, 1),  # White text color
            halign='center', 
            valign='middle'
        )
        self.password_label.bind(size=self._update_label)
        self.add_widget(self.password_label)
        
        # Copy Password button
        self.copy_button = Button(
            text="Copy Password", 
            size_hint=(1, None), 
            height=40,
            font_size='18sp', 
            background_color=(0.1, 0.6, 1, 1),  # Better button color
            color=(1, 1, 1, 1)  # White text color
        )
        self.copy_button.bind(on_press=self.copy_password)
        self.add_widget(self.copy_button)
        
        self.popup = None
        
    def _update_rect(self, instance, value):
        self.blue_rect.pos = instance.pos
        self.blue_rect.size = instance.size
    
    def _update_label(self, instance, value):
        self.password_label.text_size = instance.size
        
    def generate_password(self, instance=None):
        try:
            password_length = int(self.length_input.text)
            characters = string.ascii_letters + string.digits + string.punctuation
            generated_password = ''.join(random.choice(characters) for i in range(password_length))
            self.password_label.text = generated_password
        except ValueError:
            self.password_label.text = "Please enter a valid number for password length"

    def copy_password(self, instance):
        password = self.password_label.text
        if password:
            Clipboard.copy(password)
            self.show_popup("Password copied")

    def show_popup(self, message):
        self.popup = Popup(
            title='Information', 
            content=Label(text=message, font_size='18sp'), 
            size_hint=(None, None), 
            size=(300, 200)
        )
        self.popup.open()

class PasswordGeneratorApp(App):
    def build(self):
        # Using AnchorLayout to center the PasswordGenerator
        root = AnchorLayout()
        password_generator = PasswordGenerator(size_hint=(None, None), width=380, height=450)
        root.add_widget(password_generator)
        return root

if __name__ == "__main__":
    PasswordGeneratorApp().run()
