import logging

#setup logging configuration
logging.basicConfig(filename='app.log', 
                    level=logging.info, 
                    format='%(asctime)s - [%(levelname)s] - %(message)s')