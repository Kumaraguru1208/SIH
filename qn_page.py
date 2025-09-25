import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

Window.size = (360, 640)

questions_data = [
    {
        "question": "Which of these is 'apple'?",
        "options": ["la manzana", "el libro", "el agua"],
        "correct_answer": "la manzana"
    },
    {
        "question": "How do you say 'hello'?",
        "options": ["adiós", "hola", "por favor"],
        "correct_answer": "hola"
    },
    {
        "question": "Which of these is a common pest for tomato plants?",
        "options": ["Aphids", "Ladybugs", "Earthworms", "Bees"],
        "correct_answer": "Aphids"
    }
]

class Screenlayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 20
        self.padding = 20
        self.background_color = get_color_from_hex('#F0FFF0')

        self.current_question_index = 0
        self.incorrect_attempts = 0
        self.max_incorrect_attempts = 5

       
        self.hp_bar_container = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height='40dp',
            padding=5,
            spacing=5
        )
        self.add_widget(self.hp_bar_container)

        
        self.hp_blocks = []
        
        self.create_hp_bar()

        self.question_label = Label(
            text="",
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
        self.add_widget(self.options_layout)
        
        self.feedback_label = Label(
            text="",
            font_size='20sp',
            size_hint_y=0.2,
            markup=True,
            halign='center',
            valign='middle'
        )
        self.add_widget(self.feedback_label)

        self.restart_button = Button(
            text="[color=FFFFFF]Restart Quiz[/color]",
            size_hint_y=None,
            height='65dp',
            font_size='20sp',
            background_color=get_color_from_hex('#008000'),
            color=get_color_from_hex('#FFFFFF'),
            background_normal='',
            markup=True,
            bold=True,
            disabled=True,
            opacity=0
        )
        self.restart_button.bind(on_release=self.next_question)
        self.add_widget(self.restart_button)

        self.load_question()

    def load_question(self, *args):
        
        self.feedback_label.text = ""
        self.options_layout.clear_widgets()
        self.restart_button.disabled = True
        self.restart_button.opacity = 0
        
        
        if self.current_question_index >= len(questions_data):
            self.question_label.text = "[color=2F4F4F]Quiz Complete![/color]"
            self.restart_button.disabled = False
            self.restart_button.opacity = 1
            return

        
        question = questions_data[self.current_question_index]
        self.question_label.text = f"[color=2F4F4F]{question['question']}[/color]"
        
        
        for option in question['options']:
            btn = Button(
                text=f"[color=FFFFFF]{option}[/color]",
                size_hint_y=None,
                height='65dp',
                font_size='18sp',
                background_color=get_color_from_hex('#008000'),
                color=get_color_from_hex('#FFFFFF'),
                background_normal='',
                markup=True,
                bold=True
            )
            btn.bind(on_release=self.check_answer)
            self.options_layout.add_widget(btn)

    def check_answer(self, instance):
        current_question = questions_data[self.current_question_index]
        selected_answer = instance.text.replace("[color=FFFFFF]", "").replace("[/color]", "")

        if selected_answer == current_question['correct_answer']:
            self.feedback_label.text = "[color=008000]Correct![/color]"
            self.current_question_index += 1
            Clock.schedule_once(self.load_question, 1)
        else:
            self.incorrect_attempts += 1
            self.update_hp_bar()
            self.feedback_label.text = "[color=FF0000]Incorrect, try again![/color]"
            
            
            instance.background_color = get_color_from_hex('#FF0000')

            
            for btn in self.options_layout.children:
                btn.disabled = False
            
           
            if self.incorrect_attempts >= self.max_incorrect_attempts:
                self.question_label.text = "[color=FF0000]Game Over![/color]"
                self.options_layout.clear_widgets()
                self.feedback_label.text = "[color=FF0000]You have exceeded the mistake limit.[/color]"
                self.restart_button.disabled = False
                self.restart_button.opacity = 1

    def next_question(self, instance):
        self.current_question_index = 0
        self.incorrect_attempts = 0
        self.create_hp_bar()
        self.load_question()

    def create_hp_bar(self):
        
        self.hp_bar_container.clear_widgets()
        self.hp_blocks = []
        
        for i in range(self.max_incorrect_attempts):
            hp_block = Button(
                text='',
                disabled=True,
                background_normal='',
                size_hint_x=1,
                background_color=get_color_from_hex('#008000')
            )
            self.hp_blocks.append(hp_block)
            self.hp_bar_container.add_widget(hp_block)

    def update_rect(self, instance, value):
        instance.canvas.before.children[-1].pos = instance.pos
        instance.canvas.before.children[-1].size = instance.size

    def update_hp_bar(self):
        
        index_to_change = len(self.hp_blocks) - self.incorrect_attempts
        
        if index_to_change >= 0 and index_to_change < len(self.hp_blocks):
            hp_block = self.hp_blocks[index_to_change]
            hp_block.background_color = get_color_from_hex('#FF0000')


class FarmGuideApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#F0FFF0')
        return Screenlayout()
    
if __name__ == '__main__':
    FarmGuideApp().run()
