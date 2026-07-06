import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="earthquake_db"
)

cursor = conn.cursor()

while True:
    try:
        # API call
        # DataFrame
        # Filter

        for _, row in df_new.iterrows():
            cursor.execute(
                """
                INSERT INTO earthquake(time, place, magnitude, title)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    row["time"],
                    row["place"],
                    row["magnitude"],
                    row["title"]
                )
            )

        conn.commit()
        print("Data Inserted Successfully")

    except Exception as e:
        print(e)

    print("Waiting for 5 minutes...")
    time.sleep(300)