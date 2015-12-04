# Adam Naguib, 2015

# Previous code removed...

    if params["samples"]["samples"]:
        for d in params["samples"]["samples"]:
            sample_mix_tube = p.ref("sample_mix_tube%s" % d,
                                    None, "micro-2.0", discard=True)

            p.transfer(d,
                       sample_mix_tube.well(0),
                       ((sample_volume) * reps * 1.2),
                       one_tip=True)

            p.transfer(Coomassie,
                       sample_mix_tube.well(0),
                       ((reaction_volume - sample_volume) * reps * 1.2),
                       one_source=True)
            p.transfer(sample_mix_tube.well(0),
                       sample_mix_tube.well(0),
                       "%d:microliter" % mixing_volume,
                       one_source=True,
                       dispense_target=dispense_target
                       (depth("ll_bottom", distance="0.002:meter"),
                        {"start": "25:microliter/second",
                           "max": "25:microliter/second"}, None))

            for i in range(0, reps):
                p.transfer(sample_mix_tube.well(0),
                           protein_plate.well(curr),
                           reaction_volume,
                           one_tip=True,
                           one_source=True,
                           disposal_vol="15:microliter",
                           aspirate_source=aspirate_source
                           (depth=depth("ll_bottom", "0.001:meter")))
                curr += 1

# Subsequent code removed...
