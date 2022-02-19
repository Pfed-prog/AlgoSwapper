from pyteal import App, Seq, Bytes, compileTeal, Mode, Return, Int
import os

#https://pyteal.readthedocs.io/en/stable/state.html
#When an account opts out of the application, their balance is added to the reserve.
def clear_state_program():
    #To write to global state, use the App.globalPut function. 
    #The first argument is the key to write to, and the second argument is the value to write.
    program = Seq(
        [
            App.globalPut(
                Bytes("reserve"),
                App.globalGet(Bytes("reserve"))
                + App.localGet(Int(0), Bytes("balance")),
            ),
            Return(Int(1)),
        ]
    )

    return program

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(path, "asset_clear_state.teal"), "w") as f:
        f.write(compileTeal(clear_state_program(), Mode.Application, version=5))