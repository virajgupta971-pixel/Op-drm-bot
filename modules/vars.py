#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "39199066"))
API_HASH = environ.get("API_HASH", "95f9f5b87842e1ec2334f543c3dbfd0e")
BOT_TOKEN = environ.get("BOT_TOKEN", "8969720498:AAGOojJ-Fh7eD-vmHc-NtRRb2dfKGjT9f2g")

OWNER = int(environ.get("OWNER", "8873050060"))
CREDIT = environ.get("CREDIT", "v")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8873050060').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8873050060').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8000))  # Default to 8000 if not set


# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
api_url = "http://master-api-v3.vercel.app/"
api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"
token_cp ='eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9r'
adda_token = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjaGFuZHJhYmh1dGlhMTIzQGdtYWlsLmNvbSIsImF1ZCI6IjQ2MDk4MTQiLCJpYXQiOjE3OTI0MDc3NzEsImlzcyI6ImFkZGEyNDcuY29tIiwibmFtZSI6ImRlbW9uMSAiLCJlbWFpbCI6InJnOTM0Mzg3N0BnbWFpbC5jb20iLCJwaG9uZSI6Ijk3OTI5MDE4MjYiLCJ1c2VySWQiOiJhZGRhLnYxLmE3Yjk1OWRhM2UxMTZjYzk0NDEwMWVjMzcyNTU4ZjUxIiwibG9naW5BcGlWZXJzaW9uIjoxfQ.S8RzAsupH1BlH8BH11KQFanIyZCds-a3bbCxM0L01PgL7UFsyB5CQd-wZOFEXWY-ZaGynT2KuYUupb1xnFXI-A"
photologo = 'https://tinypic.host/images/2025/02/07/DeWatermark.ai_1738952933236-1.png' #https://envs.sh/GV0.jpg
photoyt = 'https://tinypic.host/images/2025/03/18/YouTube-Logo.wine.png' #https://envs.sh/GVi.jpg
photocp = 'https://tinypic.host/images/2025/03/28/IMG_20250328_133126.jpg'
photozip = 'https://envs.sh/cD_.jpg'
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.

