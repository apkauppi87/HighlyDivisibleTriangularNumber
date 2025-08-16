class HighlyDivisibleTriangularNumber:
    """
    A class to work with triangular numbers and their divisors.

    Features:
    - Calculate nth triangular number
    - Find all divisors of a number
    - Find triangular number by ordinal
    - Find first triangular number with more than N divisors
    """

    def __init__(self):
        """Initialize the class (no special state required)."""
        pass

    @staticmethod
    def triangle_number(n: int) -> int:
        """
        Return the nth triangular number.

        Triangular number formula: (sum of natural numbers)
            T(n) = n * (n + 1) / 2
        """
        return n * (n + 1) // 2

    @staticmethod
    def divisors(num: int) -> list:
        """
        Return a sorted list of divisors of num.

        Uses square root optimization to find divisors in O(sqrt(n)) time.
        """
        divs = set()
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divs.add(i)
                divs.add(num // i)
        return sorted(divs)

    def option_1(self):
        """
        Ask user for an ordinal and print the corresponding triangular number
        along with its divisors. Save result to file:
            Divisors and sum of {n}th term.txt
        """
        n = int(input("Give term ordinal: "))
        t_num = self.triangle_number(n)
        divs = self.divisors(t_num)
        print_format = f"{t_num}: {','.join(map(str, divs))}"
        print(print_format)
        filename = f"Divisors and sum of {n}th term.txt"
        with open(filename, "w") as f:
            f.write(print_format)

    def option_2(self):
        """
        Ask user for a minimum divisor count and find the first triangular
        number with more than that many divisors. Save result to file:
            The first triangle number {min_divisors}.txt
        """
        min_divisors = int(input("Give minimum number of divisors triangle number should have?\n"))
        n = 1
        while True:
            t_num = self.triangle_number(n)
            divs = self.divisors(t_num)
            if len(divs) >= min_divisors:
                print(f"The triangle number is {t_num} and divisors are {','.join(map(str, divs))}")
                filename = f"The first triangle number {min_divisors}.txt"
                with open(filename, "w") as f:
                    f.write(f"{t_num}: {','.join(map(str, divs))}")
                break
            n += 1

    def run(self):
        """
        Run the interactive menu:
        - Option 1: Triangular number by ordinal
        - Option 2: First triangular number with more than N divisors
        - q: Quit
        """
        while True:
            print("\nOptions:")
            print("1")
            print("2")
            print("q")
            choice = input().strip()
            if choice == "1":
                self.option_1()
            elif choice == "2":
                self.option_2()
            elif choice.lower() == "q":
                break
            else:
                print("Invalid choice")


if __name__ == "__main__":
    program = HighlyDivisibleTriangularNumber()
    program.run()
