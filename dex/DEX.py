from pyteal import OnComplete, Return,\
    Mode, Bytes, Int, Btoi, compileTeal, Txn,\
    And, Cond, Seq, Assert, App
import os

#At creation, the creator specifies the total supply of the asset (1).
#Initially this supply is placed in a reserve (2) and the creator is made an admin (3).
#Any admin can move funds from the reserve into the balance of any account that has opted into the application using the mint argument.
#Additionally, any admin can move funds from any account’s balance into the reserve using the burn argument.

#Accounts are free to transfer funds in their balance to any other account that has opted into the application.

# Writing local states: https://pyteal.readthedocs.io/en/stable/state.html#writing-local-state
def approval_program():
    
    on_creation = Seq(
        [
            App.globalPut(Bytes("total supply"), Int(100)), # (1)
            App.globalPut(Bytes("reserve"), Int(100)), # (2)
            App.localPut(Int(0), Bytes("admin"), Int(1)), # (3)
            #App.localPut(Int(0), Bytes("balance"), Int(0)), # initialize balance
            Return(Int(1)),
        ]
    )

    is_admin = App.localGet(Int(0), Bytes("admin")) # aka boolean

    on_closeout = Seq(
        [
            App.globalPut(
                Bytes("reserve"),
                App.globalGet(Bytes("reserve"))
                + App.localGet(Int(0), Bytes("balance")),
            ),
            Return(Int(1)),
        ]
    )

    register = Seq(
        [
            App.localPut(Int(0), Bytes("balance"), Int(0)),
            Return(Int(1))
        ]
    )

    # configure the admin status of the account Txn.accounts[1]
    # sender must be admin
    new_admin_status = Btoi(Txn.application_args[1])# get the second application argument
    set_admin = Seq(
        [
            Assert(And(is_admin, Txn.application_args.length() == Int(2))),
            App.localPut(Int(1), Bytes("admin"), new_admin_status),
            Return(Int(1)),
        ]
    )


    # move assets from the reserve to Txn.accounts[1]
    # sender must be admin
    mint_amount = Btoi(Txn.application_args[1])
    mint = Seq(
        [
            Assert(Txn.application_args.length() == Int(2)),
            Assert(mint_amount <= App.globalGet(Bytes("reserve"))),
            App.globalPut(
                Bytes("reserve"), App.globalGet(Bytes("reserve")) - mint_amount
            ),
            App.localPut(
                Int(1),
                Bytes("balance"),
                App.localGet(Int(1), Bytes("balance")) + mint_amount,
            ),
            Return(is_admin),
        ]
    )

    # transfer assets from the sender to Txn.accounts[1]
    transfer_amount = Btoi(Txn.application_args[1])
    transfer = Seq(
        [
            Assert(Txn.application_args.length() == Int(2)),
            Assert(transfer_amount <= App.localGet(Int(0), Bytes("balance"))),
            App.localPut(
                Int(0),
                Bytes("balance"),
                App.localGet(Int(0), Bytes("balance")) - transfer_amount,
            ),
            App.localPut(
                Int(1),
                Bytes("balance"),
                App.localGet(Int(1), Bytes("balance")) + transfer_amount,
            ),
            Return(Int(1)),
        ]
    )

    program = Cond(
        [Txn.application_id() == Int(0), on_creation],
        [Txn.on_completion() == OnComplete.DeleteApplication, Return(is_admin)],
        [Txn.on_completion() == OnComplete.UpdateApplication, Return(is_admin)],
        [Txn.on_completion() == OnComplete.CloseOut, on_closeout],
        [Txn.on_completion() == OnComplete.OptIn, register],
        [Txn.application_args[0] == Bytes("set admin"), set_admin],
        [Txn.application_args[0] == Bytes("mint"), mint],
        [Txn.application_args[0] == Bytes("transfer"), transfer]
    )

    return program


if __name__ == "__main__":
    
    path = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(path, "dex.teal"), "w") as f:
        f.write(compileTeal(approval_program(), mode=Mode.Application, version=5))