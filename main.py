def create_attendancetable():
    c.execute('CREATE TABLE IF NOT EXISTS attendancetable (studentID TEXT)')
    connection.commit()
