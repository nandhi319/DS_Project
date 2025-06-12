from src.DS.config.configuration import ConfigurationManager
from src.DS.components.model_trainer import ModelTrainer
from src.DS import logger

STAGE_NAME="MOdel Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer_config=ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
        