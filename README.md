# 技术文档

这是使用 Rust [mdBook](https://rust-lang.github.io/mdBook/) 构建的技术文档项目。

文档源文件位于 [`src/`](src/)，配置文件为 [`book.toml`](book.toml)。

本地预览：

```bash
mdbook serve
```

推送到 `main` 分支后，GitHub Actions 会自动构建并发布。部署说明见 [DEPLOYMENT.md](DEPLOYMENT.md)。

## 站点更新说明

- 文档更新后，需要提交并推送到 `main` 分支才能触发 GitHub Pages 自动构建。
- 如需立即刷新已发布页面，可在 GitHub 仓库中打开 **Actions**，找到 `Deploy mdBook site to Pages`，然后执行 **Re-run all jobs**。
- 若页面仍未更新，请检查 Pages 设置是否为 **GitHub Actions**，并确认 workflow 运行成功。
