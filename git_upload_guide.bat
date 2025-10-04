@echo off
cls

REM 豆瓣电影数据分析项目 - Git上传指南

:check_git
echo 正在检查Git安装状态...
git --version >nul 2>&1
if %errorlevel% neq 0 (
echo. 
echo 错误: 未找到Git命令行工具。
echo. 
echo 请按照以下步骤安装和配置Git：
echo 1. 访问Git官方下载页面: https://git-scm.com/download/win
echo 2. 下载并安装Git for Windows
echo 3. 在安装过程中，请确保选择"Add Git to the system PATH for all users"选项
echo 4. 安装完成后，重新启动命令提示符或PowerShell

echo. 
echo 安装完成后，可以再次运行此脚本检查Git是否安装成功。
echo. 
echo 按任意键退出...
pause >nul
exit /b 1
) else (
echo Git已成功安装!
echo 版本信息: 
git --version
echo.
)

:git_config
echo 您的Git用户名已预设为: 付梦强
echo 您的Git邮箱已预设为: 984841296@qq.com
echo.
echo 正在配置Git用户名和邮箱...
git config --global user.name "付梦强"
git config --global user.email "984841296@qq.com"
echo Git用户配置已完成。
echo.

:show_guide
echo ========================================================================
echo                        Git上传项目指南
echo ========================================================================
echo.
echo 请按照以下步骤将项目上传到GitHub和Gitee：
echo.
echo 1. 首先，在GitHub和Gitee上创建新的空仓库
echo    - GitHub: https://github.com/new
echo    - Gitee: https://gitee.com/projects/new
echo.
echo 2. 初始化Git仓库（如果尚未初始化）:
echo    git init
echo.
echo 3. 添加所有文件到暂存区:
echo    git add .
echo.
echo 4. 提交更改:
echo    git commit -m "初始提交: 豆瓣电影数据分析项目"
echo.
echo 5. 添加GitHub远程仓库（请替换为您的仓库URL）:
echo    git remote add github https://github.com/您的用户名/仓库名.git
echo.
echo 6. 添加Gitee远程仓库（请替换为您的仓库URL）:
echo    git remote add gitee https://gitee.com/您的用户名/仓库名.git
echo.
echo 7. 推送到GitHub:
echo    git push -u github master
echo.
echo 8. 推送到Gitee:
echo    git push -u gitee master
echo.
echo ========================================================================
echo.
echo 注意事项:
echo - 第一次推送时，系统可能会提示您输入GitHub和Gitee的用户名和密码或令牌
echo - 推荐使用SSH密钥或个人访问令牌进行认证，更加安全和方便
echo - 如果CSV文件过大，可以使用Git LFS (Large File Storage)来处理
echo - 后续更新代码后，可以使用以下命令推送到两个平台:
echo   git add .
echo   git commit -m "更新说明"
echo   git push github master
echo   git push gitee master
echo.
echo 按任意键复制这些命令到剪贴板并退出...
rem 将命令复制到剪贴板
( 
echo git init
 echo git add .
 echo git commit -m "初始提交: 豆瓣电影数据分析项目"
 echo git remote add github https://github.com/您的用户名/仓库名.git
 echo git remote add gitee https://gitee.com/您的用户名/仓库名.git
 echo git push -u github master
 echo git push -u gitee master
) | clip
echo 命令已复制到剪贴板！您可以直接粘贴到命令提示符中使用。
pause >nul