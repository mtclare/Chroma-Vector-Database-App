# Email Vector Database

A modern web application for storing and searching emails using semantic similarity with vector embeddings. Built with FastAPI, ChromaDB, and Sentence Transformers.

## 🚀 Features

- **Semantic Email Search**: Find relevant emails using natural language queries
- **Vector Database**: Powered by ChromaDB for efficient similarity search
- **Modern Web Interface**: Clean, responsive UI built with HTML, CSS, and JavaScript
- **Email Management**: Add, search, and delete emails with metadata
- **Real-time Metrics**: View database statistics and email analytics
- **Sample Data**: Pre-built sample emails for testing and demonstration

## 📁 Project Structure

```
Email Vector Database/
├── app.py                 # Main FastAPI application
├── sample_data.py         # Sample data generator
├── requirements.txt       # Python dependencies
├── static/               # Static assets
│   ├── app.js           # Frontend JavaScript
│   └── style.css        # CSS styles
├── templates/            # HTML templates
│   └── index.html       # Main web interface
├── chroma_db/           # ChromaDB database files
└── .venv/               # Virtual environment
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Email Vector Database"
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Starting the Application

1. **Run the FastAPI server**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to `http://localhost:8000`
   - The application will be available on port 8000 by default

### Adding Sample Data

To populate the database with sample emails for testing:

```bash
python sample_data.py
```

This will add 8 sample emails covering various scenarios like project announcements, budget requests, and security updates.

## 🔧 API Endpoints

The application provides the following REST API endpoints:

- `GET /` - Main web interface
- `POST /add_email` - Add a new email to the database
- `POST /search_emails` - Search emails using semantic similarity
- `GET /get_all_emails` - Retrieve all emails from the database
- `DELETE /delete_email/{email_id}` - Delete a specific email
- `GET /get_metrics` - Get database statistics and metrics
- `GET /health` - Health check endpoint

## 🎯 Key Technologies

- **FastAPI**: Modern, fast web framework for building APIs
- **ChromaDB**: Open-source embedding database for AI applications
- **Sentence Transformers**: State-of-the-art sentence embeddings
- **Uvicorn**: ASGI server for running FastAPI applications
- **Jinja2**: Template engine for dynamic HTML generation

## 📊 Features in Detail

### Semantic Search
- Uses the `all-MiniLM-L6-v2` model for generating embeddings
- Supports natural language queries
- Returns similarity scores for search results
- Configurable result limits

### Email Management
- Add emails with custom dates and content
- Automatic UUID generation for unique identification
- Metadata storage for dates and IDs
- Bulk operations support

### Database Metrics
- Total email count
- Date range analysis
- Average content length
- Database size information
- Embedding model details

## 🔒 Security & Performance

- **Local Database**: All data stored locally in ChromaDB
- **No External Dependencies**: Self-contained application
- **Efficient Embeddings**: Optimized for speed and accuracy
- **Error Handling**: Comprehensive exception handling
- **Health Monitoring**: Built-in health check endpoint

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**
   - Change the port in `app.py` or kill the process using the port

2. **Database connection errors**
   - Ensure the `chroma_db` directory has write permissions
   - Restart the application to reinitialize the database

3. **Sample data not loading**
   - Make sure the application is running on `http://localhost:8000`
   - Check that all dependencies are installed correctly

### Development

For development and debugging:

```bash
# Run with auto-reload
uvicorn app:app --reload --host 0.0.0.0 --port 8000

# Check application health
curl http://localhost:8000/health
```

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Built with ❤️ using FastAPI and ChromaDB** 