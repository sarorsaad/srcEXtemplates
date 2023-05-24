from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    MRN = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    NATIONALITY_CHOICES = [
        ('Saudi', 'Saudi'),
        ('Non-Saudi', 'Non-Saudi')
    ]
    nationality = models.CharField(max_length=9, choices=NATIONALITY_CHOICES)
    physician = models.CharField(max_length=255)
    clinical_indication = models.CharField(max_length=255)
    provisional_diagnosis = models.CharField(max_length=255)


    UNIT_CHOICES = [
        ('ER', 'Emergency Room'),
        ('pedia_ward', 'Paediatrics Ward'),
        ('male_ward', 'Male Ward'),
        ('female_ward', 'Female Ward'),
        ('OB_ward', 'Obstetrics Ward'),
        ('L&D_ward', 'Labour / Delivery Ward'),
        ('covid_ward', 'Covid Ward'),
        ('OPD', 'Outpatient Department'),
        ('referral', 'Referral'),
    ]
    STATUS_CHOICES = [
        ('emergency', 'Emergency/Immediately'),
        ('urgent', 'Urgent/24hrs'),
        ('routine', 'Routine/48 hours'),
    ]
    TRANSPORT_CHOICES = [
        ('walking', 'Walking'),
        ('wheelchair', 'Wheelchair'),
        ('trolley', 'Trolley'),
    ]
    REQUEST_CHOICES = [
        ('new', 'New Request'),
        ('followup', 'Follow Up'),
    ]
    MODALITIES_CHOICES = [
        ('CT', 'CT'),
        ('US', 'US'),
        ('X_ray', 'X-ray'),
        ('MRI', 'MRI'),
        ('Mammography', 'Mammography'),
        ('Angiogram', 'Angiogram'),
        ('Interventional_radiological_procedures', 'Interventional radiological procedures'),
        ('Fluoroscopy', 'Fluoroscopy'),
        ('Nuclear_medicine_imaging', 'Nuclear medicine imaging'),
        ('Molecular_Imaging_PET_scanning', 'Molecular Imaging /Positron Emission Tomography /PET scanning'),
        ('Bedside_critical_care_radiography', 'Bedside /critical care radiography'),
        ('Portable_radiological_machines', 'Portable radiological machines'),
    ]
    
    unit_name = models.CharField(max_length=20, choices=UNIT_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    way_of_transport = models.CharField(max_length=20, choices=TRANSPORT_CHOICES)
    is_new_request = models.CharField(max_length=20, choices=REQUEST_CHOICES)
    modalities = models.CharField(max_length=50, choices=MODALITIES_CHOICES)

    study_part_choices = (
        ('', 'Study Part'),
        ('Abdomen', 'Abdomen'),
        ('KUB', 'KUB'),
        ('OB_less_than_14_Weeks', 'OB less than 14 Weeks'),
        ('OB_more_than_14_Weeks', 'OB more than 14 Weeks'),
        ('Brain', 'Brain'),
        ('Neck', 'Neck'),
        ('Chest', 'Chest'),
        ('Pelvis', 'Pelvis'),
        ('Pan-CT', 'pan-CT'),
        ('Thyroid', 'Thyroid'),
        ('Breast', 'Breast'),
        ('Scrotal', 'Scrotal'),
        ('Cervical_spine', 'Cervical spine'),
        ('L_S_spine', 'L/S spine'),
        ('D_L_spine', 'D/L spine'),
        ('Doppler-venous-lower', 'doppler-venous-lower'),
        ('Doppler-arterial-lower', 'doppler-arterial-lower'),
        ('Doppler-venous-upper', 'doppler-venous-upper'),
        ('Doppler-arterial-upper', 'doppler-arterial-upper'),
        ('Elbow', 'Elbow'),
        ('Wrist_hand', 'Wrist/hand'),
        ('Pelvis_hip', 'Pelvis/hip'),
        ('Knee', 'Knee'),
        ('Ankle_foot', 'Ankle/foot')
    )
    study_part = models.CharField(choices=study_part_choices, max_length=50, default='', blank=True)
    
    
    side_label_choices = [
            ('right', 'Right'),
            ('left', 'Left'),
            ('none', 'None')
        ]
    need_contrast_choices = [
            ('yes', 'Yes'),
            ('no', 'No')
        ]
    contrast_specification_choices = [
            ('oral', 'Oral'),
            ('iv', 'IV Contrast'),
            ('oral_iv', 'Oral and IV Contrast'),
            ('no_contrast', 'No Contrast')
              ]
    side_label = models.CharField(max_length=50, choices=side_label_choices)
    need_contrast = models.CharField(max_length=50, choices=need_contrast_choices)
    contrast_specification = models.CharField(max_length=50, choices=contrast_specification_choices)
    
    
  
    IS_ALLERGY_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    is_allergy = models.CharField(max_length=3, choices=IS_ALLERGY_CHOICES)
    allergy_specification = models.CharField(max_length=255)
    other_study = models.CharField(max_length=255)
    date_of_request = models.DateField()

    