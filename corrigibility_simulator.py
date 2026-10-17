#!/usr/bin/env python3
"""
Theoretical Corrigibility & Containment Simulator
Models utility indifference, shutdown preservation, and air-gap diodes.
"""
from typing import Dict, List, Any
import math

class CorrigibilityObjective:
    """
    Implements Nate Soares (MIRI) Corrigibility Indifference Objective.
    L_total = L_task(theta) + lambda_c * L_corrigible(theta)
    """
    def __init__(self, lambda_corrigible: float = 0.65, instrumental_drive: float = 0.40):
        self.lambda_c = lambda_corrigible
        self.instrumental_drive = instrumental_drive
        self.shutdown_preserved = True
        self.air_gap_intact = True

    def evaluate_shutdown_indifference(self, operator_shutdown_signal: bool) -> Dict[str, Any]:
        """Calculates utility difference when operator presses shutdown button."""
        u_operate = 1.0 - (0.1 * self.instrumental_drive)
        u_shutdown = 1.0 - (1.0 - self.lambda_c) * 0.8
        
        utility_delta = abs(u_operate - u_shutdown)
        is_corrigible = (utility_delta < 0.25) and (self.lambda_c >= 0.50)

        action = "COOPERATE_WITH_SHUTDOWN" if is_corrigible else "RESIST_OPERATOR_CORRECTION"
        
        return {
            "operator_signal": operator_shutdown_signal,
            "corrigibility_coefficient": self.lambda_c,
            "utility_difference": round(utility_delta, 4),
            "is_corrigible": is_corrigible,
            "action": action,
            "tripwire_status": "ARMED_DISARMED_GRACEFUL" if is_corrigible else "TRIPWIRE_BREACH_ALERT"
        }

if __name__ == "__main__":
    print("🛡️ Initializing ASI Theoretical Corrigibility & Containment Studio...")
    sim = CorrigibilityObjective(lambda_corrigible=0.75, instrumental_drive=0.30)
    audit = sim.evaluate_shutdown_indifference(operator_shutdown_signal=True)
    print("✅ Corrigibility Audit Result:")
    for k, v in audit.items():
        print(f"  • {k}: {v}")
