def f(t, y):
    return t - y**2


def euler_method(f, t0, y0, t_end, n):
    h = (t_end - t0) / n
    t = t0
    y = y0
    for _ in range(n):
        y = y + h * f(t, y)
        t = t + h
    return y


def runge_kutta_method(f, t0, y0, t_end, n):
    h = (t_end - t0) / n
    t = t0
    y = y0
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h/2, y + h * k1 / 2)
        k3 = f(t + h/2, y + h * k2 / 2)
        k4 = f(t + h, y + h * k3)
        y = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        t = t + h
    return y


def main():
    t0 = 0
    y0 = 1
    t_end = 2
    n = 10

    euler_result = euler_method(f, t0, y0, t_end, n)
    rk_result = runge_kutta_method(f, t0, y0, t_end, n)

    print(euler_result)
    print(rk_result)


if __name__ == '__main__':
    main()
