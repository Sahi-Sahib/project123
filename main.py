from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle


class GoldenLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(GoldenLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        with self.canvas.before:
            Color(0.83, 0.69, 0.22, 1)  # Golden color (RGB: 212, 175, 55)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

        welcome_label = Label(text="Welcome")
        self.add_widget(welcome_label)

        self.weight_input = TextInput(hint_text="Enter Weight", multiline=False)
        self.add_widget(self.weight_input)

        self.rate_input = TextInput(hint_text="Enter Rate", multiline=False)
        self.add_widget(self.rate_input)

        calculate_button = Button(text="Calculate")
        calculate_button.bind(on_press=self.calculate)
        self.add_widget(calculate_button)

        self.result_label = Label()
        self.add_widget(self.result_label)

    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def calculate(self, instance):
        try:
            weight = float(self.weight_input.text)
            rate = float(self.rate_input.text)

            a = 12 / 100 * weight + weight
            b = 150 + rate
            amount = b * a

            self.result_label.text = f"Amount: {amount}"
        except ValueError:
            self.result_label.text = "Please enter valid numeric values"


class GoldenApp(App):
    def build(self):
        return GoldenLayout()


if __name__ == "__main__":
    GoldenApp().run()
