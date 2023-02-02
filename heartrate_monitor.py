try:
    import heartrate
    hrm = heartrate.HeartRateSensor(frequency=1)
    def on_reading():
        print(f"Current heart rate: {hrm.heartRate}")
    hrm.add_event_listener("reading", on_reading)
    hrm.start()
except ImportError:
    print("The heart-rate module is not available.")