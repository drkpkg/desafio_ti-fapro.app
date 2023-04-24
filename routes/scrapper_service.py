from fastapi import APIRouter, params, HTTPException

from lib.scrapper import WebScrapper

router = APIRouter()


@router.get("/")
async def scrapper_service(day: int | None = None, month: int | None = None, year: int | None = None,
                           full: bool | None = False):
    """
    Scrapper for UF values

    Will return the UF value for the given day, month and year (or today's date if none is given). Has the option to
    return all values for the given month and year.
    """
    scrapper = WebScrapper()
    scrapper.set_day(day)
    scrapper.set_month(month)
    scrapper.set_year(year)
    try:
        return scrapper.scrape(send_all=full if full else False)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
