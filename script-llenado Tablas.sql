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

INSERT INTO `aspectos_tipo` (`id`, `nombre`) VALUES
(1, 'Temporario'),
(2, 'Mixto'),
(3, 'Permanente');


INSERT INTO `aspectos_problema` (`id`, `nombre_problemas`) VALUES
(1, 'Pérdidas prematuras'),
(2, 'Anodoncias'),
(3, 'Mordida telescópica');


INSERT INTO `analisisdenticionmixta_pos` (`id`) VALUES
(1),
(2),
(3),
(4);

INSERT INTO `analisis_cefalometrico_examen` (`id`) VALUES ('1'), ('2');

--
-- Indices de la tabla `informacion_catalogo_enfermedades`
--
ALTER TABLE `informacion_catalogo_enfermedades`
  ADD PRIMARY KEY (`id_enfermedad`);

ALTER TABLE `denticion_tipo`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `denticion_problema`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `analisisdenticionmixta_pos`
  ADD PRIMARY KEY (`id`);

  
  
