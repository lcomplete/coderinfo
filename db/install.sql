-- mysql 8.0

CREATE DATABASE `cinfo`; /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */

create table capture_article
(
    id          int auto_increment
        primary key,
    short_title varchar(256)  not null,
    summary     longtext      not null,
    brief       mediumtext    not null,
    raw_url     varchar(1024) not null,
    site_id     int           not null,
    create_date datetime      not null,
    update_date datetime      not null,
    isshow      bit           not null,
    site_name   varchar(45)   not null
);

create index idx_capture_article_created
    on capture_article (create_date desc);

create table capture_site
(
    id              int auto_increment
        primary key,
    site_url        varchar(128) not null,
    site_name       varchar(45)  not null,
    article_limit   int          not null,
    interval_minute int          not null,
    isenabled       bit          not null,
    isdeleted       bit          not null,
    capture_class   varchar(45)  not null comment 'python抓取器class',
    capture_date    datetime     not null,
    failed_date     datetime     not null,
    sequence        int          not null
)
    comment '抓取站点的配置';

create table fun_pic
(
    id          int auto_increment
        primary key,
    oo          int           not null,
    xx          int           not null,
    pic_urls    varchar(1024) not null,
    pic_type    varchar(20)   not null,
    create_date datetime      not null
);

create index idx_fun_pic_type
    on fun_pic (pic_type);

