class Solution:
    """
    Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' operation, the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are infinite solutions for the equation.
    If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.

    Example 1:
    Input: equation = "x+5-3+x=6+x-2"
    Output: "x=2"

    Example 2:
    Input: equation = "x=x"
    Output: "Infinite solutions"

    Example 3:
    Input: equation = "2x=x"
    Output: "x=0"

    More challenges
    592. Fraction Addition and Subtraction
    2232. Minimize Result by Adding Parentheses to Expression
    """
    @staticmethod
    def solveEquation(equation):
        def helper(s):
            """Parse s into coefficients"""
            ii = x = y = 0
            for i in range(len(s)+1):
                if i == len(s) or s[i] in "+-":
                    if ii < i:
                        y += int(s[ii:i])
                    ii = i
                elif s[i] == "x":
                    if ii == i or s[ii:i] in "+-":
                        x += int(s[ii:i] + "1")
                    else:
                        x += int(s[ii:i])
                    ii = i+1
            return x, y

        lhs, rhs = equation.split("=")
        (lx, ly), (rx, ry) = helper(lhs), helper(rhs)
        if lx == rx:
            if ly != ry:
                return "No solution"
            else:
                return "Infinite solutions"
        else:
            return f"x={(ry-ly)//(lx-rx)}"

print(Solution.solveEquation("2x+3x-6x=x+2"))