# aria2-autoremove

> 本工具的作用是 删除 aria2 删除任务后残留的文件
>
> 在执行本程序之前，请先确定 aria2 中没有正在下载的任务，否则会一并删除

> This tool will delete aria2 remaining files after delete the task
>
> Please confirm aria2 is not have any download task before run this script, otherwise they will be deleted

## 效果 Result

### 执行之前 Before

```text
- download
    - aaaa
    - aaaa.aria2
    - 123.jpg
    - 456.zip
    - bbbb.mp4
    - bbbb.mp4.aria2
```

### 执行之后 After

```text
- download
    - 123.jpg
    - 456.zip
```

## 使用要求 Require

Python 3.6+

## 使用方法 Usage

```bash
wget https://raw.githubusercontent.com/xfzka/aria2-autoremove/master/autoremove.py
chmod +x autoremove.py
./autoremove.py
```

> 推荐把 autoremove.py 移动到 aria2 的下载目录
>
> Recommend move autoremove.py to aria2 download path
