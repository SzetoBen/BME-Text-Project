import pandas as pd

def clean_pre_ai():
    df = pd.read_csv('Datasets/pre_ai.csv')
    df = df[['Text']]

    # Remove rows where 'Text' is empty or NaN
    df = df[df['Text'].notna() & (df['Text'].str.strip() != '')]
    df = df.reset_index(drop=True)

    # Save the cleaned dataset (optional)
    df.to_csv('data/cleaned_pre_ai.csv', index=False)

if __name__ == '__main__':
    clean_pre_ai()
