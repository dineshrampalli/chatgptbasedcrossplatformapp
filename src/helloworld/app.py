import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import firebase_admin
import pyrebase

# Initialize Firebase SDK
config = {
  "apiKey": "AIzaSyDrkhC6WcpJasmFgWFSquWElQG4HrSLa94",
  "authDomain": "beeware-b23ac.firebaseapp.com",
  "databaseURL": "https://beeware-b23ac-default-rtdb.firebaseio.com",
  "projectId": "beeware-b23ac",
  "storageBucket": "beeware-b23ac.appspot.com",
  "messagingSenderId": "957494087016",
  "appId": "1:957494087016:web:2c1b2898e1ee8236125add",
  "measurementId": "G-LL998Z0XQ7"
}

firebase = pyrebase.initialize_app(config)

class LoginScreen(toga.App):
    def startup(self):
        # Create a main window
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        # Create input fields for email and password
        self.email_input = toga.TextInput(placeholder='Email', style=Pack(padding_bottom=10))
        self.password_input = toga.PasswordInput(placeholder='Password')

        # Create a signup button
        signup_button = toga.Button('Sign Up', on_press=self.handle_signup)

        # Create a login button
        login_button = toga.Button('Login', on_press=self.handle_login)

        # Add the input fields and buttons to the main box
        main_box.add(self.email_input)
        main_box.add(self.password_input)
        main_box.add(signup_button)
        main_box.add(login_button)

        # Set the main box as the main content of the app
        self.main_window = toga.MainWindow(title='Login Screen')
        self.main_window.content = main_box
        self.main_window.show()

        # Initialize Firebase Authentication
        self.auth = firebase.auth()

    def handle_signup(self, widget):
        # Handle signup functionality here
        email = self.email_input.value
        password = self.password_input.value

        try:
            # Create a new user with the provided email and password
            self.auth.create_user_with_email_and_password(email, password)
            print("Signup successful!")
        except Exception as e:
            print(f"Signup failed: {str(e)}")

    def handle_login(self, widget):
        # Handle login functionality here
        email = self.email_input.value
        password = self.password_input.value

        try:
            # Sign in the user with the provided email and password
            self.auth.sign_in_with_email_and_password(email, password)
            print("Login successful!")
        except Exception as e:
            print(f"Login failed: {str(e)}")

    def main(self):
        return LoginScreen()


if __name__ == '__main__':
    app = LoginScreen()
    app.main_loop()