from pyteal import compileTeal, Mode, Return, Int
import os

def clear_program():
    return Return(Int(1))

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(path, "counter_clear.teal"), "w") as f:
        f.write(compileTeal(clear_program(), Mode.Application, version=5))