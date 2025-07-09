from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import json
import os
from typing import List, Dict, Any
from datetime import datetime
import uuid

app = FastAPI(title="Email Vector Database", description="A free app to retrieve emails from a local vector database")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Initialize sentence transformer for embeddings
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Create or get collection
try:
    email_collection = chroma_client.get_collection("emails")
except:
    email_collection = chroma_client.create_collection("emails")

def get_embedding(text: str) -> List[float]:
    """Generate embedding for text"""
    return embedding_model.encode(text).tolist()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page with email management interface"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/add_email")
async def add_email(
    content: str = Form(...),
    date: str = Form(...)
):
    """Add an email to the vector database"""
    try:
        # Create email document
        email_id = str(uuid.uuid4())
        email_text = f"Date: {date}\n\n{content}"
        
        # Generate embedding
        embedding = get_embedding(email_text)
        
        # Add to collection
        email_collection.add(
            documents=[email_text],
            embeddings=[embedding],
            metadatas=[{
                "date": date,
                "id": email_id
            }],
            ids=[email_id]
        )
        
        return {"success": True, "message": "Email added successfully", "id": email_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search_emails")
async def search_emails(query: str = Form(...), limit: int = Form(10)):
    """Search emails using semantic similarity"""
    try:
        # Generate embedding for query
        query_embedding = get_embedding(query)
        
        # Search in collection
        results = email_collection.query(
            query_embeddings=[query_embedding],
            n_results=limit,
            include=["documents", "metadatas", "distances"]
        )
        
        # Format results
        emails = []
        if results['documents'] and results['documents'][0]:
            for i, doc in enumerate(results['documents'][0]):
                metadata = results['metadatas'][0][i]
                distance = results['distances'][0][i]
                
                emails.append({
                    "content": doc,
                    "metadata": metadata,
                    "similarity_score": 1 - distance  # Convert distance to similarity
                })
        
        return {"success": True, "emails": emails, "query": query}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_emails")
async def get_all_emails():
    """Get all emails from the database"""
    try:
        results = email_collection.get()
        
        emails = []
        if results['documents']:
            for i, doc in enumerate(results['documents']):
                metadata = results['metadatas'][i]
                emails.append({
                    "content": doc,
                    "metadata": metadata
                })
        
        return {"success": True, "emails": emails}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_email/{email_id}")
async def delete_email(email_id: str):
    """Delete an email from the database"""
    try:
        email_collection.delete(ids=[email_id])
        return {"success": True, "message": "Email deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_metrics")
async def get_metrics():
    """Get database metrics and statistics"""
    try:
        # Get collection info
        collection_info = email_collection.get()
        
        # Calculate metrics
        total_emails = len(collection_info['ids']) if collection_info['ids'] else 0
        
        # Get date range if emails exist
        date_range = {"earliest": None, "latest": None}
        if total_emails > 0 and collection_info['metadatas']:
            dates = [metadata.get('date') for metadata in collection_info['metadatas'] if metadata and metadata.get('date')]
            if dates:
                try:
                    parsed_dates = [datetime.fromisoformat(date.replace('T', ' ')) for date in dates if date]
                    if parsed_dates:
                        date_range["earliest"] = min(parsed_dates).strftime("%Y-%m-%d %H:%M")
                        date_range["latest"] = max(parsed_dates).strftime("%Y-%m-%d %H:%M")
                except:
                    pass
        
        # Calculate average content length
        avg_content_length = 0
        if total_emails > 0 and collection_info['documents']:
            content_lengths = [len(doc) for doc in collection_info['documents'] if doc]
            avg_content_length = sum(content_lengths) // len(content_lengths) if content_lengths else 0
        
        metrics = {
            "total_emails": total_emails,
            "date_range": date_range,
            "avg_content_length": avg_content_length,
            "database_size": "Local ChromaDB",
            "embedding_model": "all-MiniLM-L6-v2"
        }
        
        return {"success": True, "metrics": metrics}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    import os
    
    # Get port from environment variable (Render sets this)
    port = int(os.environ.get("PORT", 8000))
    
    # Use 0.0.0.0 to bind to all available network interfaces
    uvicorn.run(app, host="0.0.0.0", port=port) 