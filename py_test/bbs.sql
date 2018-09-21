-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.3.9-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 테이블 pythondb.tbl_uploadbbs 구조 내보내기
CREATE TABLE IF NOT EXISTS `tbl_uploadbbs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `contents` text NOT NULL,
  `author` varchar(50) NOT NULL,
  `fileurl` varchar(256) NOT NULL,
  `regdate` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COMMENT='자료실 게시판 디비';

-- 테이블 데이터 pythondb.tbl_uploadbbs:~6 rows (대략적) 내보내기
/*!40000 ALTER TABLE `tbl_uploadbbs` DISABLE KEYS */;
INSERT INTO `tbl_uploadbbs` (`id`, `title`, `contents`, `author`, `fileurl`, `regdate`) VALUES
	(1, 'hoho', 'hoho', 'hoho', 'hoho', '2018-09-17 14:27:48'),
	(2, '커피1', '1000원 아이스', 'bu', '/static/upload', '2018-09-17 14:28:23'),
	(3, 'ㄴㅇㄻ', 'ㄴㅁㅇㄹ', 'bu', '/static/upload/bu/Tulips.jpg', '2018-09-17 14:51:55'),
	(4, 'ㄴㅇㄹㄴㅇㅁ', 'ㄴㅇㅁㄹㄴㅇ', 'bu', '/static/upload/bu/Desert.jpg', '2018-09-17 14:52:51'),
	(5, '하네헤네', '응응해파리', 'bu', '/static/upload/bu/Jellyfish.jpg', '2018-09-17 15:53:30'),
	(6, '박보검이랑 김연아랑 무슨 관계인가요??', 'ㅇㄹ', 'bu', '/static/upload/bu/Hydrangeas.jpg', '2018-09-17 15:54:30'),
	(7, '끙끙', 'ㅇㄴㅁㄹ', 'bu', '/static/upload/bu/Penguins.jpg', '2018-09-17 15:55:10');
/*!40000 ALTER TABLE `tbl_uploadbbs` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
