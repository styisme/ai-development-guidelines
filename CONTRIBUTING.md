# 贡献指南

感谢你对 **AI 开发规范** 的关注！我们欢迎任何形式的贡献。

## 提交 Issue

- **Bug 报告**：如果你发现规范条款自相矛盾、有歧义，或与实际开发经验严重脱节。
- **功能建议**：如果你认为需要新增一条规范（例如“如何披露微调模型”），请说明场景与理由。
- **翻译纠错**：本规范目前有 8 种语言，如果你发现翻译不准确，请直接提 Issue 指出所在语言和行号。

## 提交 PR

1. **修改条款**
   - 请说明修改的理由，最好能提供一个真实场景作为支撑。
   - **所有语言的版本必须同步更新**。如果你不熟悉某些语言，可以先只改中文和英文，在 PR 描述里注明“需要翻译协助”，我们会用 `translation-outdated` 标签跟进。

2. **新增语言**
   - 请复制一份现有的 `README.md` 和 `DEVELOPMENT_CONSTRAINTS.md`，并命名为 `README.<lang>.md`。
   - 修改 `scripts/update_lang_headers.py` 中的语言列表。
   - 运行 `python scripts/update_lang_headers.py` 自动更新所有文件的头部链接。

3. **修改代码/脚本**
   - 脚本使用 Python 3，请确保兼容 Termux / Pydroid。
   - 不要引入过重的第三方依赖。

## 提交规范

- 使用 [Conventional Commits](https://www.conventionalcommits.org/)。
- 例如：`feat(rule): add clause about model fine-tuning`，`fix(trans): fix typo in Japanese README`。

## 检查清单

提交 PR 前，请确保：

- [ ] 所有语言的条款编号（如 1.1, 1.2）数量一致。
- [ ] 语言切换链接可以互相跳转。
- [ ] 如果是 AI 辅助生成的修改，请在 PR 中说明。

感谢你的贡献！
