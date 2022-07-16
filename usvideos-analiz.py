import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
videos = pd.read_csv("usvideos.csv",encoding='utf-8')
print(videos.head(n=5))
print("+++++++++++++++++++++++++++++++++")
videos.drop(["thumbnail_link","video_id","trending_date","publish_time","thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"],axis=1, inplace=True)
print(videos.head(0))
print("+++++++++++++++++++++++++++++++++")
print(len(videos.columns))
print(len(videos.index))
print(videos.size)

print("+++++++++++++++++++++++++++++++++")

print(videos["likes"].mean())

print(videos["dislikes"].mean())


print("+++++++++++++++++++++++++++++++++")


print(videos["views"].max())
var1 = videos["views"].max()
print(list(videos[videos.eq(var1).any(1)]['title']))

var1 = videos["views"].min()
print(list(videos[videos.eq(var1).any(1)]['title']))

print(videos.groupby("category_id")["comment_count"].mean())

print(videos.groupby("category_id")["comment_count"].count())

titles = list(videos["title"].str.len())
videos['title_length'] = titles

def findl(rows):
    a=0
    if rows == '[none]':
        return a
    for i in rows:
        if i  == '|':
            a+=1
        else:
            continue
    return a+1
        
a = list(videos['tags'].apply(findl))
videos['tag_count'] = a

videos['l_d'] = videos["likes"] / videos["dislikes"]
videos.sort_values(by = 'l_d')
print(videos.head())
videos.to_csv("videos_out.csv")


