months = (
    ('Enero', 'enero'),
    ('Febrero', 'febrero'),
    ('Marzo', 'marzo'),
    ('Abril', 'abril'),
    ('Mayo', 'mayo'),
    ('Junio', 'junio'),
    ('Julio', 'julio'),
    ('Agosto', 'agosto'),
    ('Septiembre', 'septiembre'),
    ('Octubre', 'octubre'),
    ('Noviembre', 'noviembre'),
    ('Diciembre', 'diciembre'),
)


def month_name(month):
    """
    Get month name from month number
    :param month:
    :return:
    """
    return months[month - 1][1]
