# This program helps to find the solutions to kinematic problems


def main():
    print(
        "Welcome to the 1D Kinematics Calculator\n This calculator can find Initial/Final Velocity, Final Displacement, Acceleration, and Time\n"
    )
    # Gather all values needed for suvat equation
    vunit = input(
        "What Unit are you using for your Kinematics Problem? (Meters or Centimeters) "
    ).lower()
    Iv = input('Initial Velocity? (If None say "None") ')
    Fv = input('Final Velocity? (If None say "None") ')
    A = input('Acceleration? (If None say "None") ')
    T = input('Time (Seconds)? (If None say "None")  ')
    Fs = input('Final Displacement? (If None say "None") ')
    vals = [Iv, Fv, A, T, Fs]
    suvat(vals, vunit)


def suvat(values, units):
    # make sure values are valid inputs, restarts if otherwise
    vkeys = [
        "Initial Velocity",
        "Final Velocity",
        "Acceleration",
        "Time",
        "Final Displacement",
    ]
    newV = []
    # fix element values
    for element in values:
        try:
            element = float(element)
        except ValueError:
            if element == "none":
                newV.append("none")
                continue
            else:
                print('Please ensure that your values are either numerial or "None"')
                main()
        newV.append(element)

    # put updated elements into dictionary
    vdict = dict(zip(vkeys, newV))
    missing = []
    # find all the nones, and input user for which one they want to find
    for key, val in vdict.items():
        if val == "none":
            missing.append(key)
    intendfind = input(
        f"What Value are you intending to find: {', '.join(missing)}\n(ENSURE YOUR INPUT MATCHES PERFECTLY TO YOUR OPTION)? "
    ).title()

    # find all missing values using suvat equations
    while "none" in vdict.values():

        # final velocity
        try:
            velof = vdict["Initial Velocity"] + (vdict["Acceleration"] * vdict["Time"])
        except TypeError:
            try:
                velof = (
                    2 * (vdict["Final Displacement"]) / vdict["Time"]
                    - vdict["Initial Velocity"]
                )
            except TypeError:
                try:
                    velof = (
                        vdict["Final Displacement"]
                        + ((1 / 2) * vdict["Acceleration"] * (vdict["Time"] ** 2))
                    ) / vdict["Time"]

                except TypeError:
                    try:
                        velof = (
                            vdict["Initial Velocity"]
                            + 2 * (vdict["Acceleration"] * vdict["Final Displacement"])
                        ) ** 0.5
                    except TypeError:
                        velof = "Couldn't be found"

        if vdict["Final Velocity"] == "none":
            vdict["Final Velocity"] = velof

        # Initial Velocity
        try:
            veloi = vdict["Final Velocity"] - (vdict["Acceleration"] * vdict["Time"])
        except TypeError:
            try:
                veloi = (
                    2 * (vdict["Final Displacement"] / vdict["Time"])
                    - vdict["Final Velocity"]
                )
            except TypeError:
                try:
                    veloi = (
                        vdict["Final Displacement"]
                        - ((1 / 2) * vdict["Acceleration"] * (vdict["Time"] ** 2))
                        / vdict["Time"]
                    )
                except TypeError:
                    try:
                        veloi = (
                            vdict["Final Velocity"] ** 2
                            - 2 * (vdict["Acceleration"] * vdict["Final Displacement"])
                        ) ** 0.5
                    except TypeError:
                        veloi = "Could not be found"
        if vdict["Initial Velocity"] == "none":
            vdict["Initial Velocity"] = veloi

        # Acceleration
        try:
            newA = (vdict["Final Velocity"] - vdict["Initial Velocity"]) / vdict["Time"]
        except TypeError:
            try:
                newA = (
                    2 * vdict["Final Displacement"]
                    - (vdict["Initial Velocity"] * vdict["Time"])
                ) / (vdict["Time"] ** 2)
            except TypeError:
                try:
                    newA = (
                        2
                        * (
                            vdict["Final Velocity"] * vdict["Time"]
                            - vdict["Final Displacement"]
                        )
                    ) / (vdict["Time"] ** 2)
                except TypeError:
                    try:
                        newA = (
                            vdict["Final Velocity"] ** 2
                            - vdict["Initial Velocity"] ** 2
                        ) / (2 * vdict["Final Displacement"])
                    except TypeError:
                        newA = "Could Not Be Found"

        if vdict["Acceleration"] == "none":
            vdict["Acceleration"] = newA

        # Final Displacement
        try:
            newS = (
                (vdict["Final Velocity"] + vdict["Initial Velocity"]) * vdict["Time"]
            ) / 2
        except TypeError:
            try:
                newS = (vdict["Initial Velocity"] * vdict["Time"]) + (
                    0.5 * (vdict["Acceleration"] * (vdict["Time"] ** 2))
                )
            except TypeError:
                try:
                    newS = (vdict["Final Velocity"] * vdict["Time"]) - (
                        0.5 * (vdict["Acceleration"] * (vdict["Time"] ** 2))
                    )
                except TypeError:
                    try:
                        newS = (
                            vdict["Final Velocity"] ** 2
                            - vdict["Initial Velocity"] ** 2
                        ) / (2 * vdict["Acceleration"])
                    except TypeError:
                        newS = "Could Not Be Found"

        if vdict["Final Displacement"] == "none":
            vdict["Final Displacement"] = newS

        # Time
        try:
            newT = (vdict["Final Velocity"] - vdict["Initial Velocity"]) / vdict[
                "Acceleration"
            ]
        except TypeError:
            try:
                newT = (
                    2
                    * (vdict["Final Displacement"])
                    / (vdict["Final Velocity"] + vdict["Initial Velocity"])
                )
            except TypeError:
                try:
                    newT = (
                        vdict["Final Velocity"]
                        + (
                            vdict["Final Velocity"] ** 0.5
                            - 2 * (vdict["Acceleration"] * vdict["Final Displacement"])
                        )
                        / vdict["Acceleration"]
                    )
                except TypeError:
                    try:
                        newT = (
                            vdict["Initial Velocity"]
                            - (
                                vdict["Initial Velocity"] ** 0.5
                                - 2
                                * (vdict["Acceleration"] * vdict["Final Displacement"])
                            )
                            / vdict["Acceleration"]
                        )
                    except TypeError:
                        newT = "Could Not Be Found"

        if vdict["Time"] == "none":
            vdict["Time"] = newT

        # Loop again if none is still found

        if "none" not in vdict.values():
            # print("Loop complete")
            break
        else:
            #  print("None still found")
            continue

    # print output with correct units
    # print(intendfind)
    if intendfind in vdict.keys():
        if intendfind != "Time" and intendfind != "Acceleration":
            print(f"{intendfind} = {vdict[intendfind]} {units}")
        elif intendfind == "Time":
            print(f"{intendfind} = {vdict[intendfind]} seconds")
        elif intendfind == "Acceleration":
            print(f"{intendfind} = {vdict[intendfind]} {units} per second squared")

    else:
        while intendfind not in vdict.keys():
            print("Please Input Exactly Matching Values")
            intendfind = input(
                f"What Value are you intending to find: {', '.join(missing)}\n(ENSURE YOUR INPUT MATCHES PERFECTLY TO YOUR OPTION)? "
            ).Upper()
            if intendfind in vdict.keys():
                break


if __name__ == "__main__":
    main()
