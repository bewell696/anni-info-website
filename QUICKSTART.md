# Quick Start Guide for ANNI-INFO Website

## 🚀 Quick Start

Open `index.html` directly in your browser. No build process required!

```bash
# Mac
open index.html

# Linux
xdg-open index.html

# Windows
start index.html
```

## 📦 Minimalna izgradnja (opcionalno)

If you want to compile SCSS to CSS:

```bash
cd hetyner1

# Install dependencies
npm install

# Watch and compile SCSS
npm run dev
```

## 🎨 What's Included

### 5 Complete Pages:
1. **index.html** - Homepage with hero, services preview, and contact
2. **services.html** - Detailed accounting services list
3. **advantages.html** - 11 key company advantages
4. **about.html** - Company history and philosophy
5. **contact.html** - Contact form and office locations

### Features:
- ✅ Fully responsive (mobile, tablet, desktop)
- ✅ Smooth scroll navigation
- ✅ Mobile menu toggle
- ✅ Professional accounting service design
- ✅ Slovenian language throughout
- ✅ Interactive hover effects
- ✅ Contact form with validation
- ✅ Company contact information
- ✅ Office locations (Ptuj & Domžale)
- ✅ VAT and bank account details

## 🎨 Customization

### Colors
Edit the blue tones in the CSS:

```css
.hero-pattern {
  background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);
}

.btn-primary {
  background: linear-gradient(135deg, #2d5a87 0%, #1e3a5f 100%);
}
```

### Fonts
Change to different fonts by editing the Google Fonts link in `<head>`:

```html
<link href="https://fonts.googleapis.com/css2?family=YourFont:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

### Add Images
Create an `images/` folder and add your images. Update the HTML to include them:

```html
<img src="images/your-image.jpg" alt="Description" class="your-class">
```

## 📱 Responsive Breakpoints

- **Mobile (< 768px):** Single column layout, mobile menu
- **Tablet (768px - 1024px):** Two column layout
- **Desktop (> 1024px):** Three column layout

## 🔗 Navigation

All pages have consistent navigation:
- **Desktop:** Horizontal menu bar
- **Mobile:** Hamburger menu
- **Pages:** Home, Services, Advantages, About, Contact

## 📊 Content Mapping

| Page | Content | Key Sections |
|------|---------|--------------|
| index.html | Homepage | Hero, Services Preview, Contact CTA |
| services.html | Services | Accounting, Additional Services |
| advantages.html | Advantages | 11 Key Advantages |
| about.html | About | History, Philosophy, Development |
| contact.html | Contact | Form, Office Info, Maps |

## 🚀 Local Server (Optional)

For a better development experience, use a local server:

```bash
cd hetyner1
python3 -m http.server 8000
```

Then open: `http://localhost:8000`

## 🛠️ Browser Support

- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)

## 📝 Next Steps

1. **Test the website** - Open in multiple browsers and devices
2. **Customize colors** - Adjust to match brand guidelines
3. **Add images** - Insert your company images
4. **Connect forms** - Integrate with email service (SendGrid, Formspree, etc.)
5. **SEO optimization** - Add meta tags and structure data
6. **Google Analytics** - Add tracking code
7. **Google Maps** - Integrate real maps for locations

## 🔧 Common Tasks

### Add New Page
1. Create new HTML file
2. Copy navigation from existing pages
3. Update navigation links
4. Test links between pages

### Modify Content
1. Edit the text directly in the HTML files
2. Use semantic HTML for accessibility
3. Ensure responsive design works on mobile

### Change Contact Info
1. Edit `contact.html`
2. Update phone numbers, emails, addresses
3. Update footer in all pages

## 💡 Tips

- **Keep it simple:** The website is designed to be lightweight and fast
- **Stay consistent:** Use the same styling across all pages
- **Test mobile:** Check the mobile menu and layout
- **Keep content current:** Update contact info and services as needed
- **Accessibility:** Ensure all links and forms work properly

## 🆘 Support

If you need help with:
- **Technical issues** - Check browser console for errors
- **Design questions** - Review Tailwind CSS documentation
- **Content updates** - Edit the HTML files directly
- **Integration** - Use the `package.json` for build process

---

**Remember:** No build process required! Just open `index.html` and you're ready to go! 🚀