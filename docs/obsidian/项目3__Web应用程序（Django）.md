# 项目3 · Web应用程序（Django）

**Django第18章 · Django 入门**
- 虚拟环境：`python -m venv venv`
- `pip install django`
- `django-admin startproject 项目名`
- 创建应用：`python manage.py startapp 应用名`
- 定义模型（Model）、迁移数据库、Django Admin
- URL 映射、视图函数、模板（Template）
- 模板继承：`base.html` 统一布局

**用户账户第19章 · 用户账户**
- 用户注册、登录、注销
- `@login_required` 限制未登录访问
- 数据关联到用户（ForeignKey）
- 只允许用户访问自己的数据

**样式部署第20章 · 设置样式并部署**
- `django-bootstrap5` 美化页面
- Platform.sh 部署
- 创建定制错误页面（404、500）
- requirements.txt 管理依赖

**MVTDjango 架构**
**Model**（数据层）→ **View**（业务逻辑）→ **Template**（展示层）

**综合题搭建个人博客网站**
使用 Django 搭建个人博客：

1. 创建 Django 项目 `myblog` 和博客应用 `blog`
2. 定义 `Post` 模型：标题、正文、作者、发布日期、分类
3. 实现文章列表页、详情页、分类筛选页
4. 实现用户注册、登录、注销
5. 登录用户才能发表文章和评论
6. 使用 django-bootstrap5 美化页面
7. 使用 Git 管理代码并推送到 GitHub
