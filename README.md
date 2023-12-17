# Keskustelusovellus

## Kuvaus

Web-sovellus jossa käyttäjät voivat eri aihealueiden sisällä lähetellä viestejä. 

Sovellus sisältää seuraavia ominaisuuksia:
- Käyttäjärooleja on kahdenlaisia: normaalit käyttäjät ja pääkäyttäjät
- Normaalit käyttäjät voivat:
  - Luoda käyttäjätunnuksen, joka sisältää käyttäjätunnuksen ja salasanan
  - Kirjautua sisään luodulla käyttäjätunnuksella
  - Kirjautua ulos
  - Lähettää viestin jo olemassa olevaan aihealueeseen
  - Katsella muiden lähettämiä viestejä, joissa näkyy viestin lähettäjä, lähetysaika, tykkäysten määrä ja mihin minkä aihealueen alle viesti kuuluu
  - Hakea hakusanoilla viestejä
  - Tykätä omista ja muiden viesteistä
  - Suodattaa viestit aihealueiden perusteella
  - Nähdä statistiikkaa viestien, sivulatausten ja käyttäjien määrästä
- Pääkäyttäjät voivat:
  - Tehdä kaiken mitä normaalit käyttäjät
  - Luoda uusia aihealueita

## Sovelluksen nykyinen tilanne

- Käyttäjä pystyy etusivulla näkemään lähetetyt viestit sekä niiden lähettäjän, aihealueen, lähetysajan ja tykkäysten määrän
- Käyttäjä näkee etusivulla viestien, sivulatausten ja rekisteröityneiden käyttäjien määrä
- Käyttäjä pystyy luomaan uuden tunnuksen, joka koostuu käyttäjätunnuksesta, salasanasta ja tiedosta onko käyttäjä ylläpitäjä vai normaali käyttäjä. Tunnus tallennetaan SQL tietokantaan
- Käyttäjä pystyy kirjautumaan jo olemassa olevilla tunnuksilla
- Jos annettu käyttäjätunnus tai salasana ei täsmää tietokannassa oleviin tietoihin, niin sivu antaa virheen
- Mikäli käyttäjä yrittää luoda käyttäjätunnuksen joka löytyy jo tietokannasta, niin sivu antaa virheen
- Käyttäjätunnus ja salasanakentät ovat pakollisia, käyttäjä saa näistä huomautuksen, jos näitä ei ole syötetty
- Liian pitkistä/lyhyistä salasanoista ja käyttäjätunnuksista annetaan virheilmoitus
- Ylläpitäjä voi lisätä uusia aihealueita, mutta normaalilla käyttäjällä ei ole tähän oikeuksia
- Käyttäjät voivat lähettää viestejä, viestien pituus on rajoitettu ja myöskään tyhjiä viestejä ei voida lähettää
- Käyttäjät voivat tykätä viesteistä, yksittäinen käyttäjä pystyy tykkäämään ainoastaan kerran per viesti
- Käyttäjät voivat etusivulla hakea joko vapaalla sanahaulla tai valitsemalla jonkin jo luodun aihealueen, jolloin sivu listaa kaikki hakuosumat
- Tietokannassa on taulut users, messages, visits, topics ja likes joihin tallennetaan ja joista haetaan tietoa yllä listattujen toimintojen yhteydessä
- Koodissa on pyritty huomioimaan mm. SQL-injektiot sekä XSS- ja CSRF-haavoittuvuudet


## Jatkokehitysideoita

- Luoda vielä pari kerrosta lisää rakenteeseen, esimerkiksi: Aihealueet-Viestiketjut-Viestit-Kommentointi viesteihin 
- Parantaa sivujen ulkoasua
- Pääkäyttäjän oikeudet voidaan valita nyt itse rekisteröinnin yhteydessä, todellisuudessa tämä toteutettaisiin eri tavalla
- Luoda pääkäyttäjälle oikeudet muokata ja poistaa jo olemassa olevia tietoja liittyen mm. viesteihin ja käyttäjiin
- Viedä sovellus tuotantopalvelimelle

## Kuinka käyttää ja testata sovellusta komentoriviltä

**1)** Kloonaa repositorio omalle koneellesi

**2)** Luo juurikansioon *.env*-tiedosto ja tallenna sinne seuraava sisältö: 
```bash
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```

**3)** Luo Pythonin virtuaaliympäristö projektikansioon:

```bash
python3 -m venv venv
```

**4)** Käynnistä virtuaaliympäristö:

```bash
source venv/bin/activate
```

**5)** Ympäristön riippuvuudet löytyvät tiedostosta [requirements.txt](./requirements.txt). 
Nämä voit asentaa kerralla:

```bash
pip install -r requirements.txt
```

**6)** Käytössä on Postgres-tietokanta. Skeema löytyy tiedostosta [schema.sql](./schema.sql). Pääset luomaan taulut tietokantaan:

```bash
psql < schema.sql
```

**7)** Tämän jälkeen pääset käynnistämään ohjelman virtuaaliympäristöstä:

```bash
flask run