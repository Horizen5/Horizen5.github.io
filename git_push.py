#!/usr/bin/env python
import subprocess
import os
import sys

def run_command(cmd, cwd=None):
    """执行命令并返回结果"""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {' '.join(cmd)}")
        print(f"错误信息: {e.stderr}")
        return None

def main():
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    print(f"当前目录: {script_dir}")
    
    # 检查是否在 git 仓库中
    if not os.path.exists(os.path.join(script_dir, '.git')):
        print("错误：当前目录不是 git 仓库！")
        print("请先使用 'git init' 初始化仓库")
        input("按回车键退出...")
        return
    
    # 0. 先拉取远程更新
    print("\n0. 拉取远程更新...")
    result = run_command(['git', 'pull', 'origin', 'main'], script_dir)
    if result is None:
        print("拉取失败，尝试继续执行...")
    
    # 1. 添加所有文件
    print("\n1. 添加所有文件...")
    result = run_command(['git', 'add', '.'], script_dir)
    if result is None:
        input("按回车键退出...")
        return
    
    # 2. 获取状态
    print("\n2. 检查文件状态...")
    result = run_command(['git', 'status'], script_dir)
    if result:
        print(result)
    
    # 3. 提交（使用当前日期作为提交信息）
    import datetime
    commit_msg = f"更新于 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    print(f"\n3. 提交更改: {commit_msg}")
    result = run_command(['git', 'commit', '-m', commit_msg], script_dir)
    if result is None:
        print("没有需要提交的更改")
        input("按回车键退出...")
        return
    
    # 4. 推送到 GitHub
    print("\n4. 推送到 GitHub...")
    result = run_command(['git', 'push', 'origin', 'main'], script_dir)
    
    # 如果推送失败，尝试强制推送
    if result is None:
        print("\n普通推送失败，尝试强制推送...")
        print("警告：强制推送会覆盖远程仓库的内容！")
        result = run_command(['git', 'push', '-f', 'origin', 'main'], script_dir)
        if result is None:
            input("按回车键退出...")
            return
    
    print("\n✅ 成功推送到 GitHub！")
    input("按回车键退出...")

if __name__ == '__main__':
    main()