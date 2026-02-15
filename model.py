import numpy as np


class PostConflictGrowthModel:
    """
    Augmented Solow Growth Model with:
    - Physical Capital (K)
    - Human Capital (H)
    - Governance/Productivity (A)
    - Conflict Shock Mechanism
    """

    def __init__(
        self,
        alpha=0.33,
        s=0.25,
        delta_k=0.05,
        delta_h=0.03,
        g=0.02,
        education_investment=0.02,
        governance_decay=0.01
    ):
        # Core production parameters
        self.alpha = alpha
        self.s = s

        # Depreciation
        self.delta_k = delta_k
        self.delta_h = delta_h

        # Growth parameters
        self.g = g
        self.education_investment = education_investment
        self.governance_decay = governance_decay

    # -------------------------------
    # Production Function
    # -------------------------------

    def production(self, K, H, A):
        """
        Cobb-Douglas Production Function:
        Y = A * K^alpha * H^(1-alpha)
        """
        return A * (K ** self.alpha) * (H ** (1 - self.alpha))

    # -------------------------------
    # Capital Dynamics
    # -------------------------------

    def update_capital(self, K, Y):
        """
        K_{t+1} = (1 - delta_k)K_t + sY_t
        """
        return (1 - self.delta_k) * K + self.s * Y

    def update_human_capital(self, H):
        """
        H_{t+1} = (1 - delta_h)H_t + education_investment
        """
        return (1 - self.delta_h) * H + self.education_investment

    def update_governance(self, A, conflict_effect=0.0):
        """
        A_{t+1} = A_t * (1 + g - conflict_effect - governance_decay)
        """
        return A * (1 + self.g - conflict_effect - self.governance_decay)

    # -------------------------------
    # Conflict Shock
    # -------------------------------

    def apply_conflict_shock(self, K, H, A,
                             capital_loss=0.3,
                             human_capital_loss=0.2,
                             governance_loss=0.1):
        """
        Applies an immediate conflict shock reducing:
        - Physical Capital
        - Human Capital
        - Governance/Productivity
        """
        K *= (1 - capital_loss)
        H *= (1 - human_capital_loss)
        A *= (1 - governance_loss)

        return K, H, A
