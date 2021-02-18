class PlayerView:
    def display(self):
        """Display the creation of a new player."""
        print("\n==================================================")
        print("************CREATE A NEW PLAYER **************\n")

    @staticmethod
    def check_gender(message):
        """Check if the gender value is 'm' or 'f'."""
        boolean = True
        while boolean:
            try:
                gender = input(message).lower()
                if gender not in ["m", "f"]:
                    raise ValueError
                boolean = False
                return gender
            except TypeError:
                print("Incorrect gender, it has to be 'm' / 'f' !")
            except ValueError:
                print("Incorrect gender, it has to be 'm' / 'f' !")
