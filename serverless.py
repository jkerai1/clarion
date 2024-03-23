from flask import Flask, request, send_file#

##if Teams webhook alerting wanted - uncomment below :
#import pymsteams
#myTeamsMessage = pymsteams.connectorcard("<Microsoft Webhook URL>") #replace with Teams Webhook URL

pixel_filename = "companyBranding.png"
allowed_referers = ['login.microsoftonline.com',
        'login.microsoft.net',
        'login.microsoft.com',
        'autologon.microsoftazuread-sso.com',
        'tasks.office.com',
        'login.windows.net',
        'https://login.microsoftonline.com',
        'https://login.microsoft.net',
        'https://login.microsoft.com',
        'https://autologon.microsoftazuread-sso.com',
        'https://tasks.office.com',
        'https://login.windows.net']
app = Flask(__name__)
filename = "warning.png"

@app.route(f'/{pixel_filename}')
def pixel():
    requester_ip = request.remote_addr
    referer_header = request.headers.get('Referer')
    if referer_header not in allowed_referers:
        print(f"[!] Non-Microsoft referer header detected: {referer_header}")
        print("[*] Debug Information:")
        print(f"[*] Requester IP (user logging in): {requester_ip}")
        print(f"[*] Referer header (AitM): {referer_header}")

        #Teams Webhook
        #myTeamsMessage.text(f"[*] Requester IP (user logging in): {requester_ip} & Referer header (AitM): {referer_header}")
        #myTeamsMessage.send()
        
    return send_file(filename, mimetype='image/png',as_attachment=False)

def main():
        app.run()

if __name__ == "__main__":
    main()
