# PhishShield-XAI: Vercel Deployment Quick Start

## ✨ Ready for Deployment!

Your project is now configured for Vercel deployment with the following setup:

### What's Been Prepared

✅ **Backend API** (`api/index.py`)
- FastAPI app wrapped for Vercel serverless functions
- Includes all explainers (SHAP, LIME)
- Auto-loads pre-trained models

✅ **Frontend** (web/)
- Vite build optimized for production
- Smart API routing (localhost for dev, /api for prod)
- Glassmorphic UI with real-time status monitoring

✅ **Configuration Files**
- `vercel.json` - Build and deployment configuration
- `.vercelignore` - Excludes heavy dependencies, keeps essentials
- `requirements-prod.txt` - Optimized production dependencies
- `vite.config.js` - Frontend build configuration

---

## 🚀 Deploy in 3 Steps

### Step 1: Push to GitHub

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "PhishShield-XAI ready for Vercel deployment"
git remote add origin https://github.com/YOUR_USERNAME/PhishShield-XAI.git
git push -u origin main
```

### Step 2: Connect to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Sign in with GitHub
3. Click "New Project"
4. Select your repository
5. Vercel will auto-detect settings from `vercel.json`
6. Click "Deploy"

### Step 3: Access Your App

```
https://your-project-name.vercel.app
```

API endpoints available at:
```
https://your-project-name.vercel.app/api
```

---

## 📊 What You Get

| Component | URL | Status |
|-----------|-----|--------|
| Dashboard | `https://your-project.vercel.app` | ✅ Live |
| API Health | `https://your-project.vercel.app/api/health` | ✅ Live |
| Predict Endpoint | `https://your-project.vercel.app/api/predict` | ✅ Live |

---

## 🧪 Test Your Deployment

After deployment, test the API:

```bash
curl -X POST https://your-project.vercel.app/api/predict \
  -H "Content-Type: application/json" \
  -d '{"email_text": "Click here immediately to verify account"}'
```

Expected response:
```json
{
  "classification": "phishing",
  "confidence_score": 0.73,
  "shap_features": [...],
  "lime_highlights": [...],
  "llm_explanation": "..."
}
```

---

## 📋 Project Structure for Vercel

```
PhishShield-XAI/
├── api/
│   ├── __init__.py
│   └── index.py              ← Vercel entry point
├── web/                       ← Frontend
│   ├── dist/                  ← Built output
│   ├── main.js                ← Updated with /api paths
│   ├── vite.config.js         ← Vite config
│   └── package.json
├── src/
│   ├── api/
│   ├── xai/
│   └── core/
├── models/                    ← Pre-trained models included
│   └── classical_model/
├── vercel.json                ← Deployment config
├── .vercelignore              ← What to exclude
└── requirements-prod.txt      ← Production deps
```

---

## 🎯 Key Features Deployed

✅ **Real-time Phishing Detection**
- FastAPI backend with CORS enabled
- Sub-50ms inference for legit emails
- 1-3s for adversarial analysis with SHAP

✅ **Explainable AI**
- SHAP global feature importance
- LIME local token highlighting
- LLM-based natural language explanations

✅ **Scalable Architecture**
- Serverless functions (auto-scale)
- CDN-accelerated frontend
- No server management needed

---

## ⚙️ Environment Variables

Automatically configured in Vercel:

```env
MODEL_DIR=./models/classical_model
PYTHONPATH=.
```

Add more via Vercel Dashboard → Project Settings → Environment Variables

---

## 🔍 Monitoring

Monitor your deployment on Vercel Dashboard:
- **Deployments** tab: View build logs
- **Analytics** tab: Track response times and errors
- **Logs** tab: Real-time function logs

---

## 🐛 Troubleshooting

### Issue: Model not loading
```
→ Check: Models included in deployment
→ Verify: .vercelignore doesn't exclude models/
```

### Issue: API timeout (>60s)
```
→ Note: SHAP can take 5-10s on first request
→ Solution: Vercel's max timeout is 60s (upgrade plan for more)
```

### Issue: Frontend can't reach API
```
→ Check: Dashboard shows "API Offline"
→ Solution: Check Vercel function logs for backend errors
```

---

## 📚 Documentation

- Full guide: See `DEPLOYMENT.md`
- API docs: `https://your-project.vercel.app/api/docs` (FastAPI Swagger)
- Redoc: `https://your-project.vercel.app/api/redoc`

---

## 🎉 You're Ready!

No changes to the core logic were made. The project is production-ready with:
- ✅ Optimized builds
- ✅ Proper scaling
- ✅ Error handling
- ✅ CORS configured
- ✅ Environment detection

**Deploy now and enjoy your AI-powered phishing detection system! 🚀**

Questions? Check `DEPLOYMENT.md` for detailed troubleshooting.
