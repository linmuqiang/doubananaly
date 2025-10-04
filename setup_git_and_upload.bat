@echo off
setlocal enabledelayedexpansion

REM 豆瓣电影数据分析项目Git上传脚本
REM 获取当前目录名称
for %%I in (.) do set "PROJECT_NAME=%%~nxI"

REM 检查Git是否已安装
git --version >nul 2>&1
if %errorlevel% neq 0 (
echo 错误: 未找到Git命令行工具。
echo 请先安装Git，然后再运行此脚本。
echo Git下载地址: https://git-scm.com/download/win
echo 安装完成后，请确保将Git添加到系统环境变量中。
pause
exit /b 1
)

REM 配置Git用户名和邮箱
:config_git
echo Git用户名已预设为: 付梦强
echo Git邮箱已预设为: 984841296@qq.com
set GIT_USERNAME=付梦强
set GIT_EMAIL=984841296@qq.com

git config --global user.name "%GIT_USERNAME%"
git config --global user.email "%GIT_EMAIL%"
echo Git用户配置已完成。

REM 创建.gitignore文件
if not exist .gitignore (
echo 创建.gitignore文件...
echo # Python项目忽略规则 >> .gitignore
echo __pycache__/ >> .gitignore
echo *.py[cod] >> .gitignore
echo *$py.class >> .gitignore
echo .Python >> .gitignore
echo build/ >> .gitignore
echo develop-eggs/ >> .gitignore
echo dist/ >> .gitignore
echo downloads/ >> .gitignore
echo eggs/ >> .gitignore
echo .eggs/ >> .gitignore
echo lib/ >> .gitignore
echo lib64/ >> .gitignore
echo parts/ >> .gitignore
echo sdist/ >> .gitignore
echo var/ >> .gitignore
echo *.egg-info/ >> .gitignore
echo .installed.cfg >> .gitignore
echo *.egg >> .gitignore
echo 
REM 日志文件 >> .gitignore
echo *.log >> .gitignore
echo .log >> .gitignore
echo 
REM 临时文件 >> .gitignore
echo *.tmp >> .gitignore
echo *.temp >> .gitignore
echo 
REM IDE配置文件 >> .gitignore
echo .idea/ >> .gitignore
echo .vscode/ >> .gitignore
echo *.suo >> .gitignore
echo *.ntvs*
echo *.njsproj >> .gitignore
echo *.sln >> .gitignore
echo *.sw? >> .gitignore
echo 
REM 数据集文件过大，不提交到仓库 >> .gitignore
echo *.csv >> .gitignore
echo 
REM 可视化结果文件 >> .gitignore
echo visualizations/*.png >> .gitignore
echo visualizations/top_comments.csv >> .gitignore
echo 
REM 批处理文件和说明文件保留 >> .gitignore
) else (
echo .gitignore文件已存在。
)

REM 初始化Git仓库
if not exist .git (
echo 初始化Git仓库...
git init
) else (
echo Git仓库已初始化。
)

REM 添加所有文件到暂存区
echo 添加文件到Git暂存区...
git add .
git commit -m "初始提交: 豆瓣电影数据分析项目"

REM 配置GitHub远程仓库
:setup_github
echo 请输入您的GitHub仓库URL (例如: https://github.com/username/repo.git):
set /p GITHUB_URL=
if "%GITHUB_URL%"=="" (
echo 跳过GitHub仓库配置。
) else (
git remote add github %GITHUB_URL%
echo 推送代码到GitHub...
git push -u github master
if %errorlevel% neq 0 (
echo 错误: 推送到GitHub失败。请检查仓库URL和权限设置。
echo 您可以稍后手动执行 'git push -u github master' 命令。
)
)

REM 配置Gitee远程仓库
:setup_gitee
echo 请输入您的Gitee仓库URL (例如: https://gitee.com/username/repo.git):
set /p GITEE_URL=
if "%GITEE_URL%"=="" (
echo 跳过Gitee仓库配置。
) else (
git remote add gitee %GITEE_URL%
echo 推送代码到Gitee...
git push -u gitee master
if %errorlevel% neq 0 (
echo 错误: 推送到Gitee失败。请检查仓库URL和权限设置。
echo 您可以稍后手动执行 'git push -u gitee master' 命令。
)
)

echo.
echo 项目Git配置和上传指南已完成！
echo.
echo 注意事项:
echo 1. 如果CSV文件过大，可能需要使用Git Large File Storage (LFS)来处理
   安装命令: git lfs install
echo 2. 您可以使用以下命令查看远程仓库配置: git remote -v
echo 3. 后续更新代码后，可以使用以下命令推送到两个平台:
echo    git add .
echo    git commit -m "更新说明"
echo    git push github master
echo    git push gitee master

echo 按任意键退出...
pause >nul