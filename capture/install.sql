CREATE SCHEMA `cinfo` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;

CREATE  TABLE `cinfo`.`capture_site` (
  `id` INT NOT NULL ,
  `site_url` VARCHAR(128) NOT NULL ,
  `article_limit` INT NOT NULL ,
  `interval_minute` INT NOT NULL ,
  `isenabled` BIT NOT NULL ,
  `isdeleted` BIT NOT NULL ,
  `capture_class` VARCHAR(45) NOT NULL COMMENT 'python抓取器class' ,
  PRIMARY KEY (`id`) )
COMMENT = '抓取站点的配置';

ALTER TABLE `cinfo`.`capture_site` CHANGE COLUMN `id` `id` INT(11) NOT NULL AUTO_INCREMENT  ;

CREATE  TABLE `cinfo`.`capture_article` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `short_title` VARCHAR(128) NOT NULL ,
  `summary` TEXT NOT NULL ,
  `raw_url` VARCHAR(256) NOT NULL ,
  `site_id` INT NOT NULL ,
  `create_date` DATETIME NOT NULL ,
  `update_date` DATETIME NOT NULL ,
  PRIMARY KEY (`id`) );

ALTER TABLE `cinfo`.`capture_site` ADD COLUMN `capture_date` DATETIME NOT NULL  AFTER `capture_class` , ADD COLUMN `failed_date` DATETIME NOT NULL  AFTER `capture_date` ;

update capture_site set capture_date='2000-1-1',failed_date='2000-1-1' where id=1;

ALTER TABLE `cinfo`.`capture_article` ADD COLUMN `isshow` BIT NOT NULL  AFTER `update_date` ;

ALTER TABLE `cinfo`.`capture_article` ADD COLUMN `brief` TEXT NOT NULL  AFTER `summary` ;

ALTER TABLE `cinfo`.`capture_site` ADD COLUMN `site_name` VARCHAR(45) NOT NULL  AFTER `site_url` ;

update capture_site set site_name='开源中国' where id=1;

insert into capture_site values(2,'http://news.dbanotes.net/','Startup News',
20,30,1,0,'','2000-1-1','2000-1-1');


#########################
