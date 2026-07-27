from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
import json
import os

CONFIG_PATH = "/storage/emulated/0/Documents/standoff2_cheats_config.json"

class CheatItem(BoxLayout):
    def __init__(self, cheat_id, name, desc, enabled=False, **kwargs):
        super().__init__(orientation='vertical', size_hint_y=None, height='120dp', padding='12dp', spacing='8dp', **kwargs)
        self.cheat_id = cheat_id
        self.name = name
        self.desc = desc
        self.toggle = ToggleButton(text=f"{name}", size_hint_y=None, height='48dp', state='down' if enabled else 'normal')
        self.toggle.bind(on_press=self.on_toggle)
        self.add_widget(self.toggle)
        self.add_widget(Label(text=desc, color=[0.9, 0.9, 0.9, 1], size_hint_y=None, height='60dp', text_size=(Window.width - 48, None)))

    def on_toggle(self, instance):
        self.state = instance.state

    def is_enabled(self):
        return self.toggle.state == 'down'

class CheatsMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing='10dp', padding='12dp', **kwargs)
        self.cheats = {
            'aimbot': {'name': 'Aimbot', 'desc': 'Автоматическая наводка', 'enabled': False},
            'esp': {'name': 'ESP', 'desc': 'Видеть врагов через стены', 'enabled': False},
            'speed_hack': {'name': 'Speed Hack', 'desc': 'Повышенная скорость движения', 'enabled': False},
            'no_recoil': {'name': 'No Recoil', 'desc': 'Убрать отдачу оружия', 'enabled': False},
            'wallhack': {'name': 'Wallhack', 'desc': 'Прозрачность стен', 'enabled': False},
            'infinite_ammo': {'name': 'Infinite Ammo', 'desc': 'Бесконечные патроны', 'enabled': False},
            'god_mode': {'name': 'God Mode', 'desc': 'Неуязвимость', 'enabled': False},
            'jump_hack': {'name': 'Jump Hack', 'desc': 'Высокие прыжки', 'enabled': False},
        }
        self.load_config()
        self.build_ui()

    def build_ui(self):
        header = Label(text='[b]Standoff 2 Cheats Menu[/b]', markup=True, size_hint_y=None, height='60dp', font_size='24sp', color=[1, 0.5, 0.5, 1])
        self.add_widget(header)
        scroll = ScrollView(size_hint=(1, 1))
        grid = GridLayout(cols=1, spacing='10dp', size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        self.cheat_widgets = {}
        for cheat_id, cheat in self.cheats.items():
            item = CheatItem(cheat_id, cheat['name'], cheat['desc'], enabled=cheat['enabled'])
            self.cheat_widgets[cheat_id] = item
            grid.add_widget(item)
        scroll.add_widget(grid)
        self.add_widget(scroll)
        buttons = BoxLayout(size_hint_y=None, height='60dp', spacing='10dp')
        buttons.add_widget(Button(text='Save', background_color=[0.3, 0.7, 0.3, 1], on_press=self.save_config))
        buttons.add_widget(Button(text='Clear', background_color=[0.8, 0.4, 0.2, 1], on_press=self.clear_all))
        self.add_widget(buttons)

    def save_config(self, instance=None):
        data = {cheat_id: widget.is_enabled() for cheat_id, widget in self.cheat_widgets.items()}
        try:
            os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
            with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            self.show_popup('Сохранено', f'Конфиг сохранён в:\n{CONFIG_PATH}')
        except Exception as e:
            self.show_popup('Ошибка', str(e))

    def load_config(self):
        if os.path.exists(CONFIG_PATH):
            try:
                with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for cheat_id, enabled in data.items():
                    if cheat_id in self.cheats:
                        self.cheats[cheat_id]['enabled'] = enabled
            except Exception:
                pass

    def clear_all(self, instance=None):
        for widget in self.cheat_widgets.values():
            widget.toggle.state = 'normal'
        self.show_popup('Отключено', 'Все читы отключены')

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()

class Standoff2CheatsApp(App):
    def build(self):
        Window.clearcolor = (0.09, 0.09, 0.12, 1)
        return CheatsMenu()

if __name__ == '__main__':
    Standoff2CheatsApp().run()
