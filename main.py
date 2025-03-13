class Solve:
    def __init__(self, user_input):
        self.user_input = user_input
    
    def solve(self):
        my_list = list(map(lambda x: int(x), self.user_input.split()))

)


answer = Solve(input())
answer.solve()