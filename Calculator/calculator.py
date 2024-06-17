from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window


class CalculatorApp(App):
    def build(self):
        self.expression = ""

        layout = BoxLayout(orientation='vertical', spacing=10)

        with layout.canvas.before:
            Color(0, 0, 1, 1) 
            self.rect = Rectangle(size=(100, 100), pos=(0, 0)) 

        self.display = Label(text="", font_size='24sp', size_hint=(1, 0.25), halign='right', valign='middle')
        layout.add_widget(self.display)

        buttons_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.75))
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for button in buttons:
            if button == '=':
                equals_btn = Button(text=button, background_color=(0, 0, 1, 1))
                equals_btn.bind(on_press=self.calculate)
                buttons_layout.add_widget(equals_btn)
            elif button == 'C':
                clear_btn = Button(text=button, background_color=(0, 0, 1, 1))
                clear_btn.bind(on_press=self.clear)
                buttons_layout.add_widget(clear_btn)
            else:
                btn = Button(text=button, background_color=(0, 0, 1, 1))
                btn.bind(on_press=self.on_button_press)
                buttons_layout.add_widget(btn)

        layout.add_widget(buttons_layout)

        
        Window.bind(on_textinput=self.on_textinput)
        Window.bind(on_keyboard=self.on_keyboard)

        return layout

    def on_button_press(self, instance):
        self.expression += instance.text
        self.update_display()

    def calculate(self, instance):
        try:
            self.expression = str(eval(self.expression))
        except Exception as e:
            self.expression = 'Error'
        self.update_display()

    def clear(self, instance):
        self.expression = ''
        self.update_display()

    def update_display(self):
        self.display.text = self.expression

    def on_textinput(self, instance, text):
        if text.isdigit() or text in ['+', '-', '*', '/']:
            self.expression += text
            self.update_display()

    def on_keyboard(self, window, key, scancode, codepoint, modifier):
        if key == 13:
            self.calculate(None)
        elif key == 27:
            self.clear(None)
        elif key == 8:
            self.expression = self.expression[:-1]
            self.update_display()
        elif key == 127:
            self.expression = ''
            self.update_display()
        elif modifier == ['shift'] and codepoint == 43:
            self.expression += '+'
            self.update_display()
        elif modifier == ['shift'] and codepoint == 42:
            self.expression += '*'
            self.update_display()
        elif modifier == ['shift'] and codepoint == 47:
            self.expression += '/'
            self.update_display()

        return True


if __name__ == '__main__':
    CalculatorApp().run()
