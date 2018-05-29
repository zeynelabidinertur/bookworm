-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Anamakine: 10.10.10.12
-- Üretim Zamanı: 23 May 2018, 11:45:36
-- Sunucu sürümü: 5.6.37-82.2
-- PHP Sürümü: 7.0.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `testaa01`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `distributor`
--

CREATE TABLE `distributor` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT 'tedarikçinin ismi',
  `name2` varchar(255) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'mail adresi',
  `phone` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'telefon numarası',
  `contact_person` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'yetkili kişi'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='kişisel tedarikçilerin bilgilerinin tutulduğu tablo';

--
-- Tablo döküm verisi `distributor`
--

INSERT INTO `distributor` (`id`, `name`, `name2`, `email`, `phone`, `contact_person`) VALUES
(1, 'Cengiz Balıkçılık', 'cengizBalik', 'info@cengizbalikcilik.com.tr', '02164926734', 'Alper Tomaçgil'),
(2, 'Bahriyeli Doğa Sporları San. & Tic. Ltd. Şti.', 'bahriyeli', 'info@bahriyeli.com.tr', '3123110350', 'Bahriyeli'),
(3, 'Pazar Yeri', '', '', '', ''),
(4, 'Vira Balıkçılık', 'virabalik', '', '', ''),
(5, 'Marmara Balıkçılık', 'marmarabalik', '', '', ''),
(6, 'Meydan Kamp', 'meydankamp', '', '', ''),
(7, 'Lodos Balıkçılık', 'lodosbalikcilik', '', '', ''),
(8, 'Kısık Balıkçılık', 'albashop', '', '', ''),
(9, 'Altunbaş A.Ş.', 'altunbasas', '', '', ''),
(10, 'Kaptan Balıkçılık', 'Kaptanbalik', '', '', ''),
(11, 'OGS Marine', 'ogsmarine', '', '', ''),
(12, 'Remixon', 'remixon', '', '', ''),
(13, 'Güreller', 'Effebalik', '', '', ''),
(14, 'Salt Balıkçılık', 'Saltbalik', '', '', ''),
(15, 'Free Sub', 'freesub', NULL, NULL, NULL);

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `distributor`
--
ALTER TABLE `distributor`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `distributor`
--
ALTER TABLE `distributor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
