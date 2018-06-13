# Description: Artificial intelligence that solves math puzzles like the ones posed in Calculator: The Game.
# Author: Greg Schmitt
# Date: 2018-06-13

# ----- CONSTANTS -----
CONST_NO_SOL = "No solutions found!"
CONST_SOL = "Level {} Solution: {}"
# ---------------------


# ----- OPERATION LISTS -----
# Lists of functions where the index is the operand
# which should be used on the parameter.

# e.g. ADD[7](100) = 100 + 7 = 107
ADD = []
for i in range(0, 100):
    function = lambda n, a=i: add(n, a)
    function.__name__ = "add {}".format(i)
    ADD.append(function)

# e.g. SUBTRACT[7](100) = 100 - 7 = 93
SUBTRACT = []
for i in range(0, 100):
    function = lambda n, a=i: subtract(n, a)
    function.__name__ = "subtract {}".format(i)
    SUBTRACT.append(function)

# e.g. APPEND[7](100) = 100 || 7 = 1007
APPEND = []
for i in range(0, 100):
    function = lambda n, a=i: append(n, a)
    function.__name__ = "append {}".format(i)
    APPEND.append(function)

# e.g. MULTIPLY[7](100) = 100 * 7 = 700
MULTIPLY = []
for i in range(0, 100):
    function = lambda n, a=i: multiply(n, a)
    function.__name__ = "multiply by {}".format(i)
    MULTIPLY.append(function)

# e.g. MULTIPLY_NEGATIVE[7](100) = 100 * -7 = -700
MULTIPLY_NEGATIVE = []
for i in range(0, 100):
    function = lambda n, a=i: multiply(n, -a)
    function.__name__ = "multiply by -{}".format(i)
    MULTIPLY_NEGATIVE.append(function)

# e.g. DIVIDE[7](42) = 42 / 7 = 6
DIVIDE = []
for i in range(0, 100): # WARNING: Using DIVIDE[0] will raise ZeroDivisionException
    function = lambda n, a=i: divide(n, a)
    function.__name__ = "divide by {}".format(i)
    DIVIDE.append(function)

# e.g. EXPONENTIATE[6](2) = 2^6 = 64
EXPONENTIATE = []
for i in range(0, 100):
    function = lambda n, a=i: exponentiate(n, a)
    function.__name__ = "raise to the power of {}".format(i)
    EXPONENTIATE.append(function)
# ---------------------------

# ----- OPERATION MATRICES -----
# Matrices of functions where the indices are the operands
# which should be used on the parameter.

# e.g. CHANGE[1][4](121212) = change 1 to 4 in 121212 = 424242
CHANGE = []
for i in range(0, 100):
    changei = []
    for j in range(0, 100):
        function = lambda n, a=i, b=j: change(n, a, b)
        function.__name__ = "change {} to {}".format(i, j)
        changei.append(function)
    CHANGE.append(changei)
# ------------------------------

