:- dynamic sintoma_usuario/1.
:- encoding(utf8).

% Definición de síntomas
sintoma(fiebre).
sintoma(tos).
sintoma(dolor_garganta).
sintoma(dolor_muscular).
sintoma(secrecion_nasal).
sintoma(estornudos).
sintoma(dificultad_respirar).
sintoma(dolor_pecho).
sintoma(cansancio_extremo).
sintoma(dolor_cabeza).
sintoma(perdida_olfato).
sintoma(perdida_gusto).
sintoma(escalofrios).
sintoma(sibilancias).
sintoma(tos_con_flema).
sintoma(nauseas).
sintoma(vomitos).
sintoma(fatiga).
sintoma(tos_seca).
sintoma(ronquera).
sintoma(ojos_llorosos).
sintoma(contacto_con_infectado).
sintoma(dificultad_para_tragar).
sintoma(alergico_a_algo).
sintoma(diarrea).

% Reglas de Síndromes
sindrome_gripal :-
    sintoma_usuario(fiebre),
    sintoma_usuario(tos),
    sintoma_usuario(dolor_cabeza),
    sintoma_usuario(dolor_muscular),
    sintoma_usuario(cansancio_extremo).

sindrome_resfriado :-
    sintoma_usuario(secrecion_nasal),
    sintoma_usuario(estornudos),
    sintoma_usuario(dolor_garganta).

sindrome_respiratorio_agudo :-
    sintoma_usuario(fiebre),
    sintoma_usuario(tos),
    sintoma_usuario(dificultad_respirar).

sindrome_bronquial :-
    sintoma_usuario(tos),
    sintoma_usuario(sibilancias),
    sintoma_usuario(dificultad_respirar).

sindrome_infeccion_alta :-
    sintoma_usuario(dolor_garganta),
    sintoma_usuario(dolor_cabeza),
    sintoma_usuario(fiebre).

sindrome_neumonico :-
    sintoma_usuario(tos_con_flema),
    sintoma_usuario(fiebre),
    sintoma_usuario(dolor_pecho),
    sintoma_usuario(fatiga).

sindrome_alergico :-
    sintoma_usuario(estornudos),
    sintoma_usuario(secrecion_nasal),
    sintoma_usuario(ojos_llorosos).

indicios_covid19 :-
    sintoma_usuario(perdida_gusto);
    sintoma_usuario(perdida_olfato).

% Diagnósticos
diagnostico(influenza) :-
    sindrome_gripal,
    sintoma_usuario(escalofrios).

diagnostico(resfriado_comun) :-
    sindrome_resfriado,
    \+ sintoma_usuario(fiebre).

diagnostico(covid_19) :-
    sindrome_respiratorio_agudo,
    indicios_covid19,
    sintoma_usuario(cansancio_extremo),
    sintoma_usuario(contacto_con_infectado).

diagnostico(neumonia) :-
    sindrome_neumonico,
    sintoma_usuario(diarrea).

diagnostico(bronquitis) :-
    sindrome_bronquial,
    sintoma_usuario(tos_con_flema).

diagnostico(asma) :-
    sintoma_usuario(sibilancias),
    sintoma_usuario(dificultad_respirar),
    sintoma_usuario(tos_seca).

diagnostico(epoc) :-
    sintoma_usuario(tos),
    sintoma_usuario(fatiga),
    sintoma_usuario(dificultad_respirar).

diagnostico(faringitis) :-
    sindrome_infeccion_alta,
    sintoma_usuario(dificultad_para_tragar).

diagnostico(laringitis) :-
    sintoma_usuario(ronquera),
    sintoma_usuario(dolor_garganta),
    sintoma_usuario(tos).

diagnostico(sinusitis) :-
    sintoma_usuario(dolor_cabeza),
    sintoma_usuario(secrecion_nasal),
    sintoma_usuario(fatiga).

diagnostico(tuberculosis) :-
    sintoma_usuario(tos_con_flema),
    sintoma_usuario(fiebre),
    sintoma_usuario(cansancio_extremo),
    sintoma_usuario(dolor_pecho).

diagnostico(gripe_aviar) :-
    sindrome_gripal,
    sintoma_usuario(nauseas),
    sintoma_usuario(vomitos).

diagnostico(rinitis_alergica) :-
    sindrome_alergico,
    sintoma_usuario(alergico_a_algo).

mostrar_info(influenza, Info) :-
    Info = [
        "Diagnóstico probable: Gripe (Influenza)",
        "Sistema afectado: Respiratorio",
        "Causa: Infección viral por virus influenza A o B",
        "Diagnóstico: Clínico por síntomas, pruebas rápidas de antígeno o PCR",
        "Tratamiento: Reposo, hidratación, antipiréticos, antivirales en casos graves",
        "Edad común: Todas las edades, mayor riesgo en niños, adultos mayores y personas con comorbilidades"
    ].

mostrar_info(resfriado_comun, Info) :-
    Info = [
        "Diagnóstico probable: Resfriado común",
        "Sistema afectado: Respiratorio superior",
        "Causa: Infección viral (rinovirus, coronavirus estacionales)",
        "Diagnóstico: Clínico por síntomas, sin necesidad de pruebas",
        "Tratamiento: Reposo, líquidos, medicamentos sintomáticos como analgésicos y descongestionantes",
        "Edad común: Todas las edades"
    ].

