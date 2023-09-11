import unittest
import communication_module


class TestCommunicationModule(unittest.TestCase):

    def test_set_text(self):
        communication_module = CommunicationModule()
        communication_module.text = "This is some text."
        assert communication_module.text == "This is some text."

    def test_register_observer(self):
        communication_module = CommunicationModule()
        observer = observer.Observer()
        communication_module.register_observer(observer)
        assert observer in communication_module.observers

    def test_unregister_observer(self):
        communication_module = CommunicationModule()
        observer = observer.Observer()
        communication_module.register_observer(observer)
        communication_module.unregister_observer(observer)
        assert observer not in communication_module.observers


if __name__ == "__main__":
    unittest.main()
