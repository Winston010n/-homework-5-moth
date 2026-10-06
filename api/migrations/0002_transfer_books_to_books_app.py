from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[migrations.DeleteModel(name='Books')],
        ),
    ]