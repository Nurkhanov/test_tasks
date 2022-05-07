from django.core.management.base import BaseCommand
import random, datetime
from main.models import Employee,Position


MODE_REFRESH='refresh'
MODE_CLEAR='clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')

def clear_data():
    """Deletes all the table data"""
    # logger.info("Delete Address instances")
    Employee.objects.all().delete()
def create_boss():
    boss = Employee(first_name = 'Boss',
                    middle_name = 'Boss',
                    last_name = 'Boss',
                    salary = 10000,
                    position = Position.objects.get(level=5)
                    )
    boss.save()

first_names = ['sergei','misha','grisha','dasha','natasha']
middle_names = ['olegovna','sergeevna','aleksandrovich','pavelovich',]
last_names = ['mishelov','borgun','nurhonov','komarov','sergeev']
salaries = [x for x in range(50000,120000,5000)]


def create_employee(given_pos_level:int):
    """Creates an address object combining different elements from the list"""
    # logger.info("Creating address")
    

    employee = Employee(
        first_name=random.choice(first_names),
        middle_name=random.choice(middle_names),
        last_name=random.choice(last_names),
        position = Position.objects.get(level=given_pos_level),
        salary=random.choice(salaries),
        boss = random.choice(bosses)
    )

    # logger.info("{} address created.".format(address))
    return employee

def run_seed(self, mode):
    """ Seed database based on mode
    
    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    
    starttime = datetime.datetime.now()
    if mode == MODE_CLEAR:
        return

    create_boss()
    global bosses
    bosses = [x for x in Employee.objects.filter(position__level = 5)]
    # Creating 15 addresses
    for i in range(12500):
        for y in range(4,0,-1):
            create_employee(y)
    endtime = datetime.datetime.now()
    print(f'The operation time - {endtime-starttime}')