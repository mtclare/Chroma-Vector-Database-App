# Email Vector Database - Deployment Guide

This guide will walk you through deploying the Email Vector Database application on Render, a cloud platform that makes it easy to deploy web services.

## Quick Start (Recommended)

### Option 1: One-Click Deployment
1. Click the "Deploy to Render" button in the README
2. Connect your GitHub account
3. Your app will be deployed automatically

### Option 2: Manual Deployment
1. Go to [render.com](https://render.com) and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Use these exact settings:
   - **Name**: `email-vector-database`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements-basic.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
5. Click "Create Web Service"

Your app will be available at: `https://your-app-name.onrender.com`

## Prerequisites

- A Render account (free tier available)
- Git repository with your Email Vector Database code
- Basic understanding of Python web applications

## Step 1: Prepare Your Application

### 1.1 Use the Optimized Configuration

The project is already configured with the optimal settings:

- ✅ `render.yaml` - Optimized for Render deployment
- ✅ `requirements-basic.txt` - Minimal, stable dependencies
- ✅ `app.py` - Production-ready with health checks
- ✅ All necessary files are included

### 1.2 Verify Your Files

Ensure these files are in your repository:
```
email-vector-database/
├── app.py                 # Main FastAPI application
├── requirements-basic.txt  # Optimized dependencies
├── render.yaml            # Render configuration
├── templates/
│   └── index.html        # Web interface
├── static/
│   ├── app.js           # Frontend JavaScript
│   └── style.css        # Styling
└── README.md            # Documentation
```

## Step 2: Deploy on Render

### 2.1 Connect Your Repository

1. **Sign up/Login to Render**: Go to [render.com](https://render.com)
2. **Connect GitHub/GitLab**: Link your Git repository to Render
3. **Create New Web Service**: Click "New +" and select "Web Service"

### 2.2 Configure Your Service

Use these exact settings:

- **Name**: `email-vector-database`
- **Environment**: `Python 3`
- **Region**: Choose closest to your users
- **Branch**: `main` (or your default branch)
- **Root Directory**: Leave empty
- **Build Command**: `pip install -r requirements-basic.txt`
- **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`

### 2.3 Environment Variables (Optional)

Add these in the Render dashboard if needed:

- `PYTHON_VERSION`: `3.9.16`
- `PIP_NO_CACHE_DIR`: `1`

### 2.4 Deploy

1. Click "Create Web Service"
2. Wait for build to complete (2-5 minutes)
3. Your app will be live at the provided URL

## Step 3: Post-Deployment

### 3.1 Verify Deployment

1. **Check Build Logs**: Ensure no errors during build
2. **Test Your Application**: Visit your Render URL
3. **Test Functionality**: Try adding and searching emails
4. **Check Health**: Visit `/health` endpoint

### 3.2 Add Sample Data

1. Visit your deployed app
2. Use the "Add New Email" form to add some test emails
3. Try the search functionality
4. Check the metrics dashboard

## Features Available After Deployment

✅ **Email Management**: Add, search, delete emails
✅ **Semantic Search**: AI-powered search using natural language
✅ **Metrics Dashboard**: Real-time database statistics
✅ **Responsive UI**: Works on all devices
✅ **Health Monitoring**: Built-in health checks
✅ **Modern Interface**: Beautiful, user-friendly design

## Troubleshooting

### Common Issues

#### 1. Build Failures
```
Error: Could not find a version that satisfies the requirement
```
**Solution**: The optimized `requirements-basic.txt` should prevent this

#### 2. Port Issues
```
Error: Address already in use
```
**Solution**: The `$PORT` environment variable handles this automatically

#### 3. Memory Issues
```
Error: Out of memory
```
**Solution**: The basic requirements minimize memory usage

### Debug Commands

Your app includes these endpoints for debugging:
- `/health` - Health check
- `/get_metrics` - Database statistics
- `/get_all_emails` - List all emails

## Production Considerations

### 1. Database Persistence

**Important**: Render's free tier has ephemeral storage. For production:

1. **Use Render's Persistent Disk** (paid feature):
   - Add a disk in your service settings
   - Mount it to `/opt/render/project/src/chroma_db`

2. **Alternative**: Use external vector database services:
   - Pinecone
   - Weaviate Cloud
   - Qdrant Cloud

### 2. Performance Optimization

1. **Monitor Usage**: Check Render dashboard for performance metrics
2. **Upgrade Plan**: Consider paid plan for better performance
3. **Auto-scaling**: Enable for high-traffic applications

### 3. Security

- ✅ HTTPS provided by Render
- ✅ Environment variables for secrets
- ✅ No sensitive data in code

## Cost Optimization

### Free Tier Limits
- 750 hours/month
- 512 MB RAM
- Shared CPU
- No persistent disk

### Paid Features
- Persistent disk: $7/month
- Auto-scaling: $7/month
- Dedicated instances: $25/month

## Support and Resources

- **Render Documentation**: [docs.render.com](https://docs.render.com)
- **FastAPI Documentation**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- **ChromaDB Documentation**: [docs.trychroma.com](https://docs.trychroma.com)

## Success Indicators

✅ **Successful Build**:
- All packages install without errors
- Build completes in under 5 minutes
- No dependency conflicts

✅ **Successful Deployment**:
- Health check endpoint responds (`/health`)
- Application loads without errors
- All features work as expected
- Metrics dashboard shows data

---

**Note**: This deployment guide uses the optimized configuration that has been tested and should work immediately on Render. The `requirements-basic.txt` and `render.yaml` files are specifically designed to avoid common deployment issues. 