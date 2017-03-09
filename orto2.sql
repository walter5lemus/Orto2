-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-03-2017 a las 17:18:04
-- Versión del servidor: 5.6.17-log
-- Versión de PHP: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `orto2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `analisisdenticionmixta_moyers_inferior`
--

CREATE TABLE IF NOT EXISTS `analisisdenticionmixta_moyers_inferior` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ed_izquierdo` double DEFAULT NULL,
  `ed_derecho` double DEFAULT NULL,
  `fichas_id` int(11),
  PRIMARY KEY (`id`),
  KEY `AnalisisDenticionMixta_moyers_inferior_020e3279` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `analisisdenticionmixta_moyers_inferior_ancho`
--

CREATE TABLE IF NOT EXISTS `analisisdenticionmixta_moyers_inferior_ancho` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ancho_mesiodistal` double DEFAULT NULL,
  `fichas_id` int(11),
  `posicion_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `posicion_id` (`posicion_id`),
  KEY `AnalisisDenticionMixta_moyers_inferior_ancho_020e3279` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `analisisdenticionmixta_moyers_superior`
--

CREATE TABLE IF NOT EXISTS `analisisdenticionmixta_moyers_superior` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ed_izquierdo` double DEFAULT NULL,
  `ed_derecho` double DEFAULT NULL,
  `fichas_id` int(11),
  PRIMARY KEY (`id`),
  KEY `AnalisisDenticionMixta_moyers_superior_020e3279` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `analisisdenticionmixta_moyers_superior_ancho`
--

CREATE TABLE IF NOT EXISTS `analisisdenticionmixta_moyers_superior_ancho` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ancho_mesiodistal` double DEFAULT NULL,
  `fichas_id` int(11),
  `posicion_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `posicion_id` (`posicion_id`),
  KEY `AnalisisDenticionMixta_moyers_superior_ancho_020e3279` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `analisisdenticionmixta_nance_general`
--

CREATE TABLE IF NOT EXISTS `analisisdenticionmixta_nance_general` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ed_maxi` double NOT NULL,
  `ed_mand` double NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `analisisdenticionmixta_nance_tablas`
--

CREATE TABLE IF NOT EXISTS `analisisdenticionmixta_nance_tablas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seleccion` tinyint(1) NOT NULL,
  `tabla` int(11) NOT NULL,
  `posicion` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `mdm` double DEFAULT NULL,
  `mprx` double DEFAULT NULL,
  `multiplicacion` double DEFAULT NULL,
  `mdrx` double DEFAULT NULL,
  `valor_x` double NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `AnalisisDenticionMixta_nance_tablas_020e3279` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `analisisdenticionmixta_pos`
--

CREATE TABLE IF NOT EXISTS `analisisdenticionmixta_pos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=5 ;

--
-- Volcado de datos para la tabla `analisisdenticionmixta_pos`
--

INSERT INTO `analisisdenticionmixta_pos` (`id`) VALUES
(1),
(2),
(3),
(4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `analisis_cefalometrico_analisis_cefalometrico`
--

CREATE TABLE IF NOT EXISTS `analisis_cefalometrico_analisis_cefalometrico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sna` double DEFAULT NULL,
  `snb` double DEFAULT NULL,
  `anb` double DEFAULT NULL,
  `convexidad` double DEFAULT NULL,
  `wits` double DEFAULT NULL,
  `long_cuerpo_mandibular` double DEFAULT NULL,
  `profundidad_maxilar` double DEFAULT NULL,
  `profundidad_facial` double DEFAULT NULL,
  `plano_mandibular` double DEFAULT NULL,
  `eje_y_fh` double DEFAULT NULL,
  `cono_facial` double DEFAULT NULL,
  `eje_facial` double DEFAULT NULL,
  `angulo_goniaco_superior` double DEFAULT NULL,
  `angulo_goniaco_inferior` double DEFAULT NULL,
  `angulo_goniaco_total` double DEFAULT NULL,
  `is_na` double DEFAULT NULL,
  `is_sn` double DEFAULT NULL,
  `isfh` double DEFAULT NULL,
  `impa` double DEFAULT NULL,
  `protusion_de_incisivo_max` double DEFAULT NULL,
  `protusion_de_incisivo_md` double DEFAULT NULL,
  `protusion_labial` double DEFAULT NULL,
  `fichas_id` int(11),
  `numero_de_examen_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_de_examen_id` (`numero_de_examen_id`),
  KEY `analisis_cefalometrico_analisis_cefalometrico_020e3279` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `analisis_cefalometrico_examen`
--

CREATE TABLE IF NOT EXISTS `analisis_cefalometrico_examen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `analisis_cefalometrico_examen`
--

