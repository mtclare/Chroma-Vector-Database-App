# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Running the Application
```bash
python app.py
# Starts FastAPI server on http://localhost:8000 (default) or PORT env variable
```

### Alternative Development Server
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
# Run with auto-reload for development
```

### Sample Data Population
```bash
python sample_data.py
# Adds 8 sample emails to the database (requires app to be running)
```

### Health Check
```bash
curl http://localhost:8000/health
# Verify application status
```

### Dependencies
```bash
pip install -r requirements.txt
# Install all required packages
```

## Architecture Overview

### Core Components
- **FastAPI Application** (`app.py`): Main web server with REST API endpoints
- **ChromaDB Integration**: Persistent vector database stored in `./chroma_db/` directory
- **Sentence Transformers**: Uses `all-MiniLM-L6-v2` model for text embeddings
- **Web Interface**: Single-page application with Tailwind CSS and vanilla JavaScript

### Key Features
- **Semantic Email Search**: Natural language queries against email content using vector similarity
- **Similarity Threshold Filtering**: Count and retrieve emails above configurable similarity scores (0.0-1.0)
- **Email Management**: Add, search, delete emails with automatic UUID generation
- **Database Metrics**: Real-time statistics including email count, date ranges, content analysis

### API Endpoints
- `POST /add_email` - Add email with content and date
- `POST /search_emails` - Semantic search with configurable limit
- `POST /count_similar_emails` - Count emails above similarity threshold
- `POST /get_emails_above_threshold` - Retrieve emails above threshold
- `GET /get_all_emails` - Retrieve all stored emails
- `DELETE /delete_email/{email_id}` - Delete specific email
- `GET /get_metrics` - Database statistics and metrics
- `GET /health` - Application health check

### Vector Database Details
- **Storage**: ChromaDB persistent client in `./chroma_db/`
- **Collection**: Single "emails" collection
- **Embedding Model**: `all-MiniLM-L6-v2` from Sentence Transformers
- **Similarity Calculation**: Uses inverse distance formula: `similarity = 1 / (1 + distance)`
- **Distance Metric**: L2 (Euclidean) distance for vector comparisons

### Email Document Format
Each email is stored as:
```
Date: YYYY-MM-DDTHH:MM

[email content]
```

With metadata containing:
- `date`: ISO format timestamp
- `id`: UUID string

### Frontend Architecture
- **Templates**: Jinja2 templates in `templates/` directory
- **Static Assets**: CSS and JavaScript in `static/` directory
- **Styling**: Tailwind CSS with custom gradients and animations
- **JavaScript**: Vanilla JS with utility functions for notifications and form handling

### Development Notes
- Application binds to `127.0.0.1` by default (localhost only)
- Port configurable via `PORT` environment variable
- ChromaDB data persists between application restarts
- Sample data includes 8 diverse email scenarios for testing
- Vector embeddings are generated on-demand during email addition