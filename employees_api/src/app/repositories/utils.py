from datetime import date
from typing import Type, TypeVar

from sqlalchemy import and_, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import EmployeeTrip as EmployeeTripModel
from app.schemas.employee_trip import EmployeeTrip as EmployeeTripSchema

M = TypeVar("M", bound=EmployeeTripModel)

S = TypeVar("S", bound=EmployeeTripSchema)

def is_date_between(date_to_check: date, model: Type[M]):
    return and_(
        model.start_date <= date_to_check,
        model.end_date >= date_to_check
    )

def is_range_between(range_start: date, range_end: date, model: Type[M]):
    return and_(
        model.start_date >= range_start,
        model.end_date <= range_end
    )

async def is_dates_intersects(session: AsyncSession,
                              model: Type[M],
                              trip_to_check: Type[S]
                             ) -> bool:

        check_stmt = (select(model)
                      .where(
                            and_(
                                or_
                                    (
                                    is_date_between(trip_to_check.start_date, model),
                                    # входит ли начальная точка в существующие промежутки
                                    is_date_between(trip_to_check.end_date, model),
                                    # входит ли конечная точка в существующие промежутки
                                    is_range_between(trip_to_check.start_date, 
                                                     trip_to_check.end_date,
                                                     model)
                                    # входит ли существующий промежуток в проверяемый
                                    ),
                                model.employee_id==trip_to_check.employee_id
                                )
                            )
                     )
        
        result = await session.execute(check_stmt)

        result_scalars = result.scalars().all()

        if result_scalars:
            return True
        else:
            return False