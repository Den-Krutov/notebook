from pydantic import BaseModel, field_validator, Field
import phonenumbers

from app.pkg.redis_tools.tools import RedisTools

REGION = 'RU'


class Organization(BaseModel):
    '''
    Класс для хранения организаций.

    В поле phone хранится строка с валидным телефонным номером.
    В поле address хранится строка с адресом в произвольном стиле.
    '''
    phone: str
    address: str = Field(default='', max_length=50)

    @field_validator('phone')
    def check_phone(cls, value):
        phone = phonenumbers.parse(value, REGION)
        if not phonenumbers.is_valid_number_for_region(phone, REGION):
            raise ValueError('Несуществующий номер телефона')
        return value

    @classmethod
    def get(cls, phone) -> 'Organization':
        organization = Organization(phone=phone)

        address = RedisTools.get_pair(organization.phone)
        if not address:
            raise KeyError('Нет организации с таким номером')
        organization.address = address
        return organization

    def save(self):
        RedisTools.write_pair(self.phone, self.address)
