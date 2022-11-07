# Plan de Gestión de Riesgos

## Contenido

1. Identificación de riesgos
   
   1. Riesgos Cualitativos
   
   2. Riesgos Cuantitativos
   
2. Protocolo de Respuesta al Riesgo
   
   1. Metodología de análisis de riesgos (según su tipo)
   
   2. Roles y responsabilidades
   
   3. Clasificación de riesgos (priorizar hacer RBS)
   
3. Control de Riesgos
   
   1. Implementación de respuesta al riesgo
   
   2. Monitoreo a riesgos identificados
   
   3. Identificar nuevos riesgos
   
   4. Evaluación de efectividad de respuesta al riesgo

## 1. Identificación de Riesgos

En este apartado se presentará un Registro de Riesgos para riesgos cualitativos y otro para riesgos cuantitativos. En cada uno de estos Registros de Riesgos, se presenta cada riesgo con un identificador único,  descripción con el nivel de detalle necesario para evitar ambigüedad, dueños potenciales del riesgo (Risk Owners) y principales causas del riesgo.

### 1.1 Riesgos Cualitativos

La tabla siguiente presenta el Registro de Riesgos para todos aquellos riesgos de carácter cualitativo en cuanto a su impacto y tipo de análisis requerido para su implementación.

| ID | Riesgo | Descripción | Risk Owners | Causas |
| --- | --- | --- | --- | --- |
| 1 | Actualización de buscador (browser) en máquinas de desarrollo o pruebas | El browser es el principal cliente de una aplicación web, por lo que una actualización mayor del buscador en máquinas de desarrolladores y/o de pruebas de usuario podría significar funciones deprecadas, sin soporte o inválidas que en otras versiones del browser son válidas. Esto provocaría fallos e inconsistencias del sistema dependiendo de la versión de buscador que se use. | Departamento de IT | Falta de monitoreo en documentación y anuncios de Google Chrome y Firefox, Falta de registro de versión en lista de CIs. |
| 2 | Complicaciones para implementar funcionalidades clave | Durante el desarrollo de un sistema, siempre existe la incertidumbre de que algún feature sea demasiado complejo de implementar, por lo que se complica dicho feature o tarda más en lograrse. | Departamento de IT | Dificultad del proceso, estimaciones equivocadas de tiempo, requerimientos fuera del alcance computacional del proyecto, falta de experiencia por parte del equipo de desarrollo. |
| 3 | Exceso de cambios en el producto | El cliente, durante Sprint Review o en Pruebas de Usuario, presenta demasiadas solicitudes de cambio o nuevas implementaciones al producto iterado. | Project Manager, Departamento de IT | Descontento por parte del cliente con lo que se desarrolló, poca comunicación del Project Manager con el cliente sobre lo que se está implementando o cambiando, el cliente no está bien informado sobre el alcance del proyecto. |
| 4 | Pérdida de archivos de diseño (.psd, .ai, etc) | El software que el equipo de Diseño utiliza es propenso a "congelarse" y provocar la interrupción del sistema operativo de la máquina donde se trabaja, lo que resulta comúnmente en el repentino reinicio de la computadora sin guardado de cambios en los archivos. | Departamento de Diseño | Exceso de procesos en la RAM, poco monitoreo del estado de la RAM, saturación de llamadas al CPU (clicks), falta de versiones guardadas como respaldo. | 
| 5 | Interrupción del presupuesto por parte de inversionistas | En cualquier momento durante el desarrollo del sistema se puede presentar un corte repentino del presupuesto planeado, ya sea por causas internas o externas al equipo del proyecto. | Project Manager, Departamento de Logística | Descontento de inversionistas, falta de comunicación, problemas económicos por parte de inversionistas (recortes, inflación, despidos). |
| 6 | Una aplicación similar sale al mercado antes que la nuestra. | Existe el riesgo latente en la industria tecnológica de que una aplicación similar exista en el mercado antes de que el proyecto sea liberado al mercado, lo que puede representar un cambio radical en los ingresos planeados, precio de venta y respuesta del mercado. | Departamento de Calidad | Naturaleza de cambio rápido y constante en la industria tecnológica, violaciones al acuerdo de privacidad por parte de algún miembro del equipo, falta de planeación de la respuesta ante tal contingencia. |
| 7 | Nuevas leyes de privacidad en el uso de los datos clínicos. | Existe la posibilidad que durante el transcurso del proyecto, nuevas leyes sean aprobadas acerca del uso y manejo de datos clínicos de pacientes y/o doctores, por lo que funcionalidades de la aplicación podrían pasar de legales a ilegales. | Departamento de Logística | Aprobación de nuevas leyes en el ámbito por parte Estatal o Federal, poco monitoreo de iniciativas en Cámara de Diputados. |
| 8 | Pérdida de datos durante testing o desarrollo. | Durante el proceso de desarrollo del sistema y base de datos, este riesgo se refiere al caso donde por algún error o caso de prueba no previsto, se realice alguna modificación irremediable en la base de datos que resulte en la pérdida de datos o modelos importantes en la base de datos. | Departamento de IT, Departamento de Calidad | Falta de respaldos en la base de datos, ignorar la regla de utilización de **versión local** de la base de datos, Unit Tests de los *controllers* no previstos. |
| 9 | Demandas por parte del equipo de trabajo. | Algún miembro o ex-miembro del equipo presenta una demanda legal al equipo del proyecto. | Departamento de Logística | Despidos injustificados, descontentos o maltratos no controlados, falta de atención legal en los procesos de renuncia y despidos. |
| 10 | Sistema resultante (iterado o final) es demasiado lento (execution time). | El sistema entregado al final de un Sprint o del proyecto, al unirse con las demás iteraciones, presenta un tiempo de respuesta demasiado lento en las máquinas de pruebas. | Departamento de Calidad | Fallos en análisis de métricas de mantenimiento de software, complejidad computacional del prototipo es de $O(n^3)$ o mayor, modularidad del código no supervisada por las métricas actuales. |

