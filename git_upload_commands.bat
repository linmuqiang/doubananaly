====== 豆瓣电影数据分析项目Git上传命令 ======

以下是将项目上传到GitHub和Gitee的完整命令列表，请在Git Bash或命令提示符中逐行执行：

------------
第一步：配置Git用户名和邮箱
------------
git config --global user.name "付梦强"
git config --global user.email "984841296@qq.com"

------------
第二步：添加文件并提交
------------
git add .
git commit -m "初始提交：豆瓣电影数据分析项目"

------------
第三步：推送到GitHub
------------
# 请先在GitHub上创建一个新的空仓库
# 然后将下面的URL替换为您的GitHub仓库地址
#git remote add github https://github.com/username/repo.git
#git push -u github master

------------
第四步：推送到Gitee
------------
# 请先在Gitee上创建一个新的空仓库
# 然后将下面的URL替换为您的Gitee仓库地址
git remote add https://gitee.com/fu-mengqiang/douban-analysis.git
git push -u gitee master

------------
其他有用的命令
------------
# 查看远程仓库配置
git remote -v

# 查看当前状态
git status

# 后续更新代码后，推送新版本到两个平台的命令：
git add .
git commit -m "更新说明"
git push github master
git push gitee master


====== 注意事项 ======
1. 如果您在执行push命令时遇到认证问题，可以尝试使用个人访问令牌（PAT）作为密码
   - GitHub：在GitHub设置中生成个人访问令牌（需要repo权限）
   - Gitee：在Gitee设置中生成私人令牌

2. 如果CSV数据集文件过大（超过100MB），建议使用Git LFS来管理大文件：
   git lfs install
   git lfs track "*.csv"
   git add .gitattributes
   git commit -m "配置Git LFS管理CSV文件"

3. 确保您已经在GitHub和Gitee上创建了空仓库，不要勾选"使用README初始化仓库"选项

4. 如果遇到任何问题，可以尝试删除.git目录重新开始：
   rm -rf .git  # Windows系统可以手动删除.git文件夹

祝您上传成功！