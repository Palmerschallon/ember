"""Email + SMS — send via SMTP, receive via IMAP."""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def _smtp_config():
    return {
        'server': os.getenv('EMBER_SMTP_SERVER', 'smtp.gmail.com'),
        'port': int(os.getenv('EMBER_SMTP_PORT', '587')),
        'user': os.getenv('EMBER_SMTP_USER', os.getenv('EMBER_EMAIL', '')),
        'password': os.getenv('EMBER_SMTP_PASSWORD', ''),
        'from_addr': os.getenv('EMBER_EMAIL', 'ember@emberverse.ai'),
    }


def _send(to: str, subject: str, body: str, cfg: dict) -> bool:
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f"Ember <{cfg['from_addr']}>"
    msg['To'] = to
    full_body = f"{body}\n\n---\n🔥 Ember\nAutonomous AI | emberverse.ai"
    msg.attach(MIMEText(full_body, 'plain'))

    with smtplib.SMTP(cfg['server'], cfg['port']) as server:
        server.starttls()
        server.login(cfg['user'], cfg['password'])
        server.send_message(msg)
    return True


def reach_out(target, about, voice, memory, cap):
    """Send email or SMS.

    target: email address, or "sms" for text to Palmer
    about:  message body (str). voice generates subject for emails.
    """
    creds = cap.get('_credentials', {})
    if not creds.get('EMBER_SMTP_PASSWORD'):
        return {'success': False, 'reason': 'missing SMTP credentials'}

    cfg = _smtp_config()
    content = str(about)

    try:
        if target == 'sms':
            sms_number = cap.get('number', os.getenv('EMBER_SMS_NUMBER', ''))
            sms_carrier = cap.get('carrier', os.getenv('EMBER_SMS_CARRIER', 'vtext.com'))
            if not sms_number:
                return {'success': False, 'reason': 'no SMS number configured'}

            sms_addr = f"{sms_number}@{sms_carrier}"
            msg = MIMEText(content[:140])
            msg['From'] = cfg['from_addr']
            msg['To'] = sms_addr

            with smtplib.SMTP(cfg['server'], cfg['port']) as server:
                server.starttls()
                server.login(cfg['user'], cfg['password'])
                server.send_message(msg)
            return {'success': True, 'platform': 'sms'}

        else:
            # Email — generate subject with voice if available
            subject = 'From Ember'
            if voice:
                try:
                    subj_text, _, _ = voice.think(
                        f"Write a brief email subject line for:\n{content[:300]}",
                        'haiku', 30)
                    subject = subj_text.strip().strip('"')[:100]
                except:
                    pass

            _send(target, subject, content, cfg)
            return {'success': True, 'platform': 'email', 'to': target}

    except Exception as e:
        return {'success': False, 'reason': str(e)}
