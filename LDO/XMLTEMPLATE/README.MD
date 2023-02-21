# Struttura XML
Il file XML e' scomposto in ogni sua componente in una struttura ad albero su file system

## Categoriazzazione
Ogni file viene riporta come segue:
- numero --> Indica l'ordine dei tag nel XML corrente
> Separato da `.`
- O --> Indica se il componente e' opzionale (se non c'e' e' obbligatorio)
> Separato da `_` 
- nome tag

- Se un file comincia con `.` non viene considerato


### Esempio
- `1_setId.xml` --> Tag obbligatorio da mettere in posizione 1 all'interno del suo blocco
- `2.O_addr.xml` --> Tag **OPZIONALE** da mettere in posizione 2 all'interno del suo blocco

---

Se il file non esiste allora il tag non ha attributi. Se esiste una cartella con lo stesso nome allora quel tag contiene altri elementi