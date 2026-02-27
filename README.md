## **URL Shortener Backend

A scalable backend service that converts long URLs into short, shareable links and redirects users to the original destination efficiently.

## **Features**
•	Short URL Generation: Converts long URLs into unique short strings.
•	Collision-Free IDs: Ensures generated short URLs are unique using random string validation.
•	Redirection: Redirects short URLs to their original URLs.
•	View All URLs: Fetch all stored URLs from the database.
•	Validation: Validates incoming URLs before storing.
•	Error Handling: Graceful handling of invalid URLs and missing records.
•	Recursive ID Generation: Automatically regenerates short URLs if a collision occurs.

## **Tech Stack**
•	Backend: Django, Django REST Framework
•	Database: SQLite (can be upgraded to PostgreSQL/MySQL)
•	Utilities: Django Crypto (get_random_string)
•	API Testing: Postman

## **Installation**
1.	Clone the repository:
2.	git clone https://github.com/your-username/url_shortener_backend.git
3.	Create virtual environment:
4.	python -m venv venv
5.	source venv/bin/activate  # Windows: venv\Scripts\activate
6.	Install dependencies:
7.	pip install -r requirements.txt
8.	Run migrations:
9.	python manage.py makemigrations
10.	python manage.py migrate
11.	Run the server:
12.	python manage.py runserver

## **API Endpoints**
# URL Routes
Method	Endpoint	Description
POST	/main/create/	Create a new short URL
GET	/main/getdata/	Fetch all stored URLs
GET	/main/call/<short_url>	Redirect to original URL
Example Request (Create Short URL)
{
  "original_url": "https://www.google.com/search?q=django"
}
Example Response
"http://127.0.0.1:8000/main/call/Xa9D2PqL"

## **How I Built It**
•	Designed modular structure using models, serializers, views, and utility functions.
•	Implemented a recursive random string generator to avoid short URL collisions.
•	Used Django REST Framework for clean API design.
•	Added validation for user input and handled database exceptions.
•	Implemented HTTP redirect logic for seamless navigation.
•	Followed REST principles for endpoint design.

## **Impact**
•	Provides a fast and reliable URL shortening service.
•	Demonstrates backend concepts like:
o	API design
o	Database modeling
o	Collision handling
o	Redirection logic
•	Can be extended with:
o	Click analytics
o	Expiration dates
o	User authentication
o	Rate limiting
o	Custom aliases

