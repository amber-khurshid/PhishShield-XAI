import { defineConfig } from 'vite'
import path from 'path'

export default defineConfig({
  root: './',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    minify: 'terser'
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  },
  define: {
    '__DEV__': true,
    'process.env.API_BASE': JSON.stringify(
      process.env.VERCEL ? '/api' : 'http://localhost:8000'
    )
  }
})
