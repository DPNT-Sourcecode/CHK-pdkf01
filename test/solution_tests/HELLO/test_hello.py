from solutions.HLO import hello_solution


class TestSum():
    def test_sum(self):
        assert hello_solution.hello("Hello World") == "Hello, World"
        assert hello_solution.hello("") == "Hello, World"
        assert hello_solution.hello("Hi") == "Hello, World"

