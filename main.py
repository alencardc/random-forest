from kfold import kfold, FeatureType
from csv_handler import get_csv_data
import random
import statistics

FILE_PATH = "vote.tsv"
CSV_SEPARATOR = "\t"
TARGET_COL = "target"
SEED = 42
K_FOLDS = 10
N_TREES = 3

data, features = get_csv_data(FILE_PATH, TARGET_COL, CSV_SEPARATOR)

# Feature types of wine vote dataset
feature_types = {
  "handicapped infants": FeatureType.CATEGORICAL,
  "water project cost sharing": FeatureType.CATEGORICAL,
  "adoption of the budget resolution": FeatureType.CATEGORICAL,
  "physician fee freeze": FeatureType.CATEGORICAL,
  "el salvador aid": FeatureType.CATEGORICAL,
  "religious groups in schools": FeatureType.CATEGORICAL,
  "anti satellite test ban": FeatureType.CATEGORICAL,
  "aid to nicaraguan contras": FeatureType.CATEGORICAL,
  "mx missile": FeatureType.CATEGORICAL,
  "immigration": FeatureType.CATEGORICAL,
  "synfuels corporation cutback": FeatureType.CATEGORICAL,
  "education spending": FeatureType.CATEGORICAL,
  "superfund right to sue": FeatureType.CATEGORICAL,
  "crime": FeatureType.CATEGORICAL,
  "duty free exports": FeatureType.CATEGORICAL,
  "export administration act south africa": FeatureType.CATEGORICAL
}

def reports_vote():
  FILE_PATH = "vote.tsv"
  CSV_SEPARATOR = "\t"
  TARGET_COL = "target"
  SEED = 42
  K_FOLDS = 10

  data, features = get_csv_data(FILE_PATH, TARGET_COL, CSV_SEPARATOR)

  # Feature types of vote dataset
  feature_types = {
    "handicapped infants": FeatureType.CATEGORICAL,
    "water project cost sharing": FeatureType.CATEGORICAL,
    "adoption of the budget resolution": FeatureType.CATEGORICAL,
    "physician fee freeze": FeatureType.CATEGORICAL,
    "el salvador aid": FeatureType.CATEGORICAL,
    "religious groups in schools": FeatureType.CATEGORICAL,
    "anti satellite test ban": FeatureType.CATEGORICAL,
    "aid to nicaraguan contras": FeatureType.CATEGORICAL,
    "mx missile": FeatureType.CATEGORICAL,
    "immigration": FeatureType.CATEGORICAL,
    "synfuels corporation cutback": FeatureType.CATEGORICAL,
    "education spending": FeatureType.CATEGORICAL,
    "superfund right to sue": FeatureType.CATEGORICAL,
    "crime": FeatureType.CATEGORICAL,
    "duty free exports": FeatureType.CATEGORICAL,
    "export administration act south africa": FeatureType.CATEGORICAL
  }

  # Transform categorical features in strings
  n_features = len(data[0])-1
  for col in range(n_features):
    if (feature_types[features[col]] == FeatureType.CATEGORICAL):
      for instance in data:
        instance[col] = str(instance[col])


  n_trees_test = [1, 5, 10, 25, 50]
  random.seed(SEED)
  print("------- Report accuracy vote ---------")
  for n_tree in n_trees_test:
    print("\nNúmero de árvores: ", n_tree)
    accuracies = kfold(K_FOLDS, data, features, n_trees=n_tree, seed=SEED)
    print("Média: ", statistics.mean(accuracies))
    print("Desvio Padrão: ", statistics.stdev(accuracies))

def reports_wine():
  FILE_PATH = "wine-recognition.tsv"
  CSV_SEPARATOR = "\t"
  TARGET_COL = "target"
  SEED = 12421
  K_FOLDS = 10

  data, features = get_csv_data(FILE_PATH, TARGET_COL, CSV_SEPARATOR)

  #Feature types of wine recognition dataset
  feature_types = {
    "1": FeatureType.NUMERICAL,
    "2": FeatureType.NUMERICAL,
    "3": FeatureType.NUMERICAL,
    "4": FeatureType.NUMERICAL,
    "5": FeatureType.NUMERICAL,
    "6": FeatureType.NUMERICAL,
    "7": FeatureType.NUMERICAL,
    "8": FeatureType.NUMERICAL,
    "9": FeatureType.NUMERICAL,
    "10": FeatureType.NUMERICAL,
    "11": FeatureType.NUMERICAL,
    "12": FeatureType.NUMERICAL,
    "13": FeatureType.NUMERICAL
  }

  n_trees_test = [1, 5, 10, 25, 50]
  random.seed(SEED)
  print("------- Report accuracy wine ---------")
  for n_tree in n_trees_test:
    print("\nNúmero de árvores: ", n_tree)
    accuracies = kfold(K_FOLDS, data, features, n_trees=n_tree, seed=SEED)
    print("Média: ", statistics.mean(accuracies))
    print("Desvio Padrão: ", statistics.stdev(accuracies))


#reports_vote()
reports_wine()


