from tools.time_measure import time_measure


class Solution1:
    @time_measure
    def fizzBuzz(self, n: int) -> list[str]:
        r = []
        for i in range(1, n + 1):
            d1 = i % 3 == 0
            d2 = i % 5 == 0
            if d1 and d2:
                r.append("FizzBuzz")
            if d1:
                r.append("Fizz")
            if d2:
                r.append("Buzz")
            r.append(str(i))
        return r
class Solution2:
    @time_measure
    def fizzBuzz(self, n: int) -> list[str]:
        def f(i):
            d1 = i % 3 == 0
            d2 = i % 5 == 0
            if d1 and d2:
                return "FizzBuzz"
            if d1:
                return "Fizz"
            if d2:
                return "Buzz"
            return str(i)

        return [f(i) for i in range(1, n + 1)]


class Solution3:
    @time_measure
    def fizzBuzz(self, n: int) -> list[str]:
        l = [str(i) for i in range(1, n + 1)]
        for i in range(2, n, 3):
            l[i] = "Fizz"
        for i in range(4, n, 5):
            l[i] = "Buzz"
        for i in range(14, n, 15):
            l[i] = "FizzBuzz"
        return l


# from https://beapython.dev/2020/09/16/best-python-fizzbuzz-code-on-the-entire-internet/
class Solution4:
    @time_measure
    def fizzBuzz(self, n: int) -> list[str]:
        return ["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i) for i in range(n)]


# from https://beapython.dev/2020/09/16/best-python-fizzbuzz-code-on-the-entire-internet/
class Solution5:
    @time_measure
    def fizzBuzz(self, n: int) -> list[str]:
        modulo_list = [
            (3, "Fizz"),
            (5, "Buzz")
        ]
        r = []
        for i in range(1, n):
            print_string = ""
            for mod in modulo_list:
                if i % mod[0] == 0:
                    print_string += mod[1]

            if print_string == "":
                r.append(str(i))
            else:
                r.append(print_string)


Solution1.fizzBuzz(Solution1, 1000000)
Solution2.fizzBuzz(Solution2, 1000000)
Solution3.fizzBuzz(Solution3, 1000000)
Solution4.fizzBuzz(Solution4, 1000000)
Solution5.fizzBuzz(Solution5, 1000000)

# == Execution time: 0.40635132789611816 seconds ==
# == Execution time: 0.31299352645874023 seconds ==
# == Execution time: 0.2448101043701172 seconds == - mine last version
# == Execution time: 0.30968308448791504 seconds ==
# == Execution time: 0.4215700626373291 seconds ==