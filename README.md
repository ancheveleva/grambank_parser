# grambank_parser

This is the code for processing [Grambank database](https://grambank.clld.org). To extract sertain features, their meta-info and values across languages, run the following in a command line:

```
python3 grambank_parser.py list_of_the_features save_file_path
```

## List of the features
To specify the exact features you want to get, list their codes with comma without spaces. For example, to get features concerning gender in pronouns:
```
python3 grambank_parser.py GB030,GB197,GB196
```

The whole list of features with descriptions is available on the [Grambank website](https://grambank.clld.org/parameters) or in [the project's repository](https://github.com/grambank/grambank/blob/master/cldf/parameters.csv).


**Note:** the code for downloading the values of all the feature at once is available [here](https://github.com/grambank/grambank/tree/master/recipes). Be aware though that the result file would be more than 13 Gb.

## Save file path
File-name in CSV-format, default name `grambank_output.csv`.
