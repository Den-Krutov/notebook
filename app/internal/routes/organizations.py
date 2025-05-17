from fastapi import APIRouter

from app.internal.models.organizations import Organization

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
    organization = Organization(phone=phone,
                                address='г. Москва, ул. Примерная, д. 1')
    return organization


@router.post('/write_data')
def write_or_overwrite_organization(
    organization: Organization
) -> Organization:
    '''
    Функция записи организации.

    Принимает в body номер телефона организации и её адрес.
    Возвращает ответ с данными созданной или перезаписанной организацией.
    '''
    return organization
