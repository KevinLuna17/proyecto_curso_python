from swagger_server.models.response_institution import ResponseInstitution
from swagger_server.models.response_institution_data import ResponseInstitutionData


# Aqui se crea una clase que en el constructor recibe un parametro para este ejemplo "institution_repository"
# para que cuando yo instancie mis casos de uso yo pueda usar todas las consultas a traves de dicho parametro

class InstitutionUseCase:

    def __init__(self, institution_repository):
        self.institution_repository = institution_repository

    def get_institution(self):
        """
            Lista de instutition
        :return:
        """

        data_response = []
        institutions = self.institution_repository.get_institution()

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=i.id,
                    name=i.name,
                    description=i.description,
                    address=i.address,
                )
            )

        response = ResponseInstitution(
            code=0,
            message="proceso exitoso",
            data=data_response
        )

        return response

    def get_institution_by_id(self, institution_id):
        """
            Consulta una instutition por id
        :return:
        """

        data_response = []
        institutions = self.institution_repository.get_institution_by_id(institution_id)

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=i.id,
                    name=i.name,
                    description=i.description,
                    address=i.address,
                )
            )

        response = ResponseInstitution(
            code=0,
            message="proceso exitoso",
            data=data_response
        )

        return response
