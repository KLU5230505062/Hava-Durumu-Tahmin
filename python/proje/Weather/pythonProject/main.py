import requests

print("Hava Durumu Uygulamasına Hoşgeldiniz...")
print("Hava durumunu öğrenmek istediğiniz şehri girin:")

city_name = input("Lütfen Şehri Giriniz: ")

def get_weather_report(city):
    url = f'https://wttr.in/{city}?format=3'  # Sadece özet veri verir (daha okunabilir)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("🌤 Hava Durumu:", response.text)
        else:
            print("❌ Şehir bulunamadı veya API hatası.")
    except Exception as e:
        print("⚠️ Bir hata oluştu:", e)

get_weather_report(city_name)
while True:
    city = input("Şehir ismini gir (çıkmak için 'q'): ")
    if city.lower() == 'q':
        print("Uygulama kapatılıyor...")
        break
    get_weather_report(city)

