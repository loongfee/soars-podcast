source "https://rubygems.org"

gem "jekyll", "~> 4.2"

group :jekyll_plugins do
  gem "jekyll-timeago", "~> 0.13.1"
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
end

# 移除 github-pages gem，改用 GitHub Actions
# gem "github-pages", group: :jekyll_plugins

ruby "3.3.4"

platforms :mingw, :x64_mingw, :mswin do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]
