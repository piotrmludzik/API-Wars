# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                 data format functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import locale
import data_constants as dc
import utilities as util


class _Name:
    NO_WATER = 'no water'
    UNKNOWN = 'unknown'


class _ColumnNameNew:
    MGLT = 'Megalights'


NAME = _Name()
COLUMN_NAME_NEW = _ColumnNameNew()

# -------------------------------------------------- main functions ---------------------------------------------------

def data_format(subject: str, data: list) -> list:
    """ Returns formatted the subject data. """
    locale.setlocale(locale.LC_ALL, '')

    for item in data:
        if subject == dc.SUBJECT.PLANETS:
            item[dc.KEY.PLANETS.DIAMETER] = _format_diameter(item[dc.KEY.PLANETS.DIAMETER])
            item[dc.KEY.PLANETS.WATER] = _format_water(item[dc.KEY.PLANETS.WATER])
            item[dc.KEY.PLANETS.POPULATION] = _format_population(item[dc.KEY.PLANETS.POPULATION])
            item[dc.KEY.PLANETS.ROTATION] = _format_rotation(item[dc.KEY.PLANETS.ROTATION])
            item[dc.KEY.PLANETS.ORBITAL] = _format_orbital(item[dc.KEY.PLANETS.ORBITAL])
        elif subject == dc.SUBJECT.STARSHIPS:
            item[dc.KEY.STARSHIPS.CREW] = _format_crew_and_passengers(item[dc.KEY.STARSHIPS.CREW])
            item[dc.KEY.STARSHIPS.PASSENGERS] = _format_crew_and_passengers(item[dc.KEY.STARSHIPS.PASSENGERS])
            item[dc.KEY.STARSHIPS.CARGO] = _format_mass(item[dc.KEY.STARSHIPS.CARGO])
            item[dc.KEY.STARSHIPS.LENGTH] = _format_length(item[dc.KEY.STARSHIPS.LENGTH])
            item[dc.KEY.STARSHIPS.ATSP] = _format_atsp(item[dc.KEY.STARSHIPS.ATSP])
            item[dc.KEY.STARSHIPS.MGLT] = _format_mglt(item[dc.KEY.STARSHIPS.MGLT])
        elif subject == dc.SUBJECT.VEHICLES:
            item[dc.KEY.VEHICLES.CREW] = _format_crew_and_passengers(item[dc.KEY.VEHICLES.CREW])
            item[dc.KEY.VEHICLES.PASSENGERS] = _format_crew_and_passengers(item[dc.KEY.VEHICLES.PASSENGERS])
            item[dc.KEY.VEHICLES.CARGO] = _format_mass(item[dc.KEY.VEHICLES.CARGO])
            item[dc.KEY.VEHICLES.LENGTH] = _format_length(item[dc.KEY.VEHICLES.LENGTH])
            item[dc.KEY.VEHICLES.ATSP] = _format_atsp(item[dc.KEY.VEHICLES.ATSP])
        elif subject == dc.SUBJECT.PEOPLE:
            item[dc.KEY.PEOPLE.HEIGHT] = _format_length(item[dc.KEY.PEOPLE.HEIGHT])
            item[dc.KEY.PEOPLE.MASS] = _format_mass(item[dc.KEY.PEOPLE.MASS])
    return data


def column_names_format(column_names: list) -> list:
    """ Return a formatted column name if necessary. """
    MGlT = dc.KEY.STARSHIPS.MGLT
    if MGlT in column_names:
        column_names = util.change_list_value(column_names, MGlT, COLUMN_NAME_NEW.MGLT)

    return column_names


# ------------------------------------------------- format functions --------------------------------------------------

def _format_atsp(data: str) -> str:
    data = _prepare_integer(data)
    return '{:n} km/h'.format(float(data)) if _valid_number(data) else data


def _format_crew_and_passengers(data: str) -> str:
    data = _prepare_integer(data)

    if data == '0': return 'not carry'
    if data == '1': return f'{data} person'
    if _data_range(data): return f'{data} people'

    return '{:n} people'.format(int(data)) if _valid_number(data) else data


def _format_diameter(data: str) -> str:
    data = _prepare_integer(data)
    if data == '0':
        return NAME.UNKNOWN

    return '{:n} km'.format(int(data)) if _valid_number(data) else data


def _format_length(data: str) -> str:
    data = _prepare_float(data)
    return '{:n} m'.format(float(data)) if _valid_number(data) else data


def _format_mass(data: str) -> str:
    data = _prepare_float(data)
    return '{:n} kg'.format(float(data)) if _valid_number(data) else data


def _format_mglt(data: str) -> str:
    data = _prepare_integer(data)
    return '{:n} mglt/h'.format(float(data)) if _valid_number(data) else data


def _format_orbital(data: str) -> str:
    data = _prepare_integer(data)
    if data == '0':
        return NAME.UNKNOWN

    return '{:n} days'.format(int(data)) if _valid_number(data) else data


def _format_population(data: str) -> str:
    data = _prepare_integer(data)
    return '{:n} people'.format(int(data)) if _valid_number(data) else data


def _format_rotation(data: str) -> str:
    data = _prepare_integer(data)
    if data == '0':
        return NAME.UNKNOWN

    return '{:n} hours'.format(int(data)) if _valid_number(data) else data


def _format_water(data: str) -> str:
    if data == '0':
        return NAME.NO_WATER

    return '{:n}%'.format(float(data)) if _valid_number(data) else data


# -------------------------------------------------- other functions --------------------------------------------------

def _data_range(data: str) -> bool:
    """ Checks if a string data are a numbers in range. """
    return True if data.find('-') != -1 else False


def _prepare_integer(data: str) -> str:
    """ Removes unnecessary characters from the string representing an integer """
    return data.replace(",", "")  # for numbers with the thousand separator


def _prepare_float(data: str) -> str:
    """ Removes unnecessary characters from the string representing an integer """
    return data.replace(",", ".")  # for numbers with coma ","


def _valid_number(data: str) -> bool:
    """ Checks if a data is valid integer or float number. """
    try:
        if data.isdigit():
            return isinstance(int(data), int)
        else:
            return isinstance(float(data), float)
    except ValueError:
        return False
