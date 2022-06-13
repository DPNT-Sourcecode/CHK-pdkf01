from solutions.CHK import checkout_solution


class TestSum():
    def test_sum(self):
        assert checkout_solution.checkout("BC") == 50
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout(855) == -1
        assert checkout_solution.checkout("AAAB") == 160
        assert checkout_solution.checkout(100) == -1
        assert checkout_solution.checkout("BDDD") == 75
        assert checkout_solution.checkout("AAABB") == 175
        assert checkout_solution.checkout("BAAA") == 160
        assert checkout_solution.checkout("BCCC") == 90