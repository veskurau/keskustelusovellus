# Keskustelusovellus

## Kuvaus

Web-sovellus jossa käyttäjät voivat eri aihealueiden sisällä luoda omia viestiketjuja sekä lähettää viestejä omiin ja muiden luomiin viestiketjuihin. 

Sovellus sisältää seuraavia ominaisuuksia:
- Käyttäjärooleja on kahdenlaisia: normaalit käyttäjät ja pääkäyttäjät
- Normaalit käyttäjät voivat:
  - Luoda käyttäjätunnuksen, joka sisältää käyttäjätunnuksen ja salasanan
  - Kirjautua sisään luodulla käyttäjätunnuksella
  - Kirjautua ulos
  - Luoda uuden viestiketjun, joka sisältää otsikon ja aloitusviestin
  - Lähettää viestejä viestiketjuihin
  - Muokata omia viestiketjuja ja viestejä
  - Katsella muiden lähettämiä ketjuja ja viestejä, joissa näkyy viestin lähettäjä ja lähetysaika
  - Hakea hakusanoilla viestejä
- Pääkäyttäjät voivat:
  - Tehdä kaiken mitä normaalit käyttäjät
  - Luoda uusia aihealueita
  - Poistaa aihealueita
  - Muokata ja poistaa kaikkia viestiketjuja ja viestejä
  - Luoda rajattuja aihealueita, joihin vain tietyllä käyttäjäryhmällä on pääsy

## Sovelluksen nykyinen tilanne

- Käyttäjä pystyy etusivulla näkemään lähetetyt viestit sekä niiden lähettäjän ja ajan
- Käyttäjä näkee etusivulla viestien, sivulatausten ja rekisteröityneiden käyttäjien määrä
- Käyttäjä pystyy luomaan uuden tunnuksen, joka koostuu käyttäjätunnuksesta ja salasanasta. Tunnus tallennetaan SQL tietokantaan
- Käyttäjä pystyy kirjautumaan jo olemassa olevilla tunnuksilla
- Jos annettu käyttäjätunnus tai salasana ei täsmää tietokannassa oleviin tietoihin, niin sivu antaa virheen
- Mikäli käyttäjä yrittää luoda käyttäjätunnuksen joka löytyy jo tietokannasta, niin sivu antaa virheen
- Käyttäjätunnus ja salasanakentät ovat pakollisia, käyttäjä saa näistä huomautuksen, jos näitä ei ole syötetty
- Liian pitkistä/lyhyistä salasanoista ja käyttäjätunnuksista annetaan virheilmoitus
- Tietokannassa on taulut users, messages ja visits joihin tallennetaan ja joista haetaan tietoa yllä listattujen toimintojen yhteydessä

## Jatkokehitys

- Lisätä tauluja tietokantaan
- Tehdä tarkastuksia ja varmennuksia verkkosivujen kenttiin, että mitä tietoa käyttäjä voi niihin syöttää
- Parantaa sivujen ulkoasua
- Luoda hakutoiminto
- Luoda eri keskustelualueita
- Luoda pääkäyttäjälle oikeudet muokata jo olemassa olevia tietoja

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