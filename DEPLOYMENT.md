# Email Vector Database - Deployment Guide

This guide will walk you through deploying the Email Vector Database application on Render, a cloud platform that makes it easy to deploy web services.

## Prerequisites

- A Render account (free tier available)
- Git repository with your Email Vector Database code
- Basic understanding of Python web applications

## Step 1: Prepare Your Application

### 1.1 Create a `render.yaml` file

Create a `render.yaml` file in your project root to define your service:

```yaml
services:
  - type: web
    name: email-vector-database
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.16
```

### 1.2 Update your `app.py` for production

Modify the last lines of your `app.py` to work with Render's environment:

```python
if __name__ == "__main__":
    import uvicorn
    import os
    
    # Get port from environment variable (Render sets this)
    port = int(os.environ.get("PORT", 8000))
    
    # Use 0.0.0.0 to bind to all available network interfaces
    uvicorn.run(app, host="0.0.0.0", port=port)
```

### 1.3 Create a `requirements.txt` file

Ensure your `requirements.txt` includes all necessary dependencies:

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
chromadb==0.4.15
sentence-transformers==2.2.2
python-multipart==0.0.6
jinja2==3.1.2
aiofiles==23.2.1
```

### 1.4 Create a `.gitignore` file

Create a `.gitignore` file to exclude unnecessary files:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# Database
chroma_db/
*.db
*.sqlite

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Environment variables
.env
.env.local
```

## Step 2: Deploy on Render

### 2.1 Connect Your Repository

1. **Sign up/Login to Render**: Go to [render.com](https://render.com) and create an account
2. **Connect GitHub/GitLab**: Link your Git repository to Render
3. **Create New Web Service**: Click "New +" and select "Web Service"

### 2.2 Configure Your Service

Fill in the following details:

- **Name**: `email-vector-database` (or your preferred name)
- **Environment**: `Python 3`
- **Region**: Choose closest to your users
- **Branch**: `main` (or your default branch)
- **Root Directory**: Leave empty (if your code is in the root)
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`

### 2.3 Environment Variables (Optional)

Add these environment variables in the Render dashboard if needed:

- `PYTHON_VERSION`: `3.9.16`
- `CHROMA_DB_PATH`: `/opt/render/project/src/chroma_db` (for persistent storage)

### 2.4 Deploy

1. Click "Create Web Service"
2. Render will automatically build and deploy your application
3. Wait for the build to complete (usually 2-5 minutes)

## Step 3: Post-Deployment Configuration

### 3.1 Verify Deployment

1. **Check Build Logs**: Ensure no errors during build
2. **Test Your Application**: Visit your Render URL (e.g., `https://your-app-name.onrender.com`)
3. **Test Functionality**: Try adding and searching emails

### 3.2 Custom Domain (Optional)

1. Go to your service settings in Render
2. Click "Custom Domains"
3. Add your domain and follow DNS configuration instructions

## Step 4: Production Considerations

### 4.1 Database Persistence

**Important**: Render's free tier has ephemeral storage, meaning your ChromaDB data will be lost when the service restarts. For production:

1. **Use Render's Persistent Disk** (paid feature):
   - Add a disk in your service settings
   - Mount it to `/opt/render/project/src/chroma_db`

2. **Alternative**: Use external vector database services like:
   - Pinecone
   - Weaviate Cloud
   - Qdrant Cloud

### 4.2 Environment Variables for Production

```bash
# Add these in Render dashboard
CHROMA_DB_PATH=/opt/render/project/src/chroma_db
LOG_LEVEL=INFO
ENVIRONMENT=production
```

### 4.3 Performance Optimization

1. **Enable Auto-Scaling** (paid feature):
   - Set min/max instances
   - Configure scaling rules

2. **Memory Optimization**:
   - Monitor memory usage in Render dashboard
   - Consider upgrading if needed

## Step 5: Monitoring and Maintenance

### 5.1 Monitor Your Application

- **Render Dashboard**: Check logs, metrics, and performance
- **Health Checks**: Set up health check endpoints
- **Error Tracking**: Consider adding error tracking (Sentry, etc.)

### 5.2 Regular Maintenance

1. **Update Dependencies**: Regularly update `requirements.txt`
2. **Security Updates**: Keep Python and packages updated
3. **Backup Data**: If using persistent storage, backup regularly

## Troubleshooting

### Common Issues

#### 1. Build Failures
```
Error: Could not find a version that satisfies the requirement
```
**Solution**: Check your `requirements.txt` for version conflicts

#### 2. Port Issues
```
Error: Address already in use
```
**Solution**: Ensure you're using `$PORT` environment variable

#### 3. Database Access Issues
```
Error: Permission denied for chroma_db
```
**Solution**: Check file permissions and paths

#### 4. Memory Issues
```
Error: Out of memory
```
**Solution**: Upgrade to paid plan or optimize memory usage

### Debug Commands

Add these to your `app.py` for debugging:

```python
import logging
logging.basicConfig(level=logging.INFO)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
```

## Security Considerations

### 1. Environment Variables
- Never commit sensitive data to Git
- Use Render's environment variable feature
- Rotate secrets regularly

### 2. HTTPS
- Render provides HTTPS by default
- Use HTTPS URLs in your application

### 3. Rate Limiting
- Consider adding rate limiting for production
- Monitor usage patterns

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

## Example Deployment URL

After successful deployment, your application will be available at:
```
https://your-app-name.onrender.com
```

Replace `your-app-name` with the name you chose during setup.

---

**Note**: This deployment guide assumes you're using the standard Email Vector Database setup. Custom modifications may require additional configuration steps. 