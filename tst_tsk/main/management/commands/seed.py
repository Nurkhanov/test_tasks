from django.core.management.base import BaseCommand
import random, datetime
from main.models import Employee,Position


MODE_REFRESH='refresh'
MODE_CLEAR='clear'
MODE_START='start'

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
    Position.objects.all().delete()
    Employee.objects.all().delete()

def create_boss():
    boss = Employee(first_name = 'Boss',
                    middle_name = 'Boss',
                    last_name = 'Boss',
                    salary = 10000,
                    position = Position.objects.get(level=5)
                    )
    boss.save()

def create_positions(max_position_level:int):
    for i in range(1,max_position_level+1):
        position = Position( pos_name = 'Level '+str(i),
                            level = i)
        position.save()

def create_employee(given_pos_level:int):
    """Creates an address object combining different elements from the list"""
    # logger.info("Creating address")
    first_names = ['sergei','misha','grisha','dasha','natasha']
    middle_names = ['olegovna','sergeevna','aleksandrovich','pavelovich',]
    last_names = ['mishelov','borgun','nurhonov','komarov','sergeev']
    salaries = [x for x in range(50000,120000,5000)]
    bosses = [x for x in Employee.objects.filter(position__level=given_pos_level+1)]

    employee = Employee(
        first_name=random.choice(first_names),
        middle_name=random.choice(middle_names),
        last_name=random.choice(last_names),
        position = Position.objects.get(level=given_pos_level),
        salary=random.choice(salaries),
        boss = random.choice(bosses)
    )
    employee.save()
    # logger.info("{} address created.".format(address))

def run_seed(self, mode):
    """ Seed database based on mode
    
    :param mode: start/refresh / clear 
    :return:
    """
    if mode == MODE_CLEAR:
        clear_data()
        return
    elif mode == MODE_START:
        create_positions(5)
        create_boss()
        return

    

    starttime = datetime.datetime.now()
    for i in range(15):
        for y in range(4,0,-1):
            create_employee(y)
    endtime = datetime.datetime.now()
    print(f'The operation time - {endtime-starttime}')