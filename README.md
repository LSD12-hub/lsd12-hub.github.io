# LSD12 Hub & Projects (lsd12-hub.github.io)

Personal GitHub Pages hub and portfolio for [Lesedi Jonas](https://github.com/LSD12-hub).

🌐 **Live Website**: [https://lsd12-hub.github.io](https://lsd12-hub.github.io)

---

## 📁 Repository Structure

```
.
├── index.html          # Hub & router entry page
├── 404.html            # Smart path redirection & fallback
├── .nojekyll           # Disables Jekyll to serve SvelteKit assets (_app/)
├── .github/
│   └── workflows/
│       └── deploy.yml  # Automated GitHub Actions deployment
├── Git-slides/         # Interactive Git presentation (Animotion + SvelteKit)
│   ├── src/            # Slide decks and animations
│   ├── static/         # Slide images and media
│   ├── package.json    # Dependencies & build scripts
│   └── ...             # Static built site for direct hosting
└── Portfolio site/     # Developer portfolio and CV
    ├── index.html      # Portfolio webpage
    ├── style.css       # Portfolio stylesheet
    └── images/         # Profile assets
```

---

## 🚀 Projects Included

### 1. [Git Slides Presentation](./Git-slides/)
- **Live Path**: [https://lsd12-hub.github.io/Git-slides/](https://lsd12-hub.github.io/Git-slides/)
- **Description**: An animated, interactive presentation on how Git works internally (objects, hashing, trees, commits, and branches).
- **Tech Stack**: [Animotion](https://animotion.pages.dev/), SvelteKit, Reveal.js, TailwindCSS.

### 2. [Portfolio Site](./Portfolio%20site/)
- **Live Path**: [https://lsd12-hub.github.io/Portfolio%20site/](https://lsd12-hub.github.io/Portfolio%20site/)
- **Description**: Personal portfolio and CV highlighting programming skills, education, and volunteer mentoring at WeThinkCode_.
- **Tech Stack**: HTML5, CSS3 responsive.

---

## 🛠️ Local Development (Git Slides)

To run the Git Slides presentation locally in development mode:

```bash
cd Git-slides
npm install
npm run dev
```

To build the static presentation:

```bash
npm run build
```
The build automatically compiles and syncs static assets to `Git-slides/` for GitHub Pages.
