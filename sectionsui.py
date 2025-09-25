from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from kivy.graphics import Color, Line
import math

Window.size = (360, 640)


class RoadmapPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Define sections
        self.sections = [
            {"name": "🌾 Soil & Seeds", "pos": (0.1, 0.8), "unlocked": True},
            {"name": "💧 Irrigation", "pos": (0.4, 0.65), "unlocked": True},
            {"name": "☀️ Crop Care", "pos": (0.7, 0.8), "unlocked": False},
            {"name": "🐛 Pest Management", "pos": (0.2, 0.5), "unlocked": False},
            {"name": "🌱 Harvesting", "pos": (0.5, 0.35), "unlocked": False},
        ]

        # Draw wavy dotted lines
        with self.canvas:
            Color(0, 0.5, 0, 1)
            self.draw_wavy_line(self.sections[0], self.sections[1])
            self.draw_wavy_line(self.sections[1], self.sections[2])
            self.draw_wavy_line(self.sections[1], self.sections[3])
            self.draw_wavy_line(self.sections[3], self.sections[4])

        # Add section buttons
        for sec in self.sections:
            btn = MDRaisedButton(
                text=sec["name"],
                md_bg_color=(0.2, 0.7, 0.2, 1) if sec["unlocked"] else (0.5, 0.5, 0.5, 1),
                text_color=(1, 1, 1, 1),
                pos_hint={"x": sec["pos"][0], "y": sec["pos"][1]},
                size_hint=(0.25, 0.1),
                on_release=lambda x, n=sec["name"], u=sec["unlocked"]: self.open_section(n) if u else None
            )
            self.add_widget(btn)

    def _get_pixel_coords(self, section):
        w, h = Window.size
        x = section["pos"][0] * w + 0.125 * w
        y = section["pos"][1] * h + 0.05 * h
        return x, y

    def draw_wavy_line(self, sec1, sec2, amplitude=20, points_count=50):
        x1, y1 = self._get_pixel_coords(sec1)
        x2, y2 = self._get_pixel_coords(sec2)
        line_points = []

        for i in range(points_count + 1):
            t = i / points_count
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1) + math.sin(t * math.pi * 4) * amplitude  # wavy offset
            line_points.extend([x, y])

        Line(points=line_points, width=2, dash_length=10, dash_offset=5)  # dotted line

    def open_section(self, name):
        print(f"Opening section: {name}")


class FarmingRoadmapApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return RoadmapPage()


if __name__ == "__main__":
    FarmingRoadmapApp().run()
