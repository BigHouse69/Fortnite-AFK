import flet
from flet import Page, Text, Row, Column, Switch, WindowDragArea
import threading
import time, random
import pyautogui

class AFKBotInterface:
    def __init__(self):
        self.bot_status = False  # Estado do bot: ligado/desligado
        self.running = 0
        self._comands = ['w', 'a', 's', 'd']

    def toggle_bot(self, e):
        self.bot_status = e.control.value
        status_text = "ON" if self.bot_status else "OFF"
        # Atualiza o texto do status do bot
        self.status_text.value = f"Bot Status: {status_text}"
        e.page.update()

        if self.bot_status:
            self.running = 1
            threading.Thread(target=self.run).start()
        else:
            self.running = 0

    def __build_interface(self, page: Page):
        page.title = "AFK Controller"
        page.window_opacity = 0.8
        page.window_always_on_top = True
        page.window_frameless = False
        page.window_maximized = False
        page.window_width = 200
        page.window_height = 160

        # Arrastar a janela
        window_drag = WindowDragArea(
            content=Text("AFK Bot", weight="bold", size=16),
            expand=True,
        )

        # Texto do status do bot (referência para atualização)
        self.status_text = Text(f"Bot Status: {'ON' if self.bot_status else 'OFF'}", size=14)

        # Controle de status do bot
        bot_status_switch = Row([
            Text("Ativar Bot: "),
            Switch(value=self.bot_status, on_change=self.toggle_bot),
        ])

        # Layout principal
        page.add(
            Column(
                controls=[
                    window_drag,
                    self.status_text,  # Texto do status
                    bot_status_switch,
                ],
                spacing=10,
                alignment="start",
                horizontal_alignment="center",
            )
        )

    def start(self):
        flet.app(target=self.__build_interface)

    def run(self):
        while (self.running):
            key = random.choice(self._comands)
            pyautogui.keyDown(key)
            time.sleep(random.uniform(0.5, 1.76))
            pyautogui.keyUp(key)
            time.sleep(random.randint(0, 20))


if __name__ == "__main__":
    afk_bot = AFKBotInterface()
    afk_bot.start()
