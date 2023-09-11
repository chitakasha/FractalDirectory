class Observer:

    def __init__(self):
        self.text = ""

    def update(self, subject):
        self.text = subject.text
