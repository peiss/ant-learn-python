use test;

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) DEFAULT '',
  `sex` varchar(10) DEFAULT '',
  `age` int(11) DEFAULT '0',
  `email` varchar(128) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='user table';


INSERT INTO `user`
VALUES (1,'xiaoming','man',21,'xiaoming@qq.com'),
(2,'xiaohong','women',22,'xiaohong@qq.com');
