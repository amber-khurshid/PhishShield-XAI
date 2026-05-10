# PhishShield-XAI Vercel Deployment Guide

## Quick Start

Deploy PhishShield-XAI to Vercel with both frontend and backend (API) running on serverless functions.

### Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **GitHub Repository**: Push your code to GitHub
3. **Vercel CLI** (optional): `npm i -g vercel`

---

## One-Click Deployment

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Configure settings:
   - **Build Command**: `cd web && npm install && npm run build`
   - **Output Directory**: `web/dist`
   - **Environment Variables**:
     - `MODEL_DIR`: `./models/classical_model`
     - `PYTHONPATH`: `.`
5. Click "Deploy"

### Option 2: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy from project root
vercel

# For production
vercel --prod
```

---

## Deployment Structure

```
PhishShield-XAI/
├── api/
│   └── index.py              # Serverless API endpoint
├── web/                       # Frontend (Vite)
│   ├── dist/                  # Built frontend
│   ├── package.json
│   ├── vite.config.js         # Vite configuration
│   └── main.js                # Updated with /api paths
├── src/
│   ├── api/
│   ├── xai/
│   └── core/
├── models/                    # Pre-trained models (included)
│   └── classical_model/
├── vercel.json                # Vercel configuration
├── .vercelignore              # Files to exclude
└── requirements-prod.txt      # Production dependencies
```

---

## What Gets Deployed

✅ **Frontend (Vite)**
- Optimized static build served from `web/dist`
- Automatically deployed on every push

✅ **Backend (FastAPI)**
- Serverless Python function at `/api`
- Models bundled with the deployment
- Cold startup: ~3-5 seconds
- Max timeout: 60 seconds per request

❌ **Not Deployed** (excluded via .vercelignore)
- Development dependencies (torch, transformers, etc.)
- Raw datasets
- Notebooks
- Git history

---

## API Endpoints

After deployment, your API will be available at:

```
https://<your-project>.vercel.app/api
```

### Available Routes

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Health check |
| `/api/predict` | POST | Single email analysis |
| `/api/batch_analyze` | POST | Multiple emails |

### Example Request

```bash
curl -X POST https://<your-project>.vercel.app/api/predict \
  -H "Content-Type: application/json" \
  -d '{"email_text": "Click here to verify your account"}'
```

---

## Frontend Access

Your dashboard will be available at:

```
https://<your-project>.vercel.app
```

The frontend automatically detects the environment and uses:
- `http://localhost:8000` when running locally
- `/api` when deployed on Vercel

---

## Troubleshooting

### 1. **Model Loading Error**
**Error**: `Model not loaded`

**Solution**:
- Ensure `models/classical_model/` directory is included
- Check that `.vercelignore` doesn't exclude `models/`
- Verify `MODEL_DIR` environment variable is set

### 1b. **Serverless Memory Limit Error**
**Error**: `Serverless Functions are limited to 2048 mb of memory for personal accounts (Hobby plan).`

**Solution**:
- The deployment is now configured to use `2048 MB` in [vercel.json](vercel.json)
- If the function still exceeds memory during cold start, reduce model size or move to a Vercel Team/Pro plan
- Keep SHAP background samples small to lower memory usage

### 2. **SHAP Features Unavailable**
**Error**: `"feature": "unavailable"`

**Solution**:
- This is expected on first request (cold start)
- The fixed SHAP explainer should work after initialization
- Check backend logs: `vercel logs`

### 3. **API Timeout**
**Error**: `504 Gateway Timeout`

**Solution**:
- SHAP computations can be slow (5-10 seconds initially)
- KernelExplainer has been optimized with 10 background samples
- Consider caching results for repeated queries

### 4. **CORS Issues**
**Error**: `Access to XMLHttpRequest blocked by CORS`

**Solution**:
- Already configured in `vercel.json` with proper rewrites
- Frontend uses `/api` path which bypasses CORS

---

## Performance Tips

1. **First Request**: ~3-5 seconds (cold start)
2. **Subsequent Requests**: ~1-2 seconds
3. **SHAP Computation**: ~2-5 seconds per request
4. **Caching**: Consider implementing request caching in the frontend

---

## Rollback

To rollback to a previous deployment:

```bash
# List deployments
vercel list

# Promote a specific deployment to production
vercel promote <deployment-url>
```

---

## Environment Variables

Available environment variables for customization:

```env
MODEL_DIR = ./models/classical_model
PYTHONPATH = .
LOG_LEVEL = INFO
```

---

## Size Optimization

The `.vercelignore` file excludes:
- ❌ Development dependencies (torch, transformers)
- ❌ Raw datasets
- ❌ Notebooks and reports
- ✅ Inference libraries only (scikit-learn, xgboost, shap, lime)
- ✅ Pre-trained models

**Estimated Build Size**: ~200-300 MB (within Vercel's limits)

---

## Monitoring

Track your deployment performance:

1. Go to your project on vercel.com
2. Click "Analytics" to view:
   - Response times
   - Error rates
   - Function execution times
   - Cold/warm starts

---

## Local Testing Before Deploy

```bash
# Test locally first
npm run build && vercel --prod --dry-run

# Full local deployment simulation
vercel env pull  # Get environment variables
npm run dev      # Run frontend
# In another terminal
source venv/bin/activate
python -m src.api.app  # Run backend
```

---

## Support & Resources

- **Vercel Docs**: https://vercel.com/docs
- **FastAPI Vercel Guide**: https://vercel.com/guides/using-fastapi-with-vercel
- **Project Issues**: Check the main README.md

---

## Next Steps

After successful deployment:

1. ✅ Test the API endpoints
2. ✅ Monitor performance on Vercel Analytics
3. ✅ Set up GitHub Actions for CI/CD (optional)
4. ✅ Configure custom domains (optional)
5. ✅ Set up error alerts (optional)

**Deployment Complete!** 🚀
