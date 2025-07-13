# ★ def 定义函数，名字叫 add_tag
# 参数 tag → 标签名，text → 要包起来的文字
def add_tag(tag: str, text: str) -> str:
    # ★ f-string 拼接字符串，效果：把 text 用 <tag>...</tag> 包起来
    return f"<{tag}>{text}</{tag}>"