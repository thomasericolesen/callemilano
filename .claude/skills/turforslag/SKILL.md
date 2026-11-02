---
name: turforslag
description: Lav et turforslag (PDF og mobilvenlig HTML på dansk) for CalleMilano-gæster ud fra et eller flere valgte steder. Fase 2. tools/trip.py plan samler data og tjek, Alpha laver et hurtigt tjek kun hvis nødvendigt, og Ecco skriver. Brug, når værten skriver /turforslag eller beder om et turforslag/dagsplan.
---

# /turforslag (fase 2)

Målet er et turforslag på omkring et minut. Al tung research er lavet i fase 1 (`/aabningstider`,
`/restaurant-indsamling`).

## 1. Dato

Kør `date`. Turdatoer før i dag afvises.

## 2. Spørg kort (kun det, der mangler)

Brug AskUserQuestion på dansk:
1. **Hvilke steder?** Brug `python3 tools/trip.py places` og tilbyd relevante valg. Værten kan også skrive navne.
2. **Hvilken dag?**
3. **Hvem skal med?** Voksne, børns alder, seniorer, nedsat mobilitet.
4. *(valgfrit)* Særlige ønsker.

## 3. Saml data og tjek (script, ingen AI)

```bash
python3 tools/trip.py plan <slugs...> --date ÅÅÅÅ-MM-DD --adults 2 --children 4,9 [--seniors N] [--reduced-mobility] [--wishes "..."] --out trips/<dato>-<første-slug>
```

Scriptet laver vejr, trafik, åbningsstatus, helligdage, restauranter, forslag og automatiske tjek og giver en dom:

| `verdict` | Hvad du gør |
|---|---|
| `blokeret` | Stop, og forklar værten problemet (fx dato i fortiden). |
| `kræver_tjek` | Start **alpha** (tilstand B: hurtigt tjek) med turmappen og listen `needs_quick_check`. Den skriver `hours-check.json`. Er der flere steder, så start én alpha pr. sted parallelt, og flet resultaterne. |
| `ok_med_forbehold` / `ok` | Gå videre. |

## 4. Skriv turforslaget

Start **ecco** med turmappen. Den skriver `trip.json` og laver `turforslag.html` og `turforslag.pdf`.

## 5. Aflever

- Send `trips/<id>/turforslag.pdf` til værten (SendUserFile, hvis det findes) eller giv stien. HTML-filen er
  mobilvenlig og kan også sendes.
- Fortæl kort: dagens plan i 3 linjer, forbehold og huller. Ved restauranthuller foreslås
  `/restaurant-indsamling`; ved Alphas noter til redaktøren foreslås `/aabningstider`.
- `trips/` er udelukket fra git (gæstedata); intet skal committes.
