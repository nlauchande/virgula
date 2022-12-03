import os
import csv
import typer

app = typer.Typer()

#get header of a csv
@app.command()
def header(csv_file:str):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
    print(header)

#detect different collumns in two csv files
@app.command()
def diffcol(csv_file1:str, csv_file2:str):
    header1 = header(csv_file1)
    header2 = header(csv_file2)
    diff_collumns = set(header1) - set(header2)
    print(diff_collumns)

#detect different collumns in two csv files
@app.command()
def concatenate(csv_file1:str, csv_file2:str):
    with open(csv_file1, 'r') as f1:
        reader1 = csv.reader(f1)
        header1 = next(reader1)
        data1 = list(reader1)
    with open(csv_file2, 'r') as f2:
        reader2 = csv.reader(f2)
        header2 = next(reader2)
        data2 = list(reader2)
    data = data1 + data2

    with open('result.csv', 'w') as f:    
        writer = csv.writer(f)
        writer.writerow(header1)
        writer.writerows(data)
    print("Result writen to result.csv")

if __name__ == "__main__":
    app()