INSERT INTO `analisis_cefalometrico_examen` (`id`) VALUES
(1),
(2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `analisis_radiograficos_aspectos_articulares`
--

CREATE TABLE IF NOT EXISTS `analisis_radiograficos_aspectos_articulares` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `condilo_mand_izq_alto` double NOT NULL,
  `condilo_mand_izq_ancho` double NOT NULL,
  `condilo_mand_der_alto` double NOT NULL,
  `condilo_mand_der_ancho` double NOT NULL,
  `condilo_mand_simetrico` int(11) NOT NULL,
  `condilo_mand_aspectos_observados` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `eminencia_izq` double NOT NULL,
  `eminencia_der` double NOT NULL,
  `eminencia_simetrico` int(11) NOT NULL,
  `eminencia_aspectos_observados` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `espacio_articular_simetrico` int(11) NOT NULL,
  `espacio_articular_aspectos_observados` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `analisis_radiograficos_aspectos_mandibulares2`
--

CREATE TABLE IF NOT EXISTS `analisis_radiograficos_aspectos_mandibulares2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aspectos_sinusales_simetrico` tinyint(1) NOT NULL,
  `aspectos_sinusales_izq_aspect_observ` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `aspectos_sinusales_der_aspect_observ` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `ord_ori_simetrico` tinyint(1) NOT NULL,
  `ord_ori_izq_aspect_observ` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `ord_ori_der_aspect_observ` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fpgd_fpgi_simetrico` tinyint(1) NOT NULL,
  `fpgd_fpgi_izq_aspect_observ` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fpgd_fpgi_der_aspect_observ` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `veloc_erup_simetrico` tinyint(1) NOT NULL,
  `veloc_erup_izq_aspect_observ` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `veloc_erup_der_aspect_observ` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `diagnostico` varchar(500) COLLATE utf8_spanish_ci NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `analisis_radiograficos_estadios_de_nolla`
--

CREATE TABLE IF NOT EXISTS `analisis_radiograficos_estadios_de_nolla` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `e_1_1` smallint(5) unsigned DEFAULT NULL,
  `e_1_2` smallint(5) unsigned DEFAULT NULL,
  `e_1_3` smallint(5) unsigned DEFAULT NULL,
  `e_1_4` smallint(5) unsigned DEFAULT NULL,
  `e_1_5` smallint(5) unsigned DEFAULT NULL,
  `e_1_6` smallint(5) unsigned DEFAULT NULL,
  `e_1_7` smallint(5) unsigned DEFAULT NULL,
  `e_1_8` smallint(5) unsigned DEFAULT NULL,
  `e_2_1` smallint(5) unsigned DEFAULT NULL,
  `e_2_2` smallint(5) unsigned DEFAULT NULL,
  `e_2_3` smallint(5) unsigned DEFAULT NULL,
  `e_2_4` smallint(5) unsigned DEFAULT NULL,
  `e_2_5` smallint(5) unsigned DEFAULT NULL,
  `e_2_6` smallint(5) unsigned DEFAULT NULL,
  `e_2_7` smallint(5) unsigned DEFAULT NULL,
  `e_2_8` smallint(5) unsigned DEFAULT NULL,
  `e_3_1` smallint(5) unsigned DEFAULT NULL,
  `e_3_2` smallint(5) unsigned DEFAULT NULL,
  `e_3_3` smallint(5) unsigned DEFAULT NULL,
  `e_3_4` smallint(5) unsigned DEFAULT NULL,
  `e_3_5` smallint(5) unsigned DEFAULT NULL,
  `e_3_6` smallint(5) unsigned DEFAULT NULL,
  `e_3_7` smallint(5) unsigned DEFAULT NULL,
  `e_3_8` smallint(5) unsigned DEFAULT NULL,
  `e_4_1` smallint(5) unsigned DEFAULT NULL,
  `e_4_2` smallint(5) unsigned DEFAULT NULL,
  `e_4_3` smallint(5) unsigned DEFAULT NULL,
  `e_4_4` smallint(5) unsigned DEFAULT NULL,
  `e_4_5` smallint(5) unsigned DEFAULT NULL,
  `e_4_6` smallint(5) unsigned DEFAULT NULL,
  `e_4_7` smallint(5) unsigned DEFAULT NULL,
  `e_4_8` smallint(5) unsigned DEFAULT NULL,
  `otros_hallazgos` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `analisis_radiograficos_secuencia_y_cronologia`
--

CREATE TABLE IF NOT EXISTS `analisis_radiograficos_secuencia_y_cronologia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `o_1_1` smallint(5) unsigned DEFAULT NULL,
  `o_1_2` smallint(5) unsigned DEFAULT NULL,
  `o_1_3` smallint(5) unsigned DEFAULT NULL,
  `o_1_4` smallint(5) unsigned DEFAULT NULL,
  `o_1_5` smallint(5) unsigned DEFAULT NULL,
  `o_1_6` smallint(5) unsigned DEFAULT NULL,
  `o_1_7` smallint(5) unsigned DEFAULT NULL,
  `o_1_8` smallint(5) unsigned DEFAULT NULL,
  `o_2_1` smallint(5) unsigned DEFAULT NULL,
  `o_2_2` smallint(5) unsigned DEFAULT NULL,
  `o_2_3` smallint(5) unsigned DEFAULT NULL,
  `o_2_4` smallint(5) unsigned DEFAULT NULL,
  `o_2_5` smallint(5) unsigned DEFAULT NULL,
  `o_2_6` smallint(5) unsigned DEFAULT NULL,
  `o_2_7` smallint(5) unsigned DEFAULT NULL,
  `o_2_8` smallint(5) unsigned DEFAULT NULL,
  `o_3_1` smallint(5) unsigned DEFAULT NULL,
  `o_3_2` smallint(5) unsigned DEFAULT NULL,
  `o_3_3` smallint(5) unsigned DEFAULT NULL,
  `o_3_4` smallint(5) unsigned DEFAULT NULL,
  `o_3_5` smallint(5) unsigned DEFAULT NULL,
  `o_3_6` smallint(5) unsigned DEFAULT NULL,
  `o_3_7` smallint(5) unsigned DEFAULT NULL,
  `o_3_8` smallint(5) unsigned DEFAULT NULL,
  `o_4_1` smallint(5) unsigned DEFAULT NULL,
  `o_4_2` smallint(5) unsigned DEFAULT NULL,
  `o_4_3` smallint(5) unsigned DEFAULT NULL,
  `o_4_4` smallint(5) unsigned DEFAULT NULL,
  `o_4_5` smallint(5) unsigned DEFAULT NULL,
  `o_4_6` smallint(5) unsigned DEFAULT NULL,
  `o_4_7` smallint(5) unsigned DEFAULT NULL,
  `o_4_8` smallint(5) unsigned DEFAULT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aspmandibular_aspectos_mandibulares1`
--

CREATE TABLE IF NOT EXISTS `aspmandibular_aspectos_mandibulares1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rama_mand_anch_izq_altura` int(11) NOT NULL,
  `rama_mand_anch_der_altura` int(11) NOT NULL,
  `rama_mand_anch_simetrico` int(11) NOT NULL,
  `rama_mand_anch_izq_aspect_observ` longtext COLLATE utf8_spanish_ci NOT NULL,
  `rama_mand_anch_der_aspect_observ` longtext COLLATE utf8_spanish_ci NOT NULL,
  `rama_mand_altur_izq_altura` int(11) NOT NULL,
  `rama_mand_altur_der_altura` int(11) NOT NULL,
  `rama_mand_altur_simetrico` int(11) NOT NULL,
  `rama_mand_altur_izq_aspect_observ` longtext COLLATE utf8_spanish_ci NOT NULL,
  `rama_mand_altur_der_aspect_observ` longtext COLLATE utf8_spanish_ci NOT NULL,
  `cuerpo_mand_altur_izq_altura` int(11) NOT NULL,
  `cuerpo_mand_altur_der_altura` int(11) NOT NULL,
  `cuerpo_mand_altur_simetrico` int(11) NOT NULL,
  `cuerpo_mand_altur_izq_aspect_observ` longtext COLLATE utf8_spanish_ci NOT NULL,
  `cuerpo_mand_altur_der_aspect_observ` longtext COLLATE utf8_spanish_ci NOT NULL,
  `cuerpo_mand_long_izq_altura` int(11) NOT NULL,
  `cuerpo_mand_long_der_altura` int(11) NOT NULL,
  `cuerpo_mand_long_simetrico` int(11) NOT NULL,
  `cuerpo_mand_long_izq_aspect_observ` longtext COLLATE utf8_spanish_ci NOT NULL,
  `cuerpo_mand_long_der_aspect_observ` longtext COLLATE utf8_spanish_ci NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=136 ;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add estado_general', 6, 'add_estado_general'),
(17, 'Can change estado_general', 6, 'change_estado_general'),
(18, 'Can delete estado_general', 6, 'delete_estado_general'),
(19, 'Can add user', 7, 'add_usuario'),
(20, 'Can change user', 7, 'change_usuario'),
(21, 'Can delete user', 7, 'delete_usuario'),
(22, 'Can add codigo_expediente', 8, 'add_codigo_expediente'),
(23, 'Can change codigo_expediente', 8, 'change_codigo_expediente'),
(24, 'Can delete codigo_expediente', 8, 'delete_codigo_expediente'),
(25, 'Can add motivo_consulta', 9, 'add_motivo_consulta'),
(26, 'Can change motivo_consulta', 9, 'change_motivo_consulta'),
(27, 'Can delete motivo_consulta', 9, 'delete_motivo_consulta'),
(28, 'Can add catalogo_enfermedades', 10, 'add_catalogo_enfermedades'),
(29, 'Can change catalogo_enfermedades', 10, 'change_catalogo_enfermedades'),
(30, 'Can delete catalogo_enfermedades', 10, 'delete_catalogo_enfermedades'),
(31, 'Can add fichas', 11, 'add_fichas'),
(32, 'Can change fichas', 11, 'change_fichas'),
(33, 'Can delete fichas', 11, 'delete_fichas'),
(34, 'Can add datos_generales', 12, 'add_datos_generales'),
(35, 'Can change datos_generales', 12, 'change_datos_generales'),
(36, 'Can delete datos_generales', 12, 'delete_datos_generales'),
(37, 'Can add registro', 13, 'add_registro'),
(38, 'Can change registro', 13, 'change_registro'),
(39, 'Can delete registro', 13, 'delete_registro'),
(40, 'Can add imagenes_afmp', 14, 'add_imagenes_afmp'),
(41, 'Can change imagenes_afmp', 14, 'change_imagenes_afmp'),
(42, 'Can delete imagenes_afmp', 14, 'delete_imagenes_afmp'),
(43, 'Can add funcion_mandibular', 15, 'add_funcion_mandibular'),
(44, 'Can change funcion_mandibular', 15, 'change_funcion_mandibular'),
(45, 'Can delete funcion_mandibular', 15, 'delete_funcion_mandibular'),
(46, 'Can add denticion', 16, 'add_denticion'),
(47, 'Can change denticion', 16, 'change_denticion'),
(48, 'Can delete denticion', 16, 'delete_denticion'),
(49, 'Can add problema', 17, 'add_problema'),
(50, 'Can change problema', 17, 'change_problema'),
(51, 'Can delete problema', 17, 'delete_problema'),
(52, 'Can add sobremordidas', 18, 'add_sobremordidas'),
(53, 'Can change sobremordidas', 18, 'change_sobremordidas'),
(54, 'Can delete sobremordidas', 18, 'delete_sobremordidas'),
(55, 'Can add tipo', 19, 'add_tipo'),
(56, 'Can change tipo', 19, 'change_tipo'),
(57, 'Can delete tipo', 19, 'delete_tipo'),
(58, 'Can add linea_media_facial', 20, 'add_linea_media_facial'),
(59, 'Can change linea_media_facial', 20, 'change_linea_media_facial'),
(60, 'Can delete linea_media_facial', 20, 'delete_linea_media_facial'),
(61, 'Can add registro_mordidas', 21, 'add_registro_mordidas'),
(62, 'Can change registro_mordidas', 21, 'change_registro_mordidas'),
(63, 'Can delete registro_mordidas', 21, 'delete_registro_mordidas'),
(64, 'Can add relaciones_sagitales', 22, 'add_relaciones_sagitales'),
(65, 'Can change relaciones_sagitales', 22, 'change_relaciones_sagitales'),
(66, 'Can delete relaciones_sagitales', 22, 'delete_relaciones_sagitales'),
(67, 'Can add tipo perfil', 23, 'add_tipoperfil'),
(68, 'Can change tipo perfil', 23, 'change_tipoperfil'),
(69, 'Can delete tipo perfil', 23, 'delete_tipoperfil'),
(70, 'Can add estadios_de_nolla', 24, 'add_estadios_de_nolla'),
(71, 'Can change estadios_de_nolla', 24, 'change_estadios_de_nolla'),
(72, 'Can delete estadios_de_nolla', 24, 'delete_estadios_de_nolla'),
(73, 'Can add secuencia_y_cronologia', 25, 'add_secuencia_y_cronologia'),
(74, 'Can change secuencia_y_cronologia', 25, 'change_secuencia_y_cronologia'),
(75, 'Can delete secuencia_y_cronologia', 25, 'delete_secuencia_y_cronologia'),
(76, 'Can add aspectos_mandibulares2', 26, 'add_aspectos_mandibulares2'),
(77, 'Can change aspectos_mandibulares2', 26, 'change_aspectos_mandibulares2'),
(78, 'Can delete aspectos_mandibulares2', 26, 'delete_aspectos_mandibulares2'),
(79, 'Can add aspectos_articulares', 27, 'add_aspectos_articulares'),
(80, 'Can change aspectos_articulares', 27, 'change_aspectos_articulares'),
(81, 'Can delete aspectos_articulares', 27, 'delete_aspectos_articulares'),
(82, 'Can add citas_general', 28, 'add_citas_general'),
(83, 'Can change citas_general', 28, 'change_citas_general'),
(84, 'Can delete citas_general', 28, 'delete_citas_general'),
(85, 'Can add citas', 29, 'add_citas'),
(86, 'Can change citas', 29, 'change_citas'),
(87, 'Can delete citas', 29, 'delete_citas'),
(88, 'Can add patron', 30, 'add_patron'),
(89, 'Can change patron', 30, 'change_patron'),
(90, 'Can delete patron', 30, 'delete_patron'),
(91, 'Can add diagnostico_cefalometrico', 31, 'add_diagnostico_cefalometrico'),
(92, 'Can change diagnostico_cefalometrico', 31, 'change_diagnostico_cefalometrico'),
(93, 'Can delete diagnostico_cefalometrico', 31, 'delete_diagnostico_cefalometrico'),
(94, 'Can add m dentales', 32, 'add_mdentales'),
(95, 'Can change m dentales', 32, 'change_mdentales'),
(96, 'Can delete m dentales', 32, 'delete_mdentales'),
(97, 'Can add crecimiento', 33, 'add_crecimiento'),
(98, 'Can change crecimiento', 33, 'change_crecimiento'),
(99, 'Can delete crecimiento', 33, 'delete_crecimiento'),
(100, 'Can add diagnostico_general', 34, 'add_diagnostico_general'),
(101, 'Can change diagnostico_general', 34, 'change_diagnostico_general'),
(102, 'Can delete diagnostico_general', 34, 'delete_diagnostico_general'),
(103, 'Can add aspectos_mandibulares1', 35, 'add_aspectos_mandibulares1'),
(104, 'Can change aspectos_mandibulares1', 35, 'change_aspectos_mandibulares1'),
(105, 'Can delete aspectos_mandibulares1', 35, 'delete_aspectos_mandibulares1'),
(106, 'Can add reportes', 36, 'add_reportes'),
(107, 'Can change reportes', 36, 'change_reportes'),
(108, 'Can delete reportes', 36, 'delete_reportes'),
(109, 'Can add examen', 37, 'add_examen'),
(110, 'Can change examen', 37, 'change_examen'),
(111, 'Can delete examen', 37, 'delete_examen'),
(112, 'Can add analisis_cefalometrico', 38, 'add_analisis_cefalometrico'),
(113, 'Can change analisis_cefalometrico', 38, 'change_analisis_cefalometrico'),
(114, 'Can delete analisis_cefalometrico', 38, 'delete_analisis_cefalometrico'),
(115, 'Can add moyers_inferior', 39, 'add_moyers_inferior'),
(116, 'Can change moyers_inferior', 39, 'change_moyers_inferior'),
(117, 'Can delete moyers_inferior', 39, 'delete_moyers_inferior'),
(118, 'Can add moyers_inferior_ancho', 40, 'add_moyers_inferior_ancho'),
(119, 'Can change moyers_inferior_ancho', 40, 'change_moyers_inferior_ancho'),
(120, 'Can delete moyers_inferior_ancho', 40, 'delete_moyers_inferior_ancho'),
(121, 'Can add nance_tablas', 41, 'add_nance_tablas'),
(122, 'Can change nance_tablas', 41, 'change_nance_tablas'),
(123, 'Can delete nance_tablas', 41, 'delete_nance_tablas'),
(124, 'Can add moyers_superior_ancho', 42, 'add_moyers_superior_ancho'),
(125, 'Can change moyers_superior_ancho', 42, 'change_moyers_superior_ancho'),
(126, 'Can delete moyers_superior_ancho', 42, 'delete_moyers_superior_ancho'),
(127, 'Can add nance_general', 43, 'add_nance_general'),
(128, 'Can change nance_general', 43, 'change_nance_general'),
(129, 'Can delete nance_general', 43, 'delete_nance_general'),
(130, 'Can add pos', 44, 'add_pos'),
(131, 'Can change pos', 44, 'change_pos'),
(132, 'Can delete pos', 44, 'delete_pos'),
(133, 'Can add moyers_superior', 45, 'add_moyers_superior'),
(134, 'Can change moyers_superior', 45, 'change_moyers_superior'),
(135, 'Can delete moyers_superior', 45, 'delete_moyers_superior');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citas_citas`
--

CREATE TABLE IF NOT EXISTS `citas_citas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num_cita` int(11) NOT NULL,
  `fecha_cita` date NOT NULL,
  `observaciones` varchar(250) COLLATE utf8_spanish_ci NOT NULL,
  `proxima_cita` date NOT NULL,
  `resultados` varchar(250) COLLATE utf8_spanish_ci NOT NULL,
  `autorizacion` tinyint(1) NOT NULL,
  `tutor` varchar(75) COLLATE utf8_spanish_ci DEFAULT NULL,
  `codigo_id` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `citas_citas_8a9a42fb` (`codigo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citas_citas_general`
--

CREATE TABLE IF NOT EXISTS `citas_citas_general` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aparato` int(11) NOT NULL,
  `mx` tinyint(1) NOT NULL,
  `md` tinyint(1) NOT NULL,
  `codigo_id` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `estudiante_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `citas_citas_general_8a9a42fb` (`codigo_id`),
  KEY `citas_citas_general_133716be` (`estudiante_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denticion_denticion`
--

CREATE TABLE IF NOT EXISTS `denticion_denticion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `diastemas` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `mal_posiciones` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `supernumerarios` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `tejido_intraorales` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `encias` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `frenillos` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `lengua` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `observaciones_generales` varchar(384) COLLATE utf8_spanish_ci NOT NULL,
  `fichas_id` int(11) NOT NULL,
  `tipo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`),
  UNIQUE KEY `tipo_id` (`tipo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denticion_funcion_mandibular`
--

CREATE TABLE IF NOT EXISTS `denticion_funcion_mandibular` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `apertura` int(11) NOT NULL,
  `desv_afmp_derecho` int(11) NOT NULL,
  `desv_afmp_izquierdo` int(11) NOT NULL,
  `signos_sintomas_atm` longtext COLLATE utf8_spanish_ci NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denticion_imagenes_afmp`
--

CREATE TABLE IF NOT EXISTS `denticion_imagenes_afmp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombreimagen` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `imagen` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denticion_linea_media_facial`
--

CREATE TABLE IF NOT EXISTS `denticion_linea_media_facial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mx` int(11) NOT NULL,
  `mx_desviacion` int(11) NOT NULL,
  `md` int(11) NOT NULL,
  `md_desviacion` int(11) NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denticion_problema`
--

CREATE TABLE IF NOT EXISTS `denticion_problema` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_problemas` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=4 ;

--
-- Volcado de datos para la tabla `denticion_problema`
--

INSERT INTO `denticion_problema` (`id`, `nombre_problemas`) VALUES
(1, 'Pérdidas prematuras'),
(2, 'Anodoncias'),
(3, 'Mordida telescópica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denticion_registro`
--

CREATE TABLE IF NOT EXISTS `denticion_registro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cuadrante` int(11) DEFAULT NULL,
  `pieza` int(11) DEFAULT NULL,
  `detalle` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fichas_id` int(11) NOT NULL,
  `problema_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `denticion_registro_020e3279` (`fichas_id`),
  KEY `denticion_registro_eb9e624a` (`problema_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denticion_registro_mordidas`
--

CREATE TABLE IF NOT EXISTS `denticion_registro_mordidas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cuad_superior` int(11) NOT NULL,
  `pieza_superior` int(11) NOT NULL,
  `cuad_inferior` int(11) NOT NULL,
  `pieza_inferior` int(11) NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `denticion_registro_mordidas_020e3279` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denticion_relaciones_sagitales`
--

CREATE TABLE IF NOT EXISTS `denticion_relaciones_sagitales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `molar_derecha` int(11) NOT NULL,
  `molar_izquierda` int(11) NOT NULL,
  `canina_derecha` int(11) NOT NULL,
  `canina_izquierda` int(11) NOT NULL,
  `plano_termina_recto` int(11) NOT NULL,
  `escalon_mesial` int(11) NOT NULL,
  `escalon_distal` int(11) NOT NULL,
  `observaciones` longtext COLLATE utf8_spanish_ci NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denticion_sobremordidas`
--

CREATE TABLE IF NOT EXISTS `denticion_sobremordidas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `horizontal` int(11) NOT NULL,
  `vertical` int(11) NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denticion_tipo`
--

CREATE TABLE IF NOT EXISTS `denticion_tipo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=4 ;

--
-- Volcado de datos para la tabla `denticion_tipo`
--

INSERT INTO `denticion_tipo` (`id`, `nombre`) VALUES
(1, 'Temporario'),
(2, 'Mixto'),
(3, 'Permanente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diagcefalo_crecimiento`
--

CREATE TABLE IF NOT EXISTS `diagcefalo_crecimiento` (
  `id_Crecimiento` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `tipo_de_crecimiento` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id_Crecimiento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `diagcefalo_crecimiento`
--

INSERT INTO `diagcefalo_crecimiento` (`id_Crecimiento`, `tipo_de_crecimiento`) VALUES
('1', 'Neutro'),
('2', 'Vertical'),
('3', 'Horizontal');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diagcefalo_diagnostico_cefalometrico`
--

CREATE TABLE IF NOT EXISTS `diagcefalo_diagnostico_cefalometrico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `otro_patron` longtext COLLATE utf8_spanish_ci NOT NULL,
  `medidas_esteticas` longtext COLLATE utf8_spanish_ci NOT NULL,
  `fichas_id` int(11) NOT NULL,
  `medidas_dentales_id` varchar(10) COLLATE utf8_spanish_ci,
  `patron_esqueletal_id` varchar(10) COLLATE utf8_spanish_ci,
  `tipo_de_crecimiento_id` varchar(10) COLLATE utf8_spanish_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`),
  KEY `diagCefalo_diagnostico_cefalometrico_9811a4f3` (`medidas_dentales_id`),
  KEY `diagCefalo_diagnostico_cefalometrico_44082f30` (`patron_esqueletal_id`),
  KEY `diagCefalo_diagnostico_cefalometrico_535ea7af` (`tipo_de_crecimiento_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diagcefalo_mdentales`
--

CREATE TABLE IF NOT EXISTS `diagcefalo_mdentales` (
  `id_MDentales` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `medidas_dentales` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id_MDentales`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `diagcefalo_mdentales`
--

INSERT INTO `diagcefalo_mdentales` (`id_MDentales`, `medidas_dentales`) VALUES
('1', 'Retro inclinado'),
('2', 'Pro inclinación'),
('3', 'Normo inclinacion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diagcefalo_patron`
--

CREATE TABLE IF NOT EXISTS `diagcefalo_patron` (
  `id_Patron` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `patron_esqueletal` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id_Patron`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `diagcefalo_patron`
--

INSERT INTO `diagcefalo_patron` (`id_Patron`, `patron_esqueletal`) VALUES
('1', 'Clase 1'),
('2', 'Clase 2'),
('3', 'Clase 3');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diaggeneral_diagnostico_general`
--

CREATE TABLE IF NOT EXISTS `diaggeneral_diagnostico_general` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `diagnostico_ortodontico_general` longtext COLLATE utf8_spanish_ci NOT NULL,
  `problemas` longtext COLLATE utf8_spanish_ci NOT NULL,
  `objetivos` longtext COLLATE utf8_spanish_ci NOT NULL,
  `tratamiento` int(11) NOT NULL,
  `descripcion_tratamiento` longtext COLLATE utf8_spanish_ci NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext COLLATE utf8_spanish_ci,
  `object_repr` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_spanish_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_informacion_usuario_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=46 ;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(38, 'analisis_cefalometrico', 'analisis_cefalometrico'),
(37, 'analisis_cefalometrico', 'examen'),
(27, 'analisis_radiograficos', 'aspectos_articulares'),
(26, 'analisis_radiograficos', 'aspectos_mandibulares2'),
(24, 'analisis_radiograficos', 'estadios_de_nolla'),
(25, 'analisis_radiograficos', 'secuencia_y_cronologia'),
(39, 'AnalisisDenticionMixta', 'moyers_inferior'),
(40, 'AnalisisDenticionMixta', 'moyers_inferior_ancho'),
(45, 'AnalisisDenticionMixta', 'moyers_superior'),
(42, 'AnalisisDenticionMixta', 'moyers_superior_ancho'),
(43, 'AnalisisDenticionMixta', 'nance_general'),
(41, 'AnalisisDenticionMixta', 'nance_tablas'),
(44, 'AnalisisDenticionMixta', 'pos'),
(35, 'aspMandibular', 'aspectos_mandibulares1'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(29, 'citas', 'citas'),
(28, 'citas', 'citas_general'),
(4, 'contenttypes', 'contenttype'),
(16, 'denticion', 'denticion'),
(15, 'denticion', 'funcion_mandibular'),
(14, 'denticion', 'imagenes_afmp'),
(20, 'denticion', 'linea_media_facial'),
(17, 'denticion', 'problema'),
(13, 'denticion', 'registro'),
(21, 'denticion', 'registro_mordidas'),
(22, 'denticion', 'relaciones_sagitales'),
(18, 'denticion', 'sobremordidas'),
(19, 'denticion', 'tipo'),
(33, 'diagCefalo', 'crecimiento'),
(31, 'diagCefalo', 'diagnostico_cefalometrico'),
(32, 'diagCefalo', 'mdentales'),
(30, 'diagCefalo', 'patron'),
(34, 'diagGeneral', 'diagnostico_general'),
(10, 'informacion', 'catalogo_enfermedades'),
(8, 'informacion', 'codigo_expediente'),
(12, 'informacion', 'datos_generales'),
(6, 'informacion', 'estado_general'),
(11, 'informacion', 'fichas'),
(9, 'informacion', 'motivo_consulta'),
(7, 'informacion', 'usuario'),
(36, 'reportes', 'reportes'),
(5, 'sessions', 'session'),
(23, 'tipo_perfil', 'tipoperfil');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=33 ;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2017-03-09 16:10:32'),
(2, 'contenttypes', '0002_remove_content_type_name', '2017-03-09 16:10:33'),
(3, 'auth', '0001_initial', '2017-03-09 16:10:37'),
(4, 'auth', '0002_alter_permission_name_max_length', '2017-03-09 16:10:37'),
(5, 'auth', '0003_alter_user_email_max_length', '2017-03-09 16:10:37'),
(6, 'auth', '0004_alter_user_username_opts', '2017-03-09 16:10:37'),
(7, 'auth', '0005_alter_user_last_login_null', '2017-03-09 16:10:37'),
(8, 'auth', '0006_require_contenttypes_0002', '2017-03-09 16:10:37'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2017-03-09 16:10:37'),
(10, 'auth', '0008_alter_user_username_max_length', '2017-03-09 16:10:38'),
(11, 'informacion', '0001_initial', '2017-03-09 16:10:50'),
(12, 'AnalisisDenticionMixta', '0001_initial', '2017-03-09 16:10:52'),
(13, 'AnalisisDenticionMixta', '0002_auto_20170309_1010', '2017-03-09 16:11:02'),
(14, 'admin', '0001_initial', '2017-03-09 16:11:04'),
(15, 'admin', '0002_logentry_remove_auto_add', '2017-03-09 16:11:04'),
(16, 'analisis_cefalometrico', '0001_initial', '2017-03-09 16:11:05'),
(17, 'analisis_cefalometrico', '0002_auto_20170309_1010', '2017-03-09 16:11:07'),
(18, 'analisis_radiograficos', '0001_initial', '2017-03-09 16:11:09'),
(19, 'analisis_radiograficos', '0002_auto_20170309_1010', '2017-03-09 16:11:14'),
(20, 'aspMandibular', '0001_initial', '2017-03-09 16:11:14'),
(21, 'aspMandibular', '0002_aspectos_mandibulares1_fichas', '2017-03-09 16:11:15'),
(22, 'citas', '0001_initial', '2017-03-09 16:11:16'),
(23, 'citas', '0002_auto_20170309_1010', '2017-03-09 16:11:20'),
(24, 'denticion', '0001_initial', '2017-03-09 16:11:23'),
(25, 'denticion', '0002_auto_20170309_1010', '2017-03-09 16:11:38'),
(26, 'diagCefalo', '0001_initial', '2017-03-09 16:11:39'),
(27, 'diagCefalo', '0002_auto_20170309_1010', '2017-03-09 16:11:46'),
(28, 'diagGeneral', '0001_initial', '2017-03-09 16:11:46'),
(29, 'diagGeneral', '0002_diagnostico_general_fichas', '2017-03-09 16:11:48'),
(30, 'reportes', '0001_initial', '2017-03-09 16:11:49'),
(31, 'sessions', '0001_initial', '2017-03-09 16:11:50'),
(32, 'tipo_perfil', '0001_initial', '2017-03-09 16:11:51');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `session_data` longtext COLLATE utf8_spanish_ci NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informacion_catalogo_enfermedades`
--

CREATE TABLE IF NOT EXISTS `informacion_catalogo_enfermedades` (
  `id_enfermedad` int(11) NOT NULL,
  `nombre_enfermedad` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id_enfermedad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `informacion_catalogo_enfermedades`
--

INSERT INTO `informacion_catalogo_enfermedades` (`id_enfermedad`, `nombre_enfermedad`) VALUES
(1, 'Alergias'),
(2, 'Desmayos'),
(3, 'Presión sanguinea alta'),
(4, 'Sinusitis'),
(5, 'Hepatitis'),
(6, 'Transtornos de la sangre'),
(7, 'Asma'),
(8, 'Artritis'),
(9, 'Enfermedades venéreas'),
(10, 'Diabetes'),
(11, 'Gastritis'),
(12, 'SIDA'),
(13, 'Transtornos renales'),
(14, 'Tuberculosis');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informacion_codigo_expediente`
--

CREATE TABLE IF NOT EXISTS `informacion_codigo_expediente` (
  `codigo` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informacion_datos_generales`
--

CREATE TABLE IF NOT EXISTS `informacion_datos_generales` (
  `cod_expediente` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `nombre_completo` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `edad` int(11) NOT NULL,
  `edad_registro` int(11) NOT NULL,
  `fecha_nac` date NOT NULL,
  `telefono` int(11) NOT NULL,
  `genero` int(11) NOT NULL,
  `direccion` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `nombre_resp` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_hora_creacion` datetime NOT NULL,
  `usuario_creador_id` int(11) NOT NULL,
  PRIMARY KEY (`cod_expediente`),
  KEY `informacio_usuario_creador_id_d26f1468_fk_informacion_usuario_id` (`usuario_creador_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informacion_estado_general`
--

CREATE TABLE IF NOT EXISTS `informacion_estado_general` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cambio_salud` tinyint(1) NOT NULL,
  `detalle_enf_operacion` varchar(500) COLLATE utf8_spanish_ci DEFAULT NULL,
  `detalle_medicamento` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `detalle_otra_enfermedad` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informacion_estado_general_otras_enfermedades`
--

CREATE TABLE IF NOT EXISTS `informacion_estado_general_otras_enfermedades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado_general_id` int(11) NOT NULL,
  `catalogo_enfermedades_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `informacion_estado_general_otras_estado_general_id_7b21fb26_uniq` (`estado_general_id`,`catalogo_enfermedades_id`),
  KEY `e4acb1f2aede12649dff9a8de8670719` (`catalogo_enfermedades_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informacion_fichas`
--

CREATE TABLE IF NOT EXISTS `informacion_fichas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero` int(11) NOT NULL,
  `cod_expediente_id` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `informacion_fichas_cod_expediente_id_a54f1db6_uniq` (`cod_expediente_id`,`numero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informacion_motivo_consulta`
--

CREATE TABLE IF NOT EXISTS `informacion_motivo_consulta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `motivo_consulta` varchar(500) COLLATE utf8_spanish_ci NOT NULL,
  `fechaRegistro` date NOT NULL,
  `fecha_hora_creacion` datetime NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informacion_usuario`
--

CREATE TABLE IF NOT EXISTS `informacion_usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_spanish_ci NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_spanish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `dui` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `carnet` varchar(7) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=2 ;

--
-- Volcado de datos para la tabla `informacion_usuario`
--

INSERT INTO `informacion_usuario` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `dui`, `carnet`) VALUES
(1, 'pbkdf2_sha256$30000$3K5U4fRt4EFg$HLdZE4dDwcQ9xfwaZAJHkAaQTbTuT7pWoESRKUDGxCg=', NULL, 1, 'GerardoRodas', '', '', 'edge.world3@gmail.com', 1, 1, '2017-03-09 16:12:34', '', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informacion_usuario_groups`
--

CREATE TABLE IF NOT EXISTS `informacion_usuario_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `informacion_usuario_groups_usuario_id_21d52c6d_uniq` (`usuario_id`,`group_id`),
  KEY `informacion_usuario_groups_group_id_3d98422e_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informacion_usuario_user_permissions`
--

CREATE TABLE IF NOT EXISTS `informacion_usuario_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `informacion_usuario_user_permissions_usuario_id_b5f099f0_uniq` (`usuario_id`,`permission_id`),
  KEY `informacion_usuario_permission_id_3a5f9db7_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reportes_reportes`
--

CREATE TABLE IF NOT EXISTS `reportes_reportes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(7) COLLATE utf8_spanish_ci NOT NULL,
  `numero` int(11) NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_perfil_tipoperfil`
--

CREATE TABLE IF NOT EXISTS `tipo_perfil_tipoperfil` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `frontal_facial` int(11) NOT NULL,
  `tipoPerfiltotal` int(11) NOT NULL,
  `perfilTercio_inferior` int(11) NOT NULL,
  `tipoSonrisa` int(11) NOT NULL,
  `tipo_competenciaLabial` int(11) NOT NULL,
  `grosorLabios` int(11) NOT NULL,
  `tamanoLabios` int(11) NOT NULL,
  `tipoNariz` int(11) NOT NULL,
  `angulo_Naso_labial` int(11) NOT NULL,
  `tercio_superior` int(11) NOT NULL,
  `tercio_medio` int(11) NOT NULL,
  `tercio_inferior` int(11) NOT NULL,
  `tamanoSonrisa` int(11) NOT NULL,
  `fichas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fichas_id` (`fichas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `analisisdenticionmixta_moyers_inferior`
--
ALTER TABLE `analisisdenticionmixta_moyers_inferior`
  ADD CONSTRAINT `AnalisisDenticionMix_fichas_id_8f0f9d53_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `analisisdenticionmixta_moyers_inferior_ancho`
--
ALTER TABLE `analisisdenticionmixta_moyers_inferior_ancho`
  ADD CONSTRAINT `AnalisisDe_posicion_id_b08659a4_fk_AnalisisDenticionMixta_pos_id` FOREIGN KEY (`posicion_id`) REFERENCES `analisisdenticionmixta_pos` (`id`),
  ADD CONSTRAINT `AnalisisDenticionMix_fichas_id_50f674e5_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `analisisdenticionmixta_moyers_superior`
--
ALTER TABLE `analisisdenticionmixta_moyers_superior`
  ADD CONSTRAINT `AnalisisDenticionMix_fichas_id_8c4bb9c1_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `analisisdenticionmixta_moyers_superior_ancho`
--
ALTER TABLE `analisisdenticionmixta_moyers_superior_ancho`
  ADD CONSTRAINT `AnalisisDe_posicion_id_146a23b2_fk_AnalisisDenticionMixta_pos_id` FOREIGN KEY (`posicion_id`) REFERENCES `analisisdenticionmixta_pos` (`id`),
  ADD CONSTRAINT `AnalisisDenticionMix_fichas_id_4b9323ee_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `analisisdenticionmixta_nance_general`
--
ALTER TABLE `analisisdenticionmixta_nance_general`
  ADD CONSTRAINT `AnalisisDenticionMix_fichas_id_ad4f5ba9_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `analisisdenticionmixta_nance_tablas`
--
ALTER TABLE `analisisdenticionmixta_nance_tablas`
  ADD CONSTRAINT `AnalisisDenticionMix_fichas_id_1479984d_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `analisis_cefalometrico_analisis_cefalometrico`
--
ALTER TABLE `analisis_cefalometrico_analisis_cefalometrico`
  ADD CONSTRAINT `D1afe0b866fb82ee38a53796438abfe0` FOREIGN KEY (`numero_de_examen_id`) REFERENCES `analisis_cefalometrico_examen` (`id`),
  ADD CONSTRAINT `analisis_cefalometri_fichas_id_443a1746_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `analisis_radiograficos_aspectos_articulares`
--
ALTER TABLE `analisis_radiograficos_aspectos_articulares`
  ADD CONSTRAINT `analisis_radiografic_fichas_id_b5f0a9fb_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `analisis_radiograficos_aspectos_mandibulares2`
--
ALTER TABLE `analisis_radiograficos_aspectos_mandibulares2`
  ADD CONSTRAINT `analisis_radiografic_fichas_id_ec9ae7f9_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `analisis_radiograficos_estadios_de_nolla`
--
ALTER TABLE `analisis_radiograficos_estadios_de_nolla`
  ADD CONSTRAINT `analisis_radiografic_fichas_id_850aec1d_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `analisis_radiograficos_secuencia_y_cronologia`
--
ALTER TABLE `analisis_radiograficos_secuencia_y_cronologia`
  ADD CONSTRAINT `analisis_radiografic_fichas_id_ec88fd62_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `aspmandibular_aspectos_mandibulares1`
--
ALTER TABLE `aspmandibular_aspectos_mandibulares1`
  ADD CONSTRAINT `aspMandibular_aspect_fichas_id_79bf2c74_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `citas_citas`
--
ALTER TABLE `citas_citas`
  ADD CONSTRAINT `citas_codigo_id_792f25ab_fk_informacion_codigo_expediente_codigo` FOREIGN KEY (`codigo_id`) REFERENCES `informacion_codigo_expediente` (`codigo`);

--
-- Filtros para la tabla `citas_citas_general`
--
ALTER TABLE `citas_citas_general`
  ADD CONSTRAINT `citas_citas_gen_estudiante_id_633da5ea_fk_informacion_usuario_id` FOREIGN KEY (`estudiante_id`) REFERENCES `informacion_usuario` (`id`),
  ADD CONSTRAINT `citas_codigo_id_78c3c47d_fk_informacion_codigo_expediente_codigo` FOREIGN KEY (`codigo_id`) REFERENCES `informacion_codigo_expediente` (`codigo`);

--
-- Filtros para la tabla `denticion_denticion`
--
ALTER TABLE `denticion_denticion`
  ADD CONSTRAINT `denticion_denticion_tipo_id_3b157183_fk_denticion_tipo_id` FOREIGN KEY (`tipo_id`) REFERENCES `denticion_tipo` (`id`),
  ADD CONSTRAINT `denticion_denticion_fichas_id_b27803f8_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `denticion_funcion_mandibular`
--
ALTER TABLE `denticion_funcion_mandibular`
  ADD CONSTRAINT `denticion_funcion_ma_fichas_id_98ab063e_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `denticion_imagenes_afmp`
--
ALTER TABLE `denticion_imagenes_afmp`
  ADD CONSTRAINT `denticion_imagenes_a_fichas_id_d548e463_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `denticion_linea_media_facial`
--
ALTER TABLE `denticion_linea_media_facial`
  ADD CONSTRAINT `denticion_linea_medi_fichas_id_fc1a5f9f_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `denticion_registro`
--
ALTER TABLE `denticion_registro`
  ADD CONSTRAINT `denticion_registro_problema_id_919df78e_fk_denticion_problema_id` FOREIGN KEY (`problema_id`) REFERENCES `denticion_problema` (`id`),
  ADD CONSTRAINT `denticion_registro_fichas_id_eb4c15f2_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `denticion_registro_mordidas`
--
ALTER TABLE `denticion_registro_mordidas`
  ADD CONSTRAINT `denticion_registro_m_fichas_id_d5c640d4_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `denticion_relaciones_sagitales`
--
ALTER TABLE `denticion_relaciones_sagitales`
  ADD CONSTRAINT `denticion_relaciones_fichas_id_dcd687a6_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `denticion_sobremordidas`
--
ALTER TABLE `denticion_sobremordidas`
  ADD CONSTRAINT `denticion_sobremordi_fichas_id_cc447702_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `diagcefalo_diagnostico_cefalometrico`
--
ALTER TABLE `diagcefalo_diagnostico_cefalometrico`
  ADD CONSTRAINT `D779454e12a1b904308899525ea4684c` FOREIGN KEY (`tipo_de_crecimiento_id`) REFERENCES `diagcefalo_crecimiento` (`id_Crecimiento`),
  ADD CONSTRAINT `a83526ffbd2d804752d727dedd975415` FOREIGN KEY (`medidas_dentales_id`) REFERENCES `diagcefalo_mdentales` (`id_MDentales`),
  ADD CONSTRAINT `diagCefalo_diagnosti_fichas_id_36e3471f_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`),
  ADD CONSTRAINT `dia_patron_esqueletal_id_36cd0430_fk_diagCefalo_patron_id_Patron` FOREIGN KEY (`patron_esqueletal_id`) REFERENCES `diagcefalo_patron` (`id_Patron`);

--
-- Filtros para la tabla `diaggeneral_diagnostico_general`
--
ALTER TABLE `diaggeneral_diagnostico_general`
  ADD CONSTRAINT `diagGeneral_diagnost_fichas_id_ed35cb3a_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_informacion_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `informacion_usuario` (`id`),
  ADD CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `informacion_datos_generales`
--
ALTER TABLE `informacion_datos_generales`
  ADD CONSTRAINT `informacio_usuario_creador_id_d26f1468_fk_informacion_usuario_id` FOREIGN KEY (`usuario_creador_id`) REFERENCES `informacion_usuario` (`id`);

--
-- Filtros para la tabla `informacion_estado_general`
--
ALTER TABLE `informacion_estado_general`
  ADD CONSTRAINT `informacion_estado_g_fichas_id_d2b6b55c_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `informacion_estado_general_otras_enfermedades`
--
ALTER TABLE `informacion_estado_general_otras_enfermedades`
  ADD CONSTRAINT `e4acb1f2aede12649dff9a8de8670719` FOREIGN KEY (`catalogo_enfermedades_id`) REFERENCES `informacion_catalogo_enfermedades` (`id_enfermedad`),
  ADD CONSTRAINT `info_estado_general_id_33c01a2c_fk_informacion_estado_general_id` FOREIGN KEY (`estado_general_id`) REFERENCES `informacion_estado_general` (`id`);

--
-- Filtros para la tabla `informacion_fichas`
--
ALTER TABLE `informacion_fichas`
  ADD CONSTRAINT `b5a25d573a482c8ea5e754eff61fdf4f` FOREIGN KEY (`cod_expediente_id`) REFERENCES `informacion_datos_generales` (`cod_expediente`);

--
-- Filtros para la tabla `informacion_motivo_consulta`
--
ALTER TABLE `informacion_motivo_consulta`
  ADD CONSTRAINT `informacion_motivo_c_fichas_id_27949af8_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `informacion_usuario_groups`
--
ALTER TABLE `informacion_usuario_groups`
  ADD CONSTRAINT `informacion_usuario_groups_group_id_3d98422e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `informacion_usuari_usuario_id_b551b635_fk_informacion_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `informacion_usuario` (`id`);

--
-- Filtros para la tabla `informacion_usuario_user_permissions`
--
ALTER TABLE `informacion_usuario_user_permissions`
  ADD CONSTRAINT `informacion_usuario_permission_id_3a5f9db7_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `informacion_usuari_usuario_id_9116af7a_fk_informacion_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `informacion_usuario` (`id`);

--
-- Filtros para la tabla `reportes_reportes`
--
ALTER TABLE `reportes_reportes`
  ADD CONSTRAINT `reportes_reportes_fichas_id_650f97b6_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

--
-- Filtros para la tabla `tipo_perfil_tipoperfil`
--
ALTER TABLE `tipo_perfil_tipoperfil`
  ADD CONSTRAINT `tipo_perfil_tipoperf_fichas_id_ada68be9_fk_informacion_fichas_id` FOREIGN KEY (`fichas_id`) REFERENCES `informacion_fichas` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
