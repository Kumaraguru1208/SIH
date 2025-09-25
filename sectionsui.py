from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

class VerticalRoadmapApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"

        # Main layout
        root = FloatLayout()

        # Top app bar
        toolbar = MDTopAppBar(title="Farming Roadmap", pos_hint={"top": 1}, elevation=10)
        root.add_widget(toolbar)

        # Scrollable container for sections
        scroll = ScrollView(size_hint=(1, None), size=(Window.size[0], Window.size[1]-56),
                            pos_hint={"top": 0.95})
        layout = BoxLayout(orientation='vertical', spacing=20, padding=40, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        scroll.add_widget(layout)
        root.add_widget(scroll)

        # Define sections
        sections = [
            {"name": "🌾 Soil & Seeds", "unlocked": True},
            {"name": "💧 Irrigation", "unlocked": True},
            {"name": "☀️ Crop Care", "unlocked": False},
            {"name": "🐛 Pest Management", "unlocked": False},
            {"name": "🌱 Harvesting", "unlocked": False},
            {"name": "🚜 Machinery", "unlocked": False},
            {"name": "🌾 Storage", "unlocked": False},
            {"name": "🧪 Fertilizers", "unlocked": False},
            {"name": "🌿 Advanced Techniques", "unlocked": False},
            {"name": "💡 Expert Tips", "unlocked": False},
        ]

        # Add buttons (smaller width)
        for sec in sections:
            btn = MDRaisedButton(
                text=sec["name"],
                md_bg_color=(0.2, 0.7, 0.2, 1) if sec["unlocked"] else (0.6, 0.6, 0.6, 1),
                text_color=(1, 1, 1, 1),
                size_hint=(0.5, None),  # smaller width: 50% of screen
                height=50,               # slightly smaller height
                pos_hint={"center_x": 0.5},  # center horizontally
                on_release=lambda x, n=sec["name"], u=sec["unlocked"]: self.on_button_click(x, n, u)
            )
            layout.add_widget(btn)

        # Background color
        with root.canvas.before:
            Color(0.9, 0.95, 1, 1)  # light sky-blue
            self.bg = Rectangle(size=Window.size, pos=(0, 0))

        root.bind(size=self.update_bg, pos=self.update_bg)

        return root

    def on_button_click(self, button, name, unlocked):
        if unlocked:
            print(f"Opening section: {name}")
            # Animate button click
            anim = Animation(size_hint=(0.52, 0.055), duration=0.1) + Animation(size_hint=(0.5, 0.05), duration=0.1)
            anim.start(button)

    def update_bg(self, *args):
        self.bg.size = Window.size

if __name__ == "__main__":
    VerticalRoadmapApp().run()
