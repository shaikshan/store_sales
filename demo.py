from src.pipeline.pipeline import TrainPipeline
from src.entity.config_entity import TrainingPipelineConfig


def main():
    try:
        Pipeline = TrainPipeline()
        Pipeline.run_pipeline()
    except Exception as e:
        print(e)

if __name__=="__main__":
    main()