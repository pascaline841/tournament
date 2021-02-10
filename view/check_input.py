class CheckView:
    @staticmethod
    def check_str(message):
        """Check if the value of an input is a string."""
        boolean = True
        while boolean:
            try:
                value = input(message)
                if value.isalpha() is False:
                    raise ValueError
                boolean = False
                return value
            except ValueError:
                print("Incorrect value, it has to be a word !")

    @staticmethod
    def check_int(message):
        """Check if the value of an input is an integer."""
        try:
            return int(input(message))
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return CheckView.check_int(message)
