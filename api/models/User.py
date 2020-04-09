"""
회원 정보 관련 ORM
"""

from enum import Enum
from django.db import models


class DutyType(Enum):
    """
    직군 구분 Enum 클래스
    """
    BAK = 'Backend Engineer'
    FRO = 'Frontend Engineer'
    DEV = 'DevOps Engineer'
    DES = 'Designer'
    CSX = 'Customer Support / Customer Experience'
    PM = 'Project Manager'


class User(models.Model):
    """
    회원 정보 클래스
    ---

    userId: 유저 아이디
    userName: 유저 닉네임
    password: 패스워드
    duty: 직군
    """
    userId = models.CharField(max_length=32)
    userName = models.CharField(max_length=32)
    password = models.CharField(max_length=128)
    duty = models.CharField(max_length=3, choices=[(item.name, item.value) for item in DutyType])

    def __str__(self):
        return self.userId
