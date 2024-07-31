# ScriptStack
Her finner du en samling med scripts som primært omhandler Lepton API'et til TIHLDE.

## 🚀 Kom i gang
For å kjøre programmene trenger du å ha Python installert. I tillegg vil Make gjøre det lettere å kjøre programmene, men de kan kjøres uten.

```Make
# Sett opp et lokalt repo
git clone https://github.com/TIHLDE/ScriptStack.git

cd ScriptStack

# Med Make
make install

# Uten Make
pip install -r requirements.txt
```

## ⚙ Konfigurasjon
For å kjøre programmene mer effektivt anbefaler vi å legge ved din TIHLDE Lepton API token i en .env fil. Du kan se i .env.example hvilke variabler som er nødvendig.

```
TIHLDE_API_TOKEN=your_token_here
ENVIRONMENT=PROD
```

Hvis du ikke har lagt ved TIHLDE_API_TOKEN, vil du bli promptet for en token hver gang du kjører et program.

### Hvordan få tak i din TIHLDE API token
Lepton benytter seg av en statisk token, som du kan finne ved å lese en cookie fra [tihlde.org](https://tihlde.org).

1. Høyre klikk på skjermen (inne på nettsiden), og trykk på "Inspiser".
2. Det vil åpne seg et panel til høyre, eller i bunnen av skjermen. Trykk på "Applications" menyen. Du må nok trykke på ">>" for å finne den.
3. Trykk på "Cookies" og velg cookies for tihlde.org. 
4. Verdien til "TIHLDE-AccessToken" er din API token.

OBS! Siden din token er statisk, betyr dette at enhver person som har tilgang på din token, kan gjøre API kall på vegne av deg i all evighet. Så vær forsiktig med å ikke dele din token.


## ⚡ Kjør programmer
For å kjøre programmer kan du bruke følgende kommandoer:

```Make
# Hent ut tilgjengelige programmer
make list

# Hent ut en beskrivelse av et program
make describe="your_selected_script"

# Kjør et valgt program
make args="your_selected_script"
```

Hvis du ikke har Make:

```python
# Hent ut tilgjengelige programmer
python list.py

# Hent ut en beskrivelse av et program
python describe.py "your_selected_script"

# Kjør et valgt program
python main.py "your_selected_script"
```

## ❤ Resultater
Første gang du kjører et program så vil det bli laget en mappe som heter "downloads" i mappen din. Hvis et program henter ut informasjon, vil filen bli lastet ned her.


