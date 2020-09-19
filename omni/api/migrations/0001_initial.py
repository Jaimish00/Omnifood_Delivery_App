from django.db import IntegrityError, migrations
from ..custom_user.models import User # Import Custom User Model
from django.db import transaction

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = User(
            email='admin@admin.com',
            is_staff = True,
            is_superuser = True,
            )
        try:
            with transaction.atomic():
                user.set_password('admin')
                user.save()
        except IntegrityError:
            user.delete()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
