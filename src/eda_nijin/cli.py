from president_speech.db.parquet_interpreter import get_parquet_full_path
import pandas as pd
import typer

def group_by_count(keyword:str, asc:bool=False, rcnt:int=12) -> pd.DataFrame:
    data_path = get_parquet_full_path()
    df = pd.read_parquet(data_path)
    fdf = df[df['speech_text'].str.contains(keyword, case=False)]
    gdf = fdf.groupby("president").size().reset_index(name="count")
    sdf = gdf.sort_values(by='count', ascending=asc).reset_index(drop=True)
    rdf = sdf.head(rcnt)
    return rdf

def print_group_by_count(keyword:str, asc:bool=False, rcnt:int=12):
    rdf = group_by_count(keyword, asc, rcnt)
    print(rdf.to_string(index=False))
    print(f"총 합계:{len(rdf)}")

def entry_point():
    typer.run(print_group_by_count)
