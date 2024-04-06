import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('profile_picture', models.URLField(blank=True, null=True)),
                ('account_status', models.CharField(default='active', max_length=20)),
                ('created_by', models.CharField(default='user', max_length=20)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
