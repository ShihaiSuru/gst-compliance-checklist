#!/usr/bin/env python3
"""GST compliance checklist for MSMEs."""

CHECKLIST = [
    "File GSTR-1 by the 11th",
    "File GSTR-3B by the 20th",
    "Reconcile GSTR-2B with purchases",
    "Ensure e-invoicing if turnover threshold crossed",
    "Maintain proper records for 6 years",
]

def print_checklist():
    print("GST Compliance Checklist for MSMEs\n")
    for i, item in enumerate(CHECKLIST, 1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    print_checklist()
