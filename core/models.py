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