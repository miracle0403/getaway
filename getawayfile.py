from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty


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

        field-input = [name, username, email, password, retypepassword, usertype]
        error = []
        for n in fields:
            if len(n) < 8 and n is not retypepassword:
                error.append(f"{n} must not be less than 8 characters")

            elif password is not retypepassword:
                error.append("Password Must Match")

            print(error)


class GetAwayApp(App):
    def build(self):
        return MyGrid()
