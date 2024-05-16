from django.db import models


class NODE42_AUTH_LEVEL(models.IntegerChoices):
    GUEST = 0
    CHARTER = 2
    HOST = 4
    ADMIN = 8
    SUDO = 1024


def is_valid_auth_level(value):
    return value in NODE42_AUTH_LEVEL.values


class StageRoleChoices(models.TextChoices):
    SPECTATOR = 'spectator', 'Spectator'
    PARTICIPANT = 'participant', 'Participant'
    JUDGE = 'judge', 'Judge'
    HOST = 'host', 'Host'
    OWNER = 'owner', 'Owner'


class StageOperations(models.TextChoices):
    VIEW_RESOURCES = 'view_reasources'
    VIEW_SONG_INFO = 'view_song_info'
    EDIT_SONG_INFO = 'edit_song_info'
    EDIT_RESOURCES = 'edit_reasources'
    POST_YOUR_CHART = 'post_your_chart'
    POST_ANY_CHART = 'post_any_chart'
    VIEW_YOUR_SCORE = 'view_your_score'
    VIEW_ALL_SCORE = 'view_all_score'
    VIEW_ALL_CHARTS = 'view_all_charts'
    MANAGE_PARTICIPANT = 'manage_participant'
    MANAGE_JUDGE = 'manage_judge'
    MANAGE_HOST = 'manage_host'
    MANAGE_OWNER = 'manage_owner'
