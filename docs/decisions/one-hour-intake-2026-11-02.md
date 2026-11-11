# Intake: destinations 30-60 minutes from Casa de la Familia (2026-11-02)

Owner request 2026-11-02: look at beaches, sights and other activities beyond the 30-minute local area but within about one hour's drive, plus restaurants close to them or on the way.

- Method: Google Places text search (identity, coordinates, website) and Google Routes `computeRoutes`, DRIVE, TRAFFIC_AWARE_OPTIMAL, departure Saturday 2026-11-07 10:00 local, from the origin in `AGENTS.md`. Checked 2026-11-02 by Claude.
- These are candidates only. Nothing about hours, prices, facilities, rocks, lifeguards or family suitability has been checked. Descriptions are working labels, not editorial claims.
- Owner selection is collected on the checklist page https://claude.ai/artifact/D8D2RD48rZbacv93b3J2SW (artifact database, collection `choices`).
- Restaurants come in a second step, near the destinations the owner selects.
- Open owner decision: which layer holds the 30-60 minute band. The existing `excursions_4h` layer has a catalogue group `Tæt på`, but it also holds places beyond an hour (Caminito del Rey 65-71 min, Sierra de las Nieves 79 min, Gibraltar 100 min, not all route-checked).

Excluded during the sweep: Aula del Mar / Museo Alborania (Google: permanently closed); Lagar de Torrijos, Montes de Málaga (70 min); Caminito del Rey (71 min, existing record). Queries that matched the wrong place (Los Cahorros de Monda matched a Granada route; a Campillos necropolis) were dropped.

## A. Strande

| ID | Candidate | Drive | Note | Maps | Website |
|---|---|---|---|---|---|
| bA01 | Playa de la Misericordia, Málaga | 32 min | Lang bystrand vest for Málaga centrum, ved Paseo Marítimo Antonio Banderas | https://maps.google.com/?cid=2847078778270785825 |  |
| bA02 | Playa de la Malagueta, Málaga | 41 min | Findes allerede som record (needs_fact_check). | https://maps.google.com/?cid=9240116015795400503 |  |
| bA03 | Playa de Pedregalejo, Málaga | 40 min | Strand i det gamle fiskerkvarter øst for centrum | https://maps.google.com/?cid=2554888298616883590 |  |
| bA04 | Playas del Palo, Málaga | 44 min | Kendt for spisesteder med espetos; undersøges i trin 2. | https://maps.google.com/?cid=17724748868623311986 |  |
| bA05 | Playa del Rincón de la Victoria | 46 min | Bystrand i Rincón de la Victoria øst for Málaga | https://maps.google.com/?cid=5544730715889533264 |  |
| bA06 | Playa de Venus, Marbella | 37 min | Bystranden ved Marbellas gamle by | https://maps.google.com/?cid=6655594276933228362 |  |
| bA07 | Playa de Nagüeles, Marbella | 36 min | Strand på Golden Mile mellem Marbella og Puerto Banús | https://maps.google.com/?cid=14214806510034010341 |  |
| bA08 | Playa Puerto Banús | 36 min | Stranden ved lystbådehavnen i Puerto Banús | https://maps.google.com/?cid=16497117869688909642 |  |
| bA09 | Playa de San Pedro de Alcántara | 41 min | Strand ved San Pedro, nær de romerske ruiner | https://maps.google.com/?cid=3637270001119194530 |  |
| bA10 | Playa de la Rada, Estepona | 54 min | Esteponas lange bystrand | https://maps.google.com/?cid=8799066273597614919 | http://www.estepona.es/ |
| bA11 | Playa del Cristo, Estepona | 53 min | Lille strand i en bugt ved Esteponas havn | https://maps.google.com/?cid=2950378981063869983 | http://www.estepona.es/turismo/ |

## B. Byer og landsbyer