### 1.2 Riesgos Cuantitativos

Similar a la sección anterior, la tabla siguiente presenta el Registro de Riesgos para todos aquellos riesgos de carácter cuantitativo en cuanto a su impacto y tipo de análisis requerido para su implementación. 

| ID | Riesgo | Descripción | Risk Owners | Causas |
| --- | --- | --- | --- | --- |
| 11 | Almacenamiento en la nube excedido repentinamente. | Este riesgo se refiere al caso donde la capacidad de almacenamiento contratado hasta el momento no sea suficiente para continuar con el cronograma o sea rebasado antes de lo previsto, resultando en cobros por exceso de almacenamiento. | Departamento de IT | Falta de monitoreo en los *logs* del clúster de datos y/o mensajes por parte de la empresa de almacenamiento, ejecuciones en la base de datos que por error saturan el almacenamiento. |
| 12 | Renuncias por parte del equipo del proyecto | Durante el trancurso del proyecto, siempre existe la posibilidad de que un miembro del equipo ya no forme parte del mismo, sin algún aviso o con poco tiempo de anticipación, provocando reorganización o retrasos en el cronograma. | Project Manager, Departamento de Logística | Algún miembro del equipo presenta problemas personales y renuncia por lo mismo, o renuncias por situaciones que se sucitan en el proyecto, descontentos o quejas no resueltas. |
| 13 |  Despidos por parte del equipo del proyecto | Durante el trancurso del proyecto, siempre existe la posibilidad de que un miembro del equipo sea despedido. | Project Manager, Departamento de Logística | Falta de compromiso por parte del agraviado, rendimiento deficiente, falta de motivación, comportamientos que no reflejan la filosofía del equipo. |
| 14 | Falta de personal | Existe la posibilidad de que, durante el desarrollo del proyecto, los recursos humanos sean insuficientes para cumplir con el cronograma, lo que resultaría en retrasos y/o nuevas contrataciones | Project Manager, Departamento de Logística | Estimaciones de carga de trabajo y tiempo poco realistas, exceso de *bugs* o implementaciones no previstas, procesos complejos no previstos en el cronograma. |
| 15 | Falta de presupuesto | Puede ocurrir que, durante la realización de las actividades del proyecto, se requiera de inversiones nuevas no previstas. | Project Manager, Departamento de Logística | Actividades no previstas en el cronograma, gastos repentinos no contemplados, complejidad de actividades rebasa las estimaciones. |

### 1.3 Matriz de Probabilidad e Impacto

El protocolo de mitigación de riesgo se aplicará cuando, en el Sprint Planning, una Tarea lleve consigo alguno de los riesgos de las tablas anteriores y además **dicho riesgo se encuentre en áreas de prioridad**.Con el fin de establecer una guía general sobre las áreas de prioridad y qué riesgos previstos se encuentran ahí, se presenta la siguiente Matriz de Probabilidad e Impacto. En esta matriz, los riesgos que se encuentren en el área sin sobreado se clasifican como **de mínima acción**, y un protocolo de mitigación no sería necesario. En lugar del protocolo de mitigación, sólo será necesario **informar a los involucrados para su monitoreo**, pues son riesgos que con correcta atención se evitarían.

