---
publish: true
title: 技术上如何实现一个Agent
---

# 什么是Agent
通俗语义上：能够自主运行

组成部分上：
**Agent =  LLM + 记忆 + 工具**

# MCP的出现又是解决什么问题

**解决工具标准化的问题**，也就是工程意义上的重复造轮子问题

MCP 分为两部分：
Mcp Server + MCP Client


MCP Sever: 提供工具的服务 
MCP Client: 使用工具的服务

## 自身的应用Agent 如何连接MCP能力

假如是一个langchain 应用
1. 通过client 与连接MCP Server 获取工具之后
2. 将获取的工具注册到自身Agent上下文中
3. 需要执行工具，调用执行

# SKILL的出现解决什么问题

**解决完成某类事情或者某类目标的规范动作**，类似于工程意义上的SOP

让Agent能够从调用工具 到会做事情

## 自身的应用Agent 如何连接SKILL能力

假如是一个langchain应用

最简单的做法：
1. 本地存放skill目录
2. 大模型加载前先加载skill目录
3. 通过匹配到具体的skill进行执行
4. 最后将skill说明文档 与 用户任务同时告诉给模型

进阶做法：
将所有skill 与用户任务告诉给大模型，让大模型决定使用哪些skill。







