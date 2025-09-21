from arranger import make_pairs

def test_no_self_assignment():
    participants = [
        {"name": "A", "email": "a@test.com"},
        {"name": "B", "email": "b@test.com"},
        {"name": "C", "email": "c@test.com"},
    ]
    pairs = make_pairs(participants, allow_self=False)
    for giver, recipient in pairs.items():
        assert giver != recipient