"""
api_assignment.py
CSD-325 Module 9 - APIs
"""

import requests


def test_basic_connection():
    """Test simple HTTP connection to Google."""
    print("-- TESTING BASIC CONNECTION (GOOGLE) --")
    response = requests.get("http://www.google.com")
    print("Status Code:", response.status_code, "\n")


# --------- PART 1: TUTORIAL API - ASTRONAUTS ---------

ASTRONAUTS_URL = "http://api.open-notify.org/astros.json"


def test_astronaut_api():
    """Test connection to astronauts API."""
    print("-- TESTING ASTRONAUTS API CONNECTION --")
    response = requests.get(ASTRONAUTS_URL)
    print("Status Code:", response.status_code, "\n")


def show_astronauts_raw():
    """Show raw JSON text from astronauts API."""
    print("-- RAW ASTRONAUT JSON RESPONSE --")
    response = requests.get(ASTRONAUTS_URL)
    print(response.text, "\n")  # unformatted


def show_astronauts_formatted():
    """Show formatted list of astronauts and their craft."""
    print("-- FORMATTED ASTRONAUT OUTPUT --")
    response = requests.get(ASTRONAUTS_URL)
    data = response.json()

    number = data.get("number", 0)
    people = data.get("people", [])

    print(f"There are currently {number} people in space:\n")
    for person in people:
        print(f"Name:  {person.get('name', 'Unknown')}")
        print(f"Craft: {person.get('craft', 'Unknown craft')}\n")


# --------- PART 2: YOUR OWN API - CAT FACTS ---------

CATFACT_URL = "https://catfact.ninja/fact"


def test_catfact_connection():
    """Test connection to Cat Fact API."""
    print("-- TESTING CAT FACT API CONNECTION --")
    response = requests.get(CATFACT_URL)
    print("Status Code:", response.status_code, "\n")


def show_catfact_raw():
    """Show raw JSON text from Cat Fact API."""
    print("-- RAW CAT FACT JSON RESPONSE --")
    response = requests.get(CATFACT_URL)
    print(response.text, "\n")


def show_catfact_formatted():
    """Show formatted cat fact."""
    print("-- FORMATTED CAT FACT OUTPUT --")
    response = requests.get(CATFACT_URL)
    data = response.json()

    fact = data.get("fact", "No fact found.")
    length = data.get("length", "Unknown")
    print("Cat Fact:", fact)
    print("Length:", length, "characters\n")


def main():
    # 0. basic test
    test_basic_connection()

    # 1. astronauts tutorial API
    test_astronaut_api()
    show_astronauts_raw()
    show_astronauts_formatted()

    # 2. second API - cat facts
    test_catfact_connection()
    show_catfact_raw()
    show_catfact_formatted()


if __name__ == "__main__":
    main()
