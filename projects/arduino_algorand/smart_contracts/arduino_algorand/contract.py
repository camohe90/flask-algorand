from algopy import ARC4Contract, arc4, UInt64


class ArduinoAlgorand(ARC4Contract):
    total: UInt64

    @arc4.abimethod()
    def set(self, state: UInt64) -> None:
        self.total = state

    
    @arc4.abimethod()
    def read_total(self) ->UInt64:
        return self.total
