# 在线发布

## GitHub Pages

1. 将仓库设为 Private，并推送到 `main` 分支。
2. 确认用于 Actions 的账号有仓库的 Pages 管理权限（通常需要仓库管理员权限）。工作流会在首次运行时自动启用 Pages。
3. 首次推送后，打开 **Actions** 等待 `Deploy mdBook site to Pages` 完成。
4. 访问 `https://<用户名>.github.io/<仓库名>/`。

如果组织策略禁止工作流自动启用 Pages，请先在仓库的 **Settings > Pages** 中将 **Source** 设为 **GitHub Actions**，然后重新运行工作流。

GitHub Pages 对私有仓库是否可用取决于账号套餐。GitHub Free 的个人私有仓库通常不能使用 Pages；GitHub Pro、Team 或 Enterprise 才支持。GitHub Actions 构建本身可以继续使用私有仓库的免费额度。

## 免费私有仓库方案

如果当前账号不能从私有仓库发布 GitHub Pages，可以使用 Cloudflare Pages：连接私有 GitHub 仓库，构建命令填写 `mdbook build`，输出目录填写 `book`。Cloudflare Pages 提供免费的 `pages.dev` 地址；需要在 Cloudflare 控制台配置一次 GitHub 授权和项目。
