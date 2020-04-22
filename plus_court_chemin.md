# Plus court chemin (difficile)

Critères de notation:

* Difficulté du sujet choisi 
* Lisibilité du code
* Effort de groupe, au moins 1 commit par membre du groupe (pas de commit = pas de note!)

## Enoncé du problème

La **recherche de chemin**, couramment appelée _**pathfinding**_, est un problème de l'intelligence artificielle qui se rattache plus généralement au domaine de la planification et de la recherche de solution. Il consiste à trouver comment se déplacer dans un environnement entre un point de départ et un point d'arrivée en prenant en compte différentes contraintes.

Une application classique au quotidien est la recherche du plus court chemin pour se rendre d'un point A à un point B en voiture.

## Modélisation

On peut modéliser le réseau routier sous la forme d'un [graphe](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_graphes#Graphe). Les nœuds représentent des intersections de routes et chaque arc du graphe est associé à un segment de route entre deux intersection.

Exemple :

![Réseau Routier](https://github.com/datalyo-dc-m1/algorithmie-data/blob/master/attachments/graphe_lyon.png)

On souhaite implémenter le problème comme suit : 
- une classe `RoadNetwork` qui modélise le réseau routier
- une classe `Road` qui modélise une route entre deux intersections

On numérotera les intersections de 0 à `n`.

Un réseau routier est composé d'une liste de routes et d'un nombre d'intersections.

Une route possède plusieurs attributs : 

 * deux numéros de intersection indiquant les 2 extrémités de la route
 * une distance en mètre indiquant la longueur de la route

La classe `RoadNetwork` possède deux méthodes : 

* `get_neighbours` qui prend en paramètre un numéro d'intersection et renvoie la liste des intersections voisines (deux intersections sont voisines si il existe une route directe qui les relie).
* `get_distance` qui prend en paramètre 2 numéros d'intersections voisines et renvoie leur distance en mètre.

## Implémentation

Le but de l'exercice est d'implémenter la méthode `shortest_path` qui:
 
* prend en paramètre deux numéros d'intersections `origin` et `destination` 
* renvoie la distance du chemin le plus court

On utilisera l'**algorithme de Dijkstra** pour résoudre ce problème.

### Principe

L'algorithme se base sur les propriétés mathématiques du graph (qu'on ne détaillera pas ici).

Le principe général est le suivant:

* on considère le réseau routier comme un graph: 
    * les intersections sont les noeuds du graph
    * les routes sont les arêtes
    * la longueur des routes sont les poids des arêtes

* les noeuds `origin` et `destination` sont reliés par plusieurs arêtes (les routes): on appelle cela un chemin

* la distance entre 2 intersections correspond à la somme du poids des arêtes qui composent le chemin entre les noeuds `origin` et `destination`  

*Exemple*

Plus court chemin du intersection pour aller du intersection `0` au intersection `4`: 

![Dijkstra](https://github.com/datalyo-dc-m1/algorithmie-data/blob/master/attachments/dijikstra_shortest.png)

La distance la plus courte est ici: 21 (8 + 1 + 2 + 10)

L'algorithme de Dijkstra consiste à chercher le plus court chemin en découpant le graph en sous-graph.

Avant de vous lancer dans l'implémentation, je vous conseille de lire l'exemple qui illustre le principe de l'algorithme sur sa page [Wikipedia](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra)

### Algorithme

On se propose d'implémenter une version simplifiée de l'algorithme de Dijkstra.

On calculera la distance la plus courte entre 2 intersections `origin` et `destination`.

L'algorithme prend en entrée un réseau routier (qui peut être vu comme un graph d'intersections) et une intersection d'origine.

Il s'agit de construire progressivement une liste d'intersections classées en fonction de leur distance minimale à l'intersection d'origine (de la plus proche à la plus lointaine).

La distance correspond à la somme des longueurs des routes empruntées.

Au départ:

* la liste des intersections triées est vide
* on considère que toutes les distances sont infinies, sauf pour l'intersection d'origine pour laquelle la distance est 0

Soit `n` le nombre d'intersections du réseau routier. On va donc avoir besoin d'initialiser deux listes :
 
* une liste `sorted_intersections` qui contient les intersections triées:
    * on l'initialise à vide
    
* une liste `min_distances` de taille `n` telle que :

    * `min_distances[i]` représente la distance minimale entre les intersections `origne` et `i` (où `i` désigne un numéro de intersection quelconque)
    
    * on initialise cette liste de la manière suivante:
        * si `i` == `origine`: `min_distances[i]` est égal 0
        * sinon `min_distances[i]` est égal à `sys.maxsize` (où `sys.maxint` représente la plus grande valeur que peut prendre un entier en Python).
 
**Déroulement de l'algorithme :**

Tant qu'il reste des intersections à trier:

* Sélectionner une intersection `i` à trier telle que:

    * `i` n'a jamais été triée (il n'est pas présent dans la liste `sorted_intersections`)
    * `i` est la plus proche intersection de `origin` parmi les intersections non triées (on prendra la plus petite valeur non traitée dans la liste `min_distances`)
    
* Ajouter `i` à la liste des intersections triées `sorted_intersections`

* Pour chaque intersection `v` voisine de `i` **non triée** :

	* On met à jour la distance minimale entre `v` et l'origine de la manière suivante :
	    * Soit `distance_v_i` la distance entre les intersections voisines `v` et `i`
	    * Si `min_distances[v]` > `distance_v_i` alors on met à jour la distance minimale de v (soit `min_distances[v] = distance_v_i + min_distances[i]`)

Finalement, on retourne la distance minimale entre `destination` et `origin`: `min_distances[destination]`

_N.B_:

On pourra s'aider du jeu de tests en **Annexes** pour vérifier la bonne implémentation de cette méthode.

## Tests unitaires

Ecrire des tests unitaires vérifiant le bon fonctionnement des méthodes implémentées.

## Annexes

Jeu de tests pour la méthode `shortest_path` :

```python
import unittest


class RoadNetworkTest(unittest.TestCase):

    def test_shortest_path(self):

        roads_list = [
            Road(0, 1, 4),
            Road(0, 7, 8),
            Road(1, 7, 11),
            Road(1, 2, 8),
            Road(7, 8, 7),
            Road(7, 6, 1),
            Road(2, 8, 2),
            Road(8, 6, 6),
            Road(2, 3, 7),
            Road(2, 5, 4),
            Road(5, 6, 2),
            Road(3, 5, 14),
            Road(3, 4, 9),
            Road(4, 5, 10)
        ]

        network = RoadNetwork(roads_list, 9)

        self.assertEqual(network.shortest_path(0, 0), 0)
        self.assertEqual(network.shortest_path(0, 1), 4)
        self.assertEqual(network.shortest_path(0, 2), 12)
        self.assertEqual(network.shortest_path(0, 3), 19)
        self.assertEqual(network.shortest_path(0, 4), 21)
        self.assertEqual(network.shortest_path(0, 5), 11)
        self.assertEqual(network.shortest_path(0, 6), 9)
        self.assertEqual(network.shortest_path(0, 7), 8)
        self.assertEqual(network.shortest_path(0, 8), 14)
```
