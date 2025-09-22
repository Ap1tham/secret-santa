import yaml
import logging
from utils import load_env, load_participants, save_preview, load_history
from arranger import make_pairs
from renderer import render_email
from mailer import send_email

# --- Logging setup ---
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/send.log", mode="a", encoding="utf-8"),  # append instead of overwrite
        logging.StreamHandler()
    ]
)

def main():
    # Load configuration
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    env = load_env()
    participants = load_participants("participants.csv")
    history = load_history("history.json")
    numberMailMax = config.get("number_max_mail_send", 10)
    
    # Logging setup in test mode or not
    if(config.get("test_mode", True)):
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    # Arrange Secret Santa pairs
    pairs = make_pairs(participants, config.get("allow_self_assignment", False), history)
    logging.info("🎲 Tirage terminé ! Paires générées :")
    for giver, recipient in pairs:
        logging.debug(f"  {giver['name']} → {recipient['name']}")

    logging.info("📨 Début de l'envoi des mails...")

    # For each giver, render and send mail
    for giver, recipient in pairs:
        html, text = render_email(giver, recipient)

        if config.get("test_mode", True):
            logging.debug(f"[TEST] Mail préparé pour {giver['name']} (destinataire : {recipient['name']})")
            save_preview(giver, recipient, html, text)
            continue
        
        if numberMailMax <= 0:
            logging.error("Nombre de mail pouvant être envoyé atteint ! Veuillez modifier le paramètre 'number_max_mail_send' si nécessaire dans le 'config.yaml'.")
            exit(0)
        else:
            numberMailMax -= 1

        try:
            send_email(
                smtp_conf=env,
                subject=config["subject"],
                sender=config["from_name"],
                reply_to=config["reply_to"],
                to_addr=giver["email"],
                html_body=html,
                text_body=text,
            )
            if(logging.getLogger().getEffectiveLevel() == logging.INFO):
                logging.info(f"✅ Mail envoyé à {giver['name']} (destinataire : ***)")
            elif(logging.getLogger().getEffectiveLevel() == logging.DEBUG):
                logging.info(f"✅ Mail envoyé à {giver['name']} (destinataire : {recipient['name']})")

        except Exception as e:
            logging.error(f"❌ Erreur lors de l'envoi du mail pour {giver['name']} → {recipient['name']} ({e})")

    logging.info("✅ Tous les mails ont été traités.\n")

if __name__ == "__main__":
    main()