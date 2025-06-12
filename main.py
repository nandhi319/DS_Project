from src.DS import logger
from src.DS.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.DS.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.DS.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.DS.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.DS.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion  = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_validation  = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_transformation  = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>  {STAGE_NAME} completed <<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    model_training  = ModelTrainerTrainingPipeline()
    model_training.initiate_model_trainer()
    logger.info(f">>>>  {STAGE_NAME} completed <<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e