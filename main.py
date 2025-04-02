from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # 칼럼(열)이 2개임을 정의
        self.cols = 2

        # (1,1 = 1행 1열)
        self.add_widget(Label(text='User Name'))
        # (1,2)
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        # (2,1)
        self.add_widget(Label(text='password'))
        # (2,2)
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()