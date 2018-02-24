## B003725 Intelligenza Artificiale a.a.2017/2018,CdL Ingegneria Informatica Firenze Semola Rudy (5595074)
# Inferenza in grafi orientati
Lo scopo di questo progetto è quello di implementare l'algoritmo di inferenza per grafi oriantati basato sul Junction Tree e confrontare i risultati ricavati con quelli ottenuti da Hugin usando la stessa rete.

## Prerequisiti

Per poter eseguire correttamente il codice sono necessari:

* [Numpy](http://www.numpy.org/) necessario ad eseguire le operazioni sulle tabelle.
* [pbnt](https://github.com/achille/pbnt) (in particolare il modulo Distribution) libreria usata per implementare i CPT delle variabili della rete, le tabelle (potenziali) dei nodi del Junction Tree e per determinare da esse la probabilità marginale delle variabili.
* [Hugin Educational](https://www.hugin.com/index.php/hugin-explorerhugin-educational/) software dove si confrontano i risultati.

## Breve descrizione per usare il codice 
Viene modulato in cinque file: "main.py", "InferenceEngine.py", "JTree.py", "NodeJT.py", "Variable.py".
 Per eseguire il programma andare nel "main.py". All'interno di tale modulo troviamo:
 
* istanze dei tre JunctionTree usati a titolo di esempio costruiti grazie alle funzioni built nel modulo "InferenceEngine.py",
* istanza della classe interfaccia HuginClass del modulo "InferenceEngine.py"

```python
    jt = InferenceEngine.built_jt_fire()
    inference = HuginClass(jt)
```

* Si utilizza tale interfaccia e i suoi metodi per rendere il JunctionTree inizializzato e consistente,inserire evidenza e progagarla, calcolare la probabilità marginale della variabile

```python
    inference.set_consistency_jt()
    inference.enter_evidence("Fire", True)
    var = inference.jt.get_var_cluster("Fire")
    pr = inference.get_prob(var)
```

## Riferimenti

Nella realizzazione del progetto sono stati consultati:

* [Artificial Intelligence: A Modern Approach 3rd edition](http://aima.cs.berkeley.edu//) di  Stuart Russell and Peter Norvig,Pearson 2010 
* [Bayesian Reasoning and Machine Learning](http://www.cs.ucl.ac.uk/staff/d.barber/brml/) di D. Barber, Cambridge University Press 2012.
* [Inferenza in reti bayesiane](https://www.google.it/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwjuk_jqvL_ZAhVMyKQKHT9KCkYQFggtMAE&url=http%3A%2F%2Fdigilander.libero.it%2Fsauromenchetti%2Fexams%2Fbn.pdf&usg=AOvVaw110idIIinEeXCwwY134nss) di Sauro Menchetti
* [Introduction to Bayesian Networks ](http://ai.dinfo.unifi.it/teaching/ai15/jens.zip) di Jensen
