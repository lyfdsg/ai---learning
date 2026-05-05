# Math Utilities


def add(a: int, b: int) -> int:#和这个有啥区别def add(a,b):a和b都是整数，所以返回值也是整数
    return a + b#返回值是a和b的和已经是整数，上面那行代码为啥还要写-> int呢？
    # 因为-> int是类型注解，表示返回值是整数，这个是可选的，但是最好还是写上，因为这样更清晰，更易读。

def multiply(a: int, b: int) -> int:#和这个有啥区别def multiply(a,b):a和b都是整数，所以返回值也是整数
    return a * b#返回值是a和b的积

def is_even(n: int) -> bool:#和这个有啥区别def is_even(n):n是整数，所以返回值是布尔值:True或False
    return n % 2 == 0#返回值是n是否是偶数,这里%是取模运算符，表示n除以2的余数，如果余数为0，则n是偶数，否则n是奇数