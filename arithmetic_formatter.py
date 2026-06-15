def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = []
    bottom_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        parts = problem.split()

        num1 = parts[0]
        operator = parts[1]
        num2 = parts[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2

        top_line.append(num1.rjust(width))
        bottom_line.append(operator + num2.rjust(width - 1))
        dash_line.append('-' * width)

        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            answer_line.append(result.rjust(width))

    arranged = '    '.join(top_line) + '\n' + '    '.join(bottom_line) + '\n' + '    '.join(dash_line)

    if show_answers:
        arranged += '\n' + '    '.join(answer_line)

    return arranged

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))