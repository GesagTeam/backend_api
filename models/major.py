from db import get_db

# Fetch all majors along with their associated university name
def get_all_majors():
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        # SQL Query to join major and university
        query = """
        SELECT major.*, university.name AS university_name 
        FROM major
        JOIN university ON major.university_id = university.university_id
        """
        print("Executing query:", query)  # Debugging
        cursor.execute(query)
        majors = cursor.fetchall()
        print("Query Result:", majors)  # Debugging
        return majors
    except Exception as e:
        print(f"Error fetching majors: {e}")
        return None
