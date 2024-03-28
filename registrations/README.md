# Registering av medlemmer i bulk

Dette scriptet gir brukeren mulighet til å legge til flere brukere på et arrangement. Hvis det er et betalt arrangement, vil brukerne bli registrert med en godkjent betaling. Det er dermed viktig at du gir beskjed til de påmeldte om å betale med vipps manuelt.

## Fremgangsmåte

For å benytte seg av scriptet må følgende gjøres:

* Fylle inn *deltagere.csv* filen (ligger i mappen) med en bruker id per linje for alle brukere som skal legges til.
* Hente din x-csrf-token. Dette kan du finne under cookies til applikasjonsfeltet i devtools til nettleseren. Den heter TIHLDE-AccessToken.
* Hente ut id til arrangementet du ønsker å legge til brukerne på. Id (tallverdi) finner du i url til arrangementet på nettsiden.
* Kjør scriptet med: python main.py \<brukertoken> \<arrangementid>


## Brukere med adgang

For å kunne kjøre dette scriptet må du ha en eller flere av følgende rettigheter:

### Kan utføre scriptet på sine egne arrangementer
* Medlem av undergruppen / komiteen som har opprettet arrangementet.
* Være leder for en interessegruppe som har laget arrangementet.

### Kan utføre scriptet på alle arrangementer
* Medlem av HS
* Medlem av Index