import os
import subprocess
from fractal_director_chatbot import main as chatbot_main

def check_and_install_dependencies():
    dependencies = ['socket', 'threading', 'chatterbot', 'qiskit', 'numpy', 'scipy', 'networkx']
    for dep in dependencies:
        try:
            __import__(dep)
        except ImportError:
            print(f'Installing {dep}...')
            subprocess.run(['pip', 'install', dep])

def main():
    print('Checking and installing necessary dependencies...')
    check_and_install_dependencies()
    print('Launching Fractal Director Chatbot...')
    chatbot_main()
    print('Server is running...')
    print('Hello, Admin! Welcome to the Fractal Director Chatbot.')

if __name__ == '__main__':
    main()
