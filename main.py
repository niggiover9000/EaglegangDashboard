from app import main as main_app
from functions import main as main_functions
from threading import Thread

if __name__ == '__main__':
    print("Running...")

    run_server = Thread(target=main_app)
    run_server.start()

    run_functions = Thread(target=main_functions)
    run_functions.start()
