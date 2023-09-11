import observer
import subject


class CommunicationModule(subject.Subject):

    def __init__(self):
        super().__init__()
        self._text = ""

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        self.notify_observers()

    def register_observer(self, observer):
        super().register_observer(observer)

    def unregister_observer(self, observer):
        super().unregister_observer(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)


def main():
    communication_module = CommunicationModule()

    # Register an observer
    observer = observer.Observer()
    communication_module.register_observer(observer)

    # Set the text
    communication_module.text = "This is some text."

    # Check if the observer was notified
    assert observer.text == "This is some text."


if __name__ == "__main__":
    main()
