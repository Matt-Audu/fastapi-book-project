from tests import client
import random
import sys

def test_book_id():
    response = client.get("/books/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"
    assert data["publication_year"] == 1937
    assert data["genre"] == "Sci-Fi"

    response = client.get("/books/2")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 2
    assert data["title"] == "The Lord of the Rings"
    assert data["author"] == "J.R.R. Tolkien"
    assert data["publication_year"] == 1954
    assert data["genre"] == "Fantasy"

    response = client.get("/books/3")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 3
    assert data["title"] == "The Return of the King"
    assert data["author"] == "J.R.R. Tolkien"
    assert data["publication_year"] == 1955
    assert data["genre"] == "Fantasy"


def test_non_existent_book():
    # Existing book IDs in the database
    existing_ids = {1, 2, 3}

    # Generate a random ID that is not in the database
    while True:
        non_existent_id = random.randint(1, sys.maxsize)  # Random ID from 1 to a very large number
        if non_existent_id not in existing_ids:
            break

    # Test with the non-existent ID
    response = client.get(f"/books/{non_existent_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": f"Book with ID {non_existent_id} does not exist"}