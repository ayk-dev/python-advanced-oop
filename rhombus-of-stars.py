INCREASE: int = 1 # global namespace
DECREASE: int = -1
space = ' '
sign = '* '


def print_rhombus(n: int): # global namespace
    # fn-in-fn: closure
    def print_line(i: int, direction: int): # local namespace visible in print_rhombus
        if i == 0: # i is part of the local namespace of print_line
            return
        line = (n - i) * space + i * sign
        print(line.rstrip())
        if i == n:
            direction = DECREASE # change is happening in the local namespace of print_line
        print_line(i + direction, direction) # recusrion

    print_line(1, INCREASE)


n = int(input())
print_rhombus(n)