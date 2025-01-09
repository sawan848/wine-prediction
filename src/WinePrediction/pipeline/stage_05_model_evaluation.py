from WinePrediction import logger
from WinePrediction.config.configuration import ConfigurationManager
from WinePrediction.components.model_evaluation import ModelEvaluation


STAGE_NAME="Model Evaluation Pipeline"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()

        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<<<<")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx================x")
        
    except Exception as e:
        logger.exception(e)
        
        raise e