from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Offer(models.Model):

    HELP_CHOICES = (
        ("Food", "Food"),
        ("Transportation", "Transportation"),
        ("Supplies", "Supplies"),
        ("Work", "Work"),
        ("Advice", "Advice"),
        ("Friendship", "Friendship"),
    )

    OFFERS='TO'
    HELPS='TH'


    HELP_OFFER = ((OFFERS, "I have something to offer"),
                  (HELPS, "I could use a little help"))

    NEIGHBORHOOD = (('Admiral', 'Admiral'),
                    ('Alki', 'Alki'),
                    ('Arbor Heights', 'Arbor Heights'),
                    ('Atlantic', 'Atlantic'),
                    ('Ballard', 'Ballard'),
                    ('Beacon Hill', 'Beacon Hill'),
                    ('Belltown', 'Belltown'),
                    ('Bitter Lake', 'Bitter Lake'),
                    ('Blue Ridge', 'Blue Ridge'),
                    ('Brighton', 'Brighton'),
                    ('Broadmoor', 'Broadmoor'),
                    ('Broadview', 'Broadview'),
                    ('Bryant', 'Bryant'),
                    ('Capitol Hill', 'Capitol Hill'),
                    ('Cedar Park', 'Cedar Park'),
                    ('Central District', 'Central District'),
                    ('Columbia City', 'Columbia City'),
                    ('Crown Hill', 'Crown Hill'),
                    ('Denny-Blaine', 'Denny-Blaine'),
                    ('Downtown', 'Downtown'),
                    ('Eastlake', 'Eastlake'),
                    ('Fauntleroy', 'Fauntleroy'),
                    ('First Hill', 'First Hill'),
                    ('Fremont', 'Fremont'),
                    ('Georgetown', 'Georgetown'),
                    ('Green Lake', 'Green Lake'),
                    ('Greenwood', 'Greenwood'),
                    ('Haller Lake', 'Haller Lake'),
                    ('Hawthorne Hills', 'Hawthorne Hills'),
                    ('High Point', 'High Point'),
                    ('Highland Park', 'Highland Park'),
                    ('Industrial District', 'Industrial District'),
                    ('Interbay', 'Interbay'),
                    ('International District', 'International District'),
                    ('Laurelhurst', 'Laurelhurst'),
                    ('Leschi', 'Leschi'),
                    ('Lower Queen Anne', 'Lower Queen Anne'),
                    ('Loyal Heights', 'Loyal Heights'),
                    ('Madison Park', 'Madison Park'),
                    ('Madison Valley', 'Madison Valley'),
                    ('Madrona', 'Madrona'),
                    ('Magnolia', 'Magnolia'),
                    ('Maple Leaf', 'Maple Leaf'),
                    ('Matthews Beach', 'Matthews Beach'),
                    ('Meadowbrook', 'Meadowbrook'),
                    ('Montlake', 'Montlake'),
                    ('Mount Baker', 'Mount Baker'),
                    ('North Beach', 'North Beach'),
                    ('North College Park', 'North College Park'),
                    ('North Delridge', 'North Delridge'),
                    ('Northgate', 'Northgate'),
                    ('Olympic Hills', 'Olympic Hills'),
                    ('Olympic Manor', 'Olympic Manor'),
                    ('Phinney Ridge', 'Phinney Ridge'),
                    ('Pinehurst', 'Pinehurst'),
                    ('Pioneer Square', 'Pioneer Square'),
                    ('Portage Bay', 'Portage Bay'),
                    ('Queen Anne', 'Queen Anne'),
                    ('Rainier Beach', 'Rainier Beach'),
                    ('Ravenna', 'Ravenna'),
                    ('Riverview', 'Riverview'),
                    ('Roosevelt', 'Roosevelt'),
                    ('Roxhill', 'Roxhill'),
                    ('Sand Point', 'Sand Point'),
                    ('Seward Park', 'Seward Park'),
                    ('South Delridge', 'South Delridge'),
                    ('South Lake Union', 'South Lake Union'),
                    ('South Park', 'South Park'),
                    ('Sunset Hill', 'Sunset Hill'),
                    ('University District', 'University District'),
                    ('Victory Heights', 'Victory Heights'),
                    ('View Ridge', 'View Ridge'),
                    ('Wallingford', 'Wallingford'),
                    ('Wedgwood', 'Wedgwood'),
                    ('West Seattle', 'West Seattle'),
                    ('Westlake', 'Westlake'),
                    ('Whittier Heights', 'Whittier Heights'),
                    ('Windermere', 'Windermere'),)

    author = models.ForeignKey(
        get_user_model(),on_delete=models.CASCADE)
    need_help = models.CharField(
        max_length=10, choices=HELP_OFFER, default=OFFERS)
    title = models.CharField(max_length=100, verbose_name="Additional Discription")
    neighborhood = models.CharField(max_length=100, choices=NEIGHBORHOOD)
    description = models.CharField(
        max_length=300, choices=HELP_CHOICES, verbose_name="What would you like to offer? (please choose)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('offer_posts')


class Help(models.Model):

    HELP_CHOICES = (
        ("Food", "Food"),
        ("Transportation", "Transportation"),
        ("Supplies", "Supplies"),
        ("Work", "Work"),
        ("Advice", "Advice"),
        ("Friendship", "Friendship"),
    )

    OFFERS='TO'
    HELPS='TH'


    HELP_OFFER = ((OFFERS, "I have something to offer"),
                  (HELPS, "I could use a little help"))

    NEIGHBORHOOD = (('Admiral', 'Admiral'),
                    ('Alki', 'Alki'),
                    ('Arbor Heights', 'Arbor Heights'),
                    ('Atlantic', 'Atlantic'),
                    ('Ballard', 'Ballard'),
                    ('Beacon Hill', 'Beacon Hill'),
                    ('Belltown', 'Belltown'),
                    ('Bitter Lake', 'Bitter Lake'),
                    ('Blue Ridge', 'Blue Ridge'),
                    ('Brighton', 'Brighton'),
                    ('Broadmoor', 'Broadmoor'),
                    ('Broadview', 'Broadview'),
                    ('Bryant', 'Bryant'),
                    ('Capitol Hill', 'Capitol Hill'),
                    ('Cedar Park', 'Cedar Park'),
                    ('Central District', 'Central District'),
                    ('Columbia City', 'Columbia City'),
                    ('Crown Hill', 'Crown Hill'),
                    ('Denny-Blaine', 'Denny-Blaine'),
                    ('Downtown', 'Downtown'),
                    ('Eastlake', 'Eastlake'),
                    ('Fauntleroy', 'Fauntleroy'),
                    ('First Hill', 'First Hill'),
                    ('Fremont', 'Fremont'),
                    ('Georgetown', 'Georgetown'),
                    ('Green Lake', 'Green Lake'),
                    ('Greenwood', 'Greenwood'),
                    ('Haller Lake', 'Haller Lake'),
                    ('Hawthorne Hills', 'Hawthorne Hills'),
                    ('High Point', 'High Point'),
                    ('Highland Park', 'Highland Park'),
                    ('Industrial District', 'Industrial District'),
                    ('Interbay', 'Interbay'),
                    ('International District', 'International District'),
                    ('Laurelhurst', 'Laurelhurst'),
                    ('Leschi', 'Leschi'),
                    ('Lower Queen Anne', 'Lower Queen Anne'),
                    ('Loyal Heights', 'Loyal Heights'),
                    ('Madison Park', 'Madison Park'),
                    ('Madison Valley', 'Madison Valley'),
                    ('Madrona', 'Madrona'),
                    ('Magnolia', 'Magnolia'),
                    ('Maple Leaf', 'Maple Leaf'),
                    ('Matthews Beach', 'Matthews Beach'),
                    ('Meadowbrook', 'Meadowbrook'),
                    ('Montlake', 'Montlake'),
                    ('Mount Baker', 'Mount Baker'),
                    ('North Beach', 'North Beach'),
                    ('North College Park', 'North College Park'),
                    ('North Delridge', 'North Delridge'),
                    ('Northgate', 'Northgate'),
                    ('Olympic Hills', 'Olympic Hills'),
                    ('Olympic Manor', 'Olympic Manor'),
                    ('Phinney Ridge', 'Phinney Ridge'),
                    ('Pinehurst', 'Pinehurst'),
                    ('Pioneer Square', 'Pioneer Square'),
                    ('Portage Bay', 'Portage Bay'),
                    ('Queen Anne', 'Queen Anne'),
                    ('Rainier Beach', 'Rainier Beach'),
                    ('Ravenna', 'Ravenna'),
                    ('Riverview', 'Riverview'),
                    ('Roosevelt', 'Roosevelt'),
                    ('Roxhill', 'Roxhill'),
                    ('Sand Point', 'Sand Point'),
                    ('Seward Park', 'Seward Park'),
                    ('South Delridge', 'South Delridge'),
                    ('South Lake Union', 'South Lake Union'),
                    ('South Park', 'South Park'),
                    ('Sunset Hill', 'Sunset Hill'),
                    ('University District', 'University District'),
                    ('Victory Heights', 'Victory Heights'),
                    ('View Ridge', 'View Ridge'),
                    ('Wallingford', 'Wallingford'),
                    ('Wedgwood', 'Wedgwood'),
                    ('West Seattle', 'West Seattle'),
                    ('Westlake', 'Westlake'),
                    ('Whittier Heights', 'Whittier Heights'),
                    ('Windermere', 'Windermere'),)

    author = models.ForeignKey(
        get_user_model(),on_delete=models.CASCADE)
    need_help = models.CharField(
        max_length=10, choices=HELP_OFFER, default=HELPS)
    title = models.CharField(max_length=100, verbose_name="Additional Discription")
    neighborhood = models.CharField(max_length=100, choices=NEIGHBORHOOD)
    description = models.CharField(
        max_length=300, choices=HELP_CHOICES, verbose_name="What Type of Help do You Need? (please choose)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('help_posts')
