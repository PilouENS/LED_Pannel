# LED_Pannel

Petit projet de rétro-ingénierie d’un panneau LED industriel (connecteur HUB73).  
L’objectif : afficher des images/motifs à distance en pilotant le panneau via une STM32, avec une petite interface PC côté utilisateur. 

Toutes les infos dans `CR_Panneau_LED.pdf`

## Arborescence

- **STM32/** – Deux projets STM32CubeIDE  
  - `comm_IP` : toute la partie communication IP (UDP) avec configuration réseau.  
  - `envoie_panneau` : mapping des GPIO et traduction des données reçues vers les signaux HUB73.  
  (À fusionner quand il restera un peu de temps !)  
- **Envoie données/** – `interface_graphique.py` : petite GUI Tkinter qui envoie, via UDP, le nom de l’image et les canaux RGB à afficher. :contentReference[oaicite:2]{index=2}  
- **LPC804/** – Ancien essai avec un NXP LPC804 (rapport PDF).  
- **datasheet_composants/** – Datasheets utiles pour le panneau et les buffers. :contentReference[oaicite:3]{index=3}  

Projet à continuer pour une utilisation et prestation.


Merci A.Juton et P.Varoqui pour l'accompagnement 
