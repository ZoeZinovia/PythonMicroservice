import powertop
import json

measures = powertop.Powertop().get_measures(time=1)

print(json.dumps(measures['Device Power Report'], indent=4))