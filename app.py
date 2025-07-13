from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import json
import os
from typing import List, Dict, Any, Optional
from datetime import datetime
import uuid
import numpy as np
import math

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
    emb = embedding_model.encode(text, convert_to_numpy=True)
    return np.asarray(emb).tolist()

def distance_to_similarity(distance: Optional[float]) -> Optional[float]:
    """
    Convert L2 distance to similarity score using inverse distance.
    similarity = 1 / (1 + distance)
    This gives values between 0 and 1, where 1 means identical vectors.
    """
    if distance is None:
        return None
    
    # Avoid division by zero
    if distance == 0:
        return 1.0
    
    similarity = 1 / (1 + distance)
    return similarity

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page with email management interface"""
    return templates.TemplateResponse("index.html", {"request": request, "year": datetime.now().year})

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
        docs = results.get('documents')
        metas = results.get('metadatas')
        dists = results.get('distances')
        if docs and docs[0]:
            for i, doc in enumerate(docs[0]):
                metadata = metas[0][i] if metas and metas[0] else None
                distance = dists[0][i] if dists and dists[0] else None
                similarity = distance_to_similarity(distance)
                emails.append({
                    "content": doc,
                    "metadata": metadata,
                    "similarity_score": similarity
                })
        
        return {"success": True, "emails": emails, "query": query}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/count_similar_emails")
async def count_similar_emails(query: str = Form(...), threshold: float = Form(0.7)):
    """Count emails with similarity score above threshold for a given query"""
    try:
        # Generate embedding for query
        query_embedding = get_embedding(query)
        # Search in collection (get all possible results)
        results = email_collection.query(
            query_embeddings=[query_embedding],
            n_results=1000,  # Large number to cover all
            include=["distances"]
        )
        dists = results.get('distances')
        count = 0
        if dists and dists[0]:
            for distance in dists[0]:
                similarity = distance_to_similarity(distance)
                if similarity is not None and similarity > threshold:
                    count += 1
        return {"success": True, "count": count, "threshold": threshold}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/get_emails_above_threshold")
async def get_emails_above_threshold(query: str = Form(...), threshold: float = Form(0.7)):
    """Get emails with similarity score above threshold for a given query"""
    try:
        # Generate embedding for query
        query_embedding = get_embedding(query)
        
        # Search in collection (get all possible results)
        results = email_collection.query(
            query_embeddings=[query_embedding],
            n_results=100000,  # Large number to cover all
            include=["documents", "metadatas", "distances"]
        )
        
        # Format results
        emails = []
        docs = results.get('documents')
        metas = results.get('metadatas')
        dists = results.get('distances')
        
        if docs and docs[0]:
            for i, doc in enumerate(docs[0]):
                metadata = metas[0][i] if metas and metas[0] else None
                distance = dists[0][i] if dists and dists[0] else None
                similarity = distance_to_similarity(distance)
                
                # Only include emails above threshold
                if similarity is not None and similarity > threshold:
                    emails.append({
                        "content": doc,
                        "metadata": metadata,
                        "similarity_score": similarity
                    })
        
        return {"success": True, "emails": emails, "query": query, "threshold": threshold}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_emails")
async def get_all_emails():
    """Get all emails from the database"""
    try:
        results = email_collection.get()
        
        emails = []
        docs = results.get('documents')
        metas = results.get('metadatas')
        if docs:
            for i, doc in enumerate(docs):
                metadata = metas[i] if metas else None
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
        date_range = {}
        if total_emails > 0 and collection_info['metadatas']:
            dates = [metadata.get('date') for metadata in collection_info['metadatas'] if metadata and metadata.get('date')]
            if dates:
                try:
                    parsed_dates = [datetime.fromisoformat(date.replace('T', ' ')) for date in dates if isinstance(date, str) and 'T' in date]
                    if parsed_dates:
                        earliest = min(parsed_dates).strftime("%Y-%m-%d %H:%M")
                        latest = max(parsed_dates).strftime("%Y-%m-%d %H:%M")
                        if earliest:
                            date_range["earliest"] = earliest
                        if latest:
                            date_range["latest"] = latest
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

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    import os
    
    # Get port from environment variable (Railway sets this)
    port = int(os.environ.get("PORT", 8000))
    
    # Use 0.0.0.0 to bind to all available network interfaces for container deployment
    uvicorn.run(app, host="0.0.0.0", port=port) 