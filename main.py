from WinePrediction import logger
from WinePrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from WinePrediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from WinePrediction.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from WinePrediction.pipeline.stage_04_model_training import ModelTrainingPipeline
from WinePrediction.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx================x")
        
except Exception as e:
        logger.exception(e)    
        raise e
        
        
STAGE_NAME="Data Validation stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<<<<")
    obj=DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx================x")
        
except Exception as e:
        logger.exception(e)
        
        raise e 


STAGE_NAME="Data Transformation stage"
    
try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<<<<")
    obj=DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx================x")
        
except Exception as e:
        logger.exception(e)
        
        raise e   

STAGE_NAME="Model Training Pipeline"


try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<<<<")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx================x")
        
except Exception as e:
        logger.exception(e)
        
        raise e    


STAGE_NAME="Model Evaluation Pipeline"

try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<<<<")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx================x")
        
except Exception as e:
        logger.exception(e)
        
        raise e    
