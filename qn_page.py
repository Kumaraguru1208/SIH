import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.size = (360,640)


class Screenlayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 20
        self.padding = 20
        self.background_color = get_color_from_hex('#F0FFF0')

        self.question_label = Label(
            text="[color=2F4F4F]Question Placeholder[/color]",
            font_size='24sp',
            size_hint_y=0.4,
            markup=True,
            halign='center',
            valign='middle'
        )
        self.add_widget(self.question_label)

        self.options_layout = GridLayout(
            cols=1,
            spacing=15,
            size_hint_y=0.6,
            padding=[0, 0, 0, 20]
        )

        for i in range(4):
            btn = Button(
                text=f"[color=FFFFFF]Answer Option {i + 1}[/color]",
                size_hint_y=None,
                height='65dp',
                font_size='18sp',
                background_color=get_color_from_hex('#008000'),
                color=get_color_from_hex('#FFFFFF'),
                background_normal='',
                markup=True,
                bold=True
            )
            self.options_layout.add_widget(btn)

        self.add_widget(self.options_layout)

class FarmGuideApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#F0FFF0')
        return Screenlayout()
    
if __name__ == '__main__':
    FarmGuideApp().run()

    