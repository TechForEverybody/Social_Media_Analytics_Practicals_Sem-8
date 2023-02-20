CREATE DATABASE social_media_data;
use social_media_data;

CREATE TABLE twitter_data(
    `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `date` varchar,
    `content` text,
    `username` text,
    `likes` int,
    `views` int,
    `hashtags` text,
    `url` text,
    `likes_views_ratio` float
);


CREATE TABLE himalaya_site_products_data(
    `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `title` text,
    `price` float,
    `description` text,
    `url` text
);


CREATE TABLE himalaya_site_blogs_data(
    `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` text,
    `content` text,
    `url` text,
    `date` varchar
);


CREATE TABLE facebook_data(
    `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `posted_by` text,
    `content` text,
    `likes` float
);


CREATE TABLE youtube_videos_data(
    `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `link` text,
    `title` text,
    `duration` text,
    `views` text,
    `description` text,
    `upload_date` varchar,
    `category` text
);

CREATE TABLE youtube_comments_data(
    `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `video_link` text,
    `author` text,
    `content` text,
    `likes` float
)