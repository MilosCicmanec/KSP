Na riešenie prvej úlohy som využil v Pythone zásobník . 
Program funguje nasledovne – vytvoríme si prázdny stack a vstupný reťazec si rozdelíme na jednotlivé znaky (charaktery). Následne pomocou for loop prechádzame každý znak zo vstupu a pri každom kroku sa pozrieme na vrchný prvok zásobníka. 

Ak sa na vrchu zásobníka nachádza znak, ktorý spolu s aktuálnym znakom tvorí dvojicu "PC" alebo "CP", tieto znaky sa navzájom vyrušia – čiže zrušíme túto dvojicu pomocou pop(). 

Ak takáto dvojica nevzniká, jednoducho pridáme aktuálny znak na vrch zásobníka pomocou append(). 

Tým, že prechádzame celý vstup iba raz a vykonávame konštantné operácie append alebo pop, má náš algoritmus: 

    -časovú zložitosť O(n), 

    -priestorovú zložitosť tiež O(n) – a to v najhoršom prípade, keď sa žiadne znaky nevyrušia a všetky zostanú v zásobníku. 

 
