#!/usr/bin/python3
import os, glob, shutil

help = """
本工具的作用是 删除 aria2 删除任务后残留的文件
在执行本程序之前，请先确定 aria2 中没有正在下载的任务，否则会一并删除
"""

print(help)

currentDir = os.getcwd()
aria2downloadPath = input(f"请输入 aria2 的下载目录({currentDir})：").strip()
if aria2downloadPath:
    if not os.path.exists(aria2downloadPath):
        print("路径不存在")
        exit(1)
    if not os.path.isdir(aria2downloadPath):
        print("不是文件夹")
        exit(1)
else:
    aria2downloadPath = currentDir

willDelete = []
for name in glob.glob(f"{aria2downloadPath}/*.aria2"):
    willDelete.append(name)
    willDelete.append(name.replace(".aria2", ""))

if len(willDelete) == 0:
    print("没有需要删除的文件")
    exit(0)

print(f"要删除的文件：")
print("\n".join(willDelete) + "\n")
confirmDelete = input(f"确定要删除上面的所有文件吗({len(willDelete)}个) y|N :").strip()

if confirmDelete.lower() == "y":
    for target in willDelete:
        if os.path.isdir(target):
            shutil.rmtree(target, ignore_errors=True)
        else:
            os.remove(target)
    print("删除完毕")
else:
    print("取消删除")
