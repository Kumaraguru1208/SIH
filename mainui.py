from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp

Window.size = (360, 640)  # for desktop preview

KV = """
Screen:
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(30)
        canvas.before:
            Color:
                rgb: 0.9, 1, 0.9   # light green background
            Rectangle:
                pos: self.pos
                size: self.size

        MDLabel:
            text: "FARMEASY"
            halign: "center"
            font_style: "H2"
            bold: True
            theme_text_color: "Custom"
            text_color: 0, 0.4, 0, 1

        MDLabel:
            text: "Learn Farming with Fun!"
            halign: "center"
            font_style: "H6"
            theme_text_color: "Custom"
            text_color: 0.1, 0.5, 0.1, 1

        Widget:

        MDCard:
            orientation: "vertical"
            padding: dp(20)
            spacing: dp(15)
            size_hint_y: None
            height: dp(180)
            md_bg_color: 0.9, 0.95, 1, 1
            radius: [20,]

            MDRaisedButton:
                text: "🌾 Start Lesson"
                md_bg_color: 0.2, 0.7, 0.2, 1
                text_color: 1,1,1,1
                font_size: "20sp"
                pos_hint: {"center_x": 0.5}

            MDRaisedButton:
                text: "📊 Check Progress"
                md_bg_color: 0.1, 0.5, 0.8, 1
                text_color: 1,1,1,1
                font_size: "20sp"
                pos_hint: {"center_x": 0.5}

            MDRaisedButton:
                text: "⚙️ Settings"
                md_bg_color: 0.9, 0.6, 0.1, 1
                text_color: 1,1,1,1
                font_size: "20sp"
                pos_hint: {"center_x": 0.5}

        Widget:
"""

class FarmingHomeApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

if __name__ == "__main__":
    FarmingHomeApp().run()


from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.scrollview import MDScrollView

Window.size = (360, 640)  # for desktop preview

# ---------- Screens ----------
class HomeScreen(Screen):
    pass

class RoadmapScreen(Screen):
    pass

class ContentScreen(Screen):
    pass

# ---------- App ----------
class FarmingApp(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(RoadmapScreen(name="roadmap"))
        self.sm.add_widget(ContentScreen(name="content"))

        return Builder.load_string(self.kv)

    def open_content(self, section_name):
        self.sm.get_screen("content").ids.content_label.text = f"📖 Learning content for:\n{section_name}"
        self.sm.current = "content"

    kv = """
ScreenManager:
    HomeScreen:
    RoadmapScreen:
    ContentScreen:

<HomeScreen>:
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(30)
        spacing: dp(20)

        Widget:

        MDLabel:
            text: "🌱 Farming Duolingo"
            halign: "center"
            font_style: "H3"

        MDRaisedButton:
            text: "View Roadmap"
            md_bg_color: 0.2,0.7,0.2,1
            text_color: 1,1,1,1
            pos_hint: {"center_x": 0.5}
            on_release: app.sm.current = "roadmap"

        Widget:

<RoadmapScreen>:
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(10)

        MDLabel:
            text: "🛤️ Learning Roadmap"
            halign: "center"
            font_style: "H5"
            size_hint_y: None
            height: dp(40)

        MDScrollView:
            MDBoxLayout:
                id: roadmap_layout
                orientation: "vertical"
                adaptive_height: True
                spacing: dp(15)
                padding: dp(10)

                # Sections
                MDRaisedButton:
                    text: "🌾 Section 1: Soil & Seeds"
                    md_bg_color: 0.3,0.7,0.3,1
                    text_color: 1,1,1,1
                    on_release: app.open_content(self.text)

                MDRaisedButton:
                    text: "💧 Section 2: Irrigation & Water Management"
                    md_bg_color: 0.2,0.6,0.9,1
                    text_color: 1,1,1,1
                    on_release: app.open_content(self.text)

                MDRaisedButton:
                    text: "☀️ Section 3: Crop Growth & Care"
                    md_bg_color: 0.9,0.7,0.2,1
                    text_color: 1,1,1,1
                    on_release: app.open_content(self.text)

                MDRaisedButton:
                    text: "🐛 Section 4: Pest Management"
                    md_bg_color: 0.9,0.4,0.2,1
                    text_color: 1,1,1,1
                    on_release: app.open_content(self.text)

<ContentScreen>:
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(30)
        spacing: dp(20)

        MDLabel:
            id: content_label
            text: "Content will appear here"
            halign: "center"
            font_style: "H5"

        MDRaisedButton:
            text: "Back to Roadmap"
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0.2,0.7,0.2,1
            text_color: 1,1,1,1
            on_release: app.sm.current = "roadmap"
"""

if __name__ == "__main__":
    FarmingApp().run()
