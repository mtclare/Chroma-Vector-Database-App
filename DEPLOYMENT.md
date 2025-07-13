# Email Vector Database - Railway Deployment Guide

This guide will help you deploy your Email Vector Database application on Railway.

## 🚀 Quick Deploy

### Option 1: Deploy via Railway Dashboard

1. **Fork/Clone this repository** to your GitHub account
2. **Go to [Railway.app](https://railway.app)** and sign in
3. **Click "New Project"** → "Deploy from GitHub repo"
4. **Select your repository** and Railway will automatically detect the Dockerfile
5. **Deploy** - Railway will build and deploy your application

### Option 2: Deploy via Railway CLI

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway:**
   ```bash
   railway login
   ```

3. **Initialize and deploy:**
   ```bash
   railway init
   railway up
   ```

## 🐳 Local Testing

Before deploying, test your Docker container locally:

```bash
# Test the deployment locally
./deploy.sh test

# Clean up after testing
./deploy.sh clean
```

Or manually:

```bash
# Build the Docker image
docker build -t email-vector-db .

# Run with Docker Compose
docker-compose up --build

# Test the application
curl http://localhost:8000/health
```

## 📁 Project Structure

```
Chroma-Vector-Database-App/
├── app.py                 # FastAPI application
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Local development setup
├── railway.json          # Railway deployment config
├── requirements.txt      # Python dependencies
├── deploy.sh            # Deployment helper script
├── .dockerignore        # Docker build exclusions
├── static/              # Static assets
├── templates/           # HTML templates
└── chroma_db/          # Vector database storage
```

## 🔧 Configuration

### Environment Variables

Railway will automatically set:
- `PORT` - The port your application should listen on

### Database Storage

⚠️ **Important**: ChromaDB data is stored locally in the container. For production use, consider:
- Using a persistent volume
- Migrating to a cloud vector database (Pinecone, Weaviate, etc.)

## 🏥 Health Checks

The application includes a health check endpoint at `/health` that Railway uses to monitor the application status.

## 📊 Monitoring

Railway provides:
- **Logs**: View application logs in the Railway dashboard
- **Metrics**: Monitor CPU, memory, and network usage
- **Deployments**: Track deployment history and rollback if needed

## 🔍 Troubleshooting

### Common Issues

1. **Build fails**: Check that all dependencies are in `requirements.txt`
2. **Application won't start**: Verify the port is set to `0.0.0.0` in `app.py`
3. **Health check fails**: Ensure the `/health` endpoint returns a 200 status

### Debug Commands

```bash
# View Railway logs
railway logs

# Check application status
railway status

# Restart the application
railway restart
```

## 🚀 Production Considerations

1. **Database Persistence**: Consider using Railway's persistent volumes or external database
2. **Environment Variables**: Set any sensitive configuration via Railway's environment variables
3. **Custom Domain**: Configure a custom domain in Railway dashboard
4. **SSL**: Railway provides automatic SSL certificates

## 📝 Next Steps

After deployment:
1. **Test the application** by visiting your Railway URL
2. **Add sample data** using the sample_data.py script (update the URL to your Railway domain)
3. **Monitor performance** in the Railway dashboard
4. **Set up custom domain** if needed

## 🆘 Support

- **Railway Documentation**: https://docs.railway.app
- **FastAPI Documentation**: https://fastapi.tiangolo.com
- **ChromaDB Documentation**: https://docs.trychroma.com 