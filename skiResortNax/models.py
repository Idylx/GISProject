from django.db import models
from django.contrib.gis.db import models

# Model Grenouillere
class Grenouillere(models.Model):
    geom = models.MultiPolygonField(srid=3857, null=True)
    capacity = models.IntegerField()
    altitude = models.IntegerField()
    nbrperson = models.IntegerField() #lui
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        db_table= "grenouilleres"

# Model lift
class Lift(models.Model):
    geom = models.MultiPolygonField(srid=3857, null=True)
    avgqueue = models.IntegerField() #lui
    altstart = models.IntegerField()
    altarrival = models.IntegerField()
    maxflow = models.IntegerField()
    seatchair = models.IntegerField()
    length = models.IntegerField()
    status = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "lifts"

    def __str__(self):
        return self.name

# Model Parking
class Parking(models.Model):
    geom = models.MultiPolygonField(srid=3857, null=True)
    capacity = models.IntegerField()
    altitude = models.IntegerField()
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "parkings"

# Model Restaurant
class Restaurant(models.Model):
    geom = models.MultiPolygonField(srid=3857, null=True)
    capacity = models.IntegerField() #lui
    altitude = models.IntegerField()
    status = models.CharField(max_length=50)
    name = models.CharField(max_length=50) #lui

    class Meta:
        db_table = "restaurants"

    def __str__(self):
        return self.name

# Model slopes
class Slope(models.Model):
    geom = models.MultiPolygonField(srid=3857, null=True)
    difficulty =  models.CharField(max_length=50)
    altstart = models.IntegerField()
    altarrival = models.IntegerField()
    difheight = models.IntegerField()
    statrus = models.CharField(max_length=50) #lui
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "slopes"

    def __str__(self):
        return self.name