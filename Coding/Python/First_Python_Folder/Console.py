class System:
    class out:
        @staticmethod
        def writeln(msg, /):
            """
                Outputs a message to the console, with a newline appended to the end of the message.
            """
            print(msg, end="\n")

        @staticmethod
        def write(msg, /):
            """
                Outputs a message to the console, without a newline appended to the end of the message.
            """
            print(msg, end="")

        @staticmethod
        def read(prompt, /):
            """
                Gives a prompt to the console and waits for the user to type their response and press enter.
            """
            return input(prompt)