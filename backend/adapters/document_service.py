import time
from typing import Dict, Any

class MockDocumentService:
    """
    Document Generation & E-Signature Service (DocuSign / HelloSign / PandaDoc ready).
    """
    @staticmethod
    def generate_offer_letter(candidate_name: str, role: str, compensation: str = "₹9,00,000 / year", start_date: str = "First Monday of next month") -> Dict[str, Any]:
        document_id = f"OFFER-FOS-{int(time.time()) % 100000}"
        
        offer_text = f"""AGENTGRID TECHNOLOGIES PVT. LTD.
CONFIDENTIAL EMPLOYMENT OFFER LETTER

Date: {time.strftime('%B %d, %Y')}

To: {candidate_name}
Position: {role}
Reporting to: Founder & CEO, AgentGrid

Dear {candidate_name},

We are thrilled to offer you the full-time position of {role} at AgentGrid.

1. COMPENSATION & BENEFITS:
• Annual Base CTC: {compensation}
• Performance Incentive: Up to 10% annual milestone bonus
• Employee Stock Options (ESOP): Subject to standard 4-year vesting with 1-year cliff
• Comprehensive Health & Medical Insurance coverage
• Home Office & Tech Equipment Stipend: ₹1,50,000 upfront

2. KEY TERMS & COMPLIANCE:
• Proprietary Information and Inventions Assignment Agreement (100% IP rights assigned to AgentGrid)
• Mutual Non-Disclosure Agreement (NDA)
• Standard 30-day notice period post probation

3. TARGET START DATE:
{start_date}

This offer is valid for 7 business days from the date of issuance."""

        return {
            "document_id": document_id,
            "document_type": "EMPLOYMENT_OFFER_LETTER",
            "candidate_name": candidate_name,
            "role": role,
            "compensation": compensation,
            "status": "AWAITING_FOUNDER_SIGN_AND_SEND",
            "offer_text": offer_text,
            "key_clauses": [
                "100% Intellectual Property (IP) Assignment to AgentGrid",
                "Strict Non-Disclosure of Proprietary AI Models & Codebases",
                "Non-Solicitation & Non-Compete Standard Covenants",
                "Remote Work Security & Data Protection Addendum"
            ],
            "actions_available": [
                {"id": "approve_send_offer", "name": "APPROVE & SEND OFFER VIA EMAIL", "target": candidate_name, "consequential": True},
                {"id": "download_pdf", "name": "DOWNLOAD SIGNED PDF", "target": document_id, "consequential": False}
            ]
        }

    @staticmethod
    def dispatch_docusign_envelope(document_id: str, recipient_name: str, recipient_email: str = "candidate@example.com") -> Dict[str, Any]:
        return {
            "envelope_id": f"DOCUSIGN-ENV-{int(time.time())}",
            "document_id": document_id,
            "recipient": recipient_name,
            "email": recipient_email,
            "status": "DISPATCHED_FOR_SIGNATURE",
            "sent_at": time.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "tracking_url": "https://demo.docusign.net/signing/envelopes/8f9a2b1c"
        }
