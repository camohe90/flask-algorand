from algopy import ARC4Contract, arc4


class ArduinoAlgorand(ARC4Contract):
    def __init__(self) -> None:
        self.total = arc4.String("")

    @arc4.abimethod()
    def set(self, state: arc4.String) -> arc4.String:
        self.total = state
        return self.total
    
    @arc4.abimethod()
    def read_total(self) ->arc4.String:
        return self.total
