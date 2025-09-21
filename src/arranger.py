import random

def make_pairs(participants, allow_self=False):
    givers = participants[:]
    recipients = participants[:]
    random.shuffle(recipients)

    pairs = []  # list of (giver_dict, recipient_dict)
    for giver in givers:
        candidate = recipients.pop()
        if not allow_self and candidate == giver:
            # simple swap
            other = pairs[0][1] if pairs else recipients.pop()
            recipients.append(candidate)
            candidate = other
        pairs.append((giver, candidate))
    return pairs
