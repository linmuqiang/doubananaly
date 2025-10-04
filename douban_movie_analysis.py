import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

class DoubanMovieAnalysis:
    def __init__(self, data_dir='.'):
        self.data_dir = data_dir
        self.movies = None
        self.person = None
        self.users = None
        self.comments = None
        self.ratings = None
        self.output_dir = os.path.join(self.data_dir, 'visualizations')
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def load_data(self):
        """加载所有CSV文件数据"""
        print("正在加载数据...")
        
        try:
            # 使用chunksize来避免大文件加载内存问题
            chunk_size = 100000
            
            # 加载movies.csv
            print("加载电影数据...")
            movie_chunks = []
            for chunk in pd.read_csv(os.path.join(self.data_dir, 'movies.csv'), chunksize=chunk_size, low_memory=False):
                movie_chunks.append(chunk)
            self.movies = pd.concat(movie_chunks)
            print(f"电影数据加载完成: {len(self.movies)}部电影")
            
            # 加载person.csv
            print("加载人物数据...")
            person_chunks = []
            for chunk in pd.read_csv(os.path.join(self.data_dir, 'person.csv'), chunksize=chunk_size, low_memory=False):
                person_chunks.append(chunk)
            self.person = pd.concat(person_chunks)
            print(f"人物数据加载完成: {len(self.person)}个人物")
            
            # 加载users.csv
            print("加载用户数据...")
            user_chunks = []
            for chunk in pd.read_csv(os.path.join(self.data_dir, 'users.csv'), chunksize=chunk_size, low_memory=False):
                user_chunks.append(chunk)
            self.users = pd.concat(user_chunks)
            print(f"用户数据加载完成: {len(self.users)}个用户")
            
            # 加载ratings.csv
            print("加载评分数据...")
            rating_chunks = []
            for chunk in pd.read_csv(os.path.join(self.data_dir, 'ratings.csv'), chunksize=chunk_size, low_memory=False):
                rating_chunks.append(chunk)
            self.ratings = pd.concat(rating_chunks)
            print(f"评分数据加载完成: {len(self.ratings)}条评分")
            
            # 加载comments.csv，尝试使用不同的编码
            print("加载评论数据...")
            comment_chunks = []
            encodings = ['utf-8-sig', 'gbk', 'latin1']
            
            for encoding in encodings:
                try:
                    for chunk in pd.read_csv(os.path.join(self.data_dir, 'comments.csv'), 
                                            chunksize=chunk_size, 
                                            low_memory=False, 
                                            encoding=encoding):
                        comment_chunks.append(chunk)
                    self.comments = pd.concat(comment_chunks)
                    print(f"评论数据加载完成: {len(self.comments)}条评论 (使用编码: {encoding})")
                    break  # 成功加载后跳出循环
                except UnicodeDecodeError:
                    print(f"尝试使用{encoding}编码失败，继续尝试下一个编码...")
                    comment_chunks = []
                    continue
            
            if not comment_chunks:
                print("所有编码都尝试失败，无法加载评论数据")
        
        except Exception as e:
            print(f"加载数据时出错: {e}")
    
    def preprocess_data(self):
        """数据预处理"""
        print("正在进行数据预处理...")
        
        # 预处理电影数据
        if self.movies is not None:
            # 转换评分和投票数为数值类型
            self.movies['DOUBAN_SCORE'] = pd.to_numeric(self.movies['DOUBAN_SCORE'], errors='coerce')
            self.movies['DOUBAN_VOTES'] = pd.to_numeric(self.movies['DOUBAN_VOTES'], errors='coerce')
            
            # 转换上映年份为数值类型
            self.movies['YEAR'] = pd.to_numeric(self.movies['YEAR'], errors='coerce')
            
            # 过滤掉无效的年份数据
            self.movies = self.movies[(self.movies['YEAR'] >= 1900) & (self.movies['YEAR'] <= datetime.now().year)]
        
        # 预处理评分数据
        if self.ratings is not None:
            # 转换评分为数值类型
            self.ratings['RATING'] = pd.to_numeric(self.ratings['RATING'], errors='coerce')
            
            # 转换评分时间为日期类型
            try:
                self.ratings['RATING_TIME'] = pd.to_datetime(self.ratings['RATING_TIME'], errors='coerce')
            except:
                pass
    
    def analyze_movie_ratings(self):
        """分析电影评分分布"""
        if self.movies is None:
            print("电影数据未加载")
            return
        
        print("分析电影评分分布...")
        
        # 过滤掉没有评分的电影
        rated_movies = self.movies.dropna(subset=['DOUBAN_SCORE'])
        
        plt.figure(figsize=(10, 6))
        sns.histplot(rated_movies['DOUBAN_SCORE'], bins=20, kde=True)
        plt.title('豆瓣电影评分分布')
        plt.xlabel('评分')
        plt.ylabel('电影数量')
        plt.grid(True, alpha=0.3)
        plt.savefig(os.path.join(self.output_dir, 'movie_rating_distribution.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"电影评分分布图表已保存至: {os.path.join(self.output_dir, 'movie_rating_distribution.png')}")
    
    def analyze_movie_genres(self):
        """分析电影类型分布"""
        if self.movies is None:
            print("电影数据未加载")
            return
        
        print("分析电影类型分布...")
        
        # 统计类型分布
        genre_counts = {}
        
        for genres in self.movies['GENRES'].dropna():
            if isinstance(genres, str):
                for genre in genres.split('/'):
                    genre = genre.strip()
                    if genre:
                        genre_counts[genre] = genre_counts.get(genre, 0) + 1
        
        # 排序并取前20个类型
        sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)[:20]
        genres, counts = zip(*sorted_genres)
        
        plt.figure(figsize=(12, 8))
        sns.barplot(x=list(counts), y=list(genres))
        plt.title('电影类型分布前20名')
        plt.xlabel('电影数量')
        plt.ylabel('类型')
        plt.grid(True, alpha=0.3, axis='x')
        plt.savefig(os.path.join(self.output_dir, 'movie_genre_distribution.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"电影类型分布图表已保存至: {os.path.join(self.output_dir, 'movie_genre_distribution.png')}")
    
    def analyze_movies_over_years(self):
        """分析电影数量随年份变化趋势"""
        if self.movies is None:
            print("电影数据未加载")
            return
        
        print("分析电影数量随年份变化趋势...")
        
        # 统计每年的电影数量
        yearly_counts = self.movies['YEAR'].value_counts().sort_index()
        
        # 创建一个新的绘图窗口，设置图形大小为宽12英寸，高6英寸，用于绘制电影数量随年份变化的折线图
        plt.figure(figsize=(12, 6))
        yearly_counts.plot(kind='line', marker='o')
        plt.title('电影数量随年份变化趋势')
        plt.xlabel('年份')
        plt.ylabel('电影数量')
        # 显示网格线，增强图表可读性，alpha=0.3 设置网格线透明度为 0.3，使其半透明
        plt.grid(True, alpha=0.3)
        plt.savefig(os.path.join(self.output_dir, 'movies_over_years.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"电影数量随年份变化图表已保存至: {os.path.join(self.output_dir, 'movies_over_years.png')}")
    
    def analyze_ratings_distribution(self):
        """分析用户评分分布"""
        if self.ratings is None:
            print("评分数据未加载")
            return
        
        print("分析用户评分分布...")
        
        plt.figure(figsize=(10, 6))
        sns.countplot(x='RATING', data=self.ratings)
        plt.title('用户评分分布')
        plt.xlabel('评分')
        plt.ylabel('评分数量')
        plt.grid(True, alpha=0.3, axis='y')
        plt.savefig(os.path.join(self.output_dir, 'user_rating_distribution.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"用户评分分布图表已保存至: {os.path.join(self.output_dir, 'user_rating_distribution.png')}")
    
    def analyze_top_rated_movies(self):
        """分析评分最高的电影"""
        if self.movies is None:
            print("电影数据未加载")
            return
        
        print("分析评分最高的电影...")
        
        # 过滤掉没有评分和投票数太少的电影
        top_movies = self.movies.dropna(subset=['DOUBAN_SCORE', 'DOUBAN_VOTES'])
        top_movies = top_movies[top_movies['DOUBAN_VOTES'] > 1000]  # 只考虑投票数超过1000的电影
        top_movies = top_movies.sort_values('DOUBAN_SCORE', ascending=False).head(20)
        
        plt.figure(figsize=(12, 10))
        sns.barplot(x='DOUBAN_SCORE', y='NAME', data=top_movies)
        plt.title('评分最高的20部电影 (投票数>1000)')
        plt.xlabel('评分')
        plt.ylabel('电影名称')
        plt.grid(True, alpha=0.3, axis='x')
        plt.savefig(os.path.join(self.output_dir, 'top_rated_movies.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"评分最高的电影图表已保存至: {os.path.join(self.output_dir, 'top_rated_movies.png')}")
    
    def analyze_comments_votes(self):
        """分析评论获赞情况"""
        if self.comments is None:
            print("评论数据未加载")
            return
        
        print("分析评论获赞情况...")
        
        # 转换评论赞同数为数值类型
        self.comments['VOTES'] = pd.to_numeric(self.comments['VOTES'], errors='coerce')
        
        # 过滤掉无效数据
        valid_comments = self.comments.dropna(subset=['VOTES'])
        valid_comments = valid_comments[valid_comments['VOTES'] > 0]
        
        # 取获赞最多的20条评论
        top_comments = valid_comments.nlargest(20, 'VOTES')
        
        # 保存这些评论到CSV文件
        # 使用正确的列名 USER_MD5 而不是 USER_ID
        top_comments[['MOVIE_ID', 'USER_MD5', 'VOTES', 'CONTENT']].to_csv(
            os.path.join(self.output_dir, 'top_comments.csv'), index=False, encoding='utf-8-sig')
        
        print(f"获赞最多的评论已保存至: {os.path.join(self.output_dir, 'top_comments.csv')}")
    
    def analyze_movie_countries(self):
        """分析电影产地分布"""
        if self.movies is None:
            print("电影数据未加载")
            return
        
        print("分析电影产地分布...")
        
        # 统计产地分布
        country_counts = {}
        
        for countries in self.movies['REGIONS'].dropna():
            if isinstance(countries, str):
                for country in countries.split('/'):
                    country = country.strip()
                    if country:
                        country_counts[country] = country_counts.get(country, 0) + 1
        
        # 排序并取前15个产地
        sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:15]
        countries, counts = zip(*sorted_countries)
        
        plt.figure(figsize=(12, 6))
        plt.pie(counts, labels=countries, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # 保证饼图是正圆形
        plt.title('电影产地分布前15名')
        plt.savefig(os.path.join(self.output_dir, 'movie_countries_distribution.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"电影产地分布图表已保存至: {os.path.join(self.output_dir, 'movie_countries_distribution.png')}")
    
    def run_analysis(self):
        """运行完整的数据分析"""
        self.load_data()
        self.preprocess_data()
        
        # 执行各种分析
        self.analyze_movie_ratings()
        self.analyze_movie_genres()
        self.analyze_movies_over_years()
        self.analyze_ratings_distribution()
        self.analyze_top_rated_movies()
        self.analyze_comments_votes()
        self.analyze_movie_countries()
        
        print("所有分析已完成！可视化结果保存在visualizations文件夹中。")

if __name__ == '__main__':
    analyzer = DoubanMovieAnalysis()
    analyzer.run_analysis()