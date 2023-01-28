from typing import Dict


class Database:
    id = 1
    makes = [
        {

            'id': 1,

            'make': 'Mercedes Benz',

            'year': 2002,

            'price': 6000,

            'image': 'https://s.aolcdn.com/commerce/autodata/images/20MBGEA1.jpg',

            'description': 'C230 Sports Coupe, a car designed to attract first-time Mercedes buyers with its combination of style, space, and a very complete equipment package',

            'contacts': 'Please contact by email sale@carsale.com or phone 555 555 555'} ]

    @classmethod
    def get_make_by_pk(cls, pk: int) -> Dict[str, int | str]:
        result = list(filter(lambda p: p.get("id") == pk, cls.makes))
        return result[0] if result else None

    @classmethod
    def add(cls, makes):
        cls.makes.append(makes)