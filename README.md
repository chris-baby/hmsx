海马生鲜电商项目实战

use hmsc_db;

drop table if exists `user`;
create table `user` (
	`uid` bigint(20) not null auto_increment comment '用户id',
	`nickname` varchar(100) not null default '' comment '用户昵称',
	`mobile` varchar(20) not null default '' comment '手机号码',
	`email` varchar(100) not null default '' comment '用户邮箱',
	`sex` tinyint(1) not null default '0' comment '1:男 2:女 0:没有填写',
	`avatar` varchar(64) not null default '' comment '头像',
	`login_name` varchar(20) not null default '' comment '登录用户名',
	`login_pwd` varchar(32) not null default '' comment '登录密码',
	`login_salt` varchar(32) not null default '' comment '登录密码的随机密钥',
	`status` tinyint(1) not null default '1' comment '1:有效 0:无效',
	`updated_time` timestamp not null default current_timestamp comment '最后一次更新时间',
	`created_time` timestamp not null default current_timestamp comment '创建时间',
	primary key (`uid`),
	unique key `login_name` (`login_name`)
)ENGINE=InnoDB default charset=utf8 comment='用户表（管理员）';


insert into `user` (`uid`,`nickname`,`mobile`,`email`,`sex`,`avatar`,`login_name`,`login_pwd`,`login_salt`,`status`,`updated_time`,`created_time`) values (1,'BruceNick','13933746521','Bruce@aliyun.com',1,'','Bruce','816440c40b7a9d55ff9eb7b20760862c','cF3JfH5FJfQ8B2Ba',1,'2020-04-23 11:30:30','2020-04-23 11:10:30');