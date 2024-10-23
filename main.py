from datetime import datetime
from pci_dss_requirements import get_pci_dss_requirements
from report_generator import generate_report
from database import init_db, save_assessment

def main():
    init_db()  
    requirements = get_pci_dss_requirements()
    compliance_scores = {}
    
    print("PCI DSS Compliance Assessment Tool")
    print("=" * 40)

    for requirement, description in requirements.items():
        print(f"{requirement}: {description}")
        
        while True:
            response = input("Is this requirement met? (yes/no): ").strip().lower()
            if response in ('yes', 'no'):
                break  
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        status = "Met" if response == 'yes' else "Not Met"
        compliance_scores[requirement] = response == 'yes'
        
        save_assessment(datetime.now().isoformat(), requirement, status)
    
    report = generate_report(compliance_scores)
    print(report)

if __name__ == "__main__":
    main()

