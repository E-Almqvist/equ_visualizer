from copy import deepcopy as copy

class Function:
    def __init__(self, equ_str: str, variables: list):
        self.equ_str = equ_str # Function string
        self.variables = variables # list of all the variables (in order)

    def __get_eval(self, var_map: dict) -> str:
        eval_str = copy(self.equ_str)
        for var in var_map:
            eval_str = eval_str.replace(var, str(var_map[var]))

        return eval_str

    def eval(self, var_map: dict) -> float:
        return eval( self.__get_eval(var_map) )


class ODE:
    def __init__(self, funcs: list):
        self.funcs = funcs # list of "Function" objects
        # as index increases so does the derivative "order"

    def get_point(self, var_map: dict):
        point = []
        for i in range(0, len(var_map.keys())):
            point.append( self.funcs[i].eval(var_map) )
        return point

    
