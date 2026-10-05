# Identity clarification report

This report covers destination rows in `data/destination-classification.csv` that were previously flagged for manual clarification, unresolved identity/scope, or possible name collision. Match confidence is an estimate for identifying the intended collection entry from its displayed name, visible Maps listing type, and available location clues. It is not a confidence score for visitor information.

The supplied Google Maps URL is a shared list URL, not an individual place URL. Its visible capture does not preserve the pins for these entries. Consequently, even a strong name match may not prove which exact listing the owner saved.

## Roca Foradada

**Plausible matches**

- **La Foradada, Cantonigròs (L'Esquirol, Osona, Barcelona):** rock opening beside a waterfall and pool on the Riera de les Gorgues. Osona tourism describes a route from Cantonigròs to the waterfall. [Osona Turisme route guide](https://osonaturisme.cat/wp-content/uploads/2026/03/osona-turisme-rutes-OSONA-ESP-GB-fi.pdf)
- **Roca Foradada, Foradada (Noguera, Lleida):** rock formation directly above the village, with steps and a nearby Sant Urbà viewpoint. [Foradada municipal tourism](https://www.foradada.cat/turisme/rutes-turistiques/rutes-turistiques-i-culturals-1/foradada)
- **Roca Foradada, Capafonts (Tarragona):** natural arch on the Puntal del Colomer, reached from Prades. [Muntanyes de la Costa Daurada](https://www.muntanyescostadaurada.cat/es/la-roca-foradada)
- **Roca Foradada / natural arch of Bruguers, Gavà (Barcelona):** a sandstone rock arch in the Garraf area. [Turisme Baix Llobregat](https://www.turismebaixllobregat.cat/es/node/11068)
- **La Cadireta and Roca Foradada, Montserrat (Barcelona):** a distinctive rock formation accessed by a mountain route. [Fundació Catalunya La Pedrera route leaflet](https://www.fundaciocatalunya-lapedrera.com/sites/default/files/2020-07/MCM_fullet-mapa-eng.pdf)

**Most likely:** La Foradada at Cantonigròs. It is a well-known named natural attraction and fits the surrounding waterfall/nature names in the imported list, but list order alone is weak evidence.

**Confidence:** 40% (low). Several real attractions share this name; the classification file does not retain a locality or individual pin.

**Needed to confirm:** individual Google Maps place URL or coordinates; alternatively the province/town, or confirmation that the intended feature is the waterfall and pool at Cantonigròs.

## Salt de la Coromina

**Plausible matches**

- **Salt de la Coromina, Falgars d'en Bas / Vall d'en Bas (Garrotxa, Girona):** waterfall on the Fluvià near Falgars d'en Bas; the named waterfall and viewpoint are shown in local hiking references. [Salt de la Coromina route reference](https://ichn-garrotxa.iec.cat/wp-content/uploads/2020/02/Guia-excursions-naturalistes-Garrotxa-3a-part.pdf), [Vall del Ges i el Bisaura](https://www.vallgesbisaura.com/territori/cascades-i-salts-daigua/salts-daigua-salt-de-la-coromina-al-riu-fluvia/)
- **Mirador del Salt de la Coromina:** a nearby overlook of that same waterfall, potentially a distinct saved pin from the waterfall itself. [Map listing/context](https://mapcarta.com/es/N1682163241)

**Most likely:** the waterfall in the Vall d'en Bas/Falgars d'en Bas area. The exact name is a close match, and the source list places it among Catalan nature destinations.

**Confidence:** 75% (medium-high) for the waterfall area; 55% for whether the saved place is the waterfall or its viewpoint.

**Needed to confirm:** individual Maps URL or pin coordinates; confirm whether the saved item is the waterfall, viewpoint, or trail access point.

## Cueva de los Arcos

**Plausible matches**

- **Cova dels Arcs / Cueva de los Arcos, Cala del Moraig, El Poble Nou de Benitatxell (Alicante):** coastal sea cave and natural arches by Cala Moraig. A visitor listing uses the Spanish name “Cueva de los Arcos” for Benitatxell. [Benitatxell listing](https://www.tripadvisor.es/Attraction_Review-g1627817-d25321606-Reviews-Cueva_De_Los_Arcos-Benitachell_Costa_Blanca_Province_of_Alicante_Valencian_Comm.html)
- **Cueva de los Arcos, Aldeaquemada (Jaén):** a rock-shelter/cave with prehistoric rock art, referenced among sites in the municipality. [Jaén Paraíso Interior](https://www.jaenparaisointerior.es/en/w/arte-rupestre)
- **Other local “Cueva de los Arcos” / “Cova dels Arcs” names:** the phrase describes a common cave/arch formation and is not unique without a locality.

**Most likely:** Cova dels Arcs at Cala del Moraig, Benitatxell. The Spanish label and the visible Maps type “attraction” with a substantial review count fit a recognized coastal attraction; the source list gives no province to establish that match.

**Confidence:** 60% (medium).

**Needed to confirm:** individual place URL or coordinates; confirm whether this is a sea cave at Cala Moraig or the rock-art site at Aldeaquemada. If the former, confirm that the intended listing represents the cave rather than Cala Moraig beach or a diving access point.

## Miradouro da Serpente do Medal

**Plausible matches**

- **Miradouro da Serpente do Medal, near Estevais/Meirinhos, municipality of Mogadouro, Bragança, Portugal:** natural viewpoint overlooking the Sabor reservoir landscape. Several routes describe access from Estevais; one source distinguishes an upper viewpoint from the main viewpoint. [Mogadouro municipal financial record mentioning the project](https://www.mogadouro.pt/cmmogadouro/uploads/document/file/3001/demonstracoes_financeiras.pdf), [route description](https://www.vagamundos.pt/miradouro-da-serpente-do-medal/)
- **A nearby upper/secondary overlook with a similar label:** route accounts refer to a “miradouro superior,” so two close map pins may be confused.

**Most likely:** the named natural viewpoint near Estevais in Mogadouro, Portugal. The exact unusual name is distinctive; the destination record's country and municipality clues agree.

**Confidence:** 85% (high) for the named destination; 65% for the exact saved viewpoint pin.

**Needed to confirm:** individual Maps URL or coordinates and whether the pin denotes the principal overlook or its upper/secondary viewpoint. The existing `Mogadouro` municipality clue should be retained as a clue, not treated as proof of the pin.

## Columpio de Riaño

**Plausible matches**

- **Columpio at Mirador de Las Hazas, Riaño (León):** the town’s official website identifies the swing as being at Mirador de Las Hazas, at about 1,200 m, above Riaño and the reservoir. [Ayuntamiento de Riaño](https://www.aytoriano.es/ayuntamiento/noticias/)
- **The nearby Mirador Alto de Valcayo:** a separate viewpoint on the same hillside, sometimes grouped with the swing in visitor accounts. [Ayuntamiento of Riaño map](https://www.aytoriano.es/export/sites/aytoriano/galerias/descargas/turismo/mapa_completo_web.pdf)
- **Other swings in the Riaño mountain region:** the general label could point to another local installation, though no equally strong candidate is indicated by the imported name.

**Most likely:** the swing at Mirador de Las Hazas in Riaño. This matches the exact name and the municipality’s own description.

**Confidence:** 90% (high) for the attraction; 70% for the precise pin/approach point.

**Needed to confirm:** individual Maps URL or coordinates; clarify whether the saved point is the swing, the nearby Alto de Valcayo viewpoint, or a parking/trail access point.

## Cares

**Plausible matches**

- **River Cares (Río Cares):** the Maps capture labels the entry as a river. Asturias Tourism describes the river as rising in Valdeón (León), flowing mainly through Asturias, and joining the Deva at Panes. [Turismo Asturias — River Cares](https://www.turismoasturias.es/en/descubre/naturaleza/otros-espacios/rios/rio-cares)
- **Ruta del Cares (PR-AS 229):** a distinct hiking route between Poncebos (Asturias) and Caín (León), through the Cares gorge. The official route page reports its route details and current closure notice. [Turismo Asturias — Ruta del Cares](https://www.turismoasturias.es/en/senderismo/rutas/montaneros/ruta-del-cares)
- **A specific river access, gorge viewpoint, or trailhead:** the short label may refer to a point along either the river corridor or hiking route.

**Most likely:** the river as the named Maps destination, because the supplied capture explicitly showed the Maps type as “river.” Do not transfer the Ruta del Cares hiking facts onto that river record without confirming the intended scope.

**Confidence:** 65% (medium) for river-vs-route interpretation; low for the exact visitor point.

**Needed to confirm:** individual Maps URL or coordinates; owner confirmation whether the saved item means the river, the Ruta del Cares, or a particular access/viewpoint. If it is the route, confirm the intended endpoint and recheck official closure status before any visit use.

## La Vall d'Uixó

**Plausible matches**

- **La Vall d'Uixó municipality/town (Castellón):** the imported list shows a province-level geographic entry, consistent with a town destination.
- **Coves de Sant Josep:** the municipality's major visitor attraction, a navigable underground river cave in the Paraje de Sant Josep. The official local tourism site treats it as a specific attraction with ticket purchase, separate from the municipality record. [Official Coves de Sant Josep visitor page](https://turismolavallduixo.es/coves-de-sant-josep/), [municipal visitor information](https://turismolavallduixo.es/venir/informacion-practica/)
- **Other nature/trail destinations in the municipality:** the municipal tourism office also describes local walking routes and natural areas.

**Most likely:** La Vall d'Uixó town/municipality as the saved-list identity, with Coves de Sant Josep a likely reason for saving it rather than an interchangeable identity. The visible saved name is the town name, not the cave attraction.

**Confidence:** 80% (high) for town identity; 55% that the owner's intended experience is the caves.

**Needed to confirm:** individual Maps URL or coordinates and whether to keep a town-level record or create/link a separate Coves de Sant Josep destination record.

## CONIL DE LA FRONTERA

**Plausible matches**

- **Conil de la Frontera town/municipality (Cádiz):** the exact displayed name is the municipality; its official tourism page describes the town and its beaches and routes. [Ayuntamiento de Conil tourism](https://www.conildelafrontera.es/areas-y-servicios-municipales/turismo)
- **An apartment complex or accommodation listing named “Conil de la Frontera”:** the supplied Maps capture displayed the type “apartment complex,” which indicates the saved pin may be lodging rather than the town centre.
- **A broad area/search result for the town:** a Maps result can show a geographic place name while associating the selected pin/category with a lodging property.

**Most likely:** unresolved. Name favors the municipality; the displayed category favors a lodging listing. Neither clue safely overrides the other.

**Confidence:** 45% (low) for the town record as the saved pin; 50% for an accommodation listing. These estimates express the conflict, not independent measured probabilities.

**Needed to confirm:** the individual Maps listing URL or coordinates, its full listing title/address, or owner confirmation whether the saved item means the town or a particular accommodation. Do not retain the `City` classification as a settled identity until confirmed.

## Zumaia

**Plausible matches**

- **Zumaia town:** the general geographic destination named in the list.
- **Flysch coastline / Basque Coast Geopark around Zumaia:** a geological coastal visit, with routes, interpretation, and boat experiences associated with Zumaia. [Zumaia tourism — geological heritage](https://zumaia.eus/es/turismo/que-hacer/planes/1-patrimonio-geologico), [official Flysch tour](https://zumaia.eus/en/tourism/agenda/flysch-tour)
- **A specific town beach, lookout, visitor centre, or harbour point:** none is identified by the imported town label.

**Most likely:** Zumaia as the town-level destination. The Flysch coastline is a strong likely interest/theme, but should be a linked experience rather than silently substituted for the town identity.

**Confidence:** 75% (medium-high) for the town; 55% that the owner intended the geological coastline specifically.

**Needed to confirm:** individual Maps URL or coordinates, or owner confirmation of whether the desired destination is town-centre exploration, the Flysch coast/geopark, or a specific access/interpretation point.

## Salt de Sallent

**Plausible matches**

- **Salt de Sallent, Rupit i Pruit (Osona, Barcelona):** waterfall on the Riera de Rupit, approximately 3 km from Rupit. This is the location identified in the existing draft record and supported by the municipality and Catalonia tourism sources. [Ajuntament de Rupit i Pruit](https://www.rupitpruit.cat/turisme/llocs-dinteres/riera-de-rupit-i-salt-del-sallent.html), [Catalunya Turisme](https://catalunyaturisme.cat/salt-de-sallent/)
- **Other waterfalls with similar names, including Salto de Sallent in Sallent de Gállego (Huesca):** a possible name collision if the pin lacks the Catalan locality.

**Most likely:** Salt de Sallent in Rupit i Pruit. The existing draft's locality and matching municipal source support it, but the shared-list URL does not prove that this is the saved pin.

**Confidence:** 85% (high) for Rupit i Pruit; 65% until checked against the original individual listing.

**Needed to confirm:** individual Maps URL or pin coordinates. If it resolves to Rupit i Pruit, retain that identity; otherwise distinguish the other waterfall explicitly by municipality/province.

## Aracena

**Plausible matches**

- **Aracena town/municipality (Huelva):** the exact imported name and province clue.
- **Gruta de las Maravillas:** major cave attraction within the town; its municipal page identifies it as an urban visitor attraction. [Ayuntamiento de Aracena — Gruta](https://www.aracena.es/es/municipio/gruta/)
- **Castillo/recinto fortificado and historic centre:** another discrete visitor experience within Aracena, separately described in municipal heritage information. [Ayuntamiento de Aracena — historic heritage route](https://www.aracena.es/es/municipio/puntos-de-interes/ruta-patrimonio.html)

**Most likely:** Aracena town as the saved geographic identity. The cave and castle are plausible intended activities, but both are individual attractions and should not be presumed to be the pin represented by the town name.

**Confidence:** 85% (high) for the town; 45% for which specific activity prompted the save.

**Needed to confirm:** individual Maps URL or coordinates; owner confirmation whether the collection should retain a town record with related attractions or refer to a specific attraction.

## Cases that are possible name collisions versus confirmed duplicates

No duplicate pair is established by the available list. The most plausible collision candidates are **Roca Foradada** (multiple distinct Catalan formations) and **Salt de Sallent** (waterfalls in different municipalities). They should remain separate candidate identities until the individual saved-place pins are compared. `Cueva de los Arcos` also has more than one plausible real-world match, but no pair of imported rows is shown to be a duplicate.

## Confirmation data that resolves most cases

For each unresolved entry, the most useful single item is the individual Google Maps place URL. If unavailable, provide the saved pin coordinates or a screenshot showing the pin on the map and its locality. For broad-area entries, also specify the intended visitor scope (town, attraction, route, viewpoint, or access point). The shared-list URL alone does not resolve these identities.
