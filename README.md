# 🎅 Secret Santa

Automatise le tirage au sort d'un Secret Santa et l'envoi d'emails personnalisés (HTML + texte) à chaque participant. Les identifiants SMTP, les paramètres et la liste des participants sont externalisés du code pour plus de sécurité et de flexibilité.

## ✨ Fonctionnalités

- Tirage au sort équitable des paires donneur/receveur (`src/arranger.py`), avec évitement de l'auto-attribution et pondération basée sur l'historique des tirages précédents (`history.json`) pour limiter les répétitions d'une année sur l'autre.
- Templates d'email HTML et texte personnalisables (`templates/`), rendus avec Jinja2.
- **Mode test** : génère un aperçu des emails dans `previews/` sans rien envoyer, pour valider le contenu avant l'envoi réel.
- Envoi sécurisé via SMTP (TLS), avec une limite configurable du nombre d'emails envoyés par exécution.
- Logs détaillés de chaque exécution dans `logs/send.log`.

## 📂 Structure du projet

```
config.yaml            # Paramètres du tirage et de l'envoi
participants.csv        # Liste des participants (nom, email)
history.json             # Historique des tirages précédents
.env                        # Identifiants SMTP (à créer, non versionné)
src/
  main.py                # Point d'entrée du script
  arranger.py           # Logique du tirage au sort
  renderer.py            # Rendu des templates Jinja2
  mailer.py               # Envoi des emails via SMTP
  utils.py                  # Chargement config/participants/historique, previews
templates/
  email_template.html  # Template HTML de l'email
  email_template.txt    # Template texte de l'email
previews/                # Aperçus générés en mode test
logs/                        # Journaux d'exécution
```

## ⚙️ Installation

### Prérequis
- Python 3.9+
- Un compte email avec accès SMTP (ex. Gmail avec un [mot de passe d'application](https://support.google.com/accounts/answer/185833))

### Étapes

1. Cloner le dépôt puis se placer dans le dossier du projet.
2. Créer le fichier `.env` à partir de `.env.exemple` et renseigner vos identifiants SMTP :
   ```
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=organizer@gmail.com
   SMTP_PASS=CHANGEME
   SMTP_TLS=true
   ```
3. Renseigner les participants dans `participants.csv` (colonnes `name`, `email`).
4. Adapter `config.yaml` selon vos besoins (sujet, expéditeur, mode test, limites d'envoi...).

## ▶️ Utilisation

Le script `run.sh` crée l'environnement virtuel, installe les dépendances et lance le tirage :
```bash
./run.sh
```

Ou manuellement :
```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows (Git Bash)
pip install -r requirements.txt
python src/main.py
```

### Mode test
Tant que `test_mode: true` dans `config.yaml`, aucun email n'est envoyé : un aperçu HTML/texte est généré par participant dans `previews/`. Passez `test_mode` à `false` pour envoyer réellement les emails.

## 🔧 Configuration (`config.yaml`)

| Paramètre | Description |
|---|---|
| `subject` | Objet de l'email envoyé |
| `from_name` | Nom affiché comme expéditeur |
| `reply_to` | Adresse de réponse |
| `test_mode` | `true` = aperçu uniquement, `false` = envoi réel |
| `number_max_mail_send` | Nombre maximum d'emails envoyés par exécution (sécurité) |
| `max_sends_per_minute` | Limite de débit d'envoi |
| `allow_self_assignment` | Autorise ou non qu'un participant se tire lui-même |

## 🖼️ Image de fond du template

L'image de fond utilisée dans `templates/email_template.html` est hébergée sur GitHub via [jsDelivr](https://www.jsdelivr.com/). Pour la mettre à jour, placez votre image dans `assets/images/` du dépôt, poussez-la sur la branche `main`, puis mettez à jour l'URL correspondante dans le template.

## 🧪 Tests

Les tests unitaires se trouvent dans `tests/` et peuvent être lancés avec :
```bash
pytest
```
