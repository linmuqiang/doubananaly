---
layout: page
homepage: true
---

# Douban Analysis

## Description
Douban Analysis: An open-source project focused on data mining and analysis of Douban, covering movies, books and other domains, providing data crawling, analysis and visualization tools to help deeply understand cultural trends.

## Dataset Introduction

This dataset is collected from Douban Movies. Movie and actor data were collected in early August 2019, and movie review data (users, ratings, comments) were collected in early September 2019, totaling 9.45 million data, including 140,000 movies, 70,000 actors, 630,000 users, 4.16 million movie ratings, and 4.42 million movie reviews, making it the most comprehensive movie dataset publicly available on the Chinese domestic Internet (to my knowledge)!

The dataset consists of 5 files: movies.csv, person.csv, users.csv, comments.csv, ratings.csv. The specific contents of each file will be introduced below.


## License

This dataset is only for the convenience of researchers. **If it involves infringement of the interests of individuals or groups, please contact us and we will take the initiative to withdraw all relevant data, thank you**!

This dataset is for research purposes only. We cannot guarantee the correctness of the data or its applicability in any scenario. Users of this dataset must strictly adhere to the following conditions:

1. Users may not use this dataset for any commercial or income-generating purposes without permission.
2. Users may not re-forward the data without separate permission.
3. Users must declare the source of the data when using the dataset.


Under no circumstances shall we be liable for any loss caused by the use of this data (including but not limited to data loss or data inaccuracy). If you have any other questions or comments, please send an email to: csu.ldw@csu.edu.cn


## Data Format

### Movie Data Format

There are 140,502 movies in total, 139,129 movies before 2019, and 1,373 movies not yet released. It contains 21 fields, some of which are empty. The field descriptions are as follows:

- MOVIE_ID: Movie ID, corresponding to DOUBAN_ID on Douban
- NAME: Movie name
- ALIAS: Alias
- ACTORS: Starring actors
- COVER: Cover image address
- DIRECTORS: Directors
- GENRES: Genres
- OFFICIAL_SITE: Official site
- REGIONS: Countries/regions of production
- LANGUAGES: Languages
- RELEASE_DATE: Release date
- MINS: Duration
- IMDB_ID: IMDbID
- DOUBAN_SCORE: Douban score
- DOUBAN_VOTES: Douban votes
- TAGS: Tags
- STORYLINE: Movie description
- SLUG: Encrypted URL, can be ignored
- YEAR: Year
- ACTOR_IDS: Correspondence between actors and PERSON_ID, multiple actors are separated by "|" symbol, format "Actor A:ID|Actor B:ID";
- DIRECTOR_IDS: Correspondence between directors and PERSON_ID, multiple directors are separated by "|" symbol, format "Director A:ID|Director B:ID";

### Person Data Format

The Person file includes only actors and directors, not Douban user data. There are 72,959 celebrity data in total, including 10 fields. Each PERSON_ID corresponds to a name, and data without PERSON_ID has been filtered out. The field descriptions are as follows:

- PERSON_ID: Celebrity ID
- NAME: Actor name
- SEX: Gender
- NAME_EN: More English names
- NAME_ZH: More Chinese names
- BIRTH: Date of birth
- BIRTHPLACE: Place of birth
- CONSTELLATORY: Constellation
- PROFESSION: Profession
- BIOGRAPHY: Biography, only 15,135 celebrities have biography data.



### User Data Format

users.csv contains unmasked information of Douban users, mainly bound with comments and ratings. A total of 639,125 user data were obtained, including 4 fields. The specific fields are as follows:

- USER_ID: Douban user ID
- USER_NICKNAME: Comment user nickname
- USER_AVATAR: Comment user avatar
- USER_URL: Comment user URL


### Rating Data

Rating data is obtained from comment data. Due to Douban's restriction on the amount of data visible to unlogged-in users, each movie has a maximum of 320 ratings. Finally, 4,169,420 rating data from 600,384 users were obtained, involving 68,471 movies. The rating values are 1-5 points (1-Poor, 2-Fair, 3-Average, 4-Good, 5-Excellent). It contains 5 fields, and the data format is as follows:

- RATING_ID: Rating ID
- USER_ID: Douban user ID
- MOVIE_ID: Movie ID, corresponding to DOUBAN_ID on Douban
- RATING: Rating
- RATING_TIME: Rating time


### Comment Data Format

There are 4,428,475 comments in total, including 6 fields. The field descriptions are as follows:

- COMMENT_ID: Comment ID
- USER_ID: User ID
- MOVIE_ID: Movie ID, corresponding to DOUBAN_ID on Douban
- CONTENT: Comment content
- VOTES: Number of votes for the comment
- COMMENT_TIME: Comment time


## Download Address

Sample data has been uploaded to: [http://moviedata.csuldw.com/dataset/moviedata_small.tar.gz](http://moviedata.csuldw.com/dataset/moviedata_small.tar.gz), each file contains 1000 data. The complete dataset has been stored in the network disk, users who need it can go to download it. The password needs to be obtained from the WeChat official account (changed irregularly). The method to obtain it is as follows:

1. Search for the WeChat official account **[斗码小院]** and click to follow;
2. Reply **[电影数据集]** to get the password.

Data collection is not easy. To initially understand how many people use this data, please do not publicly forward it again, thank you! "It's better to teach someone to fish than to give him a fish."
If you are interested in crawler technology, you can refer to the author's [AntSpider](https://github.com/csuldw/AntSpider) project source code on Github. If the data is useful to you, please follow the official account [斗码小院](http://www.csuldw.com/assets/articleImg/2019/code-main-fun.png) and click Star on the Github below.


## Contributing

1. Fork this repository
2. Create a new Feat_xxx branch
3. Commit your changes
4. Create a new Pull Request

## Contributors

1. [Diwei Liu](http://www.csuldw.com)
2. [Yong Gao](http://www.yogolab.com)
3. [Yina Xu](https://github.com/SnailXu)