mostrar_info(covid_19, Info) :-
    Info = [
        "Diagnóstico probable: COVID-19",
        "Sistema afectado: Respiratorio, con posibles complicaciones sistémicas",
        "Causa: Infección por SARS-CoV-2",
        "Diagnóstico: Prueba PCR o antígeno, evaluación clínica de síntomas",
        "Tratamiento: Sintomático en casos leves, antivirales y soporte respiratorio en casos graves",
        "Edad común: Todas las edades, mayor riesgo en adultos mayores y personas con enfermedades crónicas"
    ].

mostrar_info(neumonia, Info) :-
    Info = [
        "Diagnóstico probable: Neumonía",
        "Sistema afectado: Pulmones (alvéolos)",
        "Causa: Infección bacteriana, viral o fúngica",
        "Diagnóstico: Clínico, radiografía de tórax, pruebas de laboratorio",
        "Tratamiento: Antibióticos, antipiréticos, oxigenoterapia en casos severos",
        "Edad común: Niños pequeños, adultos mayores, personas inmunocomprometidas"
    ].

mostrar_info(bronquitis, Info) :-
    Info = [
        "Diagnóstico probable: Bronquitis",
        "Sistema afectado: Bronquios",
        "Causa: Infección viral o exposición prolongada a irritantes como el humo",
        "Diagnóstico: Evaluación clínica, ocasionalmente radiografía para descartar neumonía",
        "Tratamiento: Reposo, líquidos, medicamentos para la tos, broncodilatadores en algunos casos",
        "Edad común: Adultos jóvenes a mayores, especialmente fumadores"
    ].

mostrar_info(asma, Info) :-
    Info = [
        "Diagnóstico probable: Asma",
        "Sistema afectado: Vías respiratorias",
        "Causa: Inflamación crónica de las vías respiratorias, desencadenada por alérgenos, ejercicio, frío o infecciones",
        "Diagnóstico: Historia clínica, espirometría, pruebas de función pulmonar",
        "Tratamiento: Broncodilatadores, corticosteroides inhalados, control ambiental",
        "Edad común: Frecuente en niños, pero puede persistir o aparecer en adultos"
    ].

mostrar_info(epoc, Info) :-
    Info = [
        "Diagnóstico probable: EPOC (Enfermedad Pulmonar Obstructiva Crónica)",
        "Sistema afectado: Pulmones (bronquios y alvéolos)",
        "Causa: Exposición prolongada al humo del tabaco u otros irritantes",
        "Diagnóstico: Espirometría, antecedentes de tabaquismo, síntomas crónicos",
        "Tratamiento: Broncodilatadores, esteroides inhalados, oxígeno suplementario",
        "Edad común: Mayores de 40 años, especialmente fumadores o exfumadores"
    ].

mostrar_info(faringitis, Info) :-
    Info = [
        "Diagnóstico probable: Faringitis",
        "Sistema afectado: Garganta (faringe)",
        "Causa: Infección viral o bacteriana (como estreptococo)",
        "Diagnóstico: Evaluación clínica, cultivo faríngeo si es necesario",
        "Tratamiento: Analgésicos, antibióticos en casos bacterianos",
        "Edad común: Más común en niños y adolescentes"
    ].

mostrar_info(laringitis, Info) :-
    Info = [
        "Diagnóstico probable: Laringitis",
        "Sistema afectado: Laringe (cuerdas vocales)",
        "Causa: Infección viral, uso excesivo de la voz, irritantes",
        "Diagnóstico: Clínico por síntomas como ronquera y tos",
        "Tratamiento: Reposo vocal, líquidos, humidificadores, analgésicos",
        "Edad común: Todas las edades"
    ].

mostrar_info(sinusitis, Info) :-
    Info = [
        "Diagnóstico probable: Sinusitis",
        "Sistema afectado: Senos paranasales",
        "Causa: Infección viral o bacteriana, alergias",
        "Diagnóstico: Evaluación clínica, imagenología en casos recurrentes",
        "Tratamiento: Descongestionantes, antibióticos si hay infección bacteriana",
        "Edad común: Adultos jóvenes a mayores"
    ].

mostrar_info(tuberculosis, Info) :-
    Info = [
        "Diagnóstico probable: Tuberculosis",
        "Sistema afectado: Pulmones (aunque puede afectar otros órganos)",
        "Causa: Infección bacteriana por *Mycobacterium tuberculosis*",
        "Diagnóstico: Prueba de tuberculina, radiografía de tórax, baciloscopía",
        "Tratamiento: Antibióticos específicos por 6 meses o más",
        "Edad común: Todas las edades, más común en poblaciones vulnerables"
    ].

mostrar_info(gripe_aviar, Info) :-
    Info = [
        "Diagnóstico probable: Gripe aviar",
        "Sistema afectado: Respiratorio y sistémico",
        "Causa: Infección por virus de influenza aviar (H5N1, H7N9, etc.)",
        "Diagnóstico: PCR específica para influenza aviar, historia de exposición a aves",
        "Tratamiento: Antivirales, hospitalización en casos graves",
        "Edad común: Personas en contacto con aves infectadas, cualquier edad"
    ].

mostrar_info(rinitis_alergica, Info) :-
    Info = [
        "Diagnóstico probable: Rinitis alérgica",
        "Sistema afectado: Vías respiratorias superiores (nariz, ojos)",
        "Causa: Reacción alérgica a polen, polvo, ácaros, pelos de animales",
        "Diagnóstico: Historia clínica, pruebas de alergia",
        "Tratamiento: Antihistamínicos, descongestionantes, inmunoterapia en casos graves",
        "Edad común: Común en niños y adultos jóvenes, puede persistir en la adultez"
    ].

diagnosticar(Diagnosticos) :-
    findall(D, diagnostico(D), Diagnosticos).
