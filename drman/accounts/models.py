from django.db import models
from django.contrib.auth.models import User
import csv
# Create your models here.


class Customer(models.Model):

    customer_id = models.CharField("Customer ID",max_length=50, null=True)

    LOAN_STATUS = (
        ('a', 'Active'),
        ('r', 'Registered'),
        ('i', 'Inactive')
    )

    status = models.CharField(
        max_length=1, choices=LOAN_STATUS, blank=True, default='a', null=True)
    sys_access = models.BooleanField("System Access",default=False,null=True)
    zone = models.CharField(max_length=10, null=True)
    first_name = models.CharField(max_length=20, null=True)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200, null=True)
    company_name = models.CharField("Company Name",max_length=200, null=True)
    mobile = models.CharField("Mobile Number",max_length=15, null=True, blank=True)
    line1 = models.CharField("Address Line 1",max_length=50, null=True)
    line2 = models.CharField("Address Line 2",max_length=50, null=True)
    line3 = models.CharField("Address Line 3",max_length=50, null=True)
    city = models.CharField(max_length=15, null=True)
    zip_code = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=50, null=True)
    date_created = models.DateField("Date Created",auto_now=True, null=True,blank=True)
    date_start = models.DateField("Date Started",auto_now=True, null=True,blank=True)
    date_end = models.DateField("Date Ended",auto_now_add=False, null=True,blank=True)

    def __str__(self):
        return f'{self.customer_id}'


class Location(models.Model):
    location_id = models.CharField(max_length=20, null=True)
    zone = models.CharField(max_length=10,null=True)
    station_name = models.CharField(max_length=100,null=True)
    manager = models.ManyToManyField(User)
    phone = models.CharField(max_length=15,null=True)
    email=models.CharField(max_length=30,null=True)
    line_1 = models.CharField(max_length=50,null=True)
    line_2 = models.CharField(max_length=50,null=True)
    line_3 = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=20,null=True,blank=True)
    zip_code  = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=70,null=True)
    area = models.CharField(max_length=150,null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    altitude = models.IntegerField(null=True)

    def __str__(self):
        return self.location_id


class Drone(models.Model):

    droneid = models.CharField("Drone ID",max_length=200, null=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1, choices=LOAN_STATUS, blank=True, default='m', null=True)
    locale = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL,verbose_name="Drone Station")
    make = models.CharField(max_length=100, null=True, blank=True)
    model_no = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    ean = models.CharField(max_length=10, null=True, blank=True)
    price_currency = models.CharField(max_length=3, blank=True, null=True)
    price = models.CharField(max_length=5, null=True, blank=False)
    warranty = models.CharField(max_length=10, null=True, blank=True)
    date_purchase = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)
    date_operation = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)
    date_shelved = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.droneid


class Mission(models.Model):

    def incrementid():
        no = Mission.objects.count()
        np = f'{no:06}'
        if no == None:
            return 'M000001'
        else:
            no = no+1
            np = f'M{no:06}'
            return np

    mission_id = models.CharField(
        max_length=10, null=True, default=incrementid, editable=False)
    date = models.DateField(auto_now_add=False, null=True)
    time = models.TimeField(auto_now_add=False,null=True)
    drone = models.ForeignKey(Drone, null=True, on_delete=models.SET_NULL)
    state = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    manager = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    MISSION_TYPE = (
        ('1', 'Loiter'),
        ('2', 'Circumferance'),
        ('3', 'Lawn-Mower'),
    )

    mission_type = models.CharField(
        max_length=10, choices=MISSION_TYPE, blank=True, default='2', null=True)

    INFO_TYPE = (
        ('1', 'Photo'),
        ('2', 'Video'),
    )
    mode_type = models.CharField(
        max_length=10, choices=INFO_TYPE, blank=True, default='1', null=True)

    STATE_TYPE = (
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
        ('Cancelled', 'Cancelled'),
        ('On Schedule','On Schedule')
    )
    mission_status = models.CharField(
        max_length=15, choices=STATE_TYPE, default='Pending', blank=True, null=True)

    LAUNCH_MODE = {
        ('AUTO', 'AUTO'),
        ('MANUAL', 'MANUAL')
    }
    launch_mode = models.CharField(
        max_length=7, choices=LAUNCH_MODE, default='MANUAL', null=True)
    mission_pic = models.ImageField(null=True, blank=True, default="logo.png",upload_to='mission_img')
    launch_now = models.BooleanField(null=True, default=False)

    def __str__(self):
        return str(self.mission_id)


class Launch(models.Model):

    mission = models.CharField(max_length=10, null=True)
    now = models.CharField(max_length=1, default='1', null=True)

    def __str__(self):
        return self.mission


class CSVFileFolder(models.Model):

    csf_file = models.FileField(upload_to='csvfodler')

    def save(self, *args, **kwargs):
        """
        This is where you analyze the CSV file and update 
        Category and Product models' data
        """
        super(CSVFileFolder, self).save(*args, **kwargs)
        self.csv_file.open(mode='rb')
        f = csv.reader(self.csv_file)
        for row in f:
            # currently the row is a list of all fields in CSV file
            # change it to a dict for ease
            #row_dict = self.row_to_dict(row) # this method is defined below
            # check if product exists in db
            mission = self.product_is_in_db(row['\ufeffmission_id']) # this method is defined below
            if mission:
                # product is in db
                # update fields values
                self.update_product(mission, row) # this method is defined below
            else:
                # product is not in db
                # create this product
                self.create_product(row) # this method is defined below

        self.csv_file.close()


    def row_to_dict(self, row):
        """Returns the given row in a dict format"""
        # Here's how the row list looks like:
        # ['category', 'product name', 'product uid' 'price', 'qty']
        return {'category': row[0], 'name': row[1], 
            'uid': row[2], 'price': row[3], 'qty': row[4]
            }

    def product_is_in_db(self, uid):
        """Check the product is in db. 
        If yes, return the product, else return None
        """
        try:
            return Mission.objects.get(mission_id=uid)
        except Mission.DoesNotExist:
            return None

    def update_product(self, mission, row):
        """Update the given product with new data in row_dict"""
        mission.mission_id = row['mission_id']
        #mission.state = row['state']
        #mission.drone = row['drone']
        mission.mission_type = row['mission_type']
        mission.date = row['date']
        mission.time = row['time']
        mission.mission_status = row['mission_status']
        mission.mode_type = row['mode_type']
        #mission.customer = row['customer']
        mission.save()

    def create_product(self, row_dict):
        # First see, if category exists
        # If not, create a new category
        try:
            state = Location.objects.get(row['state'])
        except Location.DoesNotExist:
            state = None
        try:
            drone = Drone.objects.get(row['drone'])
        except Drone.DoesNotExist:
            drone = None
        
        try:
            customer = Customer.objects.get(row['customer'])
        except Customer.DoesNotExist:
            customer = None



        # Now, create the product
        Mission.objects.create(
            mission_id = row['mission_id'],
            state = row['state'],
            drone = row['drone'],
            mission_type = row['mission_type'],
            date = row['date'],
            time = row['time'],
            mission_status = row['mission_status'],
            mode_type = row['mode_type'],
            customer = row['customer'],
        )
        print("uPDATING")