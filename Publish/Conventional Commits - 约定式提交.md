---
publish: true
title: Conventional Commits - 约定式提交
---

**Conventional Commits（约定式提交）** 是一种轻量级的规范，用于定义 Git 提交信息（commit message）的格式。

它的核心目的是：**让提交历史变得可读、可解析，并能够自动化生成变更日志（CHANGELOG）、确定语义化版本号（Semantic Versioning）以及触发 CI/CD流程**


|Type|含义|示例场景|
|---|---|---|
|`feat`|新功能|新增用户登录功能|
|`fix`|修复 bug|修复支付页面崩溃问题|
|`docs`|文档更改|更新 README.md|
|`style`|代码格式调整|空格、分号、缩进等不影响逻辑的修改|
|`refactor`|重构|既不是新增功能也不是修复 bug 的代码改动|
|`perf`|性能优化|提升接口响应速度|
|`test`|测试相关|添加或修正单元测试|
|`build`|构建系统或外部依赖|修改 webpack 配置、package.json 依赖|
|`ci`|CI 配置文件和脚本|修改 .github/workflows, Jenkinsfile|
|`chore`|其他杂项|不修改 src 或 test 文件的变更|
|`revert`|回滚|撤销之前的 commit|