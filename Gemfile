source "https://rubygems.org"

gem "jekyll", "~> 4.2"

group :jekyll_plugins do
  gem "jekyll-timeago", "~> 0.13.1"
end

# 使用 GitHub Pages
gem "github-pages", group: :jekyll_plugins

# 添加必要的插件
group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
end

# 指定 Ruby 版本（可选）
ruby "3.0.0"  # 根据你的 Ruby 版本调整

# 平台特定设置
platforms :mingw, :x64_mingw, :mswin do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Windows 特定性能优化
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]