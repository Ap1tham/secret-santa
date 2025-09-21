import csv
import os

def load_env():
    env_path = ".env"
    if not os.path.exists(env_path):
        raise FileNotFoundError(
            f"'{env_path}' not found. Please create it by copying '.env.example' and filling in your SMTP credentials."
        )

    env = {}
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, val = line.split("=", 1)
                env[key] = val
    return env

def load_participants(path):
    participants = []
    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            participants.append({"name": row["name"], "email": row["email"]})
    return participants

def save_preview(giver, recipient, html, text, out_dir="previews"):
    os.makedirs(out_dir, exist_ok=True)
    safe_name = giver["name"].replace(" ", "_")
    with open(os.path.join(out_dir, f"{safe_name}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    with open(os.path.join(out_dir, f"{safe_name}.txt"), "w", encoding="utf-8") as f:
        f.write(text)
