from django.db import models


class CPU(models.Model):
    name = models.CharField(max_length=255)
    clock_speed_ghz = models.FloatField()
    core_count = models.IntegerField()
    thread_count = models.IntegerField()
    cache_size_l1 = models.IntegerField()
    cache_size_l2 = models.IntegerField()
    cache_size_l3 = models.IntegerField()
    tdp_watts = models.IntegerField()
    architecture_generation = models.CharField(max_length=255)
    ipc = models.FloatField(help_text="Instructions per clock")

    def __str__(self):
        return self.name


class GPU(models.Model):
    name = models.CharField(max_length=255)
    vram_gb = models.FloatField()
    core_count = models.IntegerField()
    core_clock_ghz = models.FloatField()
    memory_bandwidth_gbps = models.FloatField()
    architecture = models.CharField(max_length=255)
    ray_tracing_support = models.BooleanField(default=False)
    release_year = models.IntegerField()

    def __str__(self):
        return self.name


class RAM(models.Model):
    name = models.CharField(max_length=255)
    size_gb = models.IntegerField()
    speed_mhz = models.IntegerField()
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Needs(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Phone(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False)
    brand = models.CharField(max_length=255,blank=False,null=False)
    image = models.ImageField(upload_to='phones_images/',blank=False,null=False)
    ram_size = models.IntegerField(blank=True,null=True)
    memory_size = models.IntegerField(blank=True,null=True)
    processor = models.CharField(max_length=255,blank=True,null=True)
    os_type = models.CharField(max_length=255,blank=True,null=True)
    graphic_processor = models.CharField(max_length=255,blank=True,null=True)
    camera_mp = models.CharField(max_length=255,blank=True,null=True)
    screen_type = models.CharField(max_length=255,blank=True,null=True)
    battery = models.IntegerField(blank=True,null=True)
    year = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

class BrandsCoefficients(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False)
    coefficient = models.FloatField()

    def __str__(self):
        return f"{self.name}+{self.coefficient}"