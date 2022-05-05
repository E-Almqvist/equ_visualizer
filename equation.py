from copy import deepcopy as copy

class Function:
    def __init__(self, equ, var_count: int):
        self.equ = equ
        self.var_count = var_count

    def eval(self, *args):
        return self.equ(*args)


class ODE:
    def __init__(self, funcs: list):
        self.funcs = funcs # list of "Function" objects
        # as index increases so does the derivative "order"

    def get_point(self, *values):
        point = []
        for i in range(0, len(values)):
            point.append( self.funcs[i].eval(*values) )
        return point

    
