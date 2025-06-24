# Late Show API

This project is the backend API for the Late Show application.

## Project Structure

- `server/`: Contains the main application code
  - `app.py`: Main application entry point
  - `config.py`: Configuration settings
  - `seed.py`: Database seeding script
  - `models/`: Data models
  - `controllers/`: Request controllers

- `migrations/`: Database migration files

- `challenge-4-lateshow.postman_collection.json`: Postman collection for API testing

## Setup Instructions

### PostgreSQL

- Install PostgreSQL and ensure it is running.
- Create a database for the application.
- Update the database URL in the `.env` file or `server/config.py` accordingly.

### Flask and Dependencies

- Install pipenv if not installed: `pip install pipenv`
- Install dependencies: `pipenv install --dev`
- Activate the virtual environment: `pipenv shell`

### Environment Variables

- Create a `.env` file in the project root.
- Define necessary environment variables such as:
  ```
  DATABASE_URL=postgresql://user:password@localhost/dbname
  FLASK_APP=server.app
  FLASK_ENV=development
  JWT_SECRET_KEY=your_jwt_secret_key
  ```

## How to Run

1. Run database migrations:
   ```
   pipenv run flask --app server.app db migrate -m "Initial migration"
   pipenv run flask --app server.app db upgrade
   ```

2. Seed the database with initial data:
   ```
   pipenv run python3 -m server.seed
   ```

3. Run the Flask application:
   ```
   pipenv run python3 -m server.app
   ```

The server will start on `http://127.0.0.1:5555`.

## Authentication Flow

- **Register**: `POST /register` with JSON body `{ "username": "yourname", "password": "yourpassword" }`
- **Login**: `POST /login` with JSON body `{ "username": "yourname", "password": "yourpassword" }`
- On successful login, you receive a JWT token in the response:
  ```json
  {
    "access_token": "your.jwt.token.here"
  }
  ```
- Use this token in the `Authorization` header as `Bearer your.jwt.token.here` to access protected endpoints.

## API Routes

### Public Routes

- `POST /register` - Register a new user
- `POST /login` - Login and receive JWT token
- `GET /guests` - Get list of guests
- `GET /episodes` - Get list of episodes
- `GET /episodes/<id>` - Get details of a specific episode

### Protected Routes (Require JWT)

- `POST /appearances` - Create a new appearance
- `DELETE /episodes/<id>` - Delete an episode

### Sample Request and Response

**Register:**
```
POST /register
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpass"
}
```
Response:
```json
{
  "message": "User created successfully"
}
```

**Login:**
```
POST /login
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpass"
}
```
Response:
```json
{
  "access_token": "your.jwt.token.here"
}
```

**Create Appearance:**
```
POST /appearances
Authorization: Bearer your.jwt.token.here
Content-Type: application/json

{
  "rating": 5,
  "guest_id": 1,
  "episode_id": 1
}
```
Response:
```json
{
  "message": "Appearance created successfully"
}
```

## Postman Usage Guide

- Import the `challenge-4-lateshow.postman_collection.json` file into Postman.
- Use the collection to test all API endpoints.
- Set the `Authorization` header with the JWT token for protected routes.

## GitHub Repository

- [Your GitHub Repository Link Here](https://github.com/adrian-amoke/late-show-api)
