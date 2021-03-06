from pathlib import Path

from django.core.management import call_command

from pytest import fixture


@fixture(scope='class')
def django_db_setup(django_db_setup, django_db_blocker):
    fixtures_dir = Path(__file__).resolve().parent / 'fixtures'
    series_fixture = fixtures_dir / 'series.json'
    chapters_fixture = fixtures_dir / 'chapters.json'
    authors_artists_fixture = fixtures_dir / 'authors_artists.json'
    groups_fixture = fixtures_dir / 'groups.json'
    with django_db_blocker.unblock():
        call_command('flush', '--no-input')
        call_command('loaddata', 'categories.xml')
        call_command('loaddata', str(authors_artists_fixture))
        call_command('loaddata', str(groups_fixture))
        call_command('loaddata', str(series_fixture))
        call_command('loaddata', str(chapters_fixture))
