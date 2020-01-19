def replace_alpha(s):
    l = [str(char) for char in s if char.isnumeric()]
    return "".join(l)


def atoi(s):
    try:
        i = int(float(s))
        if i >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        if i <= -2 ** 31:
            return -2 ** 31
        return i
    except Exception:
        s = s.lstrip()
        if len(s) > 0 and s[0].isnumeric():
            s = replace_alpha(s)
            return int(s)
        elif not s or not s[0].isnumeric():
            return 0


def test_1():
    assert atoi("42") == 42


def test_2():
    assert atoi("   -42") == -42


def test_3():
    assert atoi("4193 with words") == 4193


def test_4():
    assert atoi("words and 987") == 0


def test_5():
    assert atoi("-91283472332") == -2 ** 31


def test_6():
    assert atoi("91283472332") == 2 ** 31 - 1


def test_7():
    assert atoi("3.14159") == 3


def test_8():
    assert atoi("") == 0


def test_9():
    assert atoi("  -0012a42") == -12
