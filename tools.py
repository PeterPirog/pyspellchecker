

class CsvTool:
    def __init__(self):
        pass
    def combine_csvs(self,dir_src_path,file_name_out='output.csv',dir_out_path=None,dataframe_only=False):
        """
        Function to combine vertically csv files.
        The files must have the same number of columns !!!
        Args:
            dir_src_path: path to directory with csv files to combine
            file_name_out: output filename with combined files
            dir_out_path:
            dataframe_only:
        Returns:

        """
