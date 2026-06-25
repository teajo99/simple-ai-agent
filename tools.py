import datetime
import operator
import re

_ALLOWED_OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

_EXPR_PATTERN = re.compile(r"^\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*$")


def calculate(expression):
    match = _EXPR_PATTERN.match(expression)
    if not match:
        return "Sorry, I can only handle simple expressions like '4 + 5'."

    left_str, op, right_str = match.groups()
    left = float(left_str)
    right = float(right_str)

    if op == "/" and right == 0:
        return "Error: division by zero."

    result = _ALLOWED_OPERATORS[op](left, right)

    if result == int(result):
        result = int(result)

    return f"{expression.strip()} = {result}"


def get_time():
    now = datetime.datetime.now()
    return now.strftime("It is currently %H:%M:%S on %A, %d %B %Y.")


AVAILABLE_TOOLS = {
    "calculate": calculate,
    "get_time": get_time,
}