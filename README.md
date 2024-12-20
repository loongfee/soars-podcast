# Soars Science Podcast

这是一个关于科学的学术播客，主要关注遥感和地球科学领域的前沿研究。

## 播客简介

- 网站：[https://loongfee.github.io/soars-podcast](https://loongfee.github.io/soars-podcast)
- RSS Feed：[https://loongfee.github.io/soars-podcast/feed.xml](https://loongfee.github.io/soars-podcast/feed.xml)
- 语言：中文
- 更新频率：每月
- 主题：遥感、地球科学、学术研究

## 最新节目

{% assign latest_post = site.posts | sort: 'date' | last %}
- [{{ latest_post.title }}]({{ latest_post.url }}) - {{ latest_post.description }}

## 收听方式

1. **网站直接收听**
   - 访问 [播客网站](https://loongfee.github.io/soars-podcast)
   - 点击具体节目即可在线收听

2. **播客客户端**
   - 添加 RSS Feed：`https://loongfee.github.io/soars-podcast/feed.xml`
   - 支持所有标准播客客户端

## 技术架构

- 网站框架：Jekyll
- 托管平台：GitHub Pages
- 音频存储：GitHub LFS
- 主题：Minima

## 本地开发

1. **环境准备**

```bash
# 安装依赖
gem install bundler
bundle install
```

2. **本地预览**

```bash
bundle exec jekyll serve
```

3. **访问本地站点**
- 打开浏览器访问 `http://localhost:4000/soars-podcast`

## 贡献指南

欢迎提出建议和意见：
1. 提交 Issue
2. 发送邮件到 loongfee@email.com

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 作者

- Soars
- Email: loongfee@email.com

## 更新日志

### 2024-12-18
- 发布第一集：SIF - 太阳诱导叶绿素荧光遥感

## 致谢

感谢所有听众的支持！