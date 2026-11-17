class Patient:
  def __init__(self, name, bill_amount):
    self.__name = name
    self.__bill_amount = bill_amount
  def get_name(self):
    return self.__name
  def set_name(self, name):
    self.__name = name
  def get_bill_amount(self):
    return self.__bill_amount
  def set_bill_amount(self, bill_amount):
    self.__bill_amount = bill_amount
  def calculate_bill(self):
    return self.__bill_amount
  def display_patient_type(self):
    return "Regular Patient"

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80
    def display_patient_type(self):
        return "Senior Citizen"

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85
    def display_patient_type(self):
        return "PhilHealth Member"

patient1 = Patient("Ania", 1000)
patient2 = SeniorPatient("Rawry", 1000)
patient3 = PhilHealthPatient("Dash", 1000)

patients = [patient1, patient2, patient3]
for patient in patients:
    print("Patient Name:", patient.get_name())
    print("Patient Type:", patient.display_patient_type())
    print("Original Bill:", patient.get_bill_amount())
    print("Final Bill:", patient.calculate_bill())
