from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
                    name='Books',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('author', models.CharField(max_length=40, verbose_name='автор книги')),
                        ('title', models.CharField(max_length=70, verbose_name='название книги')),
                        ('description', models.TextField(verbose_name='описание книги')),
                        ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена книги')),
                        ('year', models.IntegerField(verbose_name='год выпуска книги')),
                    ],
                    options={
                        'db_table': 'api_books',
                        'verbose_name': 'книга',
                        'verbose_name_plural': 'книги',
                    },
                ),
            ],
        ),
    ]