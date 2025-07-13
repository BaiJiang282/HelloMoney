import os          # ★ 操作系统相关，比如列文件、改名
import datetime    # ★ 用来获取文件修改时间

def batch_rename():
    # ★ os.listdir() 把当前目录所有文件名列出来
    # endswith 只保留 .jpg 或 .png
    files = [f for f in os.listdir() if f.lower().endswith(('.jpg', '.png'))]
    files.sort()   # ★ 按文件名排序，保证顺序

    for idx, old in enumerate(files, 1):  # ★ enumerate 同时拿到序号 idx 和文件名 old
        ext = os.path.splitext(old)[1]      # ★ 把后缀 .jpg/.png 单独取出来
        # ★ os.path.getmtime 拿文件最后修改时间 → 转成日期字符串
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(old))
        new = f"{mtime.strftime('%Y%m%d')}_{idx:02d}{ext}"  # ★ 拼新名字
        os.rename(old, new)  # ★ 真正改名
        print(f"{old} → {new}")  # ★ 打印对照表

if __name__ == "__main__":   # ★ Python 入口：双击或命令行运行时会执行 batch_rename()
    batch_rename()