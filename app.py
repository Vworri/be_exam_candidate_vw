import pandas as pd
from numpy import NaN
import json


class RecordValidation(object):
    """A class to validate record entries using buisness rules"""

    def __init__(self, inputPath="data.csv", outputPath="output.json", errorPath="error.csv"):
        inputPath = input("Please input path for input file (default: data.csv): \n") or inputPath
        outputPath = input("Please input path for output file (default: output.json): \n") or outputPath
        try:
            self.records = pd.read_csv(inputPath, header=0, index_col=None).fillna("")
        except FileNotFoundError:
            raise FileNotFoundError("Invalid input file given")
        self.invalidRecords = pd.DataFrame(columns=["Record_Number", "Error_Message"])
        self.handleRecords()
        if not self.invalidRecords.empty:
            self.invalidRecords.to_csv(inputPath, index=False)
        self.formatAndSaveOutput(outputPath)


    @staticmethod
    def validateId(id):
        """called to make sure the if is a positive integer with 8 digits
        """
        id = str(id)
        if not id or id == NaN:
            return "No id given"
        try:
            if not (int(id) > 10000000 and int(id) < 99999999):
                return "Id is not 8 digits or is not positive"
        except ValueError:
            return "Id could not be converted to integer"

    @staticmethod
    def validateName(name):
        """called to make sure the name is not too long or empty
        """

        if name == None:
            return "first or last name is empty"
        name = str(name)
        if len(name) < 1 or len(name) > 15:
            return "name length invalid"

    @staticmethod
    def validateMidName(name):
        """called to make sure that the middle name does not exceed 15 characters"""
        if name == None:
            return
        if len(name) > 15:
            return "middle name too long"

    @staticmethod
    def validatePhoneNumber(number):
        """make sure the format of the phone number is correct"""
        number = str(number).strip()
        if not number:
            return "No phone number given"
        groups = number.split("-")
        notdigit = [not group.isdigit() for group in groups]
        if any(notdigit):
            return "some phone number values not digits"
        if len(groups) > 3:
            return "phone number has too many groups"
        if len(groups) < 3:
            return "phone number has too few groups"
        if len(groups[0]) != 3:
            return "Area code invalid"
        if len(groups[1]) != 3 or len(groups[2]) != 4:
            return "phone number not valid"

    def formatAndSaveOutput(self, filepath):
        """Turn records into consumable json format"""
        formated_list = []
        recs = self.records.to_dict("records")
        for rec in recs:
            formated = {}
            name = {}
            formated["id"] = rec['INTERNAL_ID']
            name["first"] = rec['FIRST_NAME']
            if  rec['MIDDLE_NAME'] != None and  rec['MIDDLE_NAME'] != "":
                name["middle"] = rec['MIDDLE_NAME']
            name["last"] = rec['LAST_NAME']
            formated["name"] = name
            formated["phone"] = rec['PHONE_NUM']
            formated_list.append(formated)
        with open(filepath, "w") as f:
            json.dump(formated_list, f)

    def validateRecord(self, record):
        """take all validation functions and apply to entire record"""
        msgs = []
        msg = self.validateId(record["INTERNAL_ID"])
        if msg:
            msgs.append(msg)
        msg = self.validateMidName(str(record["MIDDLE_NAME"]))
        if msg:
            msgs.append(msg)
        msg = self.validateName(record["FIRST_NAME"])
        if msg:
            msgs.append(msg)
        msg = self.validateName(record["LAST_NAME"])
        if msg:
            msgs.append(msg)
        msg = self.validatePhoneNumber(record["PHONE_NUM"])
        if msg:
            msgs.append(msg)
        inValidRecords = []
        if not msgs:
            return True
        for msg in msgs:
            err = {}
            err["Record_Number"] = record.name
            err["Error_Message"] = msg
            inValidRecords.append(err)
        self.invalidRecords = self.invalidRecords.append(pd.DataFrame(inValidRecords))
        return False

    def handleRecords(self):
        """apply record validation to enture datafreame"""
        self.records["isValid"] = self.records.apply(lambda record: self.validateRecord(record), axis=1)
        self.records = self.records.drop(self.records[self.records["isValid"] == False].index)

if __name__ == '__main__':
    RecordValidation()