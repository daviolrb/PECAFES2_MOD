from __future__ import unicode_literals

from django.db import models

class FornecedorIndividual(models.Model):

    nomeprop = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    dap = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    uf = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    municipio = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    bairro = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    rua = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    numero = models.IntegerField(
        null=False,
        blank=False
    )

    tel_fixo = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )

    celular = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    objetos = models.Manager()

class FornecedorInformal(models.Model):

    nomeprop = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    dap = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    uf = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    municipio = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    bairro = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    rua = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    numero = models.IntegerField(
        null=False,
        blank=False
    )

    tel_fixo = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )

    celular = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

class FornecedorFormal(models.Model):

    nomeprop = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    dap = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    uf = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    municipio = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    bairro = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    rua = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    numero = models.IntegerField(
        null=False,
        blank=False
    )

    tel_fixo = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )

    celular = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cnpj = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )