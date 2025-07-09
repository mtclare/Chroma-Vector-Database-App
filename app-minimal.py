from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import json
import os
from typing import List, Dict, Any
from datetime import datetime
import uuid

app = FastAPI(title="Email Database", description="A simple email storage and search application")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Simple in-memory storage (for demo purposes)
emails_db = []

def simple_search(query: str, emails: List[Dict]) -> List[Dict]:
    """Simple text-based search (no ML)"""
    query_lower = query.lower()
    results = []
    
    for email in emails:
        if (query_lower in email['content'].lower() or 
            query_lower in email.get('date', '').lower()):
            results.append({
                **email,
                'similarity_score': 0.8  # Mock similarity score
            })
    
    return results

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page with email management interface"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/add_email")
async def add_email(
    content: str = Form(...),
    date: str = Form(...)
):
    """Add an email to the database"""
    try:
        # Create email document
        email_id = str(uuid.uuid4())
        
        email_data = {
            "id": email_id,
            "content": content,
            "date": date,
            "metadata": {
                "date": date,
                "id": email_id
            }
        }
        
        emails_db.append(email_data)
        
        return {"success": True, "message": "Email added successfully", "id": email_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search_emails")
async def search_emails(query: str = Form(...), limit: int = Form(10)):
    """Search emails using simple text matching"""
    try:
        # Simple search implementation
        results = simple_search(query, emails_db)
        
        # Limit results
        results = results[:limit]
        
        # Format results for frontend
        emails = []
        for result in results:
            emails.append({
                "content": f"Date: {result['date']}\n\n{result['content']}",
                "metadata": result['metadata'],
                "similarity_score": result.get('similarity_score', 0.8)
            })
        
        return {"success": True, "emails": emails, "query": query}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_emails")
async def get_all_emails():
    """Get all emails from the database"""
    try:
        emails = []
        for email in emails_db:
            emails.append({
                "content": f"Date: {email['date']}\n\n{email['content']}",
                "metadata": email['metadata']
            })
        
        return {"success": True, "emails": emails}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_email/{email_id}")
async def delete_email(email_id: str):
    """Delete an email from the database"""
    try:
        global emails_db
        emails_db = [email for email in emails_db if email['id'] != email_id]
        return {"success": True, "message": "Email deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_metrics")
async def get_metrics():
    """Get database metrics and statistics"""
    try:
        total_emails = len(emails_db)
        
        # Calculate date range if emails exist
        date_range = {"earliest": None, "latest": None}
        if total_emails > 0:
            dates = [email.get('date') for email in emails_db if email.get('date')]
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
        if total_emails > 0:
            content_lengths = [len(email['content']) for email in emails_db]
            avg_content_length = sum(content_lengths) // len(content_lengths)
        
        metrics = {
            "total_emails": total_emails,
            "date_range": date_range,
            "avg_content_length": avg_content_length,
            "database_size": "In-Memory Storage",
            "embedding_model": "Simple Text Search"
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