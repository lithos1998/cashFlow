from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3


def conect_db():
    con = sqlite3.connect("mycashflow.db")
    cursor = con.cursor()

    #cursor.execute("CREATE TABLE pruebas(id integer primary key autoincrement, title, description)")
    res = cursor.execute("SELECT name FROM sqlite_master")

    print(res.fetchone())

    res = cursor.execute("insert into pruebas(title, description) values('titulo prueba', 'asdasda dasdasdad asd asd')")

    res = cursor.execute("SELECT * FROM pruebas")
    print(res.fetchone())
    return cursor


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        conect_db()

    # llamar al boton
    def btn_action(self):
        texto = self.get_screen('first').ids.boton1.text = "toma put"
        print(texto)


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class MainApp(App):
    def build(self):
        pass


if __name__ == '__main__':
    MainApp().run()
