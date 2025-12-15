import subprocess
import re
from datetime import datetime
from domain_list import domains

# İngilizce ay → numara dönüşümü
MONTHS = {
    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
    "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
    "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
}

# Türkçe aylar
MONTHS_TR = {
    "01": "Ocak", "02": "Şubat", "03": "Mart", "04": "Nisan",
    "05": "Mayıs", "06": "Haziran", "07": "Temmuz", "08": "Ağustos",
    "09": "Eylül", "10": "Ekim", "11": "Kasım", "12": "Aralık"
}



def get_whois(domain):
    try:
        if domain.endswith(".tr"):
            result = subprocess.check_output(
                ["whois", "-h", "whois.trabis.gov.tr", domain],
                stderr=subprocess.STDOUT,
                text=True
            )
        else:
            result = subprocess.check_output(
                ["whois", domain],
                stderr=subprocess.STDOUT,
                text=True
            )
        return result

    except Exception as e:
        return str(e)

def parse_expiry(whois_data):
    # TRABIS formatı: 2026-Sep-07
    tr_match = re.search(r"Expires on.*?:\s*([0-9]{4})-([A-Za-z]{3})-([0-9]{2})", whois_data)
    if tr_match:
        year, mon_eng, day = tr_match.groups()
        month_num = MONTHS.get(mon_eng, None)
        if month_num:
            return datetime.strptime(f"{year}-{month_num}-{day}", "%Y-%m-%d")

    # GLOBAL format: 2026-08-13T00:00:00Z
    generic = re.search(r"([0-9]{4}-[0-9]{2}-[0-9]{2})", whois_data)
    if generic:
        return datetime.strptime(generic.group(1), "%Y-%m-%d")

    return None

def format_turkish_date(dt):
    day = dt.strftime("%d")
    month = MONTHS_TR[dt.strftime("%m")]
    year = dt.strftime("%Y")
    return f"{day} {month} {year}"


def domain_check():
    # ---------------- MAIN ----------------
    today = datetime.now()

    results =[]

    for domain in domains:
        whois_output = get_whois(domain)
        expiry = parse_expiry(whois_output)

        if expiry:
            turkish_date = format_turkish_date(expiry)
            days_diff = (expiry - today).days

            if days_diff < 0:
                status = "❌ Süresi geçmiş"
                days_info = f"{abs(days_diff)} gün önce doldu"
            else:
                status = "✔ Süresi devam ediyor"
                days_info = f"{days_diff} gün kaldı"

        
            results.append(f"{domain} => Son Kullanım: {turkish_date} | {status} | {days_info}")
        else:
            results.append(f"{domain} => Tarih bulunamadı.")
    return results
