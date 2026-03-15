from flask import Flask, render_template, request

from model.recommender import recommend
from model.collaborative import recommend_item_based

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    results = None
    algo = None
    message = None

    if request.method == "POST":

        algo = request.form.get("algorithm")

        # Content Based
        if algo == "cb":

            product = request.form.get("product")

            if product:
                rec = recommend(product)

                if isinstance(rec, str):
                    message = rec
                else:
                    results = rec.to_dict("records")

        # Collaborative Filtering
        elif algo == "cf":

            user_id = request.form.get("user_id")

            if user_id:

                try:
                    rec = recommend_item_based(int(user_id))

                    results = []
                    for name, score in rec.items():
                        results.append({
                            "name": name,
                            "score": round(score,2)
                        })
                                            
                except:
                    message = "Invalid User ID"

    return render_template(
        "index.html",
        results=results,
        algo=algo,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)