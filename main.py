import kb as kb
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3
import dbHelper

db = dbHelper.connect_db()
cursor = db.cursor()


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # go income screen
    def go_income_screen(self):
        result = cursor.execute("SELECT SERVICE_NAME FROM SERVICES WHERE TYPE_ID = 222")
        result = result.fetchall()

        for k in result:
            print(k[0])
            btn_name = k[0]
            self.get_screen('income_screen').ids.grid_prueba.add_widget(Button(text=btn_name, size_hint_x='1'))

        self.current = 'income_screen'
        # add_widget(new_btn)
        # ids.expense_btn.text = str(result.fetchone()[0])


class MainScreen(Screen):
    pass


class IncomeScreen(Screen):
    pass


class TransactionScreen(Screen):
    pass



class MainApp(App):
    def build(self):
        pass


if __name__ == '__main__':
    MainApp().run()
