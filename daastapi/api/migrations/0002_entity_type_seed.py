from django.db import migrations

def seed_entity_types(apps, schema_editor):
    """
    Add Entity types that we will be using in this project.
    """
    items = [{
        'name': 'Voyages',
        'url_format': 'https://www.slavevoyages.org/voyage/{key}/variables'
    }, {
        'name': 'Enslaved',
        'url_format': 'https://www.slavevoyages.org/enslaved/{key}/variables'
    }, {
        'name': 'Enslavers',
        'url_format': 'https://www.slavevoyages.org/enslaver/{key}/variables'
    }]
    # We can't import the EntityType model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    EntityType = apps.get_model("api", "EntityType")
    for item in items:
        et = EntityType(**item)
        et.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_entity_types)
    ]
