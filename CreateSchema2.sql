-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: truonghoc2
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
DROP DATABASE IF EXISTS `truonghoc2`;
CREATE DATABASE `truonghoc2`;
USE `truonghoc2`;

--
-- Table structure for table `hoc`
--

DROP TABLE IF EXISTS `hoc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hoc` (
  `MATR` int NOT NULL,
  `MAHS` int NOT NULL,
  `NAMHOC` int NOT NULL,
  `DIEMTB` float DEFAULT NULL,
  `XEPLOAI` varchar(255) DEFAULT NULL,
  `KQUA` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`MATR`,`MAHS`,`NAMHOC`),
  KEY `MAHS` (`MAHS`),
  KEY `idx_XEPLOAI` (`XEPLOAI`),
  KEY `idx_NAMHOC` (`NAMHOC`),
  CONSTRAINT `hoc_ibfk_1` FOREIGN KEY (`MATR`) REFERENCES `truong` (`MATR`),
  CONSTRAINT `hoc_ibfk_2` FOREIGN KEY (`MAHS`) REFERENCES `hs` (`MAHS`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hoc`
--

--
-- Table structure for table `hs`
--

DROP TABLE IF EXISTS `hs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hs` (
  `MAHS` int NOT NULL,
  `HO` varchar(255) DEFAULT NULL,
  `TEN` varchar(255) DEFAULT NULL,
  `CCCD` varchar(15) DEFAULT NULL,
  `NTNS` date DEFAULT NULL,
  `DCHI_HS` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`MAHS`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hs`
--

--
-- Table structure for table `truong`
--

DROP TABLE IF EXISTS `truong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `truong` (
  `MATR` int NOT NULL,
  `TENTR` varchar(255) DEFAULT NULL,
  `DCHITR` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`MATR`),
  KEY `idx_TENTR` (`TENTR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `truong`
--

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-02 23:29:52
