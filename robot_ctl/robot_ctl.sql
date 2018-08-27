-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2018-08-27 20:11:52
-- 服务器版本： 10.1.34-MariaDB
-- PHP 版本： 7.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `robot_ctl`
--

-- --------------------------------------------------------

--
-- 表的结构 `qq_list`
--

CREATE TABLE `qq_list` (
  `id` int(11) UNSIGNED NOT NULL,
  `qq_no` varchar(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `qq_list`
--

INSERT INTO `qq_list` (`id`, `qq_no`, `password`, `create_time`, `update_time`) VALUES
(1, '233', 'root1234', '2018-08-25 00:00:00', '2018-08-25 00:00:00'),
(2, '666', 'root1234', '2018-08-25 00:00:00', '2018-08-25 00:00:00'),
(3, '433', 'root3344', '2018-08-25 03:09:41', '2018-08-25 03:09:41'),
(4, '333', 'root1244', '2018-08-25 03:20:25', '2018-08-25 03:20:25'),
(5, '453', 'root1234', '2018-08-25 03:48:25', '2018-08-25 03:48:25'),
(7, '553', 'root1234', '2018-08-25 03:50:31', '2018-08-25 03:50:31'),
(8, '554', 'root1234', '2018-08-25 03:51:17', '2018-08-25 03:51:17'),
(9, '2331', 'root1234', '2018-08-25 00:00:00', '2018-08-25 00:00:00'),
(10, '6661', 'root1234', '2018-08-25 00:00:00', '2018-08-25 00:00:00'),
(11, '4331', 'root3344', '2018-08-25 03:09:41', '2018-08-25 03:09:41'),
(12, '3331', 'root1244', '2018-08-25 03:20:25', '2018-08-25 03:20:25'),
(13, '4531', 'root1234', '2018-08-25 03:48:25', '2018-08-25 03:48:25'),
(14, '5531', 'root1234', '2018-08-25 03:50:31', '2018-08-25 03:50:31'),
(15, '5541', 'root1234', '2018-08-25 03:51:17', '2018-08-25 03:51:17'),
(16, '2332', 'root1234', '2018-08-25 00:00:00', '2018-08-25 00:00:00'),
(17, '6662', 'root1234', '2018-08-25 00:00:00', '2018-08-25 00:00:00'),
(18, '4332', 'root3344', '2018-08-25 03:09:41', '2018-08-25 03:09:41'),
(19, '3332', 'root1244', '2018-08-25 03:20:25', '2018-08-25 03:20:25'),
(20, '4532', 'root1234', '2018-08-25 03:48:25', '2018-08-25 03:48:25'),
(21, '5532', 'root1234', '2018-08-25 03:50:31', '2018-08-25 03:50:31'),
(22, '5542', 'root1234', '2018-08-25 03:51:17', '2018-08-25 03:51:17'),
(23, '2333', 'root1234', '2018-08-25 00:00:00', '2018-08-25 00:00:00'),
(24, '6663', 'root1234', '2018-08-25 00:00:00', '2018-08-25 00:00:00'),
(25, '4333', 'root3344', '2018-08-25 03:09:41', '2018-08-25 03:09:41'),
(26, '3333', 'root1244', '2018-08-25 03:20:25', '2018-08-25 03:20:25'),
(27, '4533', 'root1234', '2018-08-25 03:48:25', '2018-08-25 03:48:25'),
(28, '5533', 'root1234', '2018-08-25 03:50:31', '2018-08-25 03:50:31'),
(29, '5543', 'root1234', '2018-08-25 03:51:17', '2018-08-25 03:51:17'),
(30, '2334', 'root1234', '2018-08-25 00:00:00', '2018-08-25 00:00:00'),
(31, '6664', 'root1234', '2018-08-25 00:00:00', '2018-08-25 00:00:00'),
(32, '4334', 'root3344', '2018-08-25 03:09:41', '2018-08-25 03:09:41'),
(33, '3334', 'root1244', '2018-08-25 03:20:25', '2018-08-25 03:20:25'),
(34, '4534', 'root1234', '2018-08-25 03:48:25', '2018-08-25 03:48:25'),
(35, '5534', 'root1234', '2018-08-25 03:50:31', '2018-08-25 03:50:31'),
(36, '5544', 'root1234', '2018-08-25 03:51:17', '2018-08-25 03:51:17');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`, `create_time`, `update_time`) VALUES
(1, 'admin', 'admin@admin.adminx', '123', '2018-08-24 00:27:00', '2018-08-24 00:00:00');

--
-- 转储表的索引
--

--
-- 表的索引 `qq_list`
--
ALTER TABLE `qq_list`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `qq_list`
--
ALTER TABLE `qq_list`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
