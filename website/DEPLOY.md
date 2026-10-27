# 公开站点部署说明

## 目录约定

| 路径 | 作用 | 是否公开 |
|------|------|----------|
| `Publish/` | **唯一公开源**，只有这里的笔记会上线 | 是（且需 `publish: true`） |
| `website/` | Quartz 构建工程 | 配置可公开，无隐私 |
| 其余（`Resources/`、`Archive/`、`账号信息.md` 等） | 私人笔记 | **永不进入构建** |

双重保险：

1. 构建只读 `Publish/`（`-d ../Publish`）
2. `explicit-publish` 插件要求 frontmatter 必须有 `publish: true`

## 本地预览

Quartz 链接是**无 `.html` 后缀**的干净路径（如 `/收藏夹谬论：为什么收藏不等于学会`），  
普通静态服务器会 404，需要用下面任一方式：

**方式 A（推荐，已带干净 URL 支持）：**

```powershell
cd D:\Daily_Data\Obsidian_repo\website
python serve_local.py 8080
# 或：& $env:MIMO_PYTHON serve_local.py 8080
```

**方式 B（Quartz 自带）：**

```powershell
cd D:\Daily_Data\Obsidian_repo\website
npx quartz build --serve -d ../Publish
```

浏览器打开 <http://127.0.0.1:8080>。

## 新增公开笔记

1. 把 `.md` 放进 `Publish/`
2. 在 frontmatter 加上：

```yaml
---
publish: true
---
```

3. 重新 build / 等热更新

**不要**把 `账号信息`、`记账`、密码、token、个人日记放进 `Publish/`。

## Cloudflare Pages 部署

Cloudflare Pages 默认会把 `/page` 映射到 `/page.html`，干净 URL 开箱可用。

1. 把仓库推到 **GitHub Private** 仓库（建议只推 `Publish/` + `website/`，或整库但确认私有）
2. 打开 [Cloudflare Pages](https://pages.cloudflare.com/) → Create a project → Connect to Git
3. 构建配置：

| 项 | 值 |
|----|-----|
| Framework preset | None |
| Root directory | `website` |
| Build command | `npx quartz build -d ../Publish` |
| Build output directory | `public` |
| Node version | 22+（环境变量 `NODE_VERSION=22`） |

4. 部署成功后，把 `website/quartz.config.yaml` 里的 `baseUrl` 改成你的域名
   （例如 `notes.example.com` 或 `你的项目.pages.dev`），再推一次使链接/站点地图正确。

## Vercel（备选）

- Root Directory: `website`
- Build Command: `npx quartz build -d ../Publish`
- Output Directory: `public`

## 上线前检查清单

- [ ] `Publish/` 内无密码 / token / 手机号 / 账号
- [ ] 仓库是 **Private**（若公开，历史里也不能有密钥）
- [ ] `explicit-publish` 保持开启
- [ ] 构建日志里只有 `Publish/` 下的文件（应为 8 个左右，不是几十上百）
