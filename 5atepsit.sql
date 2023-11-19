-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 19, 2023 alle 17:56
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5atepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `dipendenti_federico_oliva`
--

CREATE TABLE `dipendenti_federico_oliva` (
  `id` int(11) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `cognome` varchar(20) NOT NULL,
  `posizione_lavorativa` varchar(20) NOT NULL,
  `data_di_assunzione` date NOT NULL,
  `codice_fiscale` varchar(20) NOT NULL,
  `data_nascita` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `dipendenti_federico_oliva`
--

INSERT INTO `dipendenti_federico_oliva` (`id`, `nome`, `cognome`, `posizione_lavorativa`, `data_di_assunzione`, `codice_fiscale`, `data_nascita`) VALUES
(1, 'federico', 'oliva', 'studente', '2018-09-15', 'sdgasdgs', '2005-12-01'),
(2, 'dario', 'foroni', 'studente', '2023-11-21', 'gfsadgfsad', '2005-07-20'),
(3, 'mario', 'rossi', 'professore', '2023-11-08', 'qfSFSDGAS', '1983-11-10');

-- --------------------------------------------------------

--
-- Struttura della tabella `zone_di_lavoro_federico_oliva`
--

CREATE TABLE `zone_di_lavoro_federico_oliva` (
  `id_zona` int(11) NOT NULL,
  `nome_zona` varchar(30) DEFAULT NULL,
  `numero_clienti` int(11) DEFAULT NULL,
  `numero_posti` int(11) DEFAULT NULL,
  `id_dipendenti` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `zone_di_lavoro_federico_oliva`
--

INSERT INTO `zone_di_lavoro_federico_oliva` (`id_zona`, `nome_zona`, `numero_clienti`, `numero_posti`, `id_dipendenti`) VALUES
(1, 'ufficio', 12, 4, 3),
(2, 'classe', 12412, 5235, 1);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendenti_federico_oliva`
--
ALTER TABLE `dipendenti_federico_oliva`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `zone_di_lavoro_federico_oliva`
--
ALTER TABLE `zone_di_lavoro_federico_oliva`
  ADD PRIMARY KEY (`id_zona`),
  ADD KEY `id_dipendenti` (`id_dipendenti`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendenti_federico_oliva`
--
ALTER TABLE `dipendenti_federico_oliva`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT per la tabella `zone_di_lavoro_federico_oliva`
--
ALTER TABLE `zone_di_lavoro_federico_oliva`
  MODIFY `id_zona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `zone_di_lavoro_federico_oliva`
--
ALTER TABLE `zone_di_lavoro_federico_oliva`
  ADD CONSTRAINT `zone_di_lavoro_federico_oliva_ibfk_1` FOREIGN KEY (`id_dipendenti`) REFERENCES `dipendenti_federico_oliva` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
