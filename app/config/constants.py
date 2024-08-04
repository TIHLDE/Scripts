

ALLOW_PHOTO_BY_EVENT = """
Dette programmet henter ut informasjon om alle brukere som har plass på et arrangement, og viser om brukeren har tillatt å bli tatt bilde av eller ikke.

Du vil bli spurt om ID til arrangementet for å kunne bruke denne funksjonen. Du finner ID til arrangementet ved å gå til https://tihlde.org/arrangementer, og velge et arrangement. ID til arrangementet vil være tallet i URL-en.

Eksempel på bruk:
make start args="get_registrations_that_allow_photo_by_event"

Husk at du må ha en gyldig API-token og riktig rettigheter for å kunne bruke denne funksjonen.
"""


ALLOW_PHOTO_BY_DEFAULT = """
Dette programmet henter ut informasjon om alle brukere som ikke har tillatt å bli tatt bilde av som standard. Dette vil si at brukeren ikke har krysset av for at de tillater å bli tatt bilde av i arrangementer.

Eksempel på bruk:
make start args="get_users_with_not_allowed_photo_by_default"

Husk at du må ha en gyldig API-token og riktig rettigheter for å kunne bruke denne funksjonen.
"""


CREATE_BINGO = """
Dette programmet genererer bingobrett og slår sammen dem til en PDF-fil. Programmet bruker en liste med setninger som du kan endre i fila 'sentences.txt'. Du finner filen i 'app/scripts/bingo'.

Eksempel på bruk:
make start args="create_bingo_sheets"

Du trenger ingen API-token for å kunne bruke denne funksjonen. Resultatet vil bli lagret i mappen 'downloads'. Hvis du kjører programmet flere ganger, vil det overskrive det gamle bingobrettet. Hvis du vil beholde det gamle bingobrettet, må du flytte det til en annen mappe før du kjører programmet på nytt.
"""


ADD_REGISTRATIONS = """
Dette programmet legger til brukere i et arrangement. Du må legge ved en CSV-fil med brukerinformasjon i filen 'users.csv' i 'app/scripts/events/bulk_add/'. Programmet vil lese filen og legge til brukerne i arrangementet.

Filen skal være i følgende format:
user_id,mame,email

Eksempel på bruk:
make start args="bulk_add_registrations_to_event"

Husk at du må ha en gyldig API-token og riktig rettigheter for å kunne bruke denne funksjonen.
"""


UPLOAD_FILE = """
Dette programmet laster opp en fil til serveren. Du må legge til filen i mappen 'upload' før du kjører programmet.

Eksempel på bruk:
make start args="upload_file"

Husk at du må ha en gyldig API-token og riktig rettigheter for å kunne bruke denne funksjonen.
"""


DELETE_FILE = """
Dette programmet sletter en fil fra serveren basert på url.

Eksempel på bruk:
make start args="delete_file"

Husk at du må ha en gyldig API-token og riktig rettigheter for å kunne bruke denne funksjonen.
"""