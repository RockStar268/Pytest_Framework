import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout(orientation = 'vertical', padding= 30, spacing = 10)

        # Heading text
        header_label = Label(text= "Python User Registration App", font_size=26, bold=True, height=40)

        # Adding Labels
        name_label = Label(text="Name:", font_size=18, bold=True, height=40)
        self.name_input = TextInput(multiline=False, font_size= 18)

        email_label = Label(text="E-mail:", font_size=18, bold=True, height=40)
        self.email_input = TextInput(multiline=False, font_size=18)

        password_label = Label(text="Password:", font_size=18, bold=True)
        self.password_input = TextInput(multiline=False, font_size=18, password=True)

        confirmPassword_label = Label(text="Confirm Password:", font_size=18, bold=True, height=40)
        self.confirmPassword_input = TextInput(multiline=False, font_size=18, password=True)


        submit_Button = Button(text= "Create User", font_size= 18, italic=True, on_press=self.register)



        layout.add_widget(header_label)

        layout.add_widget(name_label)
        layout.add_widget(self.name_input)

        layout.add_widget(email_label)
        layout.add_widget(self.email_input)

        layout.add_widget(password_label)
        layout.add_widget(self.password_input)

        layout.add_widget(confirmPassword_label)
        layout.add_widget(self.confirmPassword_input)

        layout.add_widget(submit_Button)


        return layout

    def register(self, instance):
        # Collects values of input fields
        name_registration = self.name_input.text
        email_registration = self.email_input.text
        password_registration = self.password_input.text
        confirm_password_registration = self.confirmPassword_input.text

        # Validations
        if name_registration.strip() == "" or email_registration.strip() == "" or password_registration.strip() == "" or confirm_password_registration.strip() =="":
            message = "Please fill in all fields."
        elif password_registration != confirm_password_registration:
            message = "Your password does not match. Please re-check"
        else:
            file_name_registration = name_registration + ".txt"
            with open(file_name_registration, "w") as file:
                file.write("Name: {}\n".format(name_registration))
                file.write("E-mail: {}\n".format(email_registration))
                file.write("Password: {}\n".format(password_registration))
            message = "Registration successful! \nName: {}\nE-mail: {}".format(name_registration, email_registration)


        # Pop Up
        pop_up_registration = Popup(title = "Registration Status", content=Label(text=message), size_hint=(None,None), size=(500,200))
        pop_up_registration.open()

if __name__ == "__main__":
    RegistrationApp().run()