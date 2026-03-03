# Python Portfolio

This folder contains a static portfolio site generated from projects in this repository.

## Preview locally

```powershell
cd portfolio
py -m http.server 8080
```

Open http://localhost:8080

## Click-to-run behavior

- Projects marked **Browser compatible** run in-page using Pyodide.
- Runnable project files are bundled into `portfolio/runtime/*.json`, so no cross-folder fetches are required.
- Some projects still require desktop Python (for example `tkinter`, `turtle`, `smtplib`, `pyperclip`).

## Regenerate metadata and runtime bundles

```powershell
cd portfolio
powershell -NoProfile -ExecutionPolicy Bypass -File .\generate_projects.ps1
```

## Deploy notes

Deploy the full `portfolio/` folder (including `runtime/`) to any static host (GitHub Pages, Netlify, etc.).
