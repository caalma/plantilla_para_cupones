#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np
from math import floor
from os import listdir, chdir, makedirs
from os.path import basename
from shutil import copyfile, rmtree
from subprocess import Popen, PIPE
from pypdf import PdfMerger
from configuracion import *

# seteo inicial
ruta = './tmp/'
inkscape_executable = 'inkscape'
pla = open(arc_plantilla, 'r').read()
total = total_items
ppag = cantidad_por_pagina
lst = range(1, total+1)
pad_ceros = len(str(total))
lista = list(lst[i:i+ppag] for i in range(0, len(lst), ppag))
codigos_de_reemplazo = [
    '__A__',
    '__B__',
    '__C__',
    '__D__',
    '__E__',
    '__F__',
    '__G__',
    '__H__',
    '__I__',
    '__J__',
    '__K__',
    '__L__',
    '__M__',
    '__N__',
    '__O__',
    '__P__',
    '__Q__',
    '__R__',
    '__S__',
    '__T__',
    '__U__',
    '__V__',
    '__W__',
    '__X__',
    '__Y__',
    '__Z__',
    ]

# preparacion de contexto
makedirs(ruta, exist_ok=True)
for a in archivos_referenciados_a_la_plantilla:
    adest = ruta + basename(a)
    copyfile(a, adest)

# reemplazo de plantillas
print(f'TOTAL DE CUPONES : {total}')
formato_reemplazo = '{n:0' + str(pad_ceros) + 'd}'
for np, nums in enumerate(lista):
    pla_r = pla
    for i, n in enumerate(nums):
        pla_r = pla_r.replace(codigos_de_reemplazo[i], formato_reemplazo.format(n=n))
    np = np+1
    ar = f'{ruta}hoja_{np:04d}.svg'
    with open(ar, 'w') as f:
        f.write(pla_r)
    print(ar, list(nums))


# exportación de svg a pdf
chdir(ruta)
for a in sorted(listdir('./')):
    if a.endswith('.svg'):
        print(a)
        cmd = f'{inkscape_executable} --export-type=pdf "{a}"'
        p = Popen(cmd, shell=True, stdout=PIPE)
        p.stdout.read()

# unificar pdfs
merger = PdfMerger()
for a in sorted(listdir('./')):
    if a.endswith('.pdf'):
        merger.append(a)

merger.write(f'../{arc_pdf_final}')
merger.close()

# borrar carpeta temporal
chdir('../')
rmtree(ruta, True)
