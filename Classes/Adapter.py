"""


"""
# adapter
class socket_adapter:
    pass


# adaptee
class power_socket:
    def __init__(self):
        self.holes = 0
        self.pins = 0
        self.pin_shape = " "

    def getholes(self, holes):
        self.holes = holes

    def getpin_shape(self, pin_shape):
        self.pin_shape = pin_shape

    def getpins(self, pins):
        self.pins = pins


class chinese_socket(power_socket):
    def holes(self):
        self


class european_socket(power_socket):
    def __init__(self):
        self.holes = 2
        self.pins = 2
        self.pin_shape = "round"


# client
class chinese_pin_plug:
    def __init__(self):
        self.pins = 2
        self.pinshape = "Flat"


def main():
    ca = any_to_chinese_adapter
    sa = socket_adapter(ca)
    ps = power_socket
    cs = chinese_socket(ps)
    es = european_socket(ps)

    main()
