from solutions.CHK import checkout_solution


class TestSum():
    def test_sum(self):
        assert checkout_solution.checkout("BC") == 50
        assert hello_solution.hello("AAA") == 130
        assert hello_solution.hello("C") == 20
        assert hello_solution.hello("D") == 15
        assert hello_solution.hello("A") == 50
        assert hello_solution.hello("B") == 30
        assert hello_solution.hello("BB") == 45
        assert hello_solution.hello(855) == -1
        assert hello_solution.hello("AAAB") == 160
        assert hello_solution.hello(&) == -1
        assert hello_solution.hello("BDDD") == 75
        assert hello_solution.hello("AAABB") == 175
        assert hello_solution.hello("BAAA") == 160
        assert hello_solution.hello("BCCC") == 90