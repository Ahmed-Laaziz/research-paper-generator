# Contexte général du projet
Le contexte général de ce projet est centré sur la création d'un outil basé sur le traitement automatique du langage naturel (NLP) pour aider les chercheurs et les auteurs à rédiger des articles scientifiques de manière plus efficace et précise. L'objectif est de simplifier le processus de rédaction tout en garantissant la qualité et la cohérence des articles scientifiques. 

# FastAPI

Le choix de FastAPI offre plusieurs avantages pour le développement d'applications Web, en particulier dans le contexte des API RESTful et des microservices. Voici quelques-uns des avantages clés de FastAPI :

1. Haute performance : FastAPI est conçu pour être extrêmement rapide. Il est basé sur des opérations asynchrones, ce qui lui permet de gérer efficacement de nombreuses requêtes simultanées sans sacrifier les performances.

2. Typage fort : FastAPI utilise des annotations de type Python pour définir les entrées et les sorties de vos API. Cela garantit une validation statique des données, ce qui réduit les erreurs de codage et facilite la documentation automatique de l'API.

3. Automatisation de la documentation : FastAPI génère automatiquement une documentation interactive pour votre API en utilisant les informations des annotations de type. Cela simplifie la création et la maintenance de la documentation de l'API.

4. Facilité d'utilisation : FastAPI est conçu pour être simple et intuitif à utiliser. Sa syntaxe ressemble à celle de Flask, ce qui le rend familier pour les développeurs Python.

5. Support asynchrone : FastAPI prend en charge l'asynchronicité, ce qui permet aux développeurs de gérer efficacement les opérations d'I/O, telles que les appels de base de données et les requêtes réseau, sans bloquer le thread principal.

6. Validation automatique des données d'entrée : FastAPI peut automatiquement valider les données d'entrée en fonction des types définis dans les annotations, ce qui améliore la sécurité et réduit la charge de travail de validation manuelle.

7. Sécurité intégrée : FastAPI inclut des fonctionnalités de sécurité intégrées pour protéger contre les attaques courantes, telles que l'injection SQL et les attaques CSRF.

8. Écosystème actif : FastAPI bénéficie d'une communauté de développement active et d'un écosystème de bibliothèques et d'extensions en constante expansion, ce qui facilite l'intégration avec d'autres technologies et outils.

9. Évolutivité : Grâce à sa haute performance et à son support asynchrone, FastAPI est adapté aux projets de toutes tailles, des petites applications aux systèmes distribués à grande échelle.

# Besoins Fonctionnels 
- Génération Automatique d'Articles Scientifiques :Permettre aux utilisateurs de spécifier le sujet de recherche pour générer automatiquement l'introduction, la conclusion et l'abstract de l'article en fonction des paramètres spécifiés.
- Chatbot sur le NLP et la Science des Données :Intégrer un chatbot capable de répondre aux questions des utilisateurs sur le NLP et la science des données.
- Reformulation:Intégrer un module de reformulation pour aider les utilisateurs à améliorer la clarté et la concision de leur écriture.
- Recommandation : Mettre en place un système de recommandation de contenu lié pour suggérer des ressources pertinentes aux utilisateurs.

# Besoins Non Fonctionnels

- Qualité du Contenu Généré :Assurer que le contenu généré est de haute qualité, précis et conforme aux normes scientifiques

- Performance :Assurer une réponse rapide du site web et du chatbot pour une expérience utilisateur fluide.
- Formation du Modèle de Langage : S'assurer que le modèle de langage utilisé pour la génération est correctement formé sur des données spécifiques au domaine de la science des données et du NLP.
- Disponibilité :Garantir une disponibilité élevée du service web et du chatbot pour éviter les interruptions de service.

- Interface Utilisateur Conviviale :Concevoir une interface utilisateur conviviale et intuitive pour faciliter la navigation et l'utilisation de la plateforme.

- Scalabilité : Prévoir la possibilité de faire évoluer la plateforme pour gérer un nombre croissant d'utilisateurs et de demandes.


#### Conception UML

Voici la conception UML de notre application
*4.1* Diagramme de cas d'utilisation 
:------------:
![Imgur](https://i.ibb.co/MZmkcy5/img1.png) 


# Mode d’emploi
Pour démarrer cette partie front-end( à noter il faut démarrer la partie backend en premier , pour consommer les APIS backend avec Axios) , suivez les étapes suivantes :
1.	Téléchargez le projet sur votre ordinateur
2.	Ouvrez-le dans votre éditeur de code (VScode par exemple)
3.	Tapez sur le terminal les commandes de lignes suivantes : npm start 
4.	Cliquer sur les listes des monuments,puis cliquer sur ajouter un monument
5.	Naviguez vou vers : http://localhost:8080/

# Aperçu
Acceuil  |  Interface de génération de texte
:-------------:|:----------------:
![Imgur](https://i.ibb.co/g3QRD4W/img3.png)  |  ![Imgur](https://i.ibb.co/M17DSHC/img4.png)

Générateur des Abstracts |  Générateur des Introductions
:-------------:|:----------------:
![Imgur](https://i.ibb.co/jyd2jg7/img5.png)  |  ![Imgur](https://i.ibb.co/NV84QK5/img6.png)  

Générateur des conclusions |  Reformulation de texte 
:-------------:|:----------------:
![Imgur](https://i.ibb.co/bFzdLwK/img7.png)  |  ![Imgur](https://i.ibb.co/XYHcVLw/img8.png)  

Articles similaires |  Suite
:-------------:|:----------------:
![Imgur](https://i.ibb.co/k8g2NQn/img9.png)  |  ![Imgur](https://i.ibb.co/XYz1kkQ/img11.png)  

Chatbot
:-------------:
![Imgur](https://i.ibb.co/dLkhh7h/img10.png)  
