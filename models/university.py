from db import get_db

# Fetch all universities
def get_all_universities():
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM university"
        print("Executing query:", query)  # Debugging
        cursor.execute(query)
        universities = cursor.fetchall()
        print("Query Result:", universities)  # Debugging
        return universities
    except Exception as e:
        print(f"Error fetching universities: {e}")
        return None

# Fetch a specific university by ID
def get_university_by_id(university_id):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM university WHERE university_id = %s"
        print("Executing query:", query)  # Debugging
        cursor.execute(query, (university_id,))
        university = cursor.fetchone()
        print("Query Result:", university)  # Debugging
        return university
    except Exception as e:
        print(f"Error fetching university by ID: {e}")
        return None


