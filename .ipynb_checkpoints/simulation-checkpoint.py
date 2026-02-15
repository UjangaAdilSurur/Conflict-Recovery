import numpy as np


class SimulationRunner:
    def __init__(self, model, T=50):
        self.model = model
        self.T = T

    def run(self, K0, H0, A0,
            shock_time=None,
            shock_params=None,
            capital_injection=None,
            policy_change=None):

        K = np.zeros(self.T)
        H = np.zeros(self.T)
        A = np.zeros(self.T)
        Y = np.zeros(self.T)

        K[0] = K0
        H[0] = H0
        A[0] = A0

        for t in range(self.T - 1):

            Y[t] = self.model.production(K[t], H[t], A[t])

            # Apply conflict shock
            if shock_time is not None and t == shock_time:
                K[t], H[t], A[t] = self.model.apply_conflict_shock(
                    K[t], H[t], A[t], **shock_params
                )

            # Capital injection
            if capital_injection is not None and t == shock_time + 1:
                K[t] += capital_injection

            # Policy change (e.g., education reform)
            if policy_change is not None and t >= shock_time:
                for param, value in policy_change.items():
                    setattr(self.model, param, value)

            K[t + 1] = self.model.update_capital(K[t], Y[t])
            H[t + 1] = self.model.update_human_capital(H[t])
            A[t + 1] = self.model.update_governance(A[t])

        Y[-1] = self.model.production(K[-1], H[-1], A[-1])

        return {
            "K": K,
            "H": H,
            "A": A,
            "Y": Y
        }

