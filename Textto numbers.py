def turkish_to_digit(text):
    numbers = {
        "bir": 1,
        "iki": 2,
        "üç": 3,
        "dört": 4,
        "beş": 5,
        "altı": 6,
        "yedi": 7,
        "sekiz": 8,
        "dokuz": 9,
        "on": 10,
        "yirmi": 20,
        "otuz": 30,
        "kırk": 40,
        "elli": 50,
        "altmış": 60,
        "yetmiş": 70,
        "seksen": 80,
        "doksan": 90,
        "yüz": 100,
        "bin": 1000
    }

    words = text.split()
    total = 0
    current = 0

    for word in words:
        if word in numbers:
            value = numbers[word]
            if value == 100:  # Yüz ifadesi
                if current == 0:
                    current = 1
                current *= 100
            elif value == 1000:  # Bin ifadesi
                if current == 0:
                    current = 1
                total += current * 1000
                current = 0
            else:
                current += value
        else:
            return "Unknown"

    total += current
    return total


x = input("Lütfen sayıya çevrilecek metni girin: ")
result = turkish_to_digit(x)
print("Sonuç:", result)
