# Obsidian 公开站点

这个仓库只包含两类内容：

- `Publish/`：允许公开发布的笔记来源
- `website/`：Quartz 网站构建工程

## 构建

```powershell
cd website
npm ci
npx quartz build -d ../Publish
```

输出目录为 `website/public`。

## 隐私边界

只有 `Publish/` 中且 frontmatter 为 `publish: true` 的笔记允许进入站点。
其他 Obsidian 私人笔记不应复制进这个仓库。
