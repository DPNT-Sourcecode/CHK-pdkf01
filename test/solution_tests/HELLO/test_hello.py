from solutions.HLO import hello_solution


class TestSum():
    def test_sum(self):
        assert checkout_solution.checkout("Temi") == "Hello, Temi!"
        assert checkout_solution.checkout("") == "Hello, !"
        assert checkout_solution.checkout("Queen") == "Hello, Queen!"
