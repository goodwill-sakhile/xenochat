import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
root = Builder.load_string("""
<MainScreenBox>:
    md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
    MDBoxLayout:
        MDBoxLayout:
            size_hint_x:None
            width:"60dp"
            padding:5
            MDBoxLayout:
                size_hint_x:None
                width:"50dp"
                md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
                orientation:"vertical"
                spacing:20
                Widget:
                MDIconButton:
                    size_hint:None, None
                    size:"30dp", "30dp"
                    icon:"chat"
                    icon_size:"30dp"
                MDIconButton:
                    size_hint:None, None
                    size:"30dp", "30dp"
                    icon:"robot"
                    icon_size:"30dp"
                MDIconButton:
                    size_hint:None, None
                    size:"30dp", "30dp"
                    icon:"eye-settings-outline"
                    icon_size:"30dp"
                MDIconButton:
                    size_hint:None, None
                    size:"30dp", "30dp"
                    icon:"data-matrix"
                    icon_size:"30dp"
                Widget:
        MDBoxLayout:
            #md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
""")
class MainScreenBox(MDBoxLayout):
    pass
class XenoChat(MDApp):
    def build(self):
        root = MainScreenBox()
        return root
if __name__ == "__main__":
    XenoChat().run()
