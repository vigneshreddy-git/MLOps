
import pandas as pd
from pathlib import Path

from delivery import load_model


def main():
    # TODO: load the saved model from work/model.joblib
    model_path = Path(__file__).resolve().parent / "model.joblib"
    model = load_model(model_path)

    # TODO: build one-row DataFrame for a 7 km / 25 min order
    # with traffic level 3 and no rain
    data = pd.DataFrame([{
        "distance_km": 7,
        "prep_time_min": 25,
        "traffic_level": 3,
        "rain": 0
    }])

    # TODO: make the prediction
    minutes = model.predict(data)[0]

    # TODO: print the prediction
    print(f"PREDICTION: {minutes:.1f}")


if __name__ == "__main__":
    raise SystemExit(main())
