from WinePrediction import logger
from WinePrediction.config.configuration import ConfigurationManager
from WinePrediction.components.model_training import ModelTrainer


STAGE_NAME="Model Training Pipeline"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<<<<")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx================x")
        
    except Exception as e:
        logger.exception(e)
        
        raise e