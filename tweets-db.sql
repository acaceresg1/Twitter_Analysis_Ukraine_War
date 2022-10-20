DROP DATABASE IF EXISTS DBS_tweets;
CREATE DATABASE DBS_tweets;
USE DBS_tweets;
DROP TABLE IF EXISTS final_tweets;
CREATE TABLE final_tweets (
  created_at TIMESTAMP,
  id_str TEXT,
  lang TEXT(10),  
  user_followers_count BLOB(100),
  Marketing TEXT(100),
  Activity TEXT(100),
  PRIMARY KEY(created_at, id_str(255))

);
