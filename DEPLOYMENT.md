# 在线发布

## GitHub Pages

1. 将仓库设为 Private，并推送到 `main` 分支。
2. 确认用于 Actions 的账号有仓库的 Pages 管理权限（通常需要仓库管理员权限）。工作流会在首次运行时自动启用 Pages。
3. 首次推送后，打开 **Actions** 等待 `Deploy mdBook site to Pages` 完成。
4. 访问 `https://<用户名>.github.io/<仓库名>/`。

如果组织策略禁止工作流自动启用 Pages，请先在仓库的 **Settings > Pages** 中将 **Source** 设为 **GitHub Actions**，然后重新运行工作流。

GitHub Pages 对私有仓库是否可用取决于账号套餐。GitHub Free 的个人私有仓库通常不能使用 Pages；GitHub Pro、Team 或 Enterprise 才支持。GitHub Actions 构建本身不依赖仓库是否公开，关键在于 Pages 与 Actions 的授权与运行状态。

## 刷新已发布页面

如果文档已修改但站点没有立刻更新，可执行以下步骤：

1. 提交并推送修改到 `main` 分支。
2. 打开 GitHub 仓库的 **Actions** 页面。
3. 选择 `Deploy mdBook site to Pages`。
4. 点击 **Re-run all jobs** 重新触发构建和部署。
5. 等待构建完成后刷新页面确认内容更新。

## 免费私有仓库方案

如果当前账号不能从私有仓库发布 GitHub Pages，可以使用 Cloudflare Pages：连接私有 GitHub 仓库，构建命令填写 `mdbook build`，输出目录填写 `book`。Cloudflare Pages 也支持私有仓库部署，但需要额外配置构建和绑定域名。