# Main function which prints the solutions to levels 1-50 of Calculator: The Game.
def main():
    # Format: Level, getPath(OperationsTuple, Start, Goal, Moves)
    print(CONST_SOL.format(1, getPath((ADD[1],),
                                                0, 2, 2)))
    print(CONST_SOL.format(2, getPath((ADD[2], ADD[3]),
                                                0, 8, 3)))
    print(CONST_SOL.format(3, getPath((MULTIPLY[4], ADD[1], ADD[2]),
                                                0, 12, 3)))
    print(CONST_SOL.format(4, getPath((ADD[4], SUBTRACT[2]),
                                                1, 7, 3)))
    print(CONST_SOL.format(5, getPath((ADD[4], MULTIPLY[4], DIVIDE[4]),
                                                3, 4, 3)))
    print(CONST_SOL.format(6, getPath((ADD[2], MULTIPLY[4]),
                                                0, 64, 4)))
    print(CONST_SOL.format(7, getPath((DIVIDE[3], ADD[3], MULTIPLY[3]),
                                                4, 5, 3)))
    print(CONST_SOL.format(8, getPath((delete,),
                                                4321, 4, 3)))
    print(CONST_SOL.format(9, getPath((ADD[8], MULTIPLY[5], delete),
                                                0, 4, 3)))
    print(CONST_SOL.format(10, getPath((DIVIDE[5], MULTIPLY[3], delete),
                                                 50, 9, 4)))
    print(CONST_SOL.format(11, getPath((SUBTRACT[8], MULTIPLY[11], delete),
                                                 99, 100, 3)))
    print(CONST_SOL.format(12, getPath((ADD[8], MULTIPLY[10], DIVIDE[2]),
                                                 0, 404, 5)))
    print(CONST_SOL.format(13, getPath((MULTIPLY[2], SUBTRACT[9], delete),
                                                 171, 23, 4)))
    print(CONST_SOL.format(14, getPath((ADD[5], MULTIPLY[3], MULTIPLY[5], delete),
                                                 0, 21, 5)))
    print(CONST_SOL.format(15, getPath((MULTIPLY[3], MULTIPLY[2], SUBTRACT[5]),
                                                 10, 50, 3)))
    print(CONST_SOL.format(16, getPath((ADD[4], MULTIPLY[9], delete),
                                                 0, 2, 5)))
    print(CONST_SOL.format(17, getPath((APPEND[1],),
                                                 0, 11, 2)))
    print(CONST_SOL.format(18, getPath((APPEND[1], APPEND[0]),
                                                 0, 101, 3)))
    print(CONST_SOL.format(19, getPath((APPEND[2], MULTIPLY[2]),
                                                 0, 44, 3)))
    print(CONST_SOL.format(20, getPath((ADD[3], APPEND[5]),
                                                 0, 35, 2)))
    print(CONST_SOL.format(21, getPath((APPEND[1], ADD[5]),
                                                 0, 56, 3)))
    print(CONST_SOL.format(22, getPath((ADD[2], DIVIDE[3], APPEND[1]),
                                                 0, 9, 4)))
    print(CONST_SOL.format(23, getPath((APPEND[0], ADD[2], DIVIDE[5]),
                                                 15, 10, 4)))
    print(CONST_SOL.format(24, getPath((SUBTRACT[5], ADD[5], APPEND[5], APPEND[2]),
                                                 0, 210, 5)))
    print(CONST_SOL.format(25, getPath((APPEND[0], ADD[4], DIVIDE[2]),
                                                 40, 2020, 4)))
    print(CONST_SOL.format(26, getPath((APPEND[12], delete),
                                                 0, 11, 4)))
    print(CONST_SOL.format(27, getPath((APPEND[10], ADD[1], delete),
                                                 0, 102, 4)))
    print(CONST_SOL.format(28, getPath((APPEND[1], CHANGE[1][2]),
                                                 0, 222, 4)))
    print(CONST_SOL.format(29, getPath((ADD[6], MULTIPLY[7], CHANGE[6][9]),
                                                 0, 93, 4)))
    print(CONST_SOL.format(30, getPath((APPEND[1], APPEND[2], CHANGE[1][2], CHANGE[2][3]),
                                                 0, 2321, 6)))
    print(CONST_SOL.format(31, getPath((ADD[9], MULTIPLY[2], CHANGE[8][4]),
                                                 0, 24, 6)))
    print(CONST_SOL.format(32, getPath((DIVIDE[2], ADD[3], CHANGE[1][2], CHANGE[2][9]),
                                                 11, 29, 5)))
    print(CONST_SOL.format(33, getPath((ADD[3], DIVIDE[3], CHANGE[1][2]),
                                                 36, 20, 5)))
    print(CONST_SOL.format(34, getPath((DIVIDE[3], APPEND[1], MULTIPLY[2], CHANGE[4][5]),
                                                 2, 15, 4)))
    print(CONST_SOL.format(35, getPath((CHANGE[23][41], CHANGE[24][14], CHANGE[12][24], CHANGE[14][2]),
                                                 1234, 414, 4)))
    print(CONST_SOL.format(36, getPath((ADD[6], APPEND[5], SUBTRACT[7]),
                                                 0, -85, 4)))
    print(CONST_SOL.format(37, getPath((SUBTRACT[1], SUBTRACT[2], EXPONENTIATE[2]),
                                                 0, 9, 3)))
    print(CONST_SOL.format(38, getPath((MULTIPLY[5], SUBTRACT[6], APPEND[4]),
                                                 0, -120, 4)))
    print(CONST_SOL.format(39, getPath((SUBTRACT[1], APPEND[2], EXPONENTIATE[2]),
                                                 0, 144, 3)))
    print(CONST_SOL.format(40, getPath((negative,),
                                                 -5, 5, 1)))
    print(CONST_SOL.format(41, getPath((ADD[4], ADD[2], negative),
                                                 0, -6, 3)))
    print(CONST_SOL.format(42, getPath((ADD[3], SUBTRACT[7], negative),
                                                 0, -13, 4)))
    print(CONST_SOL.format(43, getPath((ADD[5], SUBTRACT[10], MULTIPLY[4], negative),
                                                 0, 60, 4)))
    print(CONST_SOL.format(44, getPath((ADD[9], DIVIDE[2], MULTIPLY[4], negative),
                                                 44, 52, 5)))
    print(CONST_SOL.format(45, getPath((ADD[5], MULTIPLY[5], negative),
                                                 9, 10, 5)))
    print(CONST_SOL.format(46, getPath((APPEND[6], ADD[5], DIVIDE[8], negative),
                                                 14, 12, 5)))
    print(CONST_SOL.format(47, getPath((ADD[9], negative, delete),
                                                 55, 13, 4)))
    print(CONST_SOL.format(48, getPath((SUBTRACT[3], APPEND[5], MULTIPLY[4], negative),
                                                 0, 245, 5)))
    print(CONST_SOL.format(49, getPath((MULTIPLY_NEGATIVE[3], DIVIDE[3], ADD[9], negative),
                                                 39, 12, 4)))
    print(CONST_SOL.format(50, getPath((MULTIPLY[3], SUBTRACT[9], negative, delete),
                                                 111, 126, 6)))

