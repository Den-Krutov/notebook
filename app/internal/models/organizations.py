from pydantic import BaseModel


class Organization(BaseModel):
    '''
    Класс для хранения организаций.

    В поле phone хранится строка с валидным телефонным номером.
    В поле address хранится строка с адресом в произвольном стиле.
    '''
    phone: str
    address: str
