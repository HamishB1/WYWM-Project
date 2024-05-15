from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('TeamWebsite', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS TeamWebsite_user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password VARCHAR(128) NOT NULL,
                last_login DATETIME NULL,
                is_superuser BOOLEAN NOT NULL DEFAULT 0,
                username VARCHAR(150) NOT NULL UNIQUE,
                first_name VARCHAR(30) NOT NULL DEFAULT '',
                last_name VARCHAR(150) NOT NULL DEFAULT '',
                email VARCHAR(254) NOT NULL,
                is_staff BOOLEAN NOT NULL DEFAULT 0,
                is_active BOOLEAN NOT NULL DEFAULT 1,
                date_joined DATETIME NOT NULL
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS TeamWebsite_user;"
        )
    ]
