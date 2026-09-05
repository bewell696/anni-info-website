# ANNI-INFO d.o.o. Website

Profesionalno spletno mesto za računovodski servis v Sloveniji. Kompletna rekreacija originalne spletne strani s Tailwind CSS in modernim designom.

## 📁 Projektna struktura

```
hetyner1/
├── index.html              # Domov (homepage)
├── services.html           # Storitve (services page)
├── advantages.html         # Naše prednosti (advantages page)
├── about.html              # O nas (about page)
├── contact.html            # Kontakt (contact page)
├── README.md               # Točka dokumentacije
├── QUICKSTART.md           # Hitri začetek
└── package.json            # Node.js dependencies (za SCSS kompozicijo)
```

## 🚀 Hitri začetek

Spletno mesto lahko odprete neposredno v brskalniku:

```bash
# Odprite index.html
open index.html
```

Ni potrebna nastavitev build procesa!

## 🎨 Technologije

- **HTML5** - Semantična markup
- **Tailwind CSS** - Utility-first CSS framework (preko CDN)
- **Font Awesome** - Ikonska biblioteka
- **Google Fonts** - Poppins font
- **JavaScript** - Interaktivna funkcionalnost
- **SCSS** - Custom styles (za kompozicijo)

## 📱 Funkcionalnosti

### Vse strani
- ✅ Polna odzivna oblikovanje (mobilni, tablet, desktop)
- ✅ Gladko skrolanje med stranmi
- ✅ Mobilni navigacijski meni
- ✅ Interaktivni hover efekti
- ✅ Profesionalno računovodsko znanje
- ✅ Slovenščina

### Domov (index.html)
- Hero sekcija s sloganom "Računovodskim skrbem se rad odpovem"
- Kratki predogled storitev
- Kontaktirajte nas gumb
- Kontaktne informacije

### Storitve (services.html)
- **Računovodsko-finančne storitve** (11 storitev):
  - Vodenje glavne knjige
  - Analitična evidenca saldakontov
  - Register osnovnih sredstev
  - DDV
  - Vodenje davčnih evidenc
  - Obračun plač
  - Obračun prispevkov
  - Poročila
  - In drugih

- **Dodatne storitve** (7 storitev):
  - Pomoč pri javnih razpisih
  - Pogajanja o posojilih
  - Elektronska izvršba računov
  - Davčni pregledi
  - Inšpekcijsko sodelovanje
  - Dokumentacija za zaposlitev

### Naše prednosti (advantages.html)
- 11 ključnih prednosti podjetja
- Profesionalna prezentacija
- Kvalificirano znanje
- Dolgoletno izkušenje

### O nas (about.html)
- Zgodovina podjetja (1989–2011)
- Razvoj iz Vlasta Auer s.p. v ANNI-INFO d.o.o.
- Filozofija in načela
- Strokovni razvoj

### Kontakt (contact.html)
- Kontaktna obrazec
- Glavni sedež Ptuj
- Poslovna enota Domžale
- Telefon, email, mobilni
- Številke za DDV in TRR

## 🎨 Design

### Barvna shema
- **Primarna:** Modri odtenki (#1e3a5f, #2d5a87)
- **Pomagajoč:** Bela in siva
- **Fokus:** Zanesljivost in profesionalnost

### Tipografija
- **Glavni:** Poppins (sans-serif)
- **Google Fonts:** Uvoženo preko CDN

### Interakcije
- ✨ Gladki animaciji
- 🎯 Hover efekti na karticah
- 🔄 Skrolanje brez prevladovanja
- 📱 Mobilni meni toggle

## 🔧 Customizacija

### Sprememba barv
V primeru potrebe po spremembi barv:

```css
/* Hero pattern */
.hero-pattern {
  background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);
}
```

### Barve gumbov
```css
.btn-primary {
  background: linear-gradient(135deg, #2d5a87 0%, #1e3a5f 100%);
}
```

## 📱 Responsive Design

- **Mobile (< 768px):** Stolpci ena vrstica
- **Tablet (768px - 1024px):** Dva stolpca
- **Desktop (> 1024px):** Tri stolpce
- **Navigacija:** Podmeni na mobilih

## 🚀 Prednostne lastnosti

1. **Enostaven za uporabo** - Ena HTML datoteka za vsako stran
2. **Brzalo** - Minimizirani external dependencies
3. **Vizualno privlačno** - Moderno in profesionalno znanje
4. **Primerljivo** - Enaka vsebina kot original
5. **Primeren za accounting** - Zanesljiv in profesionalen izgled

## 📝 Uporaba

### Odpri spletno mesto
```bash
open index.html
```

### Lokalni strežnik (opcionalno)
```bash
cd hetyner1
python3 -m http.server 8000
# Nato odprite: http://localhost:8000
```

## 🔗 Povezave

- **Domov:** [index.html](./index.html)
- **Storitve:** [services.html](./services.html)
- **Prednosti:** [advantages.html](./advantages.html)
- **O nas:** [about.html](./about.html)
- **Kontakt:** [contact.html](./contact.html)

## 📄 Omejitve

- Ni slike za storitve (omogočeno z ikonami Font Awesome)
- No realni Google Maps integracija (placeholder)
- Mobile-first pristop

## 🛠️ Napredne možnosti

Za nadaljnjo razvoj lahko:

1. **SCSS kompozicija:**
   ```bash
   npm install
   npm run dev
   ```

2. **Dodajite slike:**
   ```bash
   mkdir images
   # Dodajte slike v images/ mapo
   ```

3. **Integracija Google Maps:**
   - Dodajte Google Maps API
   - Implementirajte realne koordinate

4. **Druge strani:**
   - Oglasna stran
   - Blog
   - PDF dokumenti

## 📞 Podpora

Za vprašanja in pomož povezajte s kontakti:

- **Email:** info@anni-info.si
- **Telefon:** 02 771 99 71
- **Mobilni:** 051 636 242

## 📄 Licence

© 2024 ANNI-INFO d.o.o. Vse pravice pridržane.

---

**Nastavitev:** Preprosto odprite `index.html` v brskalniku. Ni potrebe po kompresiji ali build procesu!