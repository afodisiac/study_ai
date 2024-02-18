import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

variable_lesson = {
    "variable": "Python variables are the reserved memory locations used to store values with in a Python Program.",
    "printing variables": "we can print it using print() function.",
    "deleting variables ": "we can use del",
    "getting a data type": "we use type()",
    "casting a variable" : "this is where you can change the data type, you can do this by putting the data type your changing to and then () e.g int()",
    "python": "general-purpose interpreted, interactive, object-oriented, and high-level programmin    g language.",
    "data types": "A data type represents a kind of value and determines what operations can be done on it.",
    "function": "a block of organized, reusable code that is used to perform a single, related action.",
    "parametres": "the variables that appear between the brackets in the “def” line of a Python function definition.",
    "arguments": "Arguments are the actual objects or values you pass to a function or method when calling it.",
    "class": "is a blue print from which objects are made",
    "object": "is the implementation of aclass"
}
class Registration(Screen):
    def on_enter(self):
        
        layout = BoxLayout(orientation="vertical", padding= 30, spacing =10)

        head_label = Label(text="python User RegistrationApp", font_size=26, bold= True, height= 40)

        #adding label
        name_label = Label(text="name", font_size=10, )
        self.name_input =TextInput(multiline = False, font_size=18)

        email_label = Label(text="email", font_size=10, )
        self.email_input =TextInput(multiline = False, font_size=18)

        password_label = Label(text="password", font_size=10, )
        self.password_input =TextInput(multiline = False, font_size=18, password =True)

        confirm_label = Label(text="confirm password", font_size=10, )
        self.confirm_input =TextInput(multiline = False, font_size=18, password =True)

        #Button
        Submit_button = Button(text='register',font_size=18) 
        Submit_button.bind(on_release=self.register)

        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(confirm_label)
        layout.add_widget(self.confirm_input)
        layout.add_widget(Submit_button)
        self.add_widget(layout)

    def register(self,instance):
        #collect information
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirm_password = self.confirm_input.text
        

        #validation
        if name.strip() == '' or email.strip()=='' or password.strip() == '' or confirm_password.strip() == '':
            message ="please fill in all fields"
        elif password != confirm_password:
            message= "Passwords do not match"
        else:
            filename = name +'.txt'
            with open(filename,'w') as file:
                file.write('Name: {}\n'.format(name))
                file.write('Email: {}\n'.format(email))
                file.write('Password: {}\n'.format(password))
            message ="Registraton successful!\n Name:{}\nEmail: {}".format(name,email)
            self.manager.current = "Definitions"

        #popup
        popup =Popup(title = "registrationstatus", content =Label(text=message)
        , size_hint =(None, None),size=(400,200))
        popup.open()


class Definitions(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=30, spacing=10)
        head_label = Label(text="study Ai", font_size=26, bold=True, height=40)
        layout.add_widget(head_label)
        self.display_items(layout)
        self.add_widget(layout)

    def display_items(self, layout):
        for key, value in variable_lesson.items():
            item_label = Label(text=f"{key}: {value}")
            layout.add_widget(item_label)

class Quiz(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('studyAi.kv')

class AwesomeApp(App):
    def build(self):
        wm = WindowManager()
        wm.add_widget(Registration(name="Registration"))
        wm.add_widget(Definitions(name="Definitions"))
        wm.add_widget(Quiz(name="Quiz"))
        return wm

if __name__== '__main__':
     AwesomeApp().run()