import pyodbc

class mdb_with_ops:
    def __init__(self, mdb_name):
        self.mdb_name = mdb_name
        self.connection = None
        self.cursor = None
        self.columns = []
        self.col_names = None
    def connect(self):
        self.disconnect()
        self.connection = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ=' + self.mdb_name)
        self.cursor = self.connection.cursor()
    def delete_table(self, table_name):                 # does not work!!!
        sql = "(DROP TABLE " + table_name + ")"
        try:
            self.RunSQL(sql, True)
        except:
            pass

    def create_table(self, table_name, default_field_name, data_type):
        sql = "CREATE TABLE " + table_name + "(" + default_field_name + " " + data_type + ")"
        try:
            self.RunSQL(sql, True)
        except:
            pass

    def RunSQL(self, SQLText="", commit=True, disconnect=False):
        """
        runs SQL query in the mdb file, defined by SQLText
        """

        if self.connection == None:
            self.connect()
        try:
            result = self.cursor.execute(SQLText)
        except:
            raise
        # must use commit false for select statements returning results
        if commit:
            self.connection.commit()
        if disconnect:
            disconnect()
            return None
        else:
            return result

    def insert_row(self, table_name, cont_dict, commit_): 
        self.RunInsertSQL(table_name, cont_dict, commit_)
        return
    def clear_table(self, table_name):
        self.RunSQL("delete from " + table_name)

    def RunInsertSQL(self, table_name, cont_dict, commit=False):

        sql='insert into ' + table_name+' ('+','.join(cont_dict)+')'+' values '+'('+','.join(["'"+str(v)+"'" if v !=None else "Null" for v in cont_dict.itervalues()])+')'
        self.RunSQL(sql,commit)

    def disconnect(self):
        if self.cursor != None:
            self.cursor.close()
            del self.cursor
        if self.connection != None:
            self.connection.close()
            del self.connection
        self.connection = None
        self.cursor = None

    def get_values(self, table_name, fields = "*", commit = True):
        if fields == "*":
            sql = ('select ' + fields + ' from ' + table_name)
        else:
            sql = ('select ' + ','.join(fields) + ' from ' + table_name)

        self.cursor.execute(sql)
        rows= self.cursor.fetchall()

        self.columns = []
        if not fields == "*":
            self.columns.append(fields)

        for row in rows:
            # Now, access the fields as properties of "row"
            self.columns.append(list(row))

        self.col_names = [col[0] for col in self.cursor.description]
        return  #Returns a dictionary with an ordered list of row items in that column

    def add_field(self, table_name, field_name, data_type):
        sql = ("ALTER TABLE " + table_name + " ADD COLUMN " + field_name + " " + data_type + ";")

        try:
            self.cursor.execute(sql)
        except:
            pass

        self.connection.commit()


