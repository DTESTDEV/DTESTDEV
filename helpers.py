import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory

import csv


"""Pass_1 and Pass_2 Processing for Bell """

def BELLprocess():
    Bell_file = "uploads/Bell.csv"
    PortaOne_file = "uploads/portaoneBell.csv"

    results = []

    Bell = []
    PortaOne = []

    with open(Bell_file, "r") as input_1:
        csv_reader = csv.DictReader(input_1)
        for row in csv_reader:
            Bell.append(row["Number"])

    with open(PortaOne_file, "r") as input_2:
        csv_reader = csv.DictReader(input_2)
        for row in csv_reader:
            PortaOne.append(row["Number"])

    for num in PortaOne:
        temp = '1' + num
        if num not in Bell and temp not in Bell:
            results.append(num)
            #print(num)

    return results


def BELLprocess2():
    Bell_file = "uploads/Bell.csv"
    PortaOne_file = "uploads/portaoneBell.csv"

    results = []

    Bell = []
    PortaOne = []

    with open(Bell_file, "r") as input_1:
        csv_reader = csv.DictReader(input_1)
        for row in csv_reader:
            Bell.append(row["Number"])

    with open(PortaOne_file, "r") as input_2:
        csv_reader = csv.DictReader(input_2)
        for row in csv_reader:
            PortaOne.append(row["Number"])

    for num in Bell:
        if num not in PortaOne:
            if num[1:] not in PortaOne:
                results.append(num)

    return results







"""Pass_1 and Pass_2 Processing for ThinkTel """

def ThinkTelprocess():
    ThinkTel_file = "uploads/ThinkTel.csv"
    PortaOne_file = "uploads/portaoneThinkTel.csv"

    results = []

    ThinkTel = []
    PortaOne = []

    with open(ThinkTel_file, "r") as input_1:
        csv_reader = csv.DictReader(input_1)
        for row in csv_reader:
            ThinkTel.append(row["\ufeffNumber"])

    with open(PortaOne_file, "r") as input_2:
        csv_reader = csv.DictReader(input_2)
        for row in csv_reader:
            PortaOne.append(row["Number"])

    for num in PortaOne:
        if num[1:] not in ThinkTel:
            results.append(num)

    return results


def ThinkTelprocess2():
    ThinkTel_file = "uploads/ThinkTel.csv"
    PortaOne_file = "uploads/portaoneThinkTel.csv"

    results = []

    ThinkTel = []
    PortaOne = []

    with open(ThinkTel_file, "r") as input_1:
        csv_reader = csv.DictReader(input_1)
        for row in csv_reader:
            ThinkTel.append(row["\ufeffNumber"])

    with open(PortaOne_file, "r") as input_2:
        csv_reader = csv.DictReader(input_2)
        for row in csv_reader:
            PortaOne.append(row["Number"])

    for num in ThinkTel:
        temp = '1' + num
        if temp not in PortaOne:
            results.append(temp)

    return results





"""Pass_1 and Pass_2 Processing for Tel_synergy """

def Tel_synergyprocess():
    Tel_synergy_file = "uploads/Tel_synergy.csv"
    PortaOne_file = "uploads/portaoneTel_synergy.csv"

    results = []

    Tel_synergy = []
    PortaOne = []

    with open(Tel_synergy_file, "r") as input_1:
        csv_reader = csv.DictReader(input_1)
        for row in csv_reader:
            Tel_synergy.append(row["Number"])

    with open(PortaOne_file, "r") as input_2:
        csv_reader = csv.DictReader(input_2)
        for row in csv_reader:
            PortaOne.append(row["Number"])

    for num in PortaOne:
        temp = '1' + num
        if num not in Tel_synergy and temp not in Tel_synergy:
            results.append(num)
            #print(num)

    return results


def Tel_synergyprocess2():
    Tel_synergy_file = "uploads/Tel_synergy.csv"
    PortaOne_file = "uploads/portaoneTel_synergy.csv"

    results = []

    Tel_synergy = []
    PortaOne = []

    with open(Tel_synergy_file, "r") as input_1:
        csv_reader = csv.DictReader(input_1)
        for row in csv_reader:
            Tel_synergy.append(row["Number"])

    with open(PortaOne_file, "r") as input_2:
        csv_reader = csv.DictReader(input_2)
        for row in csv_reader:
            PortaOne.append(row["Number"])

    for num in Tel_synergy:
        if num not in PortaOne:
            if num[1:] not in PortaOne:
                results.append(num)

    return results







"""Pass_1 and Pass_2 Processing for voipms """

def voipmsprocess():
    voipms_file = "uploads/voipms.csv"
    PortaOne_file = "uploads/portaonevoipms.csv"

    results = []

    voipms = []
    PortaOne = []

    with open(voipms_file, "r") as input_1:
        csv_reader = csv.DictReader(input_1)
        for row in csv_reader:
            voipms.append(row["Number"])

    with open(PortaOne_file, "r") as input_2:
        csv_reader = csv.DictReader(input_2)
        for row in csv_reader:
            PortaOne.append(row["Number"])

    for num in PortaOne:
        temp = '1' + num
        if num not in voipms and temp not in voipms:
            results.append(num)
            #print(num)

    return results


def voipmsprocess2():
    voipms_file = "uploads/voipms.csv"
    PortaOne_file = "uploads/portaonevoipms.csv"

    results = []

    voipms = []
    PortaOne = []

    with open(voipms_file, "r") as input_1:
        csv_reader = csv.DictReader(input_1)
        for row in csv_reader:
            voipms.append(row["Number"])

    with open(PortaOne_file, "r") as input_2:
        csv_reader = csv.DictReader(input_2)
        for row in csv_reader:
            PortaOne.append(row["Number"])

    for num in voipms:
        if num not in PortaOne:
            if num[1:] not in PortaOne:
                results.append(num)

    return results