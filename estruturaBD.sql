-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema correcao_gabarito
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema correcao_gabarito
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `correcao_gabarito` DEFAULT CHARACTER SET latin1 ;
USE `correcao_gabarito` ;

-- -----------------------------------------------------
-- Table `correcao_gabarito`.`auth_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`auth_group` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name` (`name` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`django_content_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`django_content_type` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `app_label` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label` ASC, `model` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 19
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`auth_permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`auth_permission` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `content_type_id` INT(11) NOT NULL,
  `codename` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id` ASC, `codename` ASC),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `correcao_gabarito`.`django_content_type` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 55
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`auth_group_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`auth_group_permissions` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `group_id` INT(11) NOT NULL,
  `permission_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id` ASC, `permission_id` ASC),
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id` ASC),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `correcao_gabarito`.`auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `correcao_gabarito`.`auth_group` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`auth_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`auth_user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(128) NOT NULL,
  `last_login` DATETIME(6) NULL DEFAULT NULL,
  `is_superuser` TINYINT(1) NOT NULL,
  `username` VARCHAR(150) NOT NULL,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(30) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `is_staff` TINYINT(1) NOT NULL,
  `is_active` TINYINT(1) NOT NULL,
  `date_joined` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username` (`username` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`auth_user_groups`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`auth_user_groups` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `group_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id` ASC, `group_id` ASC),
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id` ASC),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `correcao_gabarito`.`auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `correcao_gabarito`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`auth_user_user_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`auth_user_user_permissions` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `permission_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id` ASC, `permission_id` ASC),
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id` ASC),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `correcao_gabarito`.`auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `correcao_gabarito`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`django_admin_log`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`django_admin_log` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `action_time` DATETIME(6) NOT NULL,
  `object_id` LONGTEXT NULL DEFAULT NULL,
  `object_repr` VARCHAR(200) NOT NULL,
  `action_flag` SMALLINT(5) UNSIGNED NOT NULL,
  `change_message` LONGTEXT NOT NULL,
  `content_type_id` INT(11) NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id` ASC),
  INDEX `django_admin_log_user_id_c564eba6_fk` (`user_id` ASC),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `correcao_gabarito`.`django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk`
    FOREIGN KEY (`user_id`)
    REFERENCES `correcao_gabarito`.`auth_user` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 438
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`django_migrations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`django_migrations` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `app` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `applied` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 16
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`django_session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`django_session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` LONGTEXT NOT NULL,
  `expire_date` DATETIME(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  INDEX `django_session_expire_date_a5c62663` (`expire_date` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`jet_bookmark`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`jet_bookmark` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `url` VARCHAR(200) NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `user` INT(10) UNSIGNED NOT NULL,
  `date_add` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`jet_pinnedapplication`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`jet_pinnedapplication` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `app_label` VARCHAR(255) NOT NULL,
  `user` INT(10) UNSIGNED NOT NULL,
  `date_add` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`tb_academico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`tb_academico` (
  `cd_academico` INT(11) NOT NULL AUTO_INCREMENT,
  `no_academico` TEXT NOT NULL,
  `email` TEXT CHARACTER SET 'utf8' NOT NULL,
  `cd_curso` INT(11) NULL DEFAULT NULL,
  `nu_cod_academico` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cd_academico`),
  INDEX `fk_curso_academico` (`cd_curso` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 49
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`tb_curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`tb_curso` (
  `cd_curso` INT(11) NOT NULL AUTO_INCREMENT,
  `no_curso` TEXT NOT NULL,
  `bo_curso` TINYINT(1) NOT NULL,
  PRIMARY KEY (`cd_curso`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`tb_gabarito`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`tb_gabarito` (
  `cd_gabarito` INT(11) NOT NULL AUTO_INCREMENT,
  `cd_periodo` INT(11) NOT NULL,
  `cd_curso` INT(11) NOT NULL,
  `cd_periodo_avaliativo` INT(11) NOT NULL,
  PRIMARY KEY (`cd_gabarito`),
  INDEX `fk_tb_gabarito_resposta_tb_periodo_avaliativo1_idx` (`cd_periodo_avaliativo` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`tb_periodo_avaliativo_has_tb_academico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`tb_periodo_avaliativo_has_tb_academico` (
  `cd_avaliativo_academico` INT(11) NOT NULL AUTO_INCREMENT,
  `cd_periodo_avaliativo` INT(11) NOT NULL,
  `cd_academico` INT(11) NOT NULL,
  `nu_matricula` VARCHAR(15) NOT NULL,
  `cd_periodo` INT(11) NOT NULL,
  PRIMARY KEY (`cd_avaliativo_academico`),
  INDEX `fk_tb_periodo_avaliativo_has_tb_academico_tb_academico1_idx` (`cd_academico` ASC),
  INDEX `fk_tb_periodo_avaliativo_has_tb_academico_tb_periodo_avalia_idx` (`cd_periodo_avaliativo` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 49
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`tb_gabarito_academico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`tb_gabarito_academico` (
  `nu_questao` INT(11) NULL DEFAULT NULL,
  `res_questao` VARCHAR(1) NULL DEFAULT NULL,
  `cd_usuario` INT(11) NOT NULL,
  `cd_gabarito_academico` INT(11) NOT NULL AUTO_INCREMENT,
  `cd_avaliativo_academico` INT(11) NOT NULL,
  PRIMARY KEY (`cd_gabarito_academico`),
  INDEX `fk_tb_gabarito_academico_auth_user` (`cd_usuario` ASC),
  INDEX `fk_tb_periodo_avaliativo_tb_academico_tb_gabarito_academico` (`cd_avaliativo_academico` ASC),
  CONSTRAINT `fk_tb_gabarito_academico_auth_user`
    FOREIGN KEY (`cd_usuario`)
    REFERENCES `correcao_gabarito`.`auth_user` (`id`),
  CONSTRAINT `fk_tb_periodo_avaliativo_tb_academico_tb_gabarito_academico`
    FOREIGN KEY (`cd_avaliativo_academico`)
    REFERENCES `correcao_gabarito`.`tb_periodo_avaliativo_has_tb_academico` (`cd_avaliativo_academico`))
ENGINE = InnoDB
AUTO_INCREMENT = 3801
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`tb_gabarito_questionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`tb_gabarito_questionario` (
  `cd_gabarito_questionario` INT(11) NOT NULL AUTO_INCREMENT,
  `cd_usuario` INT(11) NOT NULL,
  `nu_questionario` INT(11) NULL DEFAULT NULL,
  `res_questionario` VARCHAR(2) NULL DEFAULT NULL,
  `cd_avaliativo_academico` INT(11) NOT NULL,
  PRIMARY KEY (`cd_gabarito_questionario`),
  INDEX `fk_tb_gabarito_questionario_auth_user` (`cd_usuario` ASC),
  INDEX `fk_tb_periodo_avaliativo_tb_academico_tb_gabarito_questionario` (`cd_avaliativo_academico` ASC),
  CONSTRAINT `fk_tb_gabarito_questionario_auth_user`
    FOREIGN KEY (`cd_usuario`)
    REFERENCES `correcao_gabarito`.`auth_user` (`id`),
  CONSTRAINT `fk_tb_periodo_avaliativo_tb_academico_tb_gabarito_questionario`
    FOREIGN KEY (`cd_avaliativo_academico`)
    REFERENCES `correcao_gabarito`.`tb_periodo_avaliativo_has_tb_academico` (`cd_avaliativo_academico`))
ENGINE = InnoDB
AUTO_INCREMENT = 1474
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`tb_gabarito_resposta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`tb_gabarito_resposta` (
  `cd_gabarito_resposta` INT(11) NOT NULL AUTO_INCREMENT,
  `nu_questao` INT(11) NULL DEFAULT NULL,
  `res_questao` VARCHAR(1) NULL DEFAULT NULL,
  `cd_gabarito` INT(11) NOT NULL,
  PRIMARY KEY (`cd_gabarito_resposta`),
  INDEX `fk_tb_gabarito_resposta_tb_gabarito_idx` (`cd_gabarito` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 22
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`tb_periodo_avaliativo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`tb_periodo_avaliativo` (
  `cd_periodo_avaliativo` INT(11) NOT NULL AUTO_INCREMENT,
  `no_periodo_avaliativo` VARCHAR(45) NULL DEFAULT NULL,
  `bo_ativo` TINYINT(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cd_periodo_avaliativo`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `correcao_gabarito`.`tb_upload_gabarito`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `correcao_gabarito`.`tb_upload_gabarito` (
  `cd_arquivo` INT(11) NOT NULL AUTO_INCREMENT,
  `ds_arquivo` TEXT NULL DEFAULT NULL,
  `cd_avaliativo_academico` INT(11) NULL DEFAULT NULL,
  `nome` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`cd_arquivo`),
  INDEX `fk_tb_upload_gabarito_tb_periodo_avaliativo_has_tb_academic_idx` (`cd_avaliativo_academico` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 91
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
