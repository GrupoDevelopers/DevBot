-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema devbot
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema devbot
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `devbot` ;
USE `devbot` ;

-- -----------------------------------------------------
-- Table `devbot`.`chats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `devbot`.`chats` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `chat_id` BIGINT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `chat_id_UNIQUE` (`chat_id` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `devbot`.`experiences`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `devbot`.`experiences` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_telegram_id` BIGINT NOT NULL,
  `chat_id` BIGINT NOT NULL,
  `experience_points` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 10
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `devbot`.`subscribed_tag`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `devbot`.`subscribed_tag` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_user` INT NOT NULL,
  `id_tag` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `devbot`.`tag`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `devbot`.`tag` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tag` VARCHAR(255) NOT NULL,
  `approved_by` VARCHAR(45) NULL DEFAULT NULL,
  `status` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `devbot`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `devbot`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `telegram_id` BIGINT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `telegram_id_UNIQUE` (`telegram_id` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
