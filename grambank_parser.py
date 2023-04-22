from argparse import ArgumentParser
import pandas as pd


def main(features, 
         save_file_path='./grambank_output.csv'
        ):
    
    features = features.split(',')
    values = pd.read_csv('https://raw.githubusercontent.com/grambank/grambank/master/cldf/values.csv')
    values = values[values['Parameter_ID'].isin(features)]

    languages = pd.read_csv('https://raw.githubusercontent.com/grambank/grambank/master/cldf/languages.csv')
    languages = languages.rename(columns={'ID': 'Language_ID', 'Name': 'Language_Name'})
    parameters = pd.read_csv('https://raw.githubusercontent.com/grambank/grambank/master/cldf/parameters.csv')
    parameters = parameters.rename(columns={'ID': 'Parameter_ID', 'Name': 'Parameter_Name'})

    val_lngs = values.merge(languages, on='Language_ID', how='left')
    val_lngs_param = val_lngs.merge(parameters, on='Parameter_ID', how='left')

    val_lngs_param.to_csv(save_file_path, index=False)
    
    
if __name__ == '__main__':
    argparser = ArgumentParser()
    argparser.add_argument('features', type=str,
                           help='provide a list of features you want to get without space (example: GB314,GB315)'
                           )
    argparser.add_argument('save_file_path', type=str, nargs='?', default='./grambank_output.csv',
                           help='provide a route to file for the results (default: ./grambank_output.csv)'
                           )
    args = argparser.parse_args()
    main(features=args.features, 
         save_file_path=args.save_file_path
        )
