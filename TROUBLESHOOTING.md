# Render Deployment Troubleshooting Guide

## Common Issues and Solutions

### 1. Rust/Cargo Build Errors

**Error**: `cargo metadata` exited with an error or `maturin` build failures

**Causes**:
- Packages with Rust dependencies (like some ML libraries)
- Memory constraints during build
- Incompatible package versions

**Solutions**:

#### Option A: Use Simplified Requirements
1. Rename `requirements-simple.txt` to `requirements.txt`
2. Rename `render-simple.yaml` to `render.yaml`
3. Redeploy

#### Option B: Manual Build Configuration
In your Render dashboard, set these environment variables:
```
RUST_BACKTRACE=1
MATURIN_PEP517_ARGS=--no-build-isolation
PIP_NO_CACHE_DIR=1
```

#### Option C: Upgrade Render Plan
- Free tier has limited memory for builds
- Consider upgrading to paid plan for more resources

### 2. Memory Issues During Build

**Error**: Build fails due to memory constraints

**Solutions**:
- Use `requirements-simple.txt` (removes heavy ML dependencies)
- Upgrade to paid Render plan
- Split build into smaller steps

### 3. Package Version Conflicts

**Error**: Version conflicts between packages

**Solutions**:
- Use exact versions in requirements.txt
- Avoid version ranges (use `==` instead of `>=`)
- Test locally first with `pip install -r requirements.txt`

### 4. Python Version Issues

**Error**: Python version compatibility

**Solutions**:
- Set `PYTHON_VERSION=3.9.16` in environment variables
- Ensure all packages support the Python version

## Quick Fix Commands

### For Rust/Cargo Errors:
```bash
# In Render dashboard, add these environment variables:
RUST_BACKTRACE=1
MATURIN_PEP517_ARGS=--no-build-isolation
PIP_NO_CACHE_DIR=1
```

### For Memory Issues:
```bash
# Use simplified requirements
cp requirements-simple.txt requirements.txt
cp render-simple.yaml render.yaml
```

### For Package Conflicts:
```bash
# Test locally first
pip install -r requirements.txt
```

## Alternative Deployment Strategies

### 1. Use Simplified Requirements
The `requirements-simple.txt` removes heavy ML dependencies that cause build issues.

### 2. Use External Vector Database
Instead of ChromaDB, consider:
- Pinecone (cloud vector database)
- Weaviate Cloud
- Qdrant Cloud

### 3. Use Docker Deployment
Create a `Dockerfile` for more control over the build environment.

## Render-Specific Tips

### Build Optimization:
- Use `--no-cache-dir` in pip install
- Set `PIP_DISABLE_PIP_VERSION_CHECK=1`
- Use exact package versions

### Environment Variables:
```
PYTHON_VERSION=3.9.16
RUST_BACKTRACE=1
MATURIN_PEP517_ARGS=--no-build-isolation
PIP_NO_CACHE_DIR=1
PIP_DISABLE_PIP_VERSION_CHECK=1
```

### Build Command:
```bash
pip install --upgrade pip setuptools wheel
pip install --no-cache-dir -r requirements.txt
```

## Getting Help

1. **Check Render Logs**: View detailed build logs in Render dashboard
2. **Test Locally**: Run `pip install -r requirements.txt` locally first
3. **Use Simplified Version**: Try `requirements-simple.txt` for testing
4. **Contact Support**: Render has excellent support for deployment issues

## Success Indicators

✅ **Successful Build**:
- All packages install without errors
- No Rust/Cargo compilation errors
- Build completes in under 10 minutes

✅ **Successful Deployment**:
- Health check endpoint responds (`/health`)
- Application loads without errors
- All features work as expected 