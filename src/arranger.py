import random

import random

def make_pairs(participants, allow_self=False, history=None):
    """
    history = dict {giver_email: [recipient_emails_already_seen]}
    """
    if history is None:
        history = {}

    givers = participants[:]
    recipients = participants[:]
    pairs = []

    for giver in givers:
        # Liste des candidats valides
        candidates = [
            r for r in recipients
            if (allow_self or r["email"] != giver["email"])
        ]

        # Pondération : moins de chance si déjà tiré
        weights = []
        seen = history.get(giver["email"], [])
        for r in candidates:
            if r["email"] in seen:
                weights.append(0.2)  # pénalité
            else:
                weights.append(1.0)  # normal

        recipient = random.choices(candidates, weights=weights, k=1)[0]
        pairs.append((giver, recipient))
        recipients.remove(recipient)

    return pairs