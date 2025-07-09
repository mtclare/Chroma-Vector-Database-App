# Email Vector Database

A free, local email retrieval application using vector database technology for semantic search capabilities.

## Quick Deploy on Render

### One-Click Deployment
1. Click the "Deploy to Render" button below
2. Connect your GitHub account
3. Your app will be deployed automatically

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

### Manual Deployment
1. Fork this repository
2. Go to [render.com](https://render.com) and sign up
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Use these settings:
   - **Name**: `email-vector-database`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements-basic.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
6. Click "Create Web Service"

Your app will be available at: `https://your-app-name.onrender.com`

## Features

- **Local Vector Database**: Uses ChromaDB for local storage - no cloud dependencies
- **Semantic Search**: Find emails using natural language queries
- **Modern UI**: Beautiful, responsive web interface
- **Email Management**: Add, search, and delete emails
- **Similarity Scoring**: See how well search results match your query
- **Free & Open Source**: No costs, no subscriptions
- **Database Metrics**: Real-time statistics dashboard

## Technology Stack

- **Backend**: FastAPI (Python)
- **Vector Database**: ChromaDB (local)
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Frontend**: HTML, JavaScript, Tailwind CSS
- **Icons**: Font Awesome

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements-basic.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your web browser and go to:
   - `http://localhost:8000` (recommended)
   - `http://127.0.0.1:8000` (alternative)

## Usage

### Adding Emails

1. Fill out the "Add New Email" form with:
   - **Date**: Date and time of the email
   - **Content**: The email body text

2. Click "Add Email" to store it in the vector database

### Searching Emails

1. Enter your search query in the "Search Query" field
2. Select the number of results you want to see
3. Click "Search" to find semantically similar emails
4. Results will show with similarity scores (percentage match)

### Viewing All Emails

- Click "Show All" to see all emails in the database

### Deleting Emails

- Click the "Delete" button on any email card to remove it from the database

## How It Works

### Vector Database
- Uses ChromaDB, a local vector database that stores data on your computer
- No internet connection required after initial setup
- Data persists between application restarts

### Semantic Search
- Converts email text and search queries into numerical vectors (embeddings)
- Uses the `all-MiniLM-L6-v2` model for high-quality semantic understanding
- Finds emails based on meaning, not just exact keyword matches

### Example Searches
- "meeting tomorrow" → finds emails about upcoming meetings
- "project deadline" → finds emails discussing deadlines
- "budget approval" → finds emails about financial approvals

## File Structure

```
email-vector-database/
├── app.py                 # Main FastAPI application
├── requirements-basic.txt  # Python dependencies
├── render.yaml            # Render deployment config
├── README.md              # This file
├── templates/
│   └── index.html        # Web interface template
└── chroma_db/            # Vector database storage (created automatically)
```

## API Endpoints

- `GET /` - Main web interface
- `POST /add_email` - Add a new email
- `POST /search_emails` - Search emails semantically
- `GET /get_all_emails` - Retrieve all emails
- `DELETE /delete_email/{id}` - Delete an email
- `GET /get_metrics` - Get database statistics
- `GET /health` - Health check endpoint

## Customization

### Changing the Embedding Model
To use a different embedding model, modify the model name in `app.py`:
```python
embedding_model = SentenceTransformer('your-model-name')
```

### Database Location
The vector database is stored in the `./chroma_db` folder. You can change this by modifying:
```python
chroma_client = chromadb.PersistentClient(path="./your-path")
```

## Troubleshooting

### Common Issues

1. **Dependency compatibility errors**: If you see errors about NumPy or huggingface_hub, run:
   ```bash
   python fix_dependencies.py
   ```
   Or manually install: `pip install numpy==1.24.3 huggingface-hub==0.16.4`

2. **Port already in use**: Change the port in `app.py`:
   ```python
   uvicorn.run(app, host="0.0.0.0", port=8001)  # or any other port
   ```

3. **Missing dependencies**: Make sure all requirements are installed:
   ```bash
   pip install -r requirements-basic.txt
   ```

4. **Database errors**: Delete the `chroma_db` folder to reset the database

### Performance Tips

- The first search may be slower as the embedding model loads
- Large email collections may take longer to search
- Consider using a more powerful embedding model for better accuracy

## Security Notes

- This application runs locally on your machine
- No data is sent to external servers
- All email data is stored locally in the `chroma_db` folder
- Consider backing up the `chroma_db` folder for data preservation

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.

## License

This project is open source and available under the MIT License. 