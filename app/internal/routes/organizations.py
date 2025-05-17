from fastapi import APIRouter
from pydantic import ValidationError

from app.internal.schemas.organizations import Organization

router = APIRouter(
    prefix='/api/v1/organizations'
)


@router.get('/check_data')
def check_organization(phone: str) -> Organization:
    '''
    Функция поиска организации по номеру.

    Принимает в query параметрах номер телефона.
    Возвращает ответ с найденной организацией.
    '''
    try:
        organization = Organization.get(phone=phone)
    except ValidationError as e:
        return {
            'error': e.errors()[0].msg,
        }
    except KeyError as e:
        return {
            'error': str(e),
        }
    return {
        'phone': organization.phone,
        'address': organization.address,
    }


@router.post('/write_data')
def write_or_overwrite_organization(
    organization: Organization
) -> Organization:
    '''
    Функция записи организации.

    Принимает в body номер телефона и адрес.
    '''
    organization.save()
    return organization
