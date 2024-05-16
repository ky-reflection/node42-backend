from django.db import models
from myuser.models import CustomUser
from utils.node42_auth import StageRoleChoices, StageOperations

import uuid


# class StageRoleChoices(models.TextChoices):
#     SPECTATOR = 'spectator', 'Spectator'
#     PARTICIPANT = 'participant', 'Participant'
#     JUDGE = 'judge', 'Judge'
#     HOST = 'host', 'Host'

class Competition(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    start_at = models.DateTimeField(blank=False)
    end_at = models.DateTimeField(blank=False)
    name = models.CharField(max_length=150, blank=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=150, blank=False)  # 比赛类型，例如 "music"


class Stage(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=150, blank=False)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)


class Chart(models.Model):
    # User=get_user_model()
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.TextField(max_length=150, blank=True)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='owner')
    stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True)
    chartfile = models.FileField(blank=True, upload_to='charts/')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class StageAction(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    start_at = models.DateTimeField(blank=False)
    end_at = models.DateTimeField(blank=False)
    STAGE_ACTION_CHOICES = [
        ('init', 'init'),
        ('pre', 'prepare'),
        ('chart', 'chart making'),
        ('judge', 'chart judge'),
        ('end', 'end'),
    ]

    action = models.CharField(
        max_length=20, choices=STAGE_ACTION_CHOICES, default='init', verbose_name='比賽阶段')

    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    stage_action_permission = models.JSONField(default=dict)


stage_action_permission_example = {
    StageRoleChoices.SPECTATOR: {},
    StageRoleChoices.PARTICIPANT: {},
    StageRoleChoices.JUDGE: {},
    StageRoleChoices.HOST: {StageOperations.MANAGE_HOST: True},
    StageRoleChoices.OWNER: {},
}


class StageResource(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    background = models.ImageField(
        upload_to='background/', blank=True, null=True, verbose_name='背景')
    music = models.FileField(upload_to='music/',
                             blank=False, null=False, verbose_name='音乐')
    chart_template = models.FileField(
        upload_to='chart_template/', blank=True, null=True, verbose_name='谱面模板')
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)


class StageResourceMetadata(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    song_name = models.TextField(max_length=150, blank=False)
    artist = models.TextField(max_length=150, blank=False)
    illustrator = models.TextField(max_length=150, blank=True)
    difficulty_range = models.TextField(max_length=50, blank=True)

    source = models.TextField(max_length=150, blank=True)
    genre = models.TextField(max_length=150, blank=True)
    beat = models.TextField(blank=True)
    bpm = models.TextField(blank=True)
    resource = models.OneToOneField(StageResource, on_delete=models.CASCADE)


class Score(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    value = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class UserCompetitionRole(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=StageRoleChoices.choices)

    class Meta:
        unique_together = ('user', 'stage', 'role')
