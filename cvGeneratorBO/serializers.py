from rest_framework import serializers
from .models import *


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['title', 'level']


class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = ['name', 'jobTitle', 'location', 'phone', 'mail', 'github', 'gitlab', 'linkedin', 'image', 'cv']


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ['title', 'city', 'company', 'periode', 'description']


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['title']


class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology
        fields = ['title']


class TrainingSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Training
        fields = [ 'title', 'place', 'date' ,'subjects']


class SkillsetSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Skillset
        fields = ['domain', 'skills']


class ProjectSerializer(serializers.ModelSerializer):
    techs = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['title', 'client', 'summary', 'mission' ,'techs']


class SiteSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteSettings
        fields = '__all__'


class SiteSerializer(serializers.ModelSerializer):
    infos = InfoSerializer(many=False, read_only=True)
    jobs = JobSerializer(many=True, read_only=True)
    trainings = TrainingSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    skillsets = SkillsetSerializer(many=True, read_only=True)
    siteSettings = SiteSettingsSerializer(many=False, read_only=True)

    class Meta:
        model = Site
        fields = ['pk', 'title', 'urlName', 'description', 'infos', 'jobs', 'trainings', 'projects', 'skillsets', 'siteSettings']
