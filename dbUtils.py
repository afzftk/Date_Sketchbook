import psycopg2

def get_user(user_id, user_pw):
    conn = psycopg2.connect(host="", dbname="", user="", password="", port=5432)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    query =
    '''
    select *
    from user_info
    where user_id = %s
      and user_pw = %s
    '''
    cur.execute(query, (user_id, user_pw))

    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows