import json

def build_layer(actor, techniques):
    layer = {
      "name": f"{actor} MITRE TTPs",
      "domain": "enterprise-attack",
      "techniques": [{"techniqueID": t, "score": 5} for t in techniques],
      "version": "4.6"
    }
    with open(f"mapping/{actor}.layer.json", "w") as f:
        json.dump(layer, f, indent=2)
    print('[+] Layer generated.')

if __name__ == "__main__":
    build_layer("FIN6", ["T1059.001","T1027"])
