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

--
-- Índices para tablas volcadas
--

INSERT INTO `denticion_tipo` (`id`, `nombre`) VALUES
(1, 'Temporario'),
(2, 'Mixto'),
(3, 'Permanente');


INSERT INTO `tipo_perfil_ptercioinferioir` (`id_perfilTercio_inferior`, `perfilTercio_inferior`) VALUES
('1', 'Recto'),
('2', 'Concavo'),
('3', 'Convexo');


INSERT INTO `tipo_perfil_sonrisa` (`id_tipoSonrisa`, `tipoSonrisa`) VALUES
('1', 'Gingival'),
('2', 'Dental');


INSERT INTO `denticion_problema` (`id`, `nombre_problemas`) VALUES
(1, 'Pérdidas prematuras'),
(2, 'Anodoncias'),
(3, 'Mordida telescópica');

INSERT INTO `tipo_perfil_perfiltotal` (`id_tipoPerfiltotal`, `tipoPerfiltotal`) VALUES
('1', 'Ortonagtico'),
('2', 'Divergente Anterior'),
('3', 'Divergente Posterior');


INSERT INTO `tipo_perfil_facialfrontal` (`id_frontal_facial`, `frontal_facial`) VALUES
('1', 'Dolicofacial'),
('2', 'Mesofacial'),
('3', 'Braquifacial');


INSERT INTO `tipo_perfil_competencialabial` (`id_competenciaLabial`, `tipo_competenciaLabial`) VALUES
('1', 'Competente'),
('2', 'Potencialmente Competente'),
('3', 'Incompetente');


--
-- Indices de la tabla `informacion_catalogo_enfermedades`
--
ALTER TABLE `informacion_catalogo_enfermedades`
  ADD PRIMARY KEY (`id_enfermedad`);

ALTER TABLE `denticion_tipo`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `tipo_perfil_ptercioinferioir`
  ADD PRIMARY KEY (`id_perfilTercio_inferior`);

ALTER TABLE `tipo_perfil_sonrisa`
  ADD PRIMARY KEY (`id_tipoSonrisa`);
  
ALTER TABLE `denticion_problema`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `tipo_perfil_perfiltotal`
  ADD PRIMARY KEY (`id_tipoPerfiltotal`);
  
ALTER TABLE `tipo_perfil_competencialabial`
  ADD PRIMARY KEY (`id_competenciaLabial`);

  
  