![img]

## 2. Protocolo de Respuesta al Riesgo

A continuación se presentan las estrategias principales para responder a los riesgos previstos en las dos secciones anteriores y que se encuentren en las áreas de prioridad de la sección 1.3. Dichas estrategias difieren según el tipo de riesgo (cualitativo o cuantitativo), por lo que se hará la distinción entre las estrategias a seguir en caso de riesgos previstos de tipo cualitativo y de tipo cuantitativo.
   
### 1. Metodología de análisis y respuesta ante riesgos (según su tipo)

**Riesgos Cualitativos: análisis y respuesta**

En cuanto al análisis de cada riesgo cualitativo previsto en la tabla de la Sección 1.1 y que sea relevante según la tabla de la sección 1.3, éste comienza cuando el Sprint Planning implemente la(s) actividad(es) que involucren algún riesgo de dicha tabla. Si durante esta reunión se identifica que se implementará alguna actividad que conlleve algún riesgo previsto y relevante, la etapa de análisis deberá llevarse a cabo. En caso de que se prosiga a analizar algún riesgo cualitativo, se deberá realizar el siguiente proceso:

1. Análisis de causa y efecto
   
La etapa de análisis de un riesgo cualitativo comienza con un diagrama de causa y efecto (de pescado), a fin de identificar máximo **4 causas principales de tal riesgo (efecto)**, donde cada una de estas 4 causas tendrá **1 subcausa principal**. Dicho diagrama se comienza con el riesgo o amenaza, y se exploran las prosibles causas que llevarían a que dicho riesgo ocurra. El diagrama seguirá el siguiente formato:

![Diagrama de causa-efecto](res/diagramas-riesgos.png)

2. Una vez que se tenga el diagrama, se tendrá claro cuáles serían las causas de que dicho riesgo se presente. Estas 4 causas presentes en el diagrama serán el input dentro de la siguiente herramienta de análisis: Tabla AMEF, a fin de ordenar por prioridad las 4 causas.

El AMEF es una herramienta de análisis eficaz que ayuda a detectar problemas potenciales y sus **efectos** dentro del proyecto. Dicha herramienta se implementará con la siguiente tabla:

| Causa/problema | Alcance del problema | Severidad (S) | Ocurrencia (O) | Detección (D) | NPR | Responsable |
| --- | --- | --- | --- | --- | --- | --- |
| Causa 1 | Efecto inmediato | 1 <= S <= 10 | 1 <= O <= 10 | 1 <= D <= 10 | $NPR = S \times O \times D$ | Nombre(s) |
| ... | ... | ... | ... | ... | ... | ... |
| Causa 4 | ... | ... | ... | ... | ... | ... |

Donde: 

- S: número de severidad de dicha falla, mismo que permitirá darle seguimiento oportuno a las acciones. Ejemplo: 10, usuario deja de usar la aplicación; 9, usuario escribe reseña negativa.

- O: el nivel de la frecuencia con la que acontecen o la facilidad con la que se pueden detectar. Esto permitirá tomar acciones preventivas comenzando con las que tengan un grado mayor de prioridad. Ejemplo: 10, error de dedo; 9, falta de conocimiento.

- D: número de acuerdo con el grado de detección de cada falla. Mientras más grande sea el número, más fácil de detectar es aquella falla o causa del riesgo, en este caso.

- NPR: Número Prioritario de Riesgo (NPR), es el valor que establece la prioridad de dicha causa del riesgo.
  
Una vez que se tenga esta nformación de las 4 causas (filas en la tabla), de acuerdo al NPR, las filas del AMEF se ordenan: hasta arriba será la fila de la causa más importante del riesgo.

3. Una vez que se tengan las causas ordenadas de acuerdo al NPR en la Tabla AMEF, seguirá la toma de decisiones: por medio de una reunión o no, se realizarán **nuevas Tareas para el Sprint Backlog** que involucren las acciones preventivas a tomar **para la causa principal (primera fila del AMEF), y serán incluidas y priorizadas** dentro de dicho Sprint Backlog.

**Riesgos Cuantitativos: análisis y respuesta**

