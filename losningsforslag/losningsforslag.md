# Lösningsförslag Lokalisering i aktivitetsbaserad verksamhet.

## Tekniker - Android Applikation
Denna applikation ska populera en databas med referenspunkter för att kunna positionera
enheter i nätverket. Pre-användning av systemet.

## Den store och otroliga databasen
SQL-Databas som ska hålla data om:
* referenspunkter i nätverket för positionering
* Användare
* Användares relation till referenspunkterna

## Ett Python script som körs av Användare
När man startar scriptet som körs av användare av systemet ska detta ske:
1. Den promptar med ett användarnamn/userid
2. Den startar en anslutning till databasen där den lämnar uppgifter i relation till
referenspunkter som redan är definierade (detta ska ske med 5-10minuters mellanrum)
3. Den går till sajten som vi byggt som i anslutning med databasen presenterar intressant information.


## Web applikation för presentation av data från databasen
* Den visar den aktuella positionen för användare som har delat med sig av det.
* den sköter också algoritmer för att visa den ungefärliga positionen av arbetare.
### (Utbyggnad)
* Den visar historik utifrån medarbetares tidigare position.


## Intressant information:
Bygga windows paketerad executable:
![alt text](pyinstaller.png)
<!-- https://stackoverflow.com/questions/5458048/how-to-make-a-python-script-standalone-executable-to-run-without-any-dependency#5458807 -->

Öppna en hemsida från ett script:
![alt text](openwebpage.png)

Skanna wifi info från python på windows(kanske vore bra med stöd både på windows och ubuntu, men viktigt med WINDOWS):
![alt text](windowswifiscan.png)
<!-- https://stackoverflow.com/questions/31868486/list-all-wireless-networks-python-for-pc -->
