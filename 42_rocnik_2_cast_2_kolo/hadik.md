 Sssssss, tak robia hady
========================

Ako prvé si môj program načíta rozmery mriežky a následne aj jednotlivé kroky hadíka. Potom prechádza cez každý krok. Keďže hadík sa každým kolom zväčšuje, znamená to, že jeho telo ostáva na všetkých predchádzajúcich pozíciách navždy. V každom kroku teda zapíše aktuálne súradnice hlavy hadíka a spätne skontroluje, či už na takomto mieste bol.Ak áno, ide o kolíziu so sebou samým, program sa okamžite ukončí a vytlačí nulu. Ak nie, pokračuje sa ďalej.Zároveň počas tejto simulácie zaznamenávam aj minimálne a maximálne hodnoty súradníc x a y, ktoré slúžia na to, aby som vedel, do akého najmenšieho obdĺžnika by sa celá trasa hadíka dala zmestiť.Na záver vypočítam rozmery tohto obdĺžnika (šírka = max_x - min_x + 1, výška = max_y - min_y + 1). Ak sa tento obdĺžnik nezmestí do zadanej mriežky veľkosti m × n, odpoveď je 0. Inak spočítam, na koľkých rôznych miestach mohol hadík začať tak, aby sa celý jeho pohyb zmestil do mriežky bez toho, aby vyšiel mimo [a = abs(min_x-max_x) +1b = abs(min_y-max_y) +1(m-a+1)*(n-b+1)] — a túto hodnotu vytlačím ako výsledok. 

 
https://www.ksp.sk/ulohy/zadania/2932/