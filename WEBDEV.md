# Node JS
```
npm i -s express mongoose cors dotenv debug
npm init

.gitignore
node_modules
.env

package.json
"type": "module",

node server.js
```


# Vite
```
npm create vite@latest
cd dirName
npm i
npm run dev
changing port @ vite.config.ts
npm run build -> create a dist folder
npm install -s @mui/material @emotion/react @emotion/styled
IconMenu ->
npm i -s @mui/icons-material

npm i -s react-redux @reduxjs/toolkit
npm i -s i18next react-i18next i18next-http-backend
npm install -s react-router-dom localforage match-sorter sort-by
```


# PWA Config => Installable Web App
```
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { VitePWA } from 'vite-pl'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 3002
  },
  plugins: [react(), 
    VitePWA({
    registerType: 'autoUpdate',
    devOptions: {
      enabled: true
    }
    manifest: {
    "name": "CourseRegistration",
    "short_name": "CourseRegist",
    "start_url": "./",
    "display": "standalone",
    "background_color": "#fff",
    "description": "Course Registration App.",
    "theme_color": "#ffffff",
    "icons": [
    {
    "src": "images/pwa-512x512.png",
    "sizes": "168x168",
    "type": "image/png"
    },
    {
    "src": "images/pwa-192x192.png",
    "sizes": "192x192",
    "type": "image/png"
    }
    ]
    }})
    ],
})
```

## Vite Config with Server
```
import restart from 'vite-plugin-restart'

export default {
    root: 'src/', // Sources files (typically where index.html is)
    publicDir: '../static/', // Path from "root" to static assets (files that are served as they are)
    server:
    {
        host: true, // Open to local network and display URL
        open: !('SANDBOX_URL' in process.env || 'CODESANDBOX_HOST' in process.env) // Open if it's not a CodeSandbox
    },
    build:
    {
        outDir: '../dist', // Output in the dist/ folder
        emptyOutDir: true, // Empty the folder first
        sourcemap: true // Add sourcemap
    },
    plugins:
    [
        restart({ restart: [ '../static/**', ] }) // Restart server on static file change
    ],
}
```