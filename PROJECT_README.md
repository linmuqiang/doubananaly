# 豆瓣电影数据分析项目

## 项目概述
这是基于豆瓣电影数据集开发的可视化分析工具，通过Python脚本处理和分析电影、用户、评分和评论数据，生成多种可视化图表，并提供交互式HTML报告。

## 数据来源
本项目使用的数据集为豆瓣电影数据集，包含14万部电影、7万演员、63万用户、416万条评分和442万条评论数据。关于数据集的详细说明，请参阅根目录下的`README.md`文件。

## 项目文件结构
```
├── douban_movie_analysis.py  # 核心分析脚本
├── run_analysis.bat          # 一键运行分析批处理
├── open_report.bat           # 一键打开报告批处理
├── setup_git_and_upload.bat  # Git环境配置和上传脚本
├── PROJECT_README.md         # 项目说明文档
├── 代码思维导图.txt           # 代码结构思维导图
├── low_memory参数说明.txt    # pandas参数说明文档
└── visualizations/           # 可视化结果目录
    ├── index.html            # 交互式分析报告
    ├── movie_countries_distribution.png  # 电影产地分布
    ├── movie_genre_distribution.png      # 电影类型分布
    ├── movie_rating_distribution.png     # 电影评分分布
    ├── movies_over_years.png             # 电影年份趋势
    ├── top_rated_movies.png              # 高分电影排行
    ├── top_comments.csv                  # 热门评论数据
    └── user_rating_distribution.png      # 用户评分分布
```

## 环境与依赖
- Python 3.6+ 环境
- 所需Python库：
  - pandas
  - matplotlib
  - seaborn
  - numpy

## 快速开始
### 方法一：使用批处理文件
1. 确保已安装Python环境
2. 双击运行 `run_analysis.bat` - 此脚本会自动检查环境并运行分析
3. 分析完成后，双击运行 `open_report.bat` - 打开生成的可视化报告

### 方法二：手动运行
```bash
# 安装所需依赖
pip install pandas matplotlib seaborn numpy

# 运行分析脚本
python douban_movie_analysis.py

# 打开HTML报告查看结果
start visualizations\index.html
```

## 主要功能
### 1. 数据加载与预处理
- 支持大文件分块读取，优化内存使用
- 自动尝试多种编码格式，解决不同CSV文件的编码问题
- 数据清洗和类型转换，为后续分析做准备

### 2. 可视化分析结果
项目生成以下7种可视化分析结果：
1. **电影评分分布** - 展示所有电影评分的分布情况
2. **电影类型分布** - 统计并展示Top 20电影类型的分布
3. **电影年份趋势** - 展示电影数量随年份变化的趋势
4. **用户评分分布** - 分析用户的评分行为特征
5. **高分电影排行** - 展示评分最高的Top 20部电影
6. **电影产地分布** - 统计并展示Top 15电影产地的分布
7. **热门评论分析** - 提取获赞最多的评论并保存为CSV文件

### 3. 交互式报告
生成的HTML报告使用Bootstrap框架设计，具有响应式布局，支持在不同设备上良好显示所有分析结果。

## 将项目上传至GitHub和Gitee
项目包含 `setup_git_and_upload.bat` 脚本，帮助你将项目上传到代码托管平台：
1. 确保已安装Git并添加到系统环境变量
2. 双击运行 `setup_git_and_upload.bat`
3. 按照提示输入Git用户名、邮箱以及GitHub和Gitee的仓库URL
4. 脚本会自动初始化Git仓库、创建.gitignore文件并推送到指定平台

## 注意事项
1. 脚本会自动忽略CSV数据文件（过大），只提交分析代码和结果文件
2. 分析过程可能需要一定时间，取决于计算机性能和数据大小
3. 如遇到问题，请检查Python环境和依赖库是否正确安装

## 扩展建议
1. 添加更多分析维度，如演员合作关系网络分析
2. 实现评论情感分析，深入挖掘用户反馈
3. 开发Web界面，支持实时数据筛选和交互式分析

---

希望本项目能帮助您更好地理解和分析豆瓣电影数据集！如有任何问题或建议，欢迎提出。