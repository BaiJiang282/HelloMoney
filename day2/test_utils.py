# ★ from ... import 把 utils.py 里的 add_tag 拿过来用
from utils import add_tag

# ★ 真正执行：把 "Hello World" 包成 <h1>Hello World</h1> 并打印
print(add_tag("h1", "Hello World"))
