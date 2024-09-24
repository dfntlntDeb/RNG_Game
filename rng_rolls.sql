-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 24, 2024 at 05:53 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rng_rolls`
--

-- --------------------------------------------------------

--
-- Table structure for table `chances`
--

CREATE TABLE `chances` (
  `Trait` varchar(255) DEFAULT NULL,
  `Info` varchar(255) DEFAULT NULL,
  `Chance` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chances`
--

INSERT INTO `chances` (`Trait`, `Info`, `Chance`) VALUES
('Brawler 1', 'Increases damage by 10% (+10% DPS Increase)', '7.95%'),
('Brawler 2', 'Increases damage by 12.5% (+12.5% DPS Increase)', '7.9%'),
('Brawler 3', 'Increases damage by 15% (+15% DPS Increase)', '7.8%'),
('Swiftness 1', 'Reduces cooldown by -6% (+6.4% DPS Increase)', '7%'),
('Swiftness 2', 'Reduces cooldown by -9% (+9.8% DPS Increase)', '7%'),
('Swiftness 3', 'Reduces cooldown by -12.5% (+14.3% DPS Increase)', '7%'),
('Hunter 1', 'Increases range by 10%', '7%'),
('Hunter 2', 'Increases range by 12.5%', '7%'),
('Hunter 3', 'Increases range by 15%', '7%'),
('Critical 1', 'Increase crit chance by 20% (+10% DPS Increase)', '6.15%'),
('Critical 2', 'Increase crit chance by 25% (+12.5% DPS Increase)', '6.1%'),
('Critical 3', 'Increase crit chance by 30% (+15% DPS Increase)', '6%'),
('Prodigy 1', 'Increases XP gain by 50% Visual changes: Gives the unit small particles.', '10%'),
('Bullseye 1', 'Increases range by 25% Visual changes: Gives the unit red flashing eyes.', '2.5%'),
('Midas Touch 1', 'Increases farm money earned by 15 Visual changes: Gives the unit a coin aura.', '1.5%'),
('Sonic 1', 'Decreases cooldown by -20% Visual changes: Gives the unit a lightning effect around the unit. (+25% DPS Increase)', '1%'),
('Precision 1', '+30% crit chance +30% crit damage. Visual changes: Gives the unit an eyes aura. (+28.5% DPS Increase)', '0.8%'),
('Requiem 1', '+35% damage, -15% cooldown, +20% range. Visual changes: Gives the unit yellow wings. (+58.8% DPS Increase)', '0.2%'),
('Almighty 1', '+280% damage, -15% cooldown, +10% range, 1 placement cap. Visual changes: Gives the unit nebula colored wings.', '0.1%');

-- --------------------------------------------------------

--
-- Table structure for table `rolls`
--

CREATE TABLE `rolls` (
  `Rolled_Trait` varchar(255) DEFAULT NULL,
  `Date_Rolled` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rolls`
--

INSERT INTO `rolls` (`Rolled_Trait`, `Date_Rolled`) VALUES
('Brawler 1', '2024-09-24 11:51:47'),
('Hunter 1', '2024-09-24 11:51:47'),
('Hunter 1', '2024-09-24 11:51:47'),
('Hunter 3', '2024-09-24 11:51:48'),
('Hunter 3', '2024-09-24 11:51:48'),
('Prodigy', '2024-09-24 11:51:48'),
('Sonic 1', '2024-09-24 11:51:48'),
('Brawler 2', '2024-09-24 11:51:48'),
('Brawler 1', '2024-09-24 11:51:49'),
('Brawler 3', '2024-09-24 11:51:49'),
('Critical 2', '2024-09-24 11:51:49'),
('Swiftness 2', '2024-09-24 11:51:50'),
('Midas Touch 1', '2024-09-24 11:51:50'),
('Swiftness 2', '2024-09-24 11:51:50'),
('Critical 2', '2024-09-24 11:51:50'),
('Hunter 2', '2024-09-24 11:51:50'),
('Precision 1', '2024-09-24 11:51:51'),
('Brawler 1', '2024-09-24 11:51:51'),
('Brawler 2', '2024-09-24 11:51:51'),
('Hunter 2', '2024-09-24 11:51:51'),
('Precision 1', '2024-09-24 11:51:51'),
('Hunter 3', '2024-09-24 11:51:52'),
('Hunter 2', '2024-09-24 11:51:52'),
('Hunter 3', '2024-09-24 11:51:52'),
('Critical 3', '2024-09-24 11:51:52'),
('Hunter 3', '2024-09-24 11:51:52'),
('Bullseye 1', '2024-09-24 11:51:53'),
('Brawler 2', '2024-09-24 11:51:53'),
('Hunter 1', '2024-09-24 11:51:53'),
('Swiftness 3', '2024-09-24 11:51:53'),
('Hunter 3', '2024-09-24 11:51:53'),
('Hunter 3', '2024-09-24 11:51:54'),
('Critical 3', '2024-09-24 11:51:54'),
('Critical 1', '2024-09-24 11:51:54'),
('Brawler 2', '2024-09-24 11:51:55'),
('Prodigy', '2024-09-24 11:51:55'),
('Swiftness 3', '2024-09-24 11:51:55'),
('Brawler 2', '2024-09-24 11:51:56'),
('Critical 2', '2024-09-24 11:51:56'),
('Prodigy', '2024-09-24 11:51:56'),
('Brawler 2', '2024-09-24 11:51:56'),
('Swiftness 1', '2024-09-24 11:51:57'),
('Swiftness 3', '2024-09-24 11:51:57'),
('Critical 2', '2024-09-24 11:51:57'),
('Hunter 1', '2024-09-24 11:51:58'),
('Swiftness 3', '2024-09-24 11:51:58'),
('Swiftness 2', '2024-09-24 11:51:58'),
('Brawler 2', '2024-09-24 11:51:58'),
('Precision 1', '2024-09-24 11:51:59'),
('Swiftness 2', '2024-09-24 11:51:59'),
('Brawler 3', '2024-09-24 11:51:59'),
('Brawler 1', '2024-09-24 11:51:59'),
('Swiftness 3', '2024-09-24 11:52:00'),
('Prodigy', '2024-09-24 11:52:00'),
('Brawler 3', '2024-09-24 11:52:00'),
('Brawler 2', '2024-09-24 11:52:00');

-- --------------------------------------------------------

--
-- Table structure for table `traits`
--

CREATE TABLE `traits` (
  `Traits` varchar(255) DEFAULT NULL,
  `Rarity` varchar(255) DEFAULT NULL,
  `Chances` float(6,5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `traits`
--

INSERT INTO `traits` (`Traits`, `Rarity`, `Chances`) VALUES
('Brawler 1', 'Common', 0.07950),
('Brawler 2', 'Common', 0.07900),
('Brawler 3', 'Common', 0.07800),
('Swiftness 1', 'Common', 0.07000),
('Swiftness 2', 'Common', 0.07000),
('Swiftness 3', 'Common', 0.07000),
('Hunter 1', 'Common', 0.07000),
('Hunter 2', 'Common', 0.07000),
('Hunter 3', 'Common', 0.07000),
('Critical 1', 'Common', 0.06150),
('Critical 2', 'Common', 0.06100),
('Critical 3', 'Common', 0.06000),
('Prodigy', 'Common', 0.10000),
('Bullseye 1', 'Epic', 0.02500),
('Midas Touch 1', 'Epic', 0.01500),
('Sonic 1', 'Legendary', 0.01000),
('Precision 1', 'Legendary', 0.00800),
('Requiem 1', 'Mythic', 0.00200),
('Almighty 1', 'Mythic', 0.00100);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
