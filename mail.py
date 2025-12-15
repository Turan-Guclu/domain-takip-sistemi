import smtplib
from email.message import EmailMessage

def emailSender(domain_list, emailaddr):
    email = EmailMessage()
    email["Subject"] ="Takip Listesindeki Domainler Listesi"
    email["From"] = 'test@example.com'
    email["To"] = emailaddr
   
        # Domain listesini HTML tabloya dönüştürelim
    rows = ""
    for item in domain_list:
        domain, info = item.split(" => ", 1)

        # Durum ikonları
        if "Süresi devam ediyor" in info:
            icon = "🟢"
        else:
            icon = "🔴"

        rows += f"""
        <tr>
            <td style="padding:8px; border-bottom:1px solid #ddd; font-weight:bold;">{domain}</td>
            <td style="padding:8px; border-bottom:1px solid #ddd;">{info}</td>
            <td style="padding:8px; border-bottom:1px solid #ddd; text-align:center;">{icon}</td>
        </tr>
        """

    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background: #f5f5f5; padding:20px;">
    
    <div style="max-width:700px; margin:auto; background:white; padding:20px; border-radius:10px; box-shadow:0 0 10px rgba(0,0,0,0.1);">

        <h2 style="text-align:center; color:#0e4d92;">
            🔎 Alperteks Domain Takip Sistemi
        </h2>

        <p style="text-align:center; font-size:14px; color:#444;">
            Aşağıda takip listenizdeki domainlerin güncel son kullanım tarihleri ve durumları bulunmaktadır.
        </p>

        <table style="width:100%; border-collapse:collapse; margin-top:20px;">
            <tr style="background:#0e4d92; color:white;">
                <th style="padding:10px; text-align:left;">Domain</th>
                <th style="padding:10px; text-align:left;">Durum Bilgisi</th>
                <th style="padding:10px; text-align:center;">Durum</th>
            </tr>
            {rows}
        </table>

        <p style="margin-top:20px; font-size:13px; color:#666; text-align:center;">
            Bu e-posta Alperteks Domain Takip Sistemi tarafından otomatik olarak oluşturulmuştur.
        </p>
    </div>

    </body>
    </html>
    """

    email.add_alternative(html_content, subtype="html")


    try:
        with smtplib.SMTP('mail.example.com', 587) as smtp:
            smtp.login('test@example.com', '!Password123')
            smtp.send_message(email)
        return "Success: Email sent successfully!"
    except Exception as e:
        return f"Error: {str(e)}"

