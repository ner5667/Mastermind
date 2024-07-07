import random
import tools


class Game:
    def __init__(self, num_values: int, num_possible_values: int) -> None:
        self.num_values = num_values
        self.num_possible_values = num_possible_values
        self.possible_values = [str(i) for i in range(self.num_possible_values)]
        self.solution = [random.choice(self.possible_values) for i in range(self.num_values)]
        
    
    #Mostly for debuggin etc, but allows to use custom solutions
    def set_solution(self, new_solution):
        if len(new_solution) != self.num_values:
            return False
        for i in new_solution:
            if not i in self.possible_values:
                return False
        self.solution = new_solution
        return True
    
    def generate_new_solution(self):
        self.solution = [random.choice(self.possible_values) for i in range(self.num_values)]
            

    def compare(self, input_list) -> list:
        return_list = [0] * self.num_values
        if len(input_list) != self.num_values:
            return return_list
        for index, input_value in enumerate(input_list):
            compare_value = self.solution[index]
            if compare_value == input_value:
                return_list[index] = 2
                continue
            if compare_value in self.possible_values:
                return_list[index] = 1
        return return_list

