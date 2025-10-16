# GitOps

Approche de gestion d'infrastructure d'applications qui est basé sur Git. 
Toute la configuration de l'infrastructure et des applications est décrite sous forme de code dans un dépôt Git, et que tout changement passe par un commit et une pull request. 

Cette méthodologie permet d'automatiser les déploiements : dès qu'un changement est validé dans Git, des outils spécialisés se chargent automatiquement de synchroniser l'état réel de l'infrastructure avec l'état désiré décrit dans le dépôt. 
En résumé, c'est l'automatisation de la continuité de tout ce qui est développement et déploiement.

## Schéma de flux du projet

```
[Git] -> [ArgoCD] -> [Kubernetes] -> [Application]
```
