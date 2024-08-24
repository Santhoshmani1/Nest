# Generated by Django 5.1 on 2024-08-20 19:14

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("github", "0004_repository_organization"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="avatar_url",
            field=models.URLField(default="", verbose_name="Avatar URL"),
        ),
        migrations.AddField(
            model_name="organization",
            name="collaborators_count",
            field=models.PositiveIntegerField(default=0, verbose_name="Collaborators count"),
        ),
        migrations.AddField(
            model_name="organization",
            name="company",
            field=models.CharField(default="", max_length=200, verbose_name="Company"),
        ),
        migrations.AddField(
            model_name="organization",
            name="email",
            field=models.EmailField(default="", max_length=100, verbose_name="Email"),
        ),
        migrations.AddField(
            model_name="organization",
            name="followers_count",
            field=models.PositiveIntegerField(default=0, verbose_name="Followers count"),
        ),
        migrations.AddField(
            model_name="organization",
            name="following_count",
            field=models.PositiveIntegerField(default=0, verbose_name="Following count"),
        ),
        migrations.AddField(
            model_name="organization",
            name="location",
            field=models.CharField(default="", max_length=200, verbose_name="Location"),
        ),
        migrations.AddField(
            model_name="organization",
            name="login",
            field=models.CharField(default="", max_length=100, unique=True, verbose_name="Key"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="organization",
            name="name",
            field=models.CharField(default="", max_length=200, verbose_name="Name"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="organization",
            name="original_created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 8, 20, 19, 14, 44, 920859, tzinfo=datetime.UTC),
                verbose_name="Original created_at",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="organization",
            name="original_updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 8, 20, 19, 14, 50, 238981, tzinfo=datetime.UTC),
                verbose_name="Original updated_at",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="organization",
            name="public_gists_count",
            field=models.PositiveIntegerField(default=0, verbose_name="Public gists count"),
        ),
        migrations.AddField(
            model_name="organization",
            name="public_repositories_count",
            field=models.PositiveIntegerField(default=0, verbose_name="Public repositories count"),
        ),
        migrations.AddField(
            model_name="organization",
            name="twitter_username",
            field=models.CharField(default="", max_length=50, verbose_name="Twitter username"),
        ),
    ]