#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查所有语言的 README 条款数量是否一致
"""

import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

README_FILES = [
    "README.md", "README.en.md", "README.ja.md", "README.es.md",
    "README.fr.md", "README.de.md", "README.ko.md", "README.ru.md"
]

def count_clauses(filepath):
    if not os.path.exists(filepath):
        return -1
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # 匹配类似 "1.1 ", "2.3 " 这样的条款编号
    return len(re.findall(r'^\d+\.\d+\s', content, re.MULTILINE))

def main():
    print("🔍 开始检查多语言条款对齐情况...\n")
    counts = {}
    for filename in README_FILES:
        filepath = os.path.join(BASE_DIR, filename)
        counts[filename] = count_clauses(filepath)

    base_count = counts[README_FILES[0]]
    print(f"基准 ({README_FILES[0]}): {base_count} 条\n")

    error = False
    for filename in README_FILES[1:]:
        count = counts[filename]
        status = "✅" if count == base_count else "❌"
        print(f"{status} {filename}: {count} 条")
        if count != base_count:
            error = True

    if error:
        print("\n⚠️ 发现语言版本间条款数量不一致，请检查是否漏翻或漏加。")
        sys.exit(1)
    else:
        print("\n🎉 所有语言版本条款数量一致！")
        sys.exit(0)

if __name__ == "__main__":
    main()