| ID | Candidate | Drive | Note | Maps | Website |
|---|---|---|---|---|---|
| bB01 | Marbella gamle by | 35 min | Findes allerede som record (needs_fact_check). Avenida del Mar med Dalí-skulpturerne kan lægges ind her. | https://maps.google.com/?cid=16477606059241697078 | https://www.andaluciamia.com/es/casco-antiguo-de-marbella-lo-mejor-que-ver-y-hacer/ |
| bB02 | Avenida del Mar (Dalí-skulpturer), Marbella | 36 min | Forslag: lægges ind under Marbella gamle by. | https://maps.google.com/?cid=2802982148280666629 | https://www.esculturaurbanaaragon.com.es/andalucia8.htm |
| bB03 | Puerto Banús | 38 min | Luksushavn med butikker og restauranter | https://maps.google.com/?cid=13981480417362448082 | https://puerto-banus.com/?utm_source=GMB&utm_medium=organic |
| bB04 | San Pedro Alcántara (Bulevar) | 39 min | Parkboulevard med legepladser og fontæner | https://maps.google.com/?cid=426638634432005335 | http://www.bulevarsanpedro.es/ |
| bB05 | Estepona gamle by | 53 min | Ruta de los murales kan lægges ind her. | https://maps.google.com/?cid=6832883084358567301 |  |
| bB06 | Ruta de los murales, Estepona | 50 min | Forslag: lægges ind under Estepona gamle by. | https://maps.google.com/?cid=7891588474822849812 | https://turismo.estepona.es/lugares/lugares-de-interes/murales-artisticos/ |
| bB07 | Ojén | 41 min | Hvid bjerglandsby over Marbella; vej videre til Juanar | https://maps.google.com/?cid=11068725027353837749 |  |
| bB08 | Istán | 57 min | 57 min, i den øvre ende af båndet. | https://maps.google.com/?cid=12834472230370913091 |  |
| bB09 | Benahavís | 48 min | Bjerglandsby kendt for restauranter; nær Las Angosturas | https://maps.google.com/?cid=12429715200943595896 |  |
| bB10 | Monda | 35 min | Borgen (Castillo de la Villeta) er i dag hotel. | https://maps.google.com/?cid=5987299448043395331 | http://www.castillodemonda.com/ |
| bB11 | Coín | 31 min | Indlandsby med marked og appelsinlunde; vej til Río Grande | https://maps.google.com/?cid=10858380925420821440 |  |
| bB12 | Álora og borgen | 50 min | Hvid by under en maurisk borg ved Guadalhorce-dalen | https://maps.google.com/?cid=14839145985813698715 | http://www.alora.es/ |

## C. Málaga by

| ID | Candidate | Drive | Note | Maps | Website |
|---|---|---|---|---|---|
| bC01 | Alcazaba | 42 min | Málaga findes allerede som record (needs_editorial_review). Forslag: punkterne C lægges ind under Málaga, med mindre du vil have dem som selvstændige steder. | https://maps.google.com/?cid=9541330371664720487 | https://alcazabaygibralfaro.malaga.eu/es/ |
| bC02 | Castillo de Gibralfaro og udsigtspunktet | 42 min | Borg og udsigt over havn og by | https://maps.google.com/?cid=14138212742589260177 | http://alcazabaygibralfaro.malaga.eu/es/ |
| bC03 | Teatro Romano | 44 min | Romersk teater ved foden af Alcazaba | https://maps.google.com/?cid=9648473637463672617 | https://www.juntadeandalucia.es/cultura/enclaves/enclave-arqueologico-teatro-romano-de-malaga |
| bC04 | Museo Picasso Málaga | 44 min | Picasso-museet i hans fødeby | https://maps.google.com/?cid=2054424185812036537 | https://www.museopicassomalaga.org/ |
| bC05 | Katedralen | 45 min | Byens katedral, 'La Manquita' | https://maps.google.com/?cid=18213615145923320314 | https://malagacatedral.com/ |
| bC06 | Centre Pompidou Málaga | 38 min | Moderne kunst i den farvede kube ved havnen | https://maps.google.com/?cid=13558523713251466291 | http://www.centrepompidou-malaga.eu/ |
| bC07 | Museo Carmen Thyssen | 43 min | Spansk 1800-tals-maleri i et palæ | https://maps.google.com/?cid=4568007239589048319 | https://carmenthyssenmalaga.org/ |
| bC08 | Museo Interactivo de la Música (MIMMA) | 40 min | Musikmuseum hvor man må spille på instrumenterne | https://maps.google.com/?cid=13713620474989796078 | http://www.musicaenaccion.com/mimma/ |
| bC09 | Muelle Uno | 44 min | Havnepromenade med butikker og spisesteder | https://maps.google.com/?cid=2454110474856480835 | http://www.muelleuno.com/ |
| bC10 | Parque de Málaga | 40 min | Bypark med palmer langs havnen | https://maps.google.com/?cid=15047523198190580880 | http://www.malagaturismo.com/es/recursos-turisticos/detalle/parque-de-malaga/56 |
| bC11 | Mercado de Atarazanas | 38 min | Findes allerede som record (needs_fact_check). | https://maps.google.com/?cid=9008384581169661630 | https://mercadomalaga.es/mercados/mercado-central-atarazanas/ |
| bC12 | Museo del Automóvil y la Moda | 34 min | Veteranbiler og mode i en gammel tobaksfabrik | https://maps.google.com/?cid=11705854757271332990 | http://www.museoautomovilmoda.com/ |

## D. Historie langs kysten

