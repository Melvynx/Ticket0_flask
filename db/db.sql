-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:8889
-- Généré le :  mer. 03 juin 2020 à 08:21
-- Version du serveur :  5.7.26
-- Version de PHP :  7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


DROP DATABASE if exists melvyn_malherbe_tiqet_bd_104;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS melvyn_malherbe_tiqet_bd_104;

-- Utilisation de cette base de donnée

USE melvyn_malherbe_tiqet_bd_104;

--
-- Base de données :  `melvyn_malherbe_tiqet_bd_104`
--

-- --------------------------------------------------------

--
-- Structure de la table `T_Category`
--

CREATE TABLE `T_Category` (
  `id_category` int(11) NOT NULL,
  `name` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  `description` mediumtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Déchargement des données de la table `T_Category`
--

INSERT INTO `T_Category` (`id_category`, `name`, `description`, `created_at`) VALUES
(1, '🛠matos', 'famille des matériaux a réparé !a', '2020-04-06 08:41:42'),
(5, 'backoffice', 'salut', '2020-04-06 08:41:42'),
(6, 'accès', '\nwefew\n\nffefwefefewsalut', '2020-04-06 08:41:42'),
(7, '🦀crabe', 'catégory de crabe !!!!', '2020-04-10 14:42:17'),
(12, 'aaaa', 'aaaa', '2020-04-18 21:09:41'),
(13, 'Spécial Maccaud', 'fdfff', '2020-04-30 13:13:14');

-- --------------------------------------------------------

--
-- Structure de la table `T_Comment`
--

CREATE TABLE `T_Comment` (
  `id_comment` int(11) NOT NULL,
  `fk_author` int(11) NOT NULL,
  `fk_tiqet` int(11) NOT NULL,
  `content` mediumtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Déchargement des données de la table `T_Comment`
--

INSERT INTO `T_Comment` (`id_comment`, `fk_author`, `fk_tiqet`, `content`, `created_at`) VALUES
(1, 3, 8, 'Je trouve ceci affligeant de voir un test aussi mal fait.', '2020-04-11 10:21:43'),
(2, 1, 8, 'Incroyable de voir que personne ne respect le confinement . ', '2020-04-11 10:21:43'),
(3, 1, 8, 'Hier, j\'ai pris 100 francs d\'ammendes car je baisais sur une place de jeu. ', '2020-04-12 10:18:40'),
(4, 3, 8, 'Fallait pas sortir gros sac #restezChezVous 😁', '2020-04-12 10:21:46'),
(5, 2, 14, 'ddddododododo', '2020-04-28 19:30:07'),
(6, 3, 16, 'jean ', '2020-04-28 20:04:36'),
(7, 3, 16, 'jean ', '2020-04-28 20:04:50'),
(8, 3, 16, 'jean ', '2020-04-28 20:05:00'),
(9, 3, 16, 'Michel', '2020-04-29 06:33:27'),
(10, 3, 16, 'Michel', '2020-04-29 06:33:30'),
(11, 3, 16, 'Michel', '2020-04-29 06:33:32'),
(12, 3, 16, 'Michel', '2020-04-29 06:33:32'),
(13, 3, 16, 'Michel', '2020-04-29 06:33:33'),
(14, 3, 16, 'Michel', '2020-04-29 06:33:33'),
(15, 3, 16, 'Michel', '2020-04-29 06:33:33'),
(16, 3, 16, 'Michel', '2020-04-29 06:33:34'),
(17, 3, 16, 'Michel', '2020-04-29 06:33:34'),
(18, 3, 16, 'Michel', '2020-04-29 06:33:34'),
(19, 3, 16, 'Michel', '2020-04-29 06:33:34'),
(20, 3, 16, 'Michel', '2020-04-29 06:33:35'),
(21, 3, 16, 'Michel', '2020-04-29 06:33:35'),
(22, 3, 16, 'Michel', '2020-04-29 06:33:36'),
(23, 3, 16, 'Michel', '2020-04-29 06:33:42'),
(24, 3, 16, 'Michel', '2020-04-29 06:33:45'),
(25, 3, 16, 'Michel', '2020-04-29 06:33:45'),
(26, 3, 16, 'Michel', '2020-04-29 06:33:46'),
(27, 3, 16, 'Michel', '2020-04-29 06:33:46'),
(28, 3, 16, 'Michel', '2020-04-29 06:33:47'),
(29, 3, 16, 'Michel', '2020-04-29 06:33:47'),
(30, 3, 16, 'Michel', '2020-04-29 06:33:48'),
(31, 3, 16, 'Michel', '2020-04-29 06:33:48'),
(32, 3, 16, 'Michel', '2020-04-29 06:33:48'),
(33, 3, 16, 'Michel', '2020-04-29 06:33:49'),
(34, 3, 16, 'Michel', '2020-04-29 06:33:49'),
(35, 3, 16, 'Michel', '2020-04-29 06:33:49'),
(36, 3, 16, 'Michel', '2020-04-29 06:33:50'),
(37, 3, 16, 'Michel', '2020-04-29 06:33:50'),
(38, 3, 16, 'Michel', '2020-04-29 06:33:50'),
(39, 3, 16, 'Michel', '2020-04-29 06:33:50'),
(40, 3, 16, 'Michel', '2020-04-29 06:33:51'),
(41, 3, 16, 'Michel', '2020-04-29 06:33:51'),
(42, 3, 16, 'Michel', '2020-04-29 06:33:51'),
(43, 3, 16, 'Michel', '2020-04-29 06:33:51'),
(44, 3, 17, 'test', '2020-04-29 06:34:40'),
(45, 3, 17, 'test2', '2020-04-29 06:35:28'),
(46, 3, 17, 'test3', '2020-04-29 06:36:06'),
(47, 3, 17, 'test4', '2020-04-29 06:36:47'),
(48, 3, 17, 'test12', '2020-04-29 06:38:03'),
(49, 3, 17, 'bonsoir', '2020-04-29 06:38:16'),
(50, 3, 17, 'avant :  04/29/2020, 08:38:03\naprès :  29/04/2020 ,10:36:47 ', '2020-04-29 06:38:46'),
(51, 3, 17, 'test333', '2020-04-29 06:39:42'),
(52, 3, 17, 'ddddd', '2020-04-29 08:12:38'),
(53, 3, 17, 'Jean test\n\n\n3 spaces ', '2020-04-29 08:19:28'),
(54, 3, 17, '2 ème test\n\n1 space', '2020-04-29 08:20:04'),
(55, 3, 5, 'test', '2020-04-29 13:57:46'),
(56, 3, 10, 'aa', '2020-04-30 10:34:04'),
(57, 3, 10, 'Pourquoi tu veux démélé les FILLES ?? ?? ? ? ', '2020-04-30 11:18:08'),
(58, 3, 2, 'J\'ai une souris ', '2020-04-30 13:12:04'),
(59, 3, 2, 'vggggg', '2020-04-30 13:12:08'),
(60, 3, 2, 'gggggt', '2020-04-30 13:12:10'),
(61, 3, 18, 'aaaaaa', '2020-05-04 08:58:13'),
(62, 3, 18, 'ana blazouille ', '2020-05-04 08:58:18'),
(63, 3, 18, 'anapêche', '2020-05-04 09:30:09'),
(64, 3, 18, 'anaconda', '2020-05-04 09:30:17'),
(65, 3, 18, 'anafeuille', '2020-05-04 09:30:22'),
(66, 3, 19, 'uuu', '2020-05-04 09:31:55'),
(67, 3, 19, 'Que fais tu padawan ', '2020-05-04 11:27:50'),
(68, 3, 2, '<script> alert(\"bonsoir\") </script>\n', '2020-05-28 17:21:19'),
(69, 3, 2, 'dddd', '2020-05-28 17:31:31'),
(70, 3, 2, 'bonsoir \n \newg\ng\nwe\neg\nwe\ngew\ngwe', '2020-05-28 17:34:44'),
(71, 3, 2, 'bonsoir didier', '2020-05-28 17:42:08'),
(72, 3, 2, 'dddd', '2020-05-28 17:42:35'),
(73, 3, 2, 'dddd', '2020-05-28 17:43:03'),
(74, 3, 2, 'qfqqww', '2020-05-28 17:43:44'),
(75, 3, 2, 'effweffweew', '2020-05-28 17:44:03'),
(76, 3, 2, 'qffqwfqwfwqfqw', '2020-05-28 17:44:14'),
(77, 3, 2, 'cdd', '2020-05-28 17:44:33'),
(78, 3, 2, '1221r21r21r12', '2020-05-28 17:45:11');

-- --------------------------------------------------------

--
-- Structure de la table `T_History`
--

CREATE TABLE `T_History` (
  `id_history` int(11) NOT NULL,
  `fk_tiqet` int(11) NOT NULL,
  `content` mediumtext COLLATE utf8mb4_bin NOT NULL,
  `author` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Structure de la table `T_Item`
--

CREATE TABLE `T_Item` (
  `id_item` int(11) NOT NULL,
  `fk_category` int(11) NOT NULL,
  `name` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  `description` mediumtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Déchargement des données de la table `T_Item`
--

INSERT INTO `T_Item` (`id_item`, `fk_category`, `name`, `description`, `created_at`) VALUES
(2, 1, '⌨️clavier', 'le clavier tu tieks', '2020-03-05 09:20:33'),
(3, 1, '🖱souris', 'une souris d\'une rare qualité', '2020-04-06 10:50:33'),
(4, 1, '💻ordi', 'quand ton ordi est OUT', '2020-04-06 10:50:33'),
(8, 6, '<script>alert(\"machin\")</script>', 'les accès du bo ', '2020-04-06 12:19:41'),
(9, 6, 'accès google', 'Je ne pense pas que les accès google soit primordial.', '2020-04-06 12:22:39'),
(10, 5, 'aat', 'bbbb', '2020-04-06 13:52:42'),
(11, 1, '🖨imprimante', 'quand ton imprimante est morte, ta vie est triste', '2020-04-09 09:23:35'),
(12, 1, '📱téléphone portable', 'beug avec téléphone', '2020-04-09 09:24:19'),
(13, 1, 'jeanfou', 'dddd', '2020-04-09 09:24:56'),
(16, 7, '🦀jean - le crab', 'Jean est une personne sympatique.\r\nIl aime nager, voyager et surtout faire les courses ! ', '2020-04-10 14:42:43'),
(17, 7, '🦞Didier - l\'écrievise', 'Il aime voyager, nagé, dormir, se reposer et surtout voir ses amis nus !!!!!!!!!!!', '2020-04-10 14:43:22'),
(18, 7, '🦑Philipe - Le calamar', 'Il est moche, \r\nmais il a \r\nun grand coeur', '2020-04-10 14:43:41'),
(19, 7, '🦈ana - le requin', 'c\'est pas vrm un requin en vrai !!!!!!!!!!!!!!!', '2020-04-12 20:15:12'),
(25, 7, '🐠maman - le poisson', 'elle est maigre mais elle a un gros coeur', '2020-04-27 19:41:13'),
(26, 13, 'mac', 'le manche a couille', '2020-04-30 13:13:54');

-- --------------------------------------------------------

--
-- Structure de la table `T_Label`
--

CREATE TABLE `T_Label` (
  `id_label` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text,
  `color` varchar(10) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `T_Label`
--

INSERT INTO `T_Label` (`id_label`, `name`, `description`, `color`, `created_at`) VALUES
(1, 'A faire demain', NULL, '0984e3', '2020-05-13 09:11:23'),
(2, 'attente de retour', NULL, '00cec9', '2020-05-13 09:11:23'),
(3, 'mon 3ème label', NULL, '111111', '2020-05-14 09:19:41');

-- --------------------------------------------------------

--
-- Structure de la table `T_Priority`
--

CREATE TABLE `T_Priority` (
  `id_priority` int(11) NOT NULL,
  `name` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  `level` int(11) DEFAULT '0',
  `description` mediumtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Déchargement des données de la table `T_Priority`
--

INSERT INTO `T_Priority` (`id_priority`, `name`, `level`, `description`, `created_at`) VALUES
(2, 'mediumm', 6, 'moyennee', '2020-03-05 09:20:57'),
(3, 'high', 10, 'haute', '2020-04-07 08:30:25'),
(5, 'low', 4, 'low', '2020-05-07 11:44:19');

-- --------------------------------------------------------

--
-- Structure de la table `T_State`
--

CREATE TABLE `T_State` (
  `id_state` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `display` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Déchargement des données de la table `T_State`
--

INSERT INTO `T_State` (`id_state`, `name`, `display`, `created_at`) VALUES
(1, 'pending', 1, '2020-03-05 09:22:16'),
(2, 'inprogress', 1, '2020-03-05 09:22:16'),
(3, 'completed', 1, '2020-04-07 08:30:49'),
(4, 'denied', 0, '2020-04-07 08:42:16'),
(5, 'archived', 0, '2020-04-07 08:42:16');

-- --------------------------------------------------------

--
-- Structure de la table `T_Tiqet`
--

CREATE TABLE `T_Tiqet` (
  `id_tiqet` int(11) NOT NULL,
  `fk_priority` int(11) DEFAULT NULL,
  `fk_reporter` int(11) DEFAULT NULL,
  `fk_assigned` int(11) DEFAULT NULL,
  `fk_item` int(11) DEFAULT NULL,
  `title` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  `content` mediumtext COLLATE utf8mb4_bin NOT NULL,
  `fk_state` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='Table principal. ';

--
-- Déchargement des données de la table `T_Tiqet`
--

INSERT INTO `T_Tiqet` (`id_tiqet`, `fk_priority`, `fk_reporter`, `fk_assigned`, `fk_item`, `title`, `content`, `fk_state`, `created_at`) VALUES
(2, 3, 3, 1, 8, 'Besoin d\'une nouvelle sourisd', '<script> alert(\"bonsoir\") </script>', 2, '2020-04-07 08:35:59'),
(3, 3, 2, 1, 18, 'Jean - Tiqet', 'besoin de réinitialiser mon password google !!!^!', 3, '2020-04-07 08:35:59'),
(4, 2, NULL, 2, 11, 'rrrrrrrr', 'rrrrrr', 3, '2020-04-07 08:44:15'),
(5, NULL, 1, NULL, NULL, 'aaa', 'aaa', 3, '2020-04-09 11:16:17'),
(8, 2, NULL, 3, NULL, 'Mon nouveau test   ', 'Voici le sujet de ce magnfiqueh saint-test qui restera dans les annals. ', 3, '2020-04-09 14:16:33'),
(10, 3, NULL, 3, 3, 'Démélé les filles du premier', 'Il faut démélé les filles en bas.', 3, '2020-04-10 11:11:27'),
(11, NULL, NULL, 2, NULL, 'Test low pri ', 'Moi aussi', 2, '2020-04-10 11:12:12'),
(12, NULL, NULL, NULL, NULL, 'test2', '', 2, '2020-04-10 14:38:53'),
(13, NULL, NULL, NULL, 19, 'FireFox🔥', '', 2, '2020-04-10 14:40:50'),
(14, 2, NULL, 3, NULL, 'ana', 'drga9ouiooe', 3, '2020-04-12 20:13:26'),
(15, NULL, NULL, NULL, 9, 'dddd', 'k\nSalut', 2, '2020-04-13 17:02:49'),
(16, NULL, NULL, 3, 17, 'supprimer', 'mon tiqet', 2, '2020-04-13 17:04:33'),
(17, 2, NULL, 3, NULL, 'Test delete  ', 'Je ne fais rien.', 2, '2020-04-15 17:19:54'),
(18, 2, NULL, 3, 9, 'dddddddddddddddd', '', 2, '2020-04-15 17:28:18'),
(19, 2, NULL, 3, NULL, 'DDDDDDD ', 'Mon content\n\nQui est bg', 2, '2020-04-15 19:26:10'),
(20, NULL, NULL, 4, 3, 'Faire les course  ', 'Aller acheter mes pommes\n\n!!', 1, '2020-04-30 13:15:20'),
(21, NULL, NULL, NULL, 16, 'VRAI TIQET FAILE XLSLS S', 'VéRIFé FAILLE XXLFLELWEGLWEGGE', 1, '2020-05-05 12:15:46');

-- --------------------------------------------------------

--
-- Structure de la table `T_Tiqet_to_Label`
--

CREATE TABLE `T_Tiqet_to_Label` (
  `id_tiqet_to_label` int(11) NOT NULL,
  `fk_tiqet` int(11) NOT NULL,
  `fk_label` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `T_User`
--

CREATE TABLE `T_User` (
  `id_user` int(11) NOT NULL,
  `username` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `firstname` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `lastname` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `email` mediumtext COLLATE utf8mb4_bin NOT NULL,
  `password` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Déchargement des données de la table `T_User`
--

INSERT INTO `T_User` (`id_user`, `username`, `firstname`, `lastname`, `email`, `password`, `created_at`) VALUES
(1, 'Jean', 'Fils', 'Jean', 'jean@jean.com', 'michel', '2020-03-05 09:04:01'),
(2, 'pascal', 'drolito', 'fastidue', 'jean@jan.com', 'lolitod', '2020-03-05 09:04:01'),
(3, 'Melvynx', 'Melvyn', 'Malherbe', 'melvynmal@gmail.com', 'pbkdf2:sha256:150000$YfmorOs9$a5215bbd4b87295d0d5e03d2bbaf16e6b83377aafc2a80bec9885b544fa4c450', '2020-04-07 08:32:53'),
(4, 'test', 'test', 'test', 'test@test.com', 'wefefwwfeef', '2020-04-26 12:59:27'),
(5, 'username', 'firstname', 'lastname', 'email', 'pbkdf2:sha256:150000$5ikfNr68$af348e3a9033200af2408746650d6744e6b8778fa49148dbf9f7fc728d7fe5b1', '2020-04-26 13:00:20'),
(7, 'test2', NULL, NULL, 'test2', 'test2', '2020-04-27 12:58:37'),
(9, 'Test44', 'testt', '44444', 'test44@gmail.ch', 'pbkdf2:sha256:150000$0XWLj7jU$231606d1f64ae664f76101e91b7b7a70a61d6294c696b6439b2aba61fe487b3c', '2020-04-27 13:07:37');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `T_Category`
--
ALTER TABLE `T_Category`
  ADD PRIMARY KEY (`id_category`);

--
-- Index pour la table `T_Comment`
--
ALTER TABLE `T_Comment`
  ADD PRIMARY KEY (`id_comment`),
  ADD KEY `fk_author` (`fk_author`),
  ADD KEY `fk_tiqet` (`fk_tiqet`);

--
-- Index pour la table `T_History`
--
ALTER TABLE `T_History`
  ADD PRIMARY KEY (`id_history`),
  ADD KEY `fk_tiqet` (`fk_tiqet`);

--
-- Index pour la table `T_Item`
--
ALTER TABLE `T_Item`
  ADD PRIMARY KEY (`id_item`),
  ADD KEY `fk_category` (`fk_category`);

--
-- Index pour la table `T_Label`
--
ALTER TABLE `T_Label`
  ADD PRIMARY KEY (`id_label`),
  ADD KEY `id_label` (`id_label`);

--
-- Index pour la table `T_Priority`
--
ALTER TABLE `T_Priority`
  ADD PRIMARY KEY (`id_priority`);

--
-- Index pour la table `T_State`
--
ALTER TABLE `T_State`
  ADD PRIMARY KEY (`id_state`);

--
-- Index pour la table `T_Tiqet`
--
ALTER TABLE `T_Tiqet`
  ADD PRIMARY KEY (`id_tiqet`),
  ADD KEY `fk_priority` (`fk_priority`),
  ADD KEY `fk_reporter` (`fk_reporter`),
  ADD KEY `fk_assigned` (`fk_assigned`),
  ADD KEY `fk_state` (`fk_state`),
  ADD KEY `fk_item_tiqet` (`fk_item`);

--
-- Index pour la table `T_Tiqet_to_Label`
--
ALTER TABLE `T_Tiqet_to_Label`
  ADD PRIMARY KEY (`id_tiqet_to_label`),
  ADD KEY `fk_label` (`fk_label`),
  ADD KEY `fk_tiqet` (`fk_tiqet`);

--
-- Index pour la table `T_User`
--
ALTER TABLE `T_User`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `T_Category`
--
ALTER TABLE `T_Category`
  MODIFY `id_category` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT pour la table `T_Comment`
--
ALTER TABLE `T_Comment`
  MODIFY `id_comment` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;

--
-- AUTO_INCREMENT pour la table `T_History`
--
ALTER TABLE `T_History`
  MODIFY `id_history` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `T_Item`
--
ALTER TABLE `T_Item`
  MODIFY `id_item` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT pour la table `T_Label`
--
ALTER TABLE `T_Label`
  MODIFY `id_label` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `T_Priority`
--
ALTER TABLE `T_Priority`
  MODIFY `id_priority` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `T_State`
--
ALTER TABLE `T_State`
  MODIFY `id_state` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `T_Tiqet`
--
ALTER TABLE `T_Tiqet`
  MODIFY `id_tiqet` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT pour la table `T_Tiqet_to_Label`
--
ALTER TABLE `T_Tiqet_to_Label`
  MODIFY `id_tiqet_to_label` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `T_User`
--
ALTER TABLE `T_User`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `T_Comment`
--
ALTER TABLE `T_Comment`
  ADD CONSTRAINT `fk_author_comment` FOREIGN KEY (`fk_author`) REFERENCES `T_User` (`id_user`),
  ADD CONSTRAINT `fk_tiqet_comment` FOREIGN KEY (`fk_tiqet`) REFERENCES `T_Tiqet` (`id_tiqet`);

--
-- Contraintes pour la table `T_History`
--
ALTER TABLE `T_History`
  ADD CONSTRAINT `fk_tiqet_history` FOREIGN KEY (`fk_tiqet`) REFERENCES `T_Tiqet` (`id_tiqet`);

--
-- Contraintes pour la table `T_Item`
--
ALTER TABLE `T_Item`
  ADD CONSTRAINT `fk_category_item` FOREIGN KEY (`fk_category`) REFERENCES `T_Category` (`id_category`);

--
-- Contraintes pour la table `T_Tiqet`
--
ALTER TABLE `T_Tiqet`
  ADD CONSTRAINT `fk_assigned_tiqet` FOREIGN KEY (`fk_assigned`) REFERENCES `T_User` (`id_user`),
  ADD CONSTRAINT `fk_item_tiqet` FOREIGN KEY (`fk_item`) REFERENCES `T_Item` (`id_item`),
  ADD CONSTRAINT `fk_priority_tiqet` FOREIGN KEY (`fk_priority`) REFERENCES `T_Priority` (`id_priority`),
  ADD CONSTRAINT `fk_reporter_tiqet` FOREIGN KEY (`fk_reporter`) REFERENCES `T_User` (`id_user`),
  ADD CONSTRAINT `fk_state_tiqet` FOREIGN KEY (`fk_state`) REFERENCES `T_State` (`id_state`);

--
-- Contraintes pour la table `T_Tiqet_to_Label`
--
ALTER TABLE `T_Tiqet_to_Label`
  ADD CONSTRAINT `fk_label` FOREIGN KEY (`fk_label`) REFERENCES `T_Label` (`id_label`),
  ADD CONSTRAINT `fk_tiqet` FOREIGN KEY (`fk_tiqet`) REFERENCES `T_Tiqet` (`id_tiqet`);
