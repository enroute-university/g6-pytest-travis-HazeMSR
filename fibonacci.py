def last_8(some_int: object):
    """
        Return the last 8 digits of an int
        :param int some_int: the number
        :rtype: int
        @param some_int:
        @return:
    """
    # Converts input to a string and chops last 8 digits
    return int(str(some_int)[-8:])


def optimized_fibonacci(ith_element : int) -> int:
    """
        returns the i-th element of a fibonacci series
    """
    working_window = [0, 1]  # Initial Values for Fibonacci

    next_value = -1  # Default value for invalid input
    if 0 <= ith_element < 2:
        next_value = working_window[
            ith_element
        ]  # Next Value is the one indexed (trivial case)
    else:
        for _ in range(1, ith_element):  #
            next_value = sum(working_window)
            working_window[0] = working_window[1]
            working_window[1] = next_value  # Next Value is computed accordingly
    return next_value


class SummableSequence(object):
    """
        Implements a Summable Sequence of arbitrary initial values
        __call__ returns the value for the i-th element of the series
    """

    def __init__(self, *initial) -> None:
        self.ini = [int(arg) for arg in initial]
        self.len = len(initial)  # Stores the number of initial values in the Sequence

    def __call__(self, i):
        """
        returns the i-th element of the series
        """
        next_value = -1  # Default return value for invalid input
        if 0 <= i < self.len:
            next_value = self.ini[i]
        else:
            working_window = self.ini.copy()
            # minumum segment of the sumable sequence / working area

            for _ in range(self.len - 1, i):
                next_value = sum(working_window)  # Calculate next value
                working_window[:-1] = working_window[1:]  # Shift to left
                working_window[-1] = next_value  # Update last element
        return next_value


if __name__ == "__main__":
    print("fibonnaci (100000) = ", (optimized_fibonacci(1000)))