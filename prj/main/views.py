from django.shortcuts import render

# Dummy data jako náhrada za databázi
PRODUKTY = {
    1: {
        'nazev': 'Míč Mikasa V200W',
        'cena': '1 499 Kč',
        'popis': 'Oficiální míč FIVB pro plážový i halový volejbal, z vysoce odolné syntetické kůže.',
        'obrazek': 'https://example.com/volley_ball.jpg',
        'atributy': {
            'Výrobce': 'Mikasa',
            'Hmotnost': '260–280 g',
            'Obvod': '65–67 cm',
            'Materiál': 'Syntetická kůže',
            'Barva': 'Žlutá/modrá'
        }
    },
    2: {
        'nazev': 'Boty Asics Gel-Rocket',
        'cena': '2 099 Kč',
        'popis': 'Lehké a stabilní volejbalové boty s vynikajícím tlumením.',
        'obrazek': 'https://example.com/volley_shoes.jpg',
        'atributy': {
            'Výrobce': 'Asics',
            'Hmotnost': '350 g',
            'Velikosti': '38–47',
            'Materiál': 'Syntetika + síťovina',
            'Barva': 'Bílá/modrá'
        }
    }
}

def produkt_detail(request, id):
    produkt = PRODUKTY.get(id)
    if not produkt:
        return render(request, 'main/produkt_not_found.html', status=404)
    return render(request, 'main/product.html', {'produkt': produkt})