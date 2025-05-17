from fastapi import APIRouter, HTTPException

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
    except ValueError as e:
        raise HTTPException(
            status_code=404, detail=e.errors()[0]['msg'].split(', ')[1])
    except KeyError as e:
        raise HTTPException(
            status_code=404, detail=str(e).replace("'", ""))
    return organization


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
