def run_sensitivity(sim_runner, K0, H0, A0, param_name, values):

    results = {}

    for val in values:
        setattr(sim_runner.model, param_name, val)

        outcome = sim_runner.run(K0, H0, A0)

        results[f"{param_name}={val}"] = outcome

    return results

