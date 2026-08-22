# 技术文档

这是使用 Rust [mdBook](https://rust-lang.github.io/mdBook/) 构建的技术文档项目。

文档源文件位于 [`src/`](src/)，配置文件为 [`book.toml`](book.toml)。

本地预览：

```bash
mdbook serve
```

推送到 `main` 分支后，GitHub Actions 会自动构建并发布。部署说明见 [DEPLOYMENT.md](DEPLOYMENT.md)。
