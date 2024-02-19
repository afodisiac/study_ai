import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout


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

questions = [
    {"question": "what is a variable",
    "options": {
        "a": "Python variables are the reserved memory locations used to store values with in a Python Program",
        "b": "it is the equivalent of a tuple",
        "c": "it is a chance for us to use the  pass function"
        },
        "correct_answer": "a"
    },
    {"question": "how do we print variables",
    "options": {
        "a": "console.log())",
        "b": "print()",
        "c": "printf()"
        },
        "correct_answer": "b"
    },
    {"question": "how do we delete variables",
    "options": {
        "a": "pop()",
        "b": "delete()",
        "c": "del()"
        },
        "correct_answer": "c"
    },
    {
        "question": "How do we find out the data type in a variable?",
        "options": {
            "a": "type()",
            "b": "var()",
            "c": "find()"
        },
        "correct_answer": "a"
    },
    {
        "question": "What is the use of casting a variable?",
        "options": {
            "a": "to use the pass key",
            "b": "this is where you can change the data type",
            "c": "to define a function"
        },
        "correct_answer": "b"
    }
]
class Quiz(Screen):
    current_question = NumericProperty(0)
    user_answers = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.load_question()

    def load_question(self):
        self.layout.clear_widgets()
        question_data = questions[self.current_question]
        question_label = Label(text=question_data["question"], size_hint_y=None, height=50)
        self.layout.add_widget(question_label)

        options_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        options_layout.bind(minimum_height=options_layout.setter('height'))
        for option, text in question_data["options"].items():
            option_button = ToggleButton(text=f"{option.upper()}: {text}", group='options', size_hint_y=None, height=40)
            option_button.bind(on_release=self.on_option_selected)
            options_layout.add_widget(option_button)
        self.layout.add_widget(ScrollView(size_hint=(1, None), size=(400, 200), do_scroll_y=True, do_scroll_x=False, bar_width='10dp', scroll_type=['bars']))
        self.layout.add_widget(options_layout)

        next_button = Button(text="Next", size_hint_y=None, height=40)
        next_button.bind(on_release=self.next_question)
        self.layout.add_widget(next_button)

        self.add_widget(self.layout)

    def on_option_selected(self, instance):
        selected_option = instance.text.split(':')[0].lower()
        self.user_answers.append((self.current_question, selected_option))

    def next_question(self, instance):
        self.current_question += 1
        if self.current_question < len(questions):
            self.load_question()
        else:
            self.show_results()

    def show_results(self):
        self.layout.clear_widgets()
        correct_answers = 0
        for q_num, selected_option in self.user_answers:
            question = questions[q_num]
            if selected_option == question["correct_answer"]:
                correct_answers += 1
            self.layout.add_widget(Label(text=f"Question: {question['question']}\nYour answer: {selected_option}\nCorrect answer: {question['correct_answer']}"))

        self.layout.add_widget(Label(text=f"Score: {correct_answers}/{len(questions)}"))
        restart_button = Button(text="Restart Quiz", size_hint_y=None, height=40)
        restart_button.bind(on_release=self.restart_quiz)
        self.layout.add_widget(restart_button)

    def restart_quiz(self, instance):
        self.current_question = 0
        self.user_answers = []
        self.load_question()
    

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