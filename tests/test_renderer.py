from renderer import render_email

def test_render_email():
    giver = {"name": "Alice", "email": "a@test.com"}
    recipient = {"name": "Bob", "email": "b@test.com"}
    html, text = render_email(giver, recipient)
    assert "Alice" in html
    assert "Bob" in html
    assert "Alice" in text
    assert "Bob" in text