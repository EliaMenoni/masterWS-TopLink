# Test
La cartella racchiude tutti i documenti e le procedure necessarie a testare le funzionalita' degli end point della LDO

## Struttura cartelle
```
Test
├─── http_requests
│    ├─── RESPONSE // Raccolta delle risposte dei Test
│    │    ├─── OK
│    │    └─── KO
│    │
│    ├─── TEST_OK.http // Test automatici per i casi OK
│    └─── http-client.env.json // Settings ambieni di test
│    
└─── test_generator
     └─── OK // Raccolta dei Test ok da file XLS
          ├─── TestX // Informazioni del test numero X
          |    ├─── src.txt // Struttura in formato testuale originata dal file XLS
          .    ├─── test.json // Struttura JSON da inviare come body alla richiesta di test
               └─── testX.xml // Corrispettivo XML del test.json
```