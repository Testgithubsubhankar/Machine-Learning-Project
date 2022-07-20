from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration
def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        #data_validaton_config = Configuration().get_data_transformation_config()
        #print(data_validaton_config)

        # schema_file_path=r"D:\Project\machine_learning_project\config\schema.yaml"
        # file_path=r"D:\Project\machine_learning_project\housing\artifact\data_ingestion\2022-06-27-19-13-17\ingested_data\train\housing.csv"



    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()