1. La etapa de análisis de un riesgo cualitativo de prioridad comienza con la identificación de las posibles decisiones a tomar ante el riesgo. Estas posibles decisiones se acomodan en un Diagrama de Árbol. A continuación se presenta el diagrama de árbol para las posibles decisiones ante un despido en el área de IT:

![Árbol de Decisión ante Riesgo #13.](res/arbol1.png)

2. Se continúa trabajando sobre el mismo diagrama de árbol, donde ahora el siguiente paso es establecer las probabilidades de que las decisiones plasmadas ocurran, además de los costos por nodo invidual (Inversión). Los costos por nodo (Inversión) sólo establecen el costo neto de que se realice o suceda dicha decisión.

![Árbol de Decisión con Inversión por nodo.](res/arbol2.png)

3. Se calcula el NPV (Net Path Value), que es costo de cada rama hasta su final, donde el costo es la suma de las multiplicaciones de Inversión por probabilidad. Así, se obtiene **la cantidad de dinero gastado involucrado por rama de poisibilidad del riesgo**, con el fin de facilitar la decisión al mostrar lo que compromete cada camino de decisión.

![Árbol de Decisión con NPV](res/arbol3.png)

4. Se decide cuál ramificación de decisiones se hará por medio de una reunión.

5. Una vez que se decide cuál ramificación de actividades realizar, cada nodo se convertirá en una Tarea para el Sprint Backlog del sprint que se busca iniciar.

De esta manera, el protocolo a seguir ante cualquier riesgo que sea parte de las Tareas en un Sprint y se prevee en el Sprint Planning, generará nuevas Tareas de respuesta/preventivas al riesgo de la siguiente manera:

![Protocolos de análisis y respuesta a los dos tipos de riesgo](res/riesgos-overview.png)
   
### 2. Roles, responsabilidades y costos

El equipo de cada departamento del proyecto asumirá ciertas responsabilidades, las cuales se plantean a continuación. A su vez, esta dedicación de tiempo por parte del equipo de trabajo representa un costo adicional al planteado por las actividades del protocolo mitigación de riesgos de la sección anterior, mismo que también se tratará al final de esta sección.

Las responsabilidades ante la presencia de algún riesgo en las Tareas de un Sprint son:

- El Project Manager debe conducir la reunión del Sprint Planning, donde se debe identificar si el Sprint siguiente contiene alguna actividad de riesgo previsto y de prioridad. De ser así, se prosigue con los siguientes puntos.

- En las tablas de las secciones 1.1 y 1.2 se provee de un **Risk Owner**, que es el departamento directamente involucrado en el riesgo previsto. Dicho departamento tiene la responsabilidad de **convocar una reunión** para realizar los formatos de análisis del riesgo: el diagrama de pescado (en riesgos cualitativos) y el diagrama de árbol (en riesgos cuantitativos).

- De tratarse de riesgo cuantitativo, el departamento **Risk Owner** también es responsable de invitar a dicha reunión al líder de finanzas.

- Una vez completado el análisis, el líder del departamento es responsable de decidir si convocar una reunión para la creación de tickets de Tareas para el Sprint Backlog.
  
- El Project Manager es responsable de introducir y priorizar en el Sprint Backlog dichas Tareas de mitigación de riesgo generada.

- Una vez en el Sprint Backlog, las Tareas de mitigación de riesgo se dividen entre el Scrum Team y se implementan en el Sprint.

Los costos involucrados en la planeación y análisis **que dura 3 días como máximo** de riesgos son calculados de la siguiente manera:

$$
\hbox{Costo Total del Riesgo \#13} = NPV_{decisión} + \hbox{Costo del esfuezo},
\newline \hbox{Costo del esfuerzo} = P \times Sueldo \times \frac{3}{\hbox{días hábiles por mes}}
$$

donde:

$$
\newline \hbox{días hábiles por mes} = 20,
\newline P = \hbox{personas involucradas},
\newline Sueldo = \hbox{sueldo mensual}
$$

Nota: importante tratar de llevar a cabo el análisis y generación de Tareas de mitigación de riesgo en 3 días hábiles, a fin de no retrasar el Sprint.
   
### 3. Clasificación de riesgos

Los riesgos previstos en las tablas de la Sección 1.1 y 1.2 se clasificaron inicialmente por el tipo de análisis (cualitativo y cuantitativo). Ahora, con el fin de identificar los riesgos por sus fuentes, se clasifican utilizando una RBS (Risk Breakdown Structure), misma que es una estructura jerárquica de las posibles causas de los riesgos del proyecto.

![RBS de los riesgos previstos](res/rbs.png)