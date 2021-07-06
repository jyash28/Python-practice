def to_Power(x):
    def calc_power(n):
        return n**3
    return calc_power

cube = to_Power(3)
print(cube(5))
