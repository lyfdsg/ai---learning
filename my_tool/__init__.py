# python 包的 __init__.py（说明my_tool是python包） 文件可以是一个空文件，也可以包含一些初始化代码或者导入语句。
# 当你导入这个包时，__init__.py 文件中的代码会被执行。

# 这行代码控制导入哪些内容
__all__ = ['PI', 'add', 'multiply'] # 只导出这三个名字，其他的名字不会被导出

# 如果每次都要写 from my_tool.math_utils import PI, add, multiply 可能会比较麻烦，
# 我们可以在 __init__.py 文件中直接导入这些函数和变量，
# 这样用户在导入 my_tool 包时就可以直接使用它们了。：
# 这样的话调用这个包时就可以写到：from my_tool import PI, add, multiply
from .math_utils import PI, add, multiply
