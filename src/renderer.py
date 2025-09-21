from jinja2 import Template

def render_email(giver, recipient):
    with open("templates/email_template.html", "r", encoding="utf-8") as f:
        html_template = Template(f.read())
    with open("templates/email_template.txt", "r", encoding="utf-8") as f:
        text_template = Template(f.read())

    context = {
        "giver_name": giver["name"],
        "recipient_name": recipient["name"],
    }

    return (
        html_template.render(**context),
        text_template.render(**context),
    )