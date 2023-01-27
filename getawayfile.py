from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
import mysqlfile

class MyGrid(Widget):
    name = ObjectProperty(None)
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    retypepassword = ObjectProperty(None)
    usertype = ObjectProperty(None)

    def press(self):
        name = self.name.text
        username = self.username.text
        email = self.email.text
        password = self.password.text
        retypepassword = self.retypepassword.text
        usertype = self.usertype.text

        # field-input = [name, username, email, password, retypepassword, usertype]


class GetAwayApp(App):
    def build(self):

        return MyGrid()

