import os


def setup_report():
    # get the current working directory
    project_root = os.getcwd()

    # construct the absolute path to the report directory
    report_dir = os.path.join(project_root, 'report')

    # set the REPORT_DIR environment variable
    os.environ['REPORT_DIR'] = report_dir

    # return the report directory path
    return report_dir
