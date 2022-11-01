import json
from monai.data import Dataset, DataLoader
import logging
from monai.deploy.core import DataPath, ExecutionContext, Image, InputContext, IOType, Operator, OutputContext, Application
import monai.deploy.core as md
from monai.deploy.operators.dicom_text_sr_writer_operator import DICOMTextSRWriterOperator
from monai.deploy.operators.dicom_data_loader_operator import DICOMDataLoaderOperator
from monai.deploy.operators.dicom_series_selector_operator import DICOMSeriesSelectorOperator
from monai.deploy.operators.dicom_text_sr_writer_operator import DICOMTextSRWriterOperator, ModelInfo, EquipmentInfo
from monai.deploy.operators.dicom_series_to_volume_operator import DICOMSeriesToVolumeOperator
import os
from monai.deploy.operators.monai_seg_inference_operator import InMemImageReader
from monai.data.meta_tensor import MetaTensor
import numpy as np
from monai.transforms import (Compose, AsChannelFirst, 
					LoadImage, SqueezeDim,
					EnsureType, SaveImage, 
					Activations, 
					EnsureChannelFirst, 
					NormalizeIntensity, 
					Resize, 
					EnsureType, 
					ScaleIntensity, 
					AddChannel, 
					ToTensor, 
					RepeatChannel)
from pathlib import Path
import torch
from typing import Text, Dict, List
from monai.deploy.core.domain.dicom_series_selection import StudySelectedSeries
import numpy
from breast_density_classifier_operator import ClassifierOperator
from pydicom.dataset import FileDataset
from pydicom import dcmread

class BreastClassificationApp(Application):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def compose(self):
		model_info = ModelInfo("MONAI Model for Breast Density", "BreastDensity", "0.1", "Center for Augmented Intelligence in Imaging, Mayo Clinic, Florida")
		my_equipment= EquipmentInfo(manufacturer="MONAI Deploy App SD", manufacturer_model="DICOM SR Writer")
		my_special_tags={"SeriesDescription": "Not for clinical use"}
		study_loader_op = DICOMDataLoaderOperator()
		series_selector_op = DICOMSeriesSelectorOperator(rules="")
		series_to_vol_op = DICOMSeriesToVolumeOperator()
		classifier_op = ClassifierOperator()
		sr_writer_op = DICOMTextSRWriterOperator(copy_tags=False, model_info=model_info, equipment_info=my_equipment, custom_tags=my_special_tags)

		self.add_flow(study_loader_op, series_selector_op, {"dicom_study_list": "dicom_study_list"})
		self.add_flow(series_selector_op, series_to_vol_op, {"study_selected_series_list": "study_selected_series_list"})
		self.add_flow(series_to_vol_op, classifier_op, {"image": "image"})
		self.add_flow(classifier_op, sr_writer_op, {"result_text": "classification_result"})

def main():
	app = BreastClassificationApp()
	image_dir='/home/gupta/Documents/MONAI-DEPLOY/BreastDensity/sampleDICOMs/1/BI_BREAST_SCREENING_BILATERAL_WITH_TOMOSYNTHESIS-2019-07-08/1/L_CC_C-View'

	model_path = './model/traced_ts_model.pt'
	app.run(input=image_dir, output='./output', model=model_path)

if __name__ == '__main__':
	main()
