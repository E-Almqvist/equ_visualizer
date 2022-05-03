from copy import deepcopy as copy

class Equation:
    def __init__(self, equ_str: str, variables: list):
        self.equ_str = equ_str # equation string
        self.variables = variables # list of all the variables (in order)

    def __get_eval(self, var_map: dict) -> str:
        # f = func.replace("x", str(x)) 
        eval_str = copy(self.equ_str)
        for var in var_map:
            eval_str = eval_str.replace(var, str(var_map[var]))

        return eval_str

    def eval(self, var_map: dict) -> float:
        return eval( self.__get_eval(var_map) )

    
