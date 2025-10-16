# GitOps

Approche de gestion d'infrastructure d'applications qui est basé sur Git. 
Toute la configuration de l'infrastructure et des applications est décrite sous forme de code dans un dépôt Git, et que tout changement passe par un commit et une pull request. 

Cette méthodologie permet d'automatiser les déploiements : dès qu'un changement est validé dans Git, des outils spécialisés se chargent automatiquement de synchroniser l'état réel de l'infrastructure avec l'état désiré décrit dans le dépôt. 
En résumé, c'est l'automatisation de la continuité de tout ce qui est développement et déploiement.

## Schéma de flux GitOps

```
[Git] -> [ArgoCD] -> [Kubernetes] -> [Application] -> [Prometheus]
                ↑_______________________________________________|
```

### Explication du schéma

1. **Git** : Le dépôt contient toutes les configurations et le code
2. **ArgoCD** : Surveille le dépôt Git et détecte les changements
3. **Kubernetes** : Reçoit les instructions d'ArgoCD pour appliquer les changements
4. **Application** : L'application est déployée ou mise à jour selon la configuration
5. **Prometheus** : Surveille l'état de l'application et du cluster, collecte les métriques
6. **Boucle de feedback** : ArgoCD vérifie en continu que l'état réel correspond à l'état désiré dans Git (réconciliation)

---
