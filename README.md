# Diablo Immortal Discord Bot

Bot care postează automat în canalul Discord noutăți de la Diablo Immortal, folosind feed-ul oficial Blizzard.

## Configurare

1. Creează un fișier `.env` în folderul proiectului cu conținutul:
TOKEN=tokenul_tău_discord
CHANNEL_ID=id_canalului_discord
2. Instalează dependențele:
pip install -r requirements.txt
3. Rulează botul:
python main.py
---

## Hosting

Poți folosi Replit sau Railway pentru hosting gratuit:

- Replit: importă repo-ul, setează variabilele de mediu `TOKEN` și `CHANNEL_ID` în Secrets și apasă Run.
- Railway: deploy din GitHub și configurează variabilele de mediu.

---

## Permisiuni Discord

Pentru ca botul să poată scrie în canalul ales, adaugă-l pe server cu permisiunile:
- Send Messages
- Read Messages
- Embed Links

---

## Feedback

Dacă ai nevoie de alte funcții sau ajutor, scrie-mi!
