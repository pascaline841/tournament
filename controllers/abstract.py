class ABSController:
    """Abstract controller class."""

    def display(self):
        pass

    def get_command(self):
        return ""

    def update(self, command: str):
        return command
