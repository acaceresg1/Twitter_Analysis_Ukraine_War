# Twitter_Analysis_Ukraine_War

## Code & Resources Used:

** Python:** Version 3.8
** Packages:** PySpark (), pandas, matplotlib, datetime, GraphFrame

## Executive Summary:

Term II group project for Modern Data Architectures for Big Data II class at IE university - part of the Masters in Business Analytics and Big Data program.

The first goal is to build a big data pipeline using all the technologies reviewed during both Modern Data Architectures for Big Data I & II subjects.
The architecture goes from the ingestion part using NiFi, the storage using HDFS, the processing part using Hadoop and some of its tools available, and finally the serving using MariaDB.

The second project goal is to analyze, using the architecture created, a bulk of tweets regarding the Ukraine War as a social media could be the perfect tool for spreading (mis)information.
Russia has a powerful propaganda machine so it is important to uncover false or illegal information to prevent fake information and to ban/block extreme users.

For the bulk analysis was performed an initial EDA, a graphing algorithm, and machine learning algorithms to predict verified accounts.
The graphing part has been done with users as vertices and mentions as edges to create the graph, which facilitates the checking of the in-out degree for the main users. Finally With a PageRank algorithm was possible to find the tweet's importance.

## Data Architecture:

The main goal of this lab is to build and establish a data architecture to ingest tweets and play with all the tools studied during the course.

For this project, Lambda Architecture was used as it covers all the necessities. The Lambda architectures contain both a batch and a streaming layer, so let's explain in detail each: 

The batch layer uses Nifi to perform the ingestion, and Hadoop HDFS to promote from the raw to the standard layer, storing the Ukraine-War training set.
To ingest the data was used Apache NiFi to pull tweets from the Twitter API, using popular hashtags related to the war. During 7 days, more than 6 hours per day, Nifi was able to ingest 100,000 tweets pertaining to the war.
Finally, Apache Spark is used to perform the EDA, and with Apache GraphX and Apache ML the graph and the machine learning pipeline to get insights.
It is important to mention that during the storage stage of this batch layer, a txt file with all the tweets was created and saved, serving as a database for the further streaming layer.

The streaming layer was in the end a simulator, as the course goal tried to be familiar with some of the Big Data landscape tools, using a producer.py that ingests tweets directly from the txt file mentioned previously into Kafka. 
A Spark session was used as the processing engine to build some main queries to the tweet income flow in real-time. Then before the serving stage, an external static CSV was joined with our data in real-time
creating a new table with specific information, which was served using MariaDB to the final user. Using MariaDB the user can query and obtain real-time answers to its necessity.

![imagen](https://user-images.githubusercontent.com/115701510/196969868-efd610a6-571a-45b7-b038-a624fe5c09a1.png)

## EDA + Graphing  + Machine Learning:

#### EDA:

After an initial exploratory data analysis, combination of Graph and Machine Learning approaches was used to gain deeper insights.
First look at the main features, with special interest in the verified accounts and the followers count.
Important metrics such as the followers count change for verified and unverified users. The distribution is an important example.


#### Graphing:

The vertices were Users and edges were mentions (Other twitter users mentioned in the tweet). There were used three graphing tools, PageRank, In/Out Degree and Strongly Connected Components.

#### Machine Learning:

The goal was to predict account verification based on tweet and profile information
The feature selection begins by creating new features: identifying specific hashtags in the tweet. Then, follows with the normalization of nested features
After identifying numerical and categorical variables, the next step was to proceed with the known String Indexer, OneHotEncoder and Vector Assambler.

And only then do we create the Pipeline for the classifiers:
- Logistic Regession
- Decision Tree Classifier
- Random Forest Classifier
- GBT Classifier
- Naive Bayes
-  Linear SVC

Given the desproportion of the two categories Verified and Not Verified, the dataset was balanced so that 50% of the data corresponds to each possibility.
After leaving 20% of the data for testing, was reached the conclussion that Naive Bayes is the best algorithm for this prediction, just a little above the others. 

## Streaming Pipeline:

The simulator uses a text file as source, created during the batch step. This file contains more than 120k tweets.
To create the txt file, was modified the schema using spark. The structure was unstucked converting it to a flat structure.
The ingestion was made using message delivery semantic by a producer.py. It sends tweets to a Kafka topic call "tweets". Kafka is an event streaming platform storing messages sent by the producer
To check that messages are incoming it is useful to call the topic with the consumer to see in real time how are being saved.

![imagen](https://user-images.githubusercontent.com/115701510/196972907-98b79f18-7522-4dd1-94d1-28a6f4ceebb5.png)

Using Spark Streaming was easy to develop streaming queries and get batches of data in real-time.
Finally, using the tweets stored in Kafka and the external CSV (marketing information provided by the final user (Marketing department)), we are joining marketing information with tweets in real-time. 
This marketing information is a CSV file storage that divides the users between several classes depending on their use of Twitter.
This has a clear target and is to find which strategy should the company use to reach each of these classes and also their followers.

Launching the SQL file using the console, it was possible to create a SQL table in MariaDB.
Spark can join the marketing table with the tweets in streaming so once Spark is joining and sending to MariaDB, the final user is ready to make some queries in SQL!


## Insights from the Batch processing:

**News and Media remains an important source of information:** 4 out of top 5 mentions are news&media, from Ukraine

**Bots and Fake News sources are prevalent and easy to find:** Bots tend to generate an inhuman amount of mentions and tweets

**Globalization: everyone is impacted and invested in the outcome:** Top mentions coming from USA, UK, France, India

**Democracy on Twitter:** Large amounts of banned accounts drive the question of censorship vs fact checking





