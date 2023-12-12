-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2023 at 01:27 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pwcdb1`
--

-- --------------------------------------------------------

--
-- Table structure for table `employees2`
--

CREATE TABLE `employees2` (
  `empid` int(11) NOT NULL,
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(30) NOT NULL,
  `department` varchar(30) NOT NULL,
  `position` varchar(30) NOT NULL,
  `salary` int(11) NOT NULL,
  `branch` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employees2`
--

INSERT INTO `employees2` (`empid`, `firstname`, `lastname`, `department`, `position`, `salary`, `branch`) VALUES
(1, 'patrick', 'reyes', 'mis', 'devops', 70000, 'makati'),
(2, 'sandy', 'cheeks', 'hr', 'admin', 80000, 'baguio'),
(3, 'danny', 'jocson', 'hr', 'admin', 80000, 'makati'),
(4, 'cindy', 'lauper', 'mis', 'web', 61000, 'makati'),
(6, 'bruce', 'lee', 'hr', 'executive', 67000, 'makati'),
(7, 'aiza', 'seg', 'mis', 'executive', 69000, 'makati'),
(8, 'tito', 'sotto', 'hr', 'executive', 78000, 'makati'),
(9, 'vic', 'sott', 'mis', 'programmer', 68000, 'makati'),
(10, 'allie', 'mcbeal', 'accoutning', 'executive', 57000, 'manila'),
(11, 'spongebob', 'squarepants', 'MIS', 'programmer', 78000, 'makati'),
(13, 'gerry', 'gomez', 'HR', 'admin', 79000, 'manila'),
(14, 'diana', 'rocca', 'MIS', 'dev', 57000, 'manila'),
(15, 'joshua', 'garcia', 'mis', 'dev', 86000, 'manila'),
(16, 'ivana', 'santos', 'hr', 'assistant', 87000, 'makati'),
(17, 'gio', 'santos', 'mis', 'dev', 76000, 'makati');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employees2`
--
ALTER TABLE `employees2`
  ADD PRIMARY KEY (`empid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employees2`
--
ALTER TABLE `employees2`
  MODIFY `empid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
