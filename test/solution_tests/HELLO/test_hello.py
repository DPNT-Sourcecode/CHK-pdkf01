from solutions.HLO import hello_solution


class TestSum():
    def test_sum(self):
        assert hello_solution.hello("Temi") == "Hello, Temi!"
        assert hello_solution.hello("") == "Hello, !"
        assert hello_solution.hello("Queen") == "Hello, Queen!"
