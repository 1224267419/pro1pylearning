def sum_digits1(n):
    """返回正整数 n 的所有数字位之和"""
    if n < 10:  # 递归退出条件
        return n
    else:  # 求剩余整数各位之和
        return sum_digits1(n // 10) + n % 10
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def is_even(n):
    if n == 0: #偶数
        return True
    else:
        if (n - 1) == 0:#奇数
            return False
        else:
            return is_even(n-2)#递归
def play_alice(n):
    if n==1:
        return "A"
    if n==2:
        return "B"
    if n%2==0:
        return play_alice(n-2)
    if n%2==1:
        return play_alice(n-3)


# print(sum_digits1(15115))
# print(fibonacci(10))
print(is_even(98))
print(play_alice(20))