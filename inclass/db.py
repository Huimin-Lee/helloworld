import os
import sqlite3


class DatabaseDriver(object):
    """
    Task APP的資料方法
    處理資料庫的讀＆寫
    """

    def __init__(self):
        self.conn = sqlite3.connect("todo.db", check_same_thread=False)
        self.create_task_table()

    def create_task_table(self):
        try:
            self.conn.execute(
                """
                CREATE TABLE task (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    DESCRIPTION TEXT NOT NULL,
                    DONE BOOLEAN NOT NULL
                );
                """
            )
        except Exception as e:
            print(e)

    def get_all_tasks(self):
        cursor = self.conn.execute(
            """
            SELECT * FROM task;
            """
        )
        tasks = []
        for row in cursor:
            tasks.append({"id": row[0],
                        "description": row[1],
                        "done": row[2]})
        return tasks

    def insert_task_table(self, description, done):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO task (DESCRIPTION, DONE) VALUES (?, ?);",
            (description, done)
        )
        self.conn.commit()
        return cursor.lastrowid
    # 顯示操作中的最後一筆資料

    def get_task_by_id(self, id):
        cursor = self.conn.execute("SELECT * FROM task WHERE ID = ?", (id,))
        for row in cursor:
            return {
                "id": row[0],
                "description": row[1],
                "done": row[2]
            }

        return None

    def update_task_by_id(self, id, description, done):
        self.conn.execute(
            """
            UPDATE task
            SET description = ?, done = ?
            WHERE id = ?;
            """,
            (description, done, id),
        )
        self.conn.commit()

    def delete_task_by_id(self, id):
        self.conn.execute(
            """
            DELETE FROM task
            WHERE id = ?;
            """,
            (id,),
        )
        self.conn.commit()

    def success_response(data, code=200):
        return json.dumps({"success": True, "data": data}), code

    def failure_response(message, code=404):
        return json.dumps({"success": False, "error": message}), code