| ID | Candidate | Drive | Note | Maps | Website |
|---|---|---|---|---|---|
| bD01 | Villa Romana de Río Verde, Marbella | 38 min | Romersk villa med mosaikgulve | https://maps.google.com/?cid=9439904174889815030 | http://www.arsfluentes.es/villa-romana/situacion.html |
| bD02 | Termas romanas de Las Bóvedas, San Pedro | 42 min | Romerske badeanlæg ved stranden | https://maps.google.com/?cid=14140905928209983437 | https://www.marbella.es/web/cultura/patrimonio/arqueologia/item/34656-termas-romanas-de-las-bovedas.html?fbclid=IwAR1RK0UqP4NHoERBlKdSmFIhm85ZvsOQ1yWy8fuP2R_4iLvr0MoeIaVmURE |
| bD03 | Basílica Paleocristiana de Vega del Mar, San Pedro | 41 min | Tidligt kristen kirkeruin og gravplads | https://maps.google.com/?cid=5405901255071934354 | https://www.marbella.es/web/cultura/patrimonio/arqueologia/item/34657-basilica-paleocristiana-de-vega-del-mar.html?fbclid=IwAR2mHhTcYJOTq4HFfxR_T_UG5T7Gb14VoAK9MTmw4uGnEI1wMmX-FE_38sA |

## E. Natur

| ID | Candidate | Drive | Note | Maps | Website |
|---|---|---|---|---|---|
| bE01 | Jardín Botánico La Concepción, Málaga | 36 min | Historisk botanisk have nord for Málaga | https://maps.google.com/?cid=2527569419136067586 | http://laconcepcion.malaga.eu/ |
| bE02 | Juanar og Mirador del Macho Montés | 49 min | Skov, vandring og udsigt over Ojén og Marbella | https://maps.google.com/?cid=9612961884393079949 |  |
| bE03 | Cañón de las Angosturas, Benahavís | 46 min | Kløft ved Río Guadalmina; badning i floden om sommeren | https://maps.google.com/?cid=16969812549091975637 | http://andaluciarustica.com/canon-de-las-angosturas-del-rio-guadalmina-benahavis.htm |
| bE04 | Río Grande ved Coín | 40 min | Flodsti med naturlige badehuller | https://maps.google.com/?cid=9448389620354316181 |  |
| bE05 | Paseo Marítimo de Marbella | 37 min | Lang strandpromenade, god til gåture og cykling | https://maps.google.com/?cid=2497278789135368861 |  |
| bE06 | Orquidario de Estepona | 54 min | Orkidéhus i Esteponas centrum | https://maps.google.com/?cid=872064740314117478 | https://orchidariumestepona.com/ |
| bE07 | Cueva del Tesoro, Rincón de la Victoria | 43 min | Havgrotte man kan gå ind i | https://maps.google.com/?cid=3758341386343282416 | https://www.turismoenrincon.es/cueva-del-tesoro/ |
| bE08 | Senda Litoral ved Málaga | 30 min | Kyststi mod Málaga vest; i den nedre ende af båndet | https://maps.google.com/?cid=11147761019358704387 |  |

## F. Oplevelser

| ID | Candidate | Drive | Note | Maps | Website |
|---|---|---|---|---|---|
| bF01 | Selwo Aventura, Estepona | 46 min | Findes allerede som record (needs_fact_check). | https://maps.google.com/?cid=14324532108288129059 | https://www.selwo.es/?utm_id=GMBtraffic&utm_medium=OrganicGMB&utm_source=google |
| bF02 | Funny Hill Karting, Marbella | 34 min | Søgning efter 'Funny Beach' gav dette sted; navn og drift skal bekræftes. | https://maps.google.com/?cid=2477769105084406654 | https://funnyhill.es/ |
| bF03 | Bådture fra Marbella havn | 36 min | Kræver udbydergennemgang og omdømmetjek før en record, som med bådture i Fuengirola. | https://maps.google.com/?cid=16618807846183351881 | https://perlafisher.com/ |
| bF04 | Puerto Deportivo de Estepona | 54 min | Havn med søndagsmarked og spisesteder | https://maps.google.com/?cid=16483603617881687513 | https://www.marinasmediterraneo.com/estepona |

## G. Under 30 min (fundet undervejs, hører til nærområdet)

| ID | Candidate | Drive | Note | Maps | Website |
|---|---|---|---|---|---|
| bG01 | Aventura Amazonia Marbella | 21 min | Klatrepark i træerne | https://maps.google.com/?cid=12264503478820103722 | https://aventura-amazonia.com/parques-amazonia/marbella |
| bG02 | Museo Aeronáutico de Málaga | 28 min | Flymuseum ved lufthavnen | https://maps.google.com/?cid=8739503408226916740 | https://www.aeromuseo.org/ |
| bG03 | Playa de Guadalmar | 28 min | Del af stranden kan være naturiststrand; skal tjekkes. | https://maps.google.com/?cid=934458244603290887 | http://www.kioskoguadalmar.es/ |
| bG04 | Alhaurín el Grande | 25 min | Indlandsby på vej mod Coín | https://maps.google.com/?cid=14669775383558271857 |  |
