from datetime import date
from typing import Type, TypeVar

from sqlalchemy import and_, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import EmployeeTrip

M = TypeVar("M", bound=EmployeeTrip)

async def is_dates_intersects(session: AsyncSession,
                              model: Type[M],
                              start_date_to_check: date,
                              end_date_to_check: date,
                              employee_id: int
                             ) -> bool:

        check_stmt = (select(model)
                      .where(and_(
                                or_
                                    (and_(
                                        model.start_date <= start_date_to_check,
                                        model.end_date >= start_date_to_check
                                        ),
                                    # входит ли начальная точка в существующие промежутки
                                    and_(
                                        model.start_date <= end_date_to_check,
                                        model.end_date >= end_date_to_check
                                        ),
                                    # входит ли конечная точка в существующие промежутки
                                    and_(
                                        model.start_date >= start_date_to_check,
                                        model.end_date <= end_date_to_check
                                        )
                                    # входит ли существующий промежуток в проверяемый
                                    ),
                                model.employee_id==employee_id
                                )
                            )
                     )
        
        result = await session.execute(check_stmt)

        result_scalars = result.scalars().all()

        if result_scalars:
            return True
        else:
            return False