from django.db import models
from vacancy import choices


class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Region(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class District(BaseModel):
    title = models.CharField(max_length=128)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.SlugField('self', max_length=128)

    def __str__(self):
        return self.title


class MasterType(BaseModel):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.title


class Skills(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Vacancy(BaseModel):
    title = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    from_price = models.IntegerField(blank=True, null=True)
    to_price = models.IntegerField(blank=True, null=True)

    is_position = models.BooleanField(default=True)
    is_company = models.BooleanField(default=True)
    is_job = models.BooleanField(default=True)

    degree = models.CharField(max_length=128, choices=choices.DEGREE.choices)
    bandlik = models.CharField(max_length=128, choices=choices.BANDLIK.choices)
    part_time = models.CharField(max_length=128, choices=choices.PartTimeJob.choices)
    grafik = models.CharField(max_length=128, choices=choices.IshGRAFIGI.choices)
    edu = models.CharField(max_length=128, choices=choices.EDU.choices)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    master = models.ForeignKey(MasterType, on_delete=models.CASCADE, related_name="master")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="region")
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True, related_name="district")

    skills = models.ManyToManyField(Skills, related_name="skills")

    def __str__(self):
        return self.title


class Search(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title
