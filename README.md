

LogicAI-DB is an intelligent agentic database project that integrates deep learning and agentic AI techniques to provide advanced data management and automation capabilities. The project is structured to support modular development, containerization, and easy deployment.

## Features
- Modular architecture with clear separation of concerns
- Agent-based automation for planning and execution
- MySQL database integration
- RESTful API for database operations
- Dockerized backend for easy deployment

## Project Structure
```
docker-compose.yml
frontend.py
README.md
requirements.txt
app/
    api.py
    Dockerfile
    main.py
    agent/
        dual_agent.py
        executor_agent.py
        planner_agent.py
        prompts.py
    config/
        settings.py
    db/
        connection.py
        schema.py
    tools/
        mysql_tool.py
```

## Getting Started

### Prerequisites
- Python 3.8+
- Docker
- MySQL (or use Docker Compose for local setup)

### Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd LogicAI-DB
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure database settings in `app/config/settings.py`.

### Running with Docker
1. Build and start the services:
   ```bash
   docker-compose up --build
   ```
2. The API will be available at `http://localhost:<port>`.

### Running Locally
1. Start the backend:
   ```bash
   python app/main.py
   ```
2. (Optional) Run the frontend:
   ```bash
   python frontend.py
   ```

## Usage
- Use the REST API endpoints defined in `app/api.py` to interact with the database.
- Agents in `app/agent/` automate planning and execution tasks.
- Database schema and connection logic are in `app/db/`.
- MySQL tools are in `app/tools/`.

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements.

## License
This project is licensed under the MIT License.

## Contact
For questions or support, please contact the maintainer.