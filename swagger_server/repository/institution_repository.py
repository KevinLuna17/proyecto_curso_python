sql_select = "select * from institution where status = 'A'"


# session_factory definido en la clase de sqlalchemy es quien construye el pool de conexiones y aqui se hace uso de la conexion
# hacemos uso de with que es un admin de contextos y nos permite ejecucion segura del codigo

class InstitutionRepository:

    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory

    def get_institution(self):
        with self.session_factory() as session:
            rows = session.execute(sql_select)
            return rows

    def get_institution_by_id(self, institution_id):
        with self.session_factory() as session:
            sql_select_by_id = "select * from institution where id = '" + str(institution_id) + "'"
            rows = session.execute(sql_select_by_id)
            return rows