# Description: Artificial intelligence that solves math puzzles like the ones posed in Calculator: The Game.
# Author: Greg Schmitt
# Date: 2018-06-13

# ----- CONSTANTS -----
NO_SOLUTION_STRING = "No solutions found!"
SOLUTION_STRING = "Level {} Solution: {}"

OPERAND_RANGE = 100
# ---------------------

# ----- OPERATION LISTS -----
# Lists of functions where the index is the operand
# which should be used on the parameter.

# e.g. ADD[7](100) = 100 + 7 = 107
ADD = []
for i in range(OPERAND_RANGE):
    function = lambda n, a=i: add(n, a)
    function.__name__ = "add {}".format(i)
    ADD.append(function)

# e.g. SUBTRACT[7](100) = 100 - 7 = 93
SUBTRACT = []
for i in range(OPERAND_RANGE):
    function = lambda n, a=i: subtract(n, a)
    function.__name__ = "subtract {}".format(i)
    SUBTRACT.append(function)

# e.g. APPEND[7](100) = 100 || 7 = 1007
APPEND = []
for i in range(OPERAND_RANGE):
    function = lambda n, a=i: append(n, a)
    function.__name__ = "append {}".format(i)
    APPEND.append(function)

# e.g. MULTIPLY[7](100) = 100 * 7 = 700
MULTIPLY = []
for i in range(OPERAND_RANGE):
    function = lambda n, a=i: multiply(n, a)
    function.__name__ = "multiply by {}".format(i)
    MULTIPLY.append(function)

# e.g. MULTIPLY_NEGATIVE[7](100) = 100 * -7 = -700
MULTIPLY_NEGATIVE = []
for i in range(OPERAND_RANGE):
    function = lambda n, a=i: multiply(n, -a)
    function.__name__ = "multiply by -{}".format(i)
    MULTIPLY_NEGATIVE.append(function)

# e.g. DIVIDE[7](42) = 42 / 7 = 6
DIVIDE = []
for i in range(OPERAND_RANGE): # WARNING: Using DIVIDE[0] will raise ZeroDivisionException
    function = lambda n, a=i: divide(n, a)
    function.__name__ = "divide by {}".format(i)
    DIVIDE.append(function)

# e.g. EXPONENTIATE[6](2) = 2^6 = 64
EXPONENTIATE = []
for i in range(OPERAND_RANGE):
    function = lambda n, a=i: exponentiate(n, a)
    function.__name__ = "raise to the power of {}".format(i)
    EXPONENTIATE.append(function)
# ---------------------------

# ----- OPERATION MATRICES -----
# Matrices of functions where the indices are the operands
# which should be used on the parameter.

# e.g. CHANGE[1][4](121212) = change 1 to 4 in 121212 = 424242
CHANGE = []
for i in range(OPERAND_RANGE):
    changei = []
    for j in range(OPERAND_RANGE):
        function = lambda n, a=i, b=j: change(n, a, b)
        function.__name__ = "change {} to {}".format(i, j)
        changei.append(function)
    CHANGE.append(changei)
# ------------------------------

