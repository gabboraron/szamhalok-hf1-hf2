# Feladat1
Az Alexa - top - 1 M adathalmaz tartalmazza a legnépszerűbb 1 millió website domain nevét népszerűségi sorrendben
http://s3.amazonaws.com/alexa-static/top-1m.csv.zip
Válasszuk ki az első és utolsó 10 nevet a listából, írjunk egy python programot, ami végig megy a leszűkített 20 elemű listán és minden címre lefuttatja a traceroute és ping toolokat, majd az eredményeket rendezett formában két fájlba írja!
Ld.subprocess!!!
Lehetőség szerint ne az egyetemi hálózaton futassuk az adatbegyűjtést!
Traceroute paraméterek:max 30 hopot vizsgáljunk
Ping paraméterek: 10 próba legyen 
Program paraméterezése:./programom.py<top-1m.csvelérésiútja>

# Feladat2
- Futtatás : python3 client.py cs1.json
- A paraméterben kapott json fileban szerepel a szimuláció paraméterei. Lásd gyakorlat slideok.
- A kiíratás egyezzen meg a gyakorlaton megadott módon:

    - <esemeny azonosító>. <esemény név>: <node1><-><node2> st:<szimuálciós idő> [- <sikeres/sikertelen>]
    - pl: 1. igény foglalás: A<->B st:2 - sikeres
    - pl: 2. igény felszabadítás: A<->B st:3

Adott a cs1.json, ami tartalmazza egy irányítatlan gráfleírását. A gráf végpont(end-points) és switch(switches) csomópontokat tartalmaz. Az élek(links) kapacitással rendelkeznek(valósszám). Tegyük fel, hogy egy áramkörkapcsolt hálózatban vagyunk és valamilyen RRP-szerű erőforrás foglaló protokollt használunk. Feltesszük, hogy csak a linkek megosztandó és szűk erőforrások. A json tartalmazza a kialakítható lehetséges útvonalakat(possible-cicuits), továbbá a rendszerbe beérkező, két végpontot összekötő áramkörigényeket kezdő és végidőponttal. A szimuláció a t=1 időpillanatban kezdődik és t=duration időpillanatban ér véget. Készíts programot, ami leszimulálja az erőforrások lefoglalását és felszabadítását a JSON fájlban megadott topológia, kapacitások és igények alapján! A program bemenete: cs1.json (első parancssori argumentum) A program kimenete: Minden igény lefoglalását és felszabadítását írassuk ki a stdout-ra. Foglalás esetén jelezzük, hogy sikeres vagy sikertelen volt-e. Megj.: sikertelen esetben az igénnyel más teendőnk nincs, azt eldobhatjuk
