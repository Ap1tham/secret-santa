import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(smtp_conf, subject, sender, reply_to, to_addr, html_body, text_body):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_addr
    msg["Reply-To"] = reply_to

    msg.attach(MIMEText(text_body, "plain"))
    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP(smtp_conf["SMTP_HOST"], int(smtp_conf["SMTP_PORT"])) as server:
        if smtp_conf.get("SMTP_TLS", "true").lower() == "true":
            server.starttls()
        server.login(smtp_conf["SMTP_USER"], smtp_conf["SMTP_PASS"])
        server.sendmail(smtp_conf["SMTP_USER"], [to_addr], msg.as_string())