# Performs a recursive depth-limited DFS (aka DLS) to find path to solution.
# Preconditions:
#   operationsTuple is a tuple of single-parameter operations.
#   current is the current number, or root of the tree which will be generated by this call.
#   goal is the goal number. The search will terminate when this has been reached.
#   movesLeft is the depth to which the DFS will be limited.
#   first refers to whether this is the initial call to getPath. Used for building the path string.
# Postconditions:
#   Returns a string representing the path from current to goal. It is of the format:
#   current -> operation1 -> n1 -> operation2 -> n2 -> ... -> goal
#   e.g. 0 -> add 2 -> 2 -> append 1 -> 21 -> divide by 3 -> 7 -> add 2 -> 9
def getPath(operationsTuple, current, goal, movesLeft, first=True):
    # Base case 1: Goal reached.
    if current == goal:
        return " -> {}".format(str(current))
    
    # Recursive Case: Moves left, but goal not reached.
    if movesLeft > 0:
        # Try every operation
        for operation in operationsTuple:
            # Get path to solution, if there is one
            pathToSolution = getPath(operationsTuple,
                                     operation(current),
                                     goal,
                                     movesLeft - 1,
                                     False)
            if pathToSolution != CONST_NO_SOL:
                # Path found, build current section of path
                currentPath = "" if first else " -> "
                currentPath += "{} -> {}".format(str(current),
                                                 operation.__name__)
                # Add current section of path to solution and return
                return currentPath + pathToSolution

    # Base case 2: No moves left.
    return CONST_NO_SOL

# ----- UNARY OPERATIONS ----
# operation(operand) = result

# e.g. reverse(1337) = 7331, reverse(1020) = 0201 = 201
def reverse(n):
    return num(str(n)[::-1])

# e.g. delete(1234) = 123, delete(7) = 0, delete(-7) = 0
def delete(n):
    # Convert to string for manipulation
    n = str(n)

    # Remove last character from string
    n = n[:-1]
    
    # If empty or sign only, return 0
    if n == "" or len(n) == 1 and n[0] == '-':
        return 0
    else:
        return num(n)

# e.g. negative(7) = -7, negative(-42) = 42
def negative(n):
    return -n
# ---------------------------

# ----- BINARY OPERATIONS -----
# operation(operand, operand) = result

# e.g. append(13, 37) = 13 || 37 = 1337, append(0, 7) = 0 || 7 = 07 = 7
def append(n, a):
    return num(str(n) + str(a))

# e.g. add(13, 37) = 13 + 37 = 50
def add(n, a):
    return n + a

# e.g. subtract(13, 37) = 13 - 37 = -24
def subtract(n, a):
    return n - a

# e.g. multiply(100, 7) = 100 * 7 = 700
def multiply(n, a):
    return n * a

# e.g. divide(42, 7) = 42 / 7 = 6, 9
# divide(n, 0) throws ZeroDivisionException.
def divide(n, a):
    # Try float division, then convert to integer if appropriate.
    result = n / a
    if float.is_integer(result):
        # e.g. 9 / 3 = 3.0 -> return 3
        return int(result)
    else:
        # e.g. 9 / 2 = 4.5 -> return 4.5
        return result

# e.g. exponentiate(2, 6) = 2^6 = 64
def exponentiate(n, a):
    return n ** a
# -----------------------------

# ----- TRINARY OPERATIONS -----
# operation(operand, operand, operand) = result

# e.g. change(121212, 1, 4) = change 1 to 4 in 121212 = 424242
def change(n, a, b):
    # Convert operands to ttheir string counterparts
    n = str(n)
    a = str(a)
    b = str(b)

    # Parse through string
    for i in range(len(n)):
        # Check if a appears at n[i]
        if n[i:].startswith(a):
            # Replaces a with b
            n = n[:i] + b + n[i + len(a):]

    # Convert back to number
    return num(n)
# ------------------------------

# ----- HELPER METHODS -----
# Converts string representation of number to int or float, where appropriate.
# If string cannot be converted to int or float, throws ValueError.
def num(string):
    try:
        return int(string)
    except ValueError:
        return float(string)
# --------------------------

# main() caller
if __name__ == "__main__":
    main()
