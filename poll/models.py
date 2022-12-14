from django.db import models

# Create your models here.


class Voter(models.Model):
    user_name = models.CharField(max_length=30, verbose_name='Voter', default="", blank=True)
    user_ip_addr = models.GenericIPAddressField(verbose_name="Voter's IP", protocol='both', unpack_ipv4=True)
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['user_name']
        indexes = [
            models.Index(fields=('-date_entered',)),
            models.Index(fields=('user_ip_addr',))
        ]

    def __str__(self):
        return self.user_name


class Party(models.Model):
    party_name = models.CharField(max_length=10, verbose_name='Party Name', blank=True)

    class Meta:
        ordering = ['party_name']
        indexes = [
            models.Index(fields=('party_name',))
        ]

    def __str__(self):
        return self.party_name


class State(models.Model):
    state = models.CharField(max_length=30, verbose_name='State', blank=True)

    class Meta:
        ordering = ['state']
        indexes = [
            models.Index(fields=('state',))
        ]

    def __str__(self):
        return self.state


class Lga(models.Model):
    lga_id = models.SmallIntegerField(default=0, blank=True, verbose_name='LGA ID')
    lga_name = models.CharField(max_length=30, blank=True, verbose_name='LGA Name')
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)

    class Meta:
        ordering = ['lga_id']
        indexes = [
            models.Index(fields=('lga_id',)),
            models.Index(fields=('lga_name',))
        ]

    def __str__(self):
        return f'{self.lga_name}'


class Ward(models.Model):
    ward_id = models.SmallIntegerField(verbose_name='Ward ID', blank=True, default=0)
    ward_name = models.CharField(max_length=50, verbose_name='Ward Name', blank=True)
    lga_id = models.ForeignKey(Lga, on_delete=models.CASCADE)
    ward_desc = models.CharField(max_length=50, blank=True, verbose_name='Ward Description')
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-lga_id']
        indexes = [
            models.Index(fields=('ward_name',)),
        ]

    def __str__(self):
        return f'{self.ward_name}'


class PollingUnit(models.Model):
    poll_unit_id = models.SmallIntegerField(default=0, verbose_name='Poll Unique Id', blank=True)
    ward_id = models.ForeignKey(Ward, on_delete=models.CASCADE)
    lga_id = models.ForeignKey(Lga, on_delete=models.CASCADE)
    unique_ward_id = models.SmallIntegerField(default=0, blank=True, verbose_name='Unique Ward ID')
    polling_unit_number = models.CharField(max_length=30, blank=True, verbose_name='Polling Unit Number')
    polling_unit_name = models.CharField(max_length=30, blank=True, verbose_name='Polling Unit Name')
    polling_unit_desc = models.CharField(max_length=30, blank=True, verbose_name='Polling Unit Description')
    latitude = models.DecimalField(max_digits=12, decimal_places=9, default=0)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, default=0)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=('polling_unit_name',))
        ]

    def __str__(self):
        return f'{self.polling_unit_name}'


class AnnouncedWardResult(models.Model):
    ward_name = models.ForeignKey(Ward, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)

    def __str__(self):
        return self.ward_name


class AnnouncedStateResult(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)

    def __str__(self):
        return self.state


class AnnouncedPuResult(models.Model):
    polling_unit = models.ForeignKey(PollingUnit, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    party_score = models.SmallIntegerField(default=0, blank=True, verbose_name='Party Score')
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.polling_unit}'


class AnnouncedLgaResult(models.Model):
    lga = models.ForeignKey(Lga, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    party_score = models.SmallIntegerField(default=0, blank=True, verbose_name='Party Score')
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)

    def __str__(self):
        return self.lga.lga_name


class AgentName(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First Name', blank=True)
    last_name = models.CharField(max_length=30, verbose_name='Last Name', blank=True)
    user_email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    pollingunit_uniqueid = models.SmallIntegerField(default=0, blank=True, verbose_name='Polling Unit Unique ID')

    def __str__(self):
        return self.first_name


class TotalLgaPartyScores(models.Model):
    lga_id = models.ForeignKey(Lga, on_delete=models.CASCADE)
    scores = models.SmallIntegerField(default=0, blank=True, verbose_name='Party Score')

    def __str__(self):
        return self.lga_id.lga_name