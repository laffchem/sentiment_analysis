import pandas as pd
from striprtf.striprtf import rtf_to_text

negative_df = pd.read_csv("LoughranMcDonald_Negative.csv")
positive_df = pd.read_csv("LoughranMcDonald_Positive.csv")

positive_sentiments: list[str] = (
    positive_df.values.flatten().tolist()
)  # make a list of positive sentiments
negative_sentiments: list[str] = (
    negative_df.values.flatten().tolist()
)  # make a list of negative sentiments


# Count sentiments in the file (meant to be run with both positive and negative lists)
# Count sentiments in the file (meant to be run with both positive and negative lists)
def count_sentiments(sentiments: list[str], file: str) -> int:
    sentiments = [s.lower() for s in sentiments]  # Convert sentiments to lowercase
    with open(file, "r") as f:
        text: str = f.read().lower()  # Convert text to lowercase
        count: int = 0
        for line in text.splitlines():
            for word in line.split():
                if word in sentiments:
                    count += 1
        return count


# Takes the list of files and returns a dictionary with the sentiment difference
def run_files(filenames: list[str]) -> dict[str, dict[str, int]]:
    result: dict[str, dict[str, int]] = {}
    for file in filenames:
        positive_count: int = count_sentiments(positive_sentiments, file)
        negative_count: int = count_sentiments(negative_sentiments, file)
        sentiment_diff: int = positive_count - negative_count
        result[file] = {
            "Positive Count": positive_count,
            "Negative Count": negative_count,
            "Sentiment Difference": sentiment_diff,
        }
    return result


# Creates a table with the sentiment difference
def create_sentiment_table(
    sentiment_results: dict[str, dict[str, int]]
) -> pd.DataFrame:
    df = pd.DataFrame.from_dict(sentiment_results, orient="index")
    df.index.name = "Stock"
    df = df.reset_index()
    df = df.sort_values(by="Sentiment Difference", ascending=False)
    return df


filenames: list[str] = [
    "data/3MCo-10.txt",
    "data/CiscoSystems-10.txt",
    "data/McDonalds-2.txt",
    "data/TravelersCo-3.txt",
    "data/AmazonFiles-10.txt",
    "data/CocaCola-10.txt",
    "data/MerckCo-10.txt",
    "data/UnitedHealth-10.txt",
    "data/AmericanExpressFiles-10.txt",
    "data/GoldmanSachs-10.txt",
    "data/Microsoft-10.txt",
    "data/Verizon-10.txt",
    "data/AmgenFiles10.txt",
    "data/HomeDepot-10.txt",
    "data/Nike-10.txt",
    "data/Visa-10.txt",
    "data/AppleFiles-10.txt",
    "data/Honeywell-10.txt",
    "data/Nvidia-10.txt",
    "data/Walmart-10.txt",
    "data/BoeingFiles-10.txt",
    "data/IBM-10.txt",
    "data/ProcterGamble-10.txt",
    "data/WaltDisney-10.txt",
    "data/CaterpillarFiles-10.txt",
    "data/JohnsonJohnson-10.txt",
    "data/Salesforce-10.txt",
    "data/Chevron-10.txt",
    "data/JPMorganChase-10.txt",
    "data/SherwinWilliams-6.txt",
]


def main() -> None:
    sentiment_results = run_files(filenames)
    sentiment_table = create_sentiment_table(sentiment_results)
    sentiment_table.to_csv("sentiment_table.csv", index=False)
    print(sentiment_table)


if __name__ == "__main__":
    main()
