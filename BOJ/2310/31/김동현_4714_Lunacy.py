while True:
    target = float(input())
    if target == -1.:
        break
    print("Objects weighing %.2f on Earth will weigh %.2f on the moon." % (target, target*0.167))