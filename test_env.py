# -*- coding: utf-8 -*-
"""环境验证脚本 —— 在 VS Code 里按右上角 ▶ 运行"""
import sys

print("=" * 54)
print("Python 版本 :", sys.version.split()[0])
print("解释器路径  :", sys.executable)
print("=" * 54)

for name in ("numpy", "pandas", "sklearn", "matplotlib"):
    try:
        m = __import__(name)
        print(f"  {name:12s} {getattr(m, '__version__', '?')}")
    except ImportError:
        print(f"  {name:12s} ❌ 未安装")

print("=" * 54)

# 真的算一次
import numpy as np
X = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([2.0, 4.0, 6.0, 8.0])
w = float((X @ y) / (X @ X))
print(f"  拟合 y = {w:.2f}x     （真实是 y = 2x）")
print("=" * 54)

if "envs/ml-learning" in sys.executable:
    print("✅ 解释器正确：ml-learning —— 可以开始第 1 周任务了")
elif sys.executable.endswith("/anaconda3/bin/python"):
    print("❌ 用的是 base 环境（Python 3.14），库不全")
    print("   ⌘⇧P → Python: Select Interpreter → 选 ml-learning")
else:
    print(f"❌ 解释器不对：{sys.executable}")
    print("   ⌘⇧P → Python: Select Interpreter")
    print("   → /opt/anaconda3/envs/ml-learning/bin/python")
print("=" * 54)
