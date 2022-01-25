CREATE TABLE `Anime_names`  (
  `name_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `anime_id` int UNSIGNED NOT NULL,
  `type_id` tinyint NOT NULL,
  `anime_name` varchar(255) NOT NULL,
  PRIMARY KEY (`name_id`)
);

CREATE TABLE `Anime_type_names`  (
  `type_id` tinyint UNSIGNED NOT NULL,
  `type_name` varchar(127) NOT NULL,
  PRIMARY KEY (`type_id`)
);

CREATE TABLE `Animes`  (
  `anime_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`anime_id`)
);

CREATE TABLE `Animes_from_distributor`  (
  `distributor_id` int UNSIGNED NOT NULL,
  `anime_id` int UNSIGNED NOT NULL
);

CREATE TABLE `Animes_in_list`  (
  `list_id` int UNSIGNED NOT NULL,
  `anime_id` int UNSIGNED NOT NULL
);

CREATE TABLE `Distribution_type_names`  ();

CREATE TABLE `Distribution_types`  (
  `type_id` int UNSIGNED NOT NULL,
  `type_name` varchar(63) NOT NULL,
  PRIMARY KEY (`type_id`)
);

CREATE TABLE `Distributions`  (
  `distribution_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `distributor_id` int UNSIGNED NOT NULL,
  `anime_id` int UNSIGNED NOT NULL,
  `distribution_type` int UNSIGNED NOT NULL,
  PRIMARY KEY (`distribution_id`)
);

CREATE TABLE `Distributor_names`  ();

CREATE TABLE `Distributors`  (
  `distributor_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `distributor_name` varchar(127) NULL,
  PRIMARY KEY (`distributor_id`)
);

CREATE TABLE `Episodes`  (
  `episode_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `anime_id` int UNSIGNED NOT NULL,
  `episode_number` smallint UNSIGNED NOT NULL,
  `name` varchar(63) NULL,
  `desc` text NULL,
  `link` varchar(127) NOT NULL,
  PRIMARY KEY (`episode_id`)
);

CREATE TABLE `Lists`  (
  `list_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` int UNSIGNED NOT NULL,
  `list_name` varchar(127) NOT NULL,
  PRIMARY KEY (`list_id`)
);

CREATE TABLE `Setting_id_names`  (
  `setting_name_id` tinyint UNSIGNED NOT NULL,
  `setting_name` varchar(127) NOT NULL,
  PRIMARY KEY (`setting_name_id`)
);

CREATE TABLE `Settings`  (
  `setting_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` int UNSIGNED NOT NULL,
  `setting_name_id` tinyint UNSIGNED NOT NULL,
  `setting_value` varchar(127) NOT NULL,
  PRIMARY KEY (`setting_id`)
);

CREATE TABLE `Statuses`  (
  `staus_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` int UNSIGNED NOT NULL,
  `anime_id` int UNSIGNED NOT NULL,
  `episode_id` int UNSIGNED NOT NULL,
  `distribution_type` int UNSIGNED NOT NULL,
  `distributor_id` int UNSIGNED NOT NULL,
  `watched` bit(1) NOT NULL,
  PRIMARY KEY (`staus_id`)
);

CREATE TABLE `Users`  (
  `user_id` int UNSIGNED NOT NULL,
  PRIMARY KEY (`user_id`)
);