# Main function which prints the solutions to levels 1-80 of Calculator: The Game.
def main():
    # Format: Level, getPath(OperationsTuple, Start, Goal, Moves)
    printSolution(1,  (ADD[1],),                                                              0,     2, 2)
    printSolution(2,  (ADD[2], ADD[3]),                                                       0,     8, 3)
    printSolution(3,  (MULTIPLY[4], ADD[1], ADD[2]),                                          0,    12, 3)
    printSolution(4,  (ADD[4], SUBTRACT[2]),                                                  1,     7, 3)
    printSolution(5,  (ADD[4], MULTIPLY[4], DIVIDE[4]),                                       3,     4, 3)
    printSolution(6,  (ADD[2], MULTIPLY[4]),                                                  0,    64, 4)
    printSolution(7,  (DIVIDE[3], ADD[3], MULTIPLY[3]),                                       4,     5, 3)
    printSolution(8,  (delete,),                                                           4321,     4, 3)
    printSolution(9,  (ADD[8], MULTIPLY[5], delete),                                          0,     4, 3)
    printSolution(10, (DIVIDE[5], MULTIPLY[3], delete),                                      50,     9, 4)
    printSolution(11, (SUBTRACT[8], MULTIPLY[11], delete),                                   99,   100, 3)
    printSolution(12, (ADD[8], MULTIPLY[10], DIVIDE[2]),                                      0,   404, 5)
    printSolution(13, (MULTIPLY[2], SUBTRACT[9], delete),                                   171,    23, 4)
    printSolution(14, (ADD[5], MULTIPLY[3], MULTIPLY[5], delete),                             0,    21, 5)
    printSolution(15, (MULTIPLY[3], MULTIPLY[2], SUBTRACT[5]),                               10,    50, 3)
    printSolution(16, (ADD[4], MULTIPLY[9], delete),                                          0,     2, 5)
    printSolution(17, (APPEND[1],),                                                           0,    11, 2)
    printSolution(18, (APPEND[1], APPEND[0]),                                                 0,   101, 3)
    printSolution(19, (APPEND[2], MULTIPLY[2]),                                               0,    44, 3)
    printSolution(20, (ADD[3], APPEND[5]),                                                    0,    35, 2)
    printSolution(21, (APPEND[1], ADD[5]),                                                    0,    56, 3)
    printSolution(22, (ADD[2], DIVIDE[3], APPEND[1]),                                         0,     9, 4)
    printSolution(23, (APPEND[0], ADD[2], DIVIDE[5]),                                        15,    10, 4)
    printSolution(24, (SUBTRACT[5], ADD[5], APPEND[5], APPEND[2]),                            0,   210, 5)
    printSolution(25, (APPEND[0], ADD[4], DIVIDE[2]),                                        40,  2020, 4)
    printSolution(26, (APPEND[12], delete),                                                   0,    11, 4)
    printSolution(27, (APPEND[10], ADD[1], delete),                                           0,   102, 4)
    printSolution(28, (APPEND[1], CHANGE[1][2]),                                              0,   222, 4)
    printSolution(29, (ADD[6], MULTIPLY[7], CHANGE[6][9]),                                    0,    93, 4)
    printSolution(30, (APPEND[1], APPEND[2], CHANGE[1][2], CHANGE[2][3]),                     0,  2321, 6)
    printSolution(31, (ADD[9], MULTIPLY[2], CHANGE[8][4]),                                    0,    24, 6)
    printSolution(32, (DIVIDE[2], ADD[3], CHANGE[1][2], CHANGE[2][9]),                       11,    29, 5)
    printSolution(33, (ADD[3], DIVIDE[3], CHANGE[1][2]),                                     36,    20, 5)
    printSolution(34, (DIVIDE[3], APPEND[1], MULTIPLY[2], CHANGE[4][5]),                      2,    15, 4)
    printSolution(35, (CHANGE[23][41], CHANGE[24][14], CHANGE[12][24], CHANGE[14][2]),     1234,   414, 4)
    printSolution(36, (ADD[6], APPEND[5], SUBTRACT[7]),                                       0,   -85, 4)
    printSolution(37, (SUBTRACT[1], SUBTRACT[2], EXPONENTIATE[2]),                            0,     9, 3)
    printSolution(38, (MULTIPLY[5], SUBTRACT[6], APPEND[4]),                                  0,  -120, 4)
    printSolution(39, (SUBTRACT[1], APPEND[2], EXPONENTIATE[2]),                              0,   144, 3)
    printSolution(40, (negative,),                                                           -5,     5, 1)
    printSolution(41, (ADD[4], ADD[2], negative),                                             0,    -6, 3)
    printSolution(42, (ADD[3], SUBTRACT[7], negative),                                        0,   -13, 4)
    printSolution(43, (ADD[5], SUBTRACT[10], MULTIPLY[4], negative),                          0,    60, 4)
    printSolution(44, (ADD[9], DIVIDE[2], MULTIPLY[4], negative),                            44,    52, 5)
    printSolution(45, (ADD[5], MULTIPLY[5], negative),                                        9,    10, 5)
    printSolution(46, (APPEND[6], ADD[5], DIVIDE[8], negative),                              14,    12, 5)
    printSolution(47, (ADD[9], negative, delete),                                            55,    13, 4)
    printSolution(48, (SUBTRACT[3], APPEND[5], MULTIPLY[4], negative),                        0,   245, 5)
    printSolution(49, (MULTIPLY_NEGATIVE[3], DIVIDE[3], ADD[9], negative),                   39,    12, 4)
    printSolution(50, (MULTIPLY[3], SUBTRACT[9], negative, delete),                         111,   126, 6)
    printSolution(51, (SUBTRACT[5], ADD[8], DIVIDE[7], negative),                            34,     3, 5)
    printSolution(52, (SUBTRACT[4], MULTIPLY_NEGATIVE[4], DIVIDE[3], negative, DIVIDE[8]),   25,     4, 5)
    printSolution(53, (reverse,),                                                            12,    21, 1)
    printSolution(54, (ADD[6], ADD[9], reverse),                                              0,    51, 3)
    printSolution(55, (APPEND[1], ADD[9], reverse),                                         100,   101, 3)
    printSolution(56, (SUBTRACT[1], reverse),                                              1101,   100, 4)
    printSolution(57, (ADD[4], MULTIPLY[4], SUBTRACT[3], reverse),                            0,    58, 4)
    printSolution(58, (APPEND[1], DIVIDE[4], reverse),                                        6,     4, 3)
    printSolution(59, (ADD[9], MULTIPLY[5], reverse),                                        15,    21, 3)
    printSolution(60, (DIVIDE[2], reverse),                                                 100,    13, 5)
    printSolution(61, (APPEND[1], reverse),                                                  10, 11011, 4)
    printSolution(62, (APPEND[10], MULTIPLY[4], ADD[5], reverse),                             0,   102, 4)
    printSolution(63, (APPEND[2], ADD[1], DIVIDE[3], reverse),                                0,     7, 4)
    printSolution(64, (APPEND[5], MULTIPLY[4], MULTIPLY[2], reverse),                         0,     4, 4)
    printSolution(65, (APPEND[2], SUBTRACT[1], reverse),                                    121,   212, 3)
    printSolution(66, (MULTIPLY[3], APPEND[1], DIVIDE[5], reverse),                           8,     9, 5)
    printSolution(67, (ADD[7], ADD[8], ADD[9], reverse),                                      0,    13, 5)
    printSolution(68, (ADD[3], APPEND[1], SUBTRACT[2], reverse),                              0,   123, 6)
    printSolution(69, (APPEND[6], ADD[8], reverse),                                           0,   424, 5)
    printSolution(70, (SUBTRACT[9], MULTIPLY[3], ADD[4], negative, reverse),                  7,    81, 5)
    printSolution(71, (SUBTRACT[5], ADD[7], SUBTRACT[9], reverse),                            0,   -43, 5)
    printSolution(72, (ADD[6], SUBTRACT[3], reverse, delete),                                 0,    28, 7)
    printSolution(73, (APPEND[1], ADD[2], MULTIPLY[3], reverse),                              0,   136, 5)
    printSolution(74, (ADD[5], reverse, negative),                                            0,    -1, 4)
    printSolution(75, (ADD[4], MULTIPLY[3], reverse, negative),                               0,   -25, 5)
    printSolution(76, (ADD[7], MULTIPLY[3], reverse, negative),                               0,    -5, 5)
    printSolution(77, (DIVIDE[4], SUBTRACT[4], reverse),                                     88,    41, 4)
    printSolution(78, (APPEND[0], MULTIPLY[2], CHANGE[2][10], reverse, CHANGE[0][1]),       100,   101, 5)
    printSolution(79, (DIVIDE[2], APPEND[5], CHANGE[5][4], reverse),                          0,   424, 7)
    printSolution(80, (APPEND[9], DIVIDE[9], reverse, CHANGE[1][0]),                         99,   100, 5)

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
            if pathToSolution != NO_SOLUTION_STRING:
                # Path found, build current section of path
                currentPath = "" if first else " -> "
                currentPath += "{} -> {}".format(str(current),
                                                 operation.__name__)
                # Add current section of path to solution and return
                return currentPath + pathToSolution

    # Base case 2: No moves left.
    return NO_SOLUTION_STRING

# ----- UNARY OPERATIONS ----
# operation(operand) = result

# e.g. reverse(1337) = 7331, reverse(1020) = 0201 = 201, reverse(-42) = -24
def reverse(n):
    result = str(n)[::-1]

    # Move negative sign to front if there is one
    if result[-1] == '-':
        result = "-" + result[:-1]

    return num(result)

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

# Prints the solution to a level given by operationsTuple, current, goal, and movesLeft.
def printSolution(level, operationsTuple, current, goal, movesLeft):
    print(SOLUTION_STRING.format(level, getPath(operationsTuple, current, goal, movesLeft)))
# --------------------------

# main() caller
if __name__ == "__main__":
    main()
