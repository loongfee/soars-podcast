---
layout: home
title: Soars Science
---

欢迎来到 Soars Science，这里是一个关于科学的学术播客。

<a href="https://github.com/loongfee/soars-podcast" target="_blank">View on GitHub</a>

## 最新节目

{% assign sorted_posts = site.posts | sort: 'date' | reverse %}
{% for post in sorted_posts %}
* [{{ post.title }}]({{ post.url | prepend: site.baseurl }}) - {{ post.date | date: "%Y-%m-%d" }}
{% endfor %}