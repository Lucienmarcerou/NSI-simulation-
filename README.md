Voici une description détaillée en français, prête à être utilisée sur GitHub :

---

# Simulation de la Trajectoire d'un Projectile avec Résistance de l'Air

Ce projet consiste en une simulation numérique de la trajectoire d'un projectile, tenant compte à la fois de la gravité et de la résistance de l'air. Le code est organisé de manière modulaire et se divise en plusieurs parties, permettant de comprendre, modifier et étendre facilement la simulation.

## 1. Importation des Bibliothèques et Fichiers Externes

Le script débute par l'importation des bibliothèques essentielles :

- **`math`** : Fournit les fonctions mathématiques de base (trigonométrie, exponentielle, etc.), indispensables pour le calcul des positions.
- **`matplotlib.pyplot`** : Permet de tracer des graphiques pour visualiser les résultats de la simulation (courbes du mouvement et trajectoire).

## 2. Définition des Fonctions

### Fonctions de Calcul

- **`z(Z0, ms, k, V0z, K, t)`**  
  Calcule la position verticale du projectile à un instant `t`. La fonction intègre un terme d'exponentielle décrivant la décroissance due à la résistance de l'air, combiné avec l'effet constant de la gravité modifié par le coefficient de frottement `k`.

- **`x(X0, ms, k, v0x, t)`**  
  Calcule la position horizontale à l'instant `t`. Comme pour la fonction verticale, ce calcul prend en compte la résistance de l'air qui diminue progressivement l'influence initiale de la vitesse horizontale.

### Fonctions Utilitaires

- **`Affichage(i, xmin, xmax, xm)`**  
  Permet d'afficher de manière formatée dans la console les informations de simulation pour chaque itération : numéro d'itération, temps, position horizontale et position verticale.

- **`recherche_zero(xmin, xmax, epsilon)`**  
  Réalise une recherche dichotomique pour déterminer le temps `t` auquel le projectile atteint le sol (lorsque la position verticale devient nulle). La précision de la recherche est contrôlée par la variable `epsilon`.

## 3. Corps Principal du Script

### Initialisation des Variables

Les paramètres initiaux du projet sont définis dès le début :

- **Conditions Initiales :**
  - Vitesse initiale (`V0`) et angle de tir (`O0`, converti en radians).
  - Positions initiales en `x` et en `z` (par exemple, `x0` et `Z0`).
  
- **Paramètres Physiques :**
  - Masse du projectile (`ms`) et des densités associées (solide et fluide).
  - Coefficient de frottement (`k`) et accélération due à la gravité (`g`).
  - Calcul d'une masse équivalente pour le fluide et détermination du paramètre `K` influencé par la résistance de l'air.

### Détermination Dynamique de l'Intervalle de Temps

Une boucle while ajuste la borne supérieure de l'intervalle temporel (`xmax`) en vérifiant dynamiquement que le projectile a bien atteint le sol. Cela garantit que la simulation couvre toute la durée de vol.

### Boucle de Simulation

Une boucle est exécutée sur 100 itérations pour :
- Calculer et afficher les positions horizontales et verticales à des intervalles réguliers.
- Imprimer les résultats dans un tableau formaté et déterminer avec précision le temps de chute du projectile.

## 4. Visualisation des Résultats (Section Bonus)

Pour mieux comprendre la dynamique du mouvement, le script intègre une partie dédiée à la visualisation :

- **Collecte des Données :**  
  Des listes pour le temps, la position horizontale et la position verticale sont remplies sur 100 points répartis de manière homogène.

- **Graphiques Produits :**
  - **Temps vs. Position Horizontale (`x`) :** Montre l'évolution de la distance parcourue en fonction du temps.
  - **Temps vs. Position Verticale (`z`) :** Visualise le mouvement vertical, illustrant la montée et la descente influencées par la gravité et la résistance.
  - **Trajectoire (`x` vs. `z`) :** Représente graphiquement le trajet complet du projectile, offrant une vue claire de sa trajectoire parabolique modifiée par la friction.

Chaque graphique est accompagné d'un titre explicite et d'axes correctement étiquetés pour faciliter l'interprétation.
