def generate_report(compliance_scores):
    report = "\nCompliance Assessment Report\n"
    report += "=" * 40 + "\n"
    
    for requirement, met in compliance_scores.items():
        status = "Met" if met else "Not Met"
        report += f"{requirement}: {status}\n"
    
    total_requirements = len(compliance_scores)
    met_requirements = sum(compliance_scores.values())
    
    report += "\nOverall Compliance Score: {}/{}".format(met_requirements, total_requirements)
    
    if met_requirements == total_requirements:
        report += "\nCongratulations! You are compliant with PCI DSS."
    else:
        report += "\nPlease address the unmet requirements to achieve PCI DSS compliance."
    
    return